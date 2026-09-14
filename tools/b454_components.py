# -*- coding: utf-8 -*-
"""b454_components.py -- (R63) EXECUTED UNDER (R64), AND THE SPAN-HEADING WORK-ORDER REPAIRED.

### ### **EVERY RULE IS THE LOCKED FACE'S** (`data/b454_registration_2026-09-14.txt`); this tool applies them.
### Modes, in order: `search` (1b's shapes over the pre-b450 ledgers, hits banked, no verdict); `enumera` (2's search,
### hits banked, no grade); `plan` (every write computed and printed, nothing written); `write` (the corpus writes
### and the span repair, each diff counted); `report` (the components record).
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
PRE = '687aa24'
ARC = 'archive/2026-08-24-ledger-split'
FINDJ = os.path.join(D, 'b454_findings.json')
ENUMJ = os.path.join(D, 'b454_enumera.json')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def git(repo, *a):
    p = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return p.stdout


def dump_json(path, obj):
    data = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)


TIER = re.compile(r'Tier-1|Tier 1')
FINDINGS = [
    ('F1', 'W_inf NOT sign-definite',
     lambda l: 'sign-definite' in l and re.search(r'\bnot\b|\bNOT\b', l),
     lambda l: 'sign-definite' in l or 'sign definite' in l),
    ('F2', 'the Day-1 section I attribution pole-plus-archimedean',
     lambda l: 'pole-plus-archimedean' in l,
     lambda l: 'pole' in l and 'archimedean' in l and re.search(r'Day-1|§I|attribution', l)),
    ('F3', 'Face E / keyhole',
     lambda l: 'keyhole' in l,
     lambda l: 'Face E' in l),
    ('F4', 'the T3 Tier-1 scope',
     lambda l: 'T3' in l and TIER.search(l) and 'scope' in l,
     lambda l: 'T3' in l and TIER.search(l)),
    ('F5', 'the E-Difficulty cross-link verdict DISTINCT',
     lambda l: 'cross-link' in l and 'DISTINCT' in l,
     lambda l: 'DISTINCT' in l and ('E-Difficulty' in l or 'κ' in l)),
    ('F6', 'the two-kinds windows verdict',
     lambda l: re.search(r'two-kinds|two kinds', l) and 'window' in l,
     lambda l: 'index truncation' in l and 'support truncation' in l),
    ('F7', 'the S2 Ostrowski seal',
     lambda l: 'S2' in l and 'Ostrowski' in l and 'seal' in l,
     lambda l: 'S2' in l and 'Ostrowski' in l),
    ('F8', 'the sign-face registers',
     lambda l: 'sign-face' in l and 'register' in l,
     lambda l: 'sign-face' in l or 'sign face' in l),
]
# ### the fifteen targets: b451 items with form `absent material`, less item 10 (withdrawn by (R64)(2))
TARGET_OF = {'W_inf NOT sign-definite': 'F1', 'the Day-1 section I attribution pole-plus-archimedean': 'F2',
             'Face E / keyhole': 'F3', 'the T3 Tier-1 scope': 'F4', 'the E-Difficulty cross-link verdict DISTINCT': 'F5',
             'the two-kinds windows verdict': 'F6', 'the S2 Ostrowski seal': 'F7', 'the sign-face registers': 'F8'}


def targets():
    kj = json.loads(read(os.path.join(D, 'b451_kinds.json')))
    out, withdrawn = [], []
    for it in kj['items']:
        if it['form'] != 'absent material':
            continue
        if 'bd2ae1a' in it['what']:
            withdrawn.append(it['n'])
            continue
        name = it['what'].replace('does not carry: ', '')
        out.append(dict(n=it['n'], keystone=it['keystone'], finding=name, fid=TARGET_OF.get(name)))
    return out, withdrawn


def ledgers():
    out = []
    for rel in ('FINDINGS.md', 'OPEN_TRAILS.md'):
        out.append(('%s@%s' % (rel, PRE), git(PP, 'show', '%s:%s' % (PRE, rel))))
    arc = os.path.join(PP, *ARC.split('/'))
    for f in sorted(os.listdir(arc)):
        if f.endswith('.md'):
            out.append(('%s/%s' % (ARC, f), read(os.path.join(arc, f))))
    return out


def do_search():
    tg, wd = targets()
    print('  targets %d ; withdrawn %s ; unmapped %s' % (len(tg), wd, [t for t in tg if not t['fid']]))
    L = ledgers()
    for name, txt in L:
        print('  ledger %-90s lines %d' % (name, len(txt.splitlines())))
    arc_after = git(PP, 'log', '--oneline', '%s..HEAD' % PRE, '--', ARC).strip()
    print('  commits touching the archive split after %s : %d' % (PRE, len(arc_after.splitlines()) if arc_after else 0))
    res = {}
    for fid, fname, s1, s2 in FINDINGS:
        hits = []
        y1 = y2 = 0
        for name, txt in L:
            for i, l in enumerate(txt.splitlines(), 1):
                a, b = bool(s1(l)), bool(s2(l))
                y1 += a
                y2 += b
                if a or b:
                    hits.append(dict(ledger=name, line=i, s1=a, s2=b, text=l.strip()))
        res[fid] = dict(finding=fname, s1_yield=y1, s2_yield=y2, hits=hits)
        print('  %s %-56s S1 %4d  S2 %4d  union %4d' % (fid, fname, y1, y2, len(hits)))
    dump_json(FINDJ, dict(pre=PRE, ledgers=[n for n, _ in L], archive_commits_after=arc_after, targets=tg, withdrawn=wd, shapes=res))
    print('  written %s' % os.path.basename(FINDJ))
    return 0


DECL = re.compile(r'^\s*(?:private |protected |noncomputable )?(theorem|lemma) (\S*)', re.I)
NAMEPAT = r'(exhaust|ostrowski|poisson|formation|catalog|side_exclusion|covers_all|seven)'


def kernels():
    root = 'D:' + os.sep
    return sorted((n, os.path.join(root, n)) for n in os.listdir(root)
                  if n.startswith('SIDE-') and os.path.isdir(os.path.join(root, n, '.git')))


def clauses(text):
    t = text.lower()
    c = []
    if 'exhaust' in t and re.search(r'catalog|class|seven|7|covers', t):
        c.append('E1')
    if 'poisson' in t or 'ostrowski' in t:
        c.append('E2')
    if 'formation' in t and re.search(r'7|seven|2, 3, 2, 0', t):
        c.append('E3')
    if 'exclusion' in t:
        c.append('E4')
    return c


def do_enumera():
    K = kernels()
    hits = []
    for n, p in K:
        out = git(p, 'grep', '-n', '-i', '-E', r'^\s*(private |protected |noncomputable )?(theorem|lemma) [^ ]*' + NAMEPAT, 'HEAD', '--', '*.lean')
        cache = {}
        for ln in out.splitlines():
            parts = ln.split(':', 3)
            if len(parts) < 4:
                continue
            _rev, path, lno, txt = parts
            if path not in cache:
                cache[path] = git(p, 'show', 'HEAD:%s' % path).splitlines()
            src = cache[path]
            i = int(lno) - 1
            body = []
            for j in range(i, min(i + 25, len(src))):
                body.append(src[j])
                if ':=' in src[j] or re.search(r'\bby\b\s*$', src[j]):
                    break
            m = DECL.match(src[i]) if i < len(src) else None
            name = m.group(2) if m else txt.split()[1]
            hits.append(dict(kernel=n, path=path, line=int(lno), name=name, decl=NL.join(body), clauses=clauses(NL.join(body))))
    best = max((len(h['clauses']) for h in hits), default=0)
    nearest = [h for h in hits if len(h['clauses']) == best and best > 0]
    for h in nearest:
        prof = []
        short = h['name'].split('.')[-1]
        p = dict(K)[h['kernel']]
        for f in git(p, 'grep', '-l', short, 'HEAD').splitlines():
            f = f.split(':', 1)[1]
            lines = git(p, 'show', 'HEAD:%s' % f).splitlines()
            for k, l in enumerate(lines):
                if short in l:
                    win = lines[max(0, k - 3):k + 4]
                    if any('axioms' in w for w in win):
                        prof.append(dict(file=f, line=k + 1, window=NL.join(win)))
        h['profile'] = prof[:6]
        h['profile_count'] = len(prof)
    print('  rostered kernels searched : %d' % len(K))
    print('  yield (theorem/lemma names matching) : %d' % len(hits))
    for h in sorted(hits, key=lambda h: (-len(h['clauses']), h['kernel'], h['path'], h['line'])):
        print('  %-28s %-60s %-55s %s' % (h['kernel'], ('%s:%d' % (h['path'], h['line']))[:60], h['name'][:55], h['clauses']))
    print('  ### most clauses touched : %d ; nearest candidates : %d' % (best, len(nearest)))
    dump_json(ENUMJ, dict(kernels=[n for n, _ in K], yield_=len(hits), hits=hits, best=best, nearest=nearest))
    print('  written %s' % os.path.basename(ENUMJ))
    return 0



# =====================================================================================================
# ### THE HAND-READ OF (1b), EVERY HIT OF EITHER SHAPE, BY THE FACE'S TEST. ### HOLDS: the line states the
# ### finding's content. ### Keyed (ledger tail, line) -> reason; a hit not listed under HOLD does not hold,
# ### and its reason is the per-finding NOT line below.
# =====================================================================================================
A1 = 'archive/2026-08-24-ledger-split/FINDINGS-archive-1-entries-through-2026-08-20c.md'
A2 = 'archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-2-historical-landings-and-programs.md'
HOLD = {
    'F1': [(A1, 2221, 'both sign-face annotations at grade with cite: `W_∞` not sign-definite')],
    'F6': [(A2, 7830, '### **VERDICT: `DISTINCT`.** ### **Li-index truncation DOES NOT LOCALISE SUPPORT — the width saturates near `15.7` and stops responding to `n`, while support truncation controls the width directly and exactly (`2 log a`).**'),
           (A2, 8431, '**The measured column stands: index truncation does not localise support; support truncation controls width exactly as `2 log a`. `DISTINCT` between the two kinds, confirmed, and now with the window census behind it.**'),
           (A2, 8499, 'the **two-kinds windows verdict** (support vs index; three of four windows are one kind in different coordinates)')],
    'F7': [(A2, 8808, '### **`S2` Ostrowski `COMPILED`** — `structural_exhaustiveness_proved`, SIDE-kernel v1.5 = `0e5233f`, `{propext, Classical.choice, Quot.sound}`; the roster sealed')],
    'F8': [(A2, 3476, 'the **five faces** compiled as a structure, with R4 identified as the sign face and R5 as the realization face, and the cross-register equivalences deliberately **not** claimed')],
}
NOTREAD = {
    'F1': 'no other hit.',
    'F2': 'the one hit (OPEN_TRAILS-archive-2:1060) is the Li split, archimedean against pole+Euler, a different finding; no line states the Day-1 section I attribution repaired to pole-plus-archimedean.',
    'F3': 'the 38 hits name Face E (its two-witness ruling, its Tier-1 statement, its barrier direction) or read keyhole (i), (iii) and (iv) against the flow seat`s construction (OPEN_TRAILS-archive-2:6483-:6486, :6615); none states Face E or keyhole (i)+(iv) as used by the S-table.',
    'F4': 'the one hit (OPEN_TRAILS-archive-2:1980) lists T3 = order-1 as a Tier-1 tool and scopes density estimates out; it states no scope finding for T3.',
    'F5': 'the one hit (VERIFICATION_LOOM-archive-1:2372) is the darkness/not-consumed distinction at kappa = 0, a different finding.',
    'F6': 'FINDINGS-archive-1:2224 and OPEN_TRAILS-archive-2:8471 name the verdict without stating it; :2364 is the extremal-selection two-kinds split; :7681 is the question, not the verdict.',
    'F7': 'FINDINGS-archive-1:1014 is S2 supplied at content by FORMATION_UNIVERSALITY_v3, not the seal.',
    'F8': 'the dossier headings (OPEN_TRAILS@687aa24:495, :629; archive-2:6209, :7613), the deliverable lines (:7360, :7432), :6242 and FINDINGS-archive-1:2221-:2222 name the sign face without stating its registers; FINDINGS-archive-1:2326 is a hard-wrapped fragment that does not state it on its own line; :3610 restates R4 as the sign face beside a different question.',
}
# ### THE DEFECTIVE PREDICATE, PRINTED AND NOT PATCHED (the face's shapes rule; both figures printed).
DEFECT = dict(fid='F4', ledger=A2, line=7971, returned_by='F3 S2 (`Face E`)',
              words='Euler-product consumption at Face E`s **Tier-1 scope verbatim**',
              why='the T1-T10 list names its third item without the token `T3`, so both of F4`s shapes, which need `T3` on the line, cannot return it')

PATHOF = {
    'PATHS_TO_THE_CRITICAL_LINE': 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md',
    'THE_UNCONDITIONAL_SURROUND': 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
    'SIMPLICITY_OF_RIEMANN_ZEROS': 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md',
    'INDEX_ARITY_AT_THE_CRITICAL_LINE': 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md',
    'INVARIANCE_BARRIERS': 'phase1.5/method/INVARIANCE_BARRIERS.md',
    'TECHNE_TOOLKIT': 'phase1.5/method/TECHNE_TOOLKIT.md',
    'E_DIFFICULTY_THEOREM': 'phase2/method/E_DIFFICULTY_THEOREM.md',
    'REPARAMETERIZATION_BARRIERS_v0_1': 'phase2/method/REPARAMETERIZATION_BARRIERS_v0_1.md',
    'EXHAUSTIVENESS_LICENSE': 'phase1.5/method/EXHAUSTIVENESS_LICENSE.md',
    'THE_RESIDUE_OF_RH': 'phase1.5/proofs/THE_RESIDUE_OF_RH.md',
}
WPI = ('SIDE-lv-conservation', 'word-pairing-interface', '5a14205')
WLS = ('SIDE-effects', 'w-ladder-skeleton', 'a0dc376')
# ### (1a) THE FACE'S TABLE: (keystone, survey line, needle, [(old, new)], branch)
BRANCH = [
    ('PATHS_TO_THE_CRITICAL_LINE', 420, 'The cited held branch `word-pairing-interface` of `SIDE-lv-conservation` EXISTS AND IS SOUND',
     [('The cited held branch', 'The cited merged branch')], WPI),
    ('PATHS_TO_THE_CRITICAL_LINE', 440, 'is compiled as an interface on the held branch (`SIDE-lv-conservation` `word-pairing-interface` @ `66485cb`)',
     [('on the held branch (', 'on the merged branch (')], WPI),
    ('EXHAUSTIVENESS_LICENSE', 95, 'SIDE-lv-conservation, held branch `word-pairing-interface`',
     [('held branch `word-pairing-interface`', 'merged branch `word-pairing-interface`')], WPI),
    ('EXHAUSTIVENESS_LICENSE', 101, '(HELD on branch `w-ladder-skeleton`, SIDE-effects; main untouched)',
     [('HELD on branch', 'MERGED from branch'), ('main untouched', 'main fast-forwarded')], WLS),
    ('EXHAUSTIVENESS_LICENSE', 112, 'HELD — nothing merged, nothing deposited (governing publication posture)',
     [('HELD — nothing merged, nothing deposited', 'MERGED — fast-forwarded into main, nothing deposited')], WLS),
    ('THE_RESIDUE_OF_RH', 97, 'read from the held branch `word-pairing-interface` (SIDE-lv-conservation; **not merged, nothing deposited**)',
     [('from the held branch', 'from the merged branch'), ('**not merged, nothing deposited**', '**merged by fast-forward, nothing deposited**')], WPI),
    ('THE_RESIDUE_OF_RH', 126, '### **HELD-BRANCH — NOT MERGED, NOT DEPOSITED**',
     [('### **HELD-BRANCH — NOT MERGED, NOT DEPOSITED**', '### **MERGED BY FAST-FORWARD — NOT DEPOSITED**')], WPI),
    ('THE_RESIDUE_OF_RH', 145, '| ### **one cited pin fails** |',
     [('The cited held branch', 'The cited merged branch')], WPI),
]
STATUS_WORDS = ('READY', 'DRAFT', 'SHORT', 'BLOCKED', 'UNREVIEWED', 'SUPERSEDED', 'REVIEW', 'SCOPE-DROPPED')
NEWROWS = [
    dict(id='1.5a-8', key='THE_RESIDUE_OF_RH', cluster='Phase 1.5A', heading_line=133, heading='### 1.5A: Alternative Proof Presentations', seq='1.5a-1 to 1.5a-7'),
    dict(id='1.5h-9', key='EXHAUSTIVENESS_LICENSE', cluster='Phase 1.5H', heading_line=211, heading='### 1.5H: SIDE Method Papers', seq='1.5h-1 to 1.5h-8'),
]
TODAY = '2026-09-14'


def pp(rel):
    return os.path.join(PP, *rel.split('/'))


def lines_of(text):
    return text.split(NL)


def plan_1a(texts):
    out = []
    for key, sl, needle, subs, br in BRANCH:
        L = lines_of(texts[key])
        idx = [i for i, l in enumerate(L) if needle in l]
        rec = dict(keystone=key, survey_line=sl, needle=needle, branch=br[1], repo=br[0], tip=br[2])
        if len(idx) != 1 or idx[0] + 1 != sl:
            rec.update(edited=False, why='needle found at %s, not exactly once at the survey line' % [i + 1 for i in idx])
            out.append(rec)
            continue
        old = L[idx[0]]
        new = old
        ok = True
        for a, b in subs:
            if new.count(a) != 1:
                ok = False
                break
            new = new.replace(a, b)
        rec.update(line=idx[0] + 1, original=old, new=new, subs=subs, edited=ok, why='' if ok else 'a state term is not exactly once on the line')
        out.append(rec)
    return out


def currency_block(key, recs):
    rs = [r for r in recs if r['keystone'] == key and r['edited']]
    if not rs:
        return ''
    b = ['', '<!-- b454 CURRENCY ANNOTATION, %s -->' % TODAY, '',
         '#### **CURRENCY ANNOTATION** *(%s, b454; existing text preserved apart from the state terms named here)*' % TODAY, '',
         '> ### **%d LINE(S) MOVED FROM HELD TO MERGED: EACH BRANCH WAS FAST-FORWARDED INTO `main`.** *The originals, preserved verbatim:*' % len(rs), '']
    for r in rs:
        b.append('> - line `%d` (`%s` branch `%s`; fast-forward, tip `%s` on `main`’s first-parent line; state terms %s) — *%s*'
                 % (r['line'], r['repo'], r['branch'], r['tip'], ' · '.join('`%s` → `%s`' % (x, y) for x, y in r['subs']), r['original']))
    b += ['', '> ### **WHY.** *`(R63)(a)` as amended by `(R64)(1)`: a line calling a merged branch held is a currency defect. The branch was fast-forwarded, so there is no merge commit; the tip on `main`’s first-parent line is cited. Only the state terms changed on each line; no line was removed; no grade, claim or correspondence row moved.*', '']
    return NL.join(b)


def verdicts():
    fj = json.loads(read(FINDJ))
    res = {}
    for fid, fname, _s1, _s2 in FINDINGS:
        sh = fj['shapes'][fid]
        hitkeys = set((h['ledger'].replace('@' + PRE, ''), h['line']) for h in sh['hits'])
        holds = []
        for led, ln, words in HOLD.get(fid, []):
            h = [x for x in sh['hits'] if x['ledger'] == led and x['line'] == ln]
            holds.append(dict(ledger=led, line=ln, words=words, returned=bool(h), verbatim=bool(h) and words in h[0]['text']))
        res[fid] = dict(finding=fname, s1=sh['s1_yield'], s2=sh['s2_yield'], hits=len(sh['hits']), holds=holds,
                        found=any(x['returned'] and x['verbatim'] for x in holds), not_read=NOTREAD[fid], hitkeys=len(hitkeys))
    ctl = [x for x in res['F6']['holds'] if x['line'] == 8431 and x['ledger'] == A2]
    control = bool(ctl) and ctl[0]['returned'] and ctl[0]['verbatim']
    return fj, res, control


def era_block(fid, v):
    h = [x for x in v['holds'] if x['returned'] and x['verbatim']][0]
    return NL.join(['', '<!-- b454 ERA ANNOTATION, %s -->' % TODAY, '',
                    '### ERA ANNOTATION (%s, b454) — bearing on %s' % (TODAY, v['finding']), '',
                    '> %s' % h['words'], '',
                    '*Provenance: `%s:%d`, a ledger line before b450, added under `(R63)(b)` as amended by `(R64)(2)`. **This note states a later finding and edits no argument above it.** No claim in this document moves.*' % (h['ledger'], h['line']), ''])


def head_of(text):
    L = lines_of(text)
    end = next((i for i, l in enumerate(L) if l.startswith('## 1.')), len(L))
    return L[:end]


def plan_1d():
    reg = read(pp('REGISTRY.md')).replace(chr(13) + NL, NL)
    RL = lines_of(reg)
    out = dict()
    i141 = RL[140]
    ok = i141.startswith('| 1.5a-7 |') and i141.count('| v0.5 |') == 1
    head_v = [l for l in lines_of(read(pp('phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md')))[:20] if l.startswith('v0.18, 2026-08-08')]
    out['row_update'] = dict(line=141, original=i141, new=i141.replace('| v0.5 |', '| v0.18 |'), ok=ok and bool(head_v), head_line=head_v[0][:40] if head_v else '')
    rows = []
    for nr in NEWROWS:
        text = read(pp(PATHOF[nr['key']]))
        H = head_of(text)
        title = next((l[2:].strip().lstrip('﻿') for l in H if l.lstrip('﻿').startswith('# ')), '')
        vline = next((l for l in H if re.match(r'^\*v\d', l)), '')
        ver = re.match(r'^\*(v[\d.]+)', vline).group(1) if vline else ''
        found = sorted(set(w for w in STATUS_WORDS for l in H if re.search(r'(?<![A-Z-])%s(?![A-Z-])' % re.escape(w), l)))
        status = found[0] if len(found) == 1 else ('UNGRADED' if not found else None)
        conf = [m for m in ('◆', '◇', '●', '○', '◎', '◌', '◻') if any(m in l for l in H)]
        words = len(text.split())
        prior = [x for x in re.findall(r'\|\s*(%s-\d+)\s*\|' % re.escape(nr['id'].split('-')[0]), reg)]
        nxt = '%s-%d' % (nr['id'].split('-')[0], max(int(x.split('-')[1]) for x in prior) + 1)
        rows.append(dict(nr, title=title, version=ver, version_line=vline, head_lines=len(H), status_words=found, status=status, conf_marks=conf,
                         words=words, next_id=nxt, id_ok=(nxt == nr['id'] and nr['id'] not in reg), heading_ok=RL[nr['heading_line'] - 1] == nr['heading']))
    out['rows'] = rows
    return reg, out


def registry_append(p1d):
    ru = p1d['row_update']
    b = ['', '<!-- b454 (R63)(d) ROW UPDATE, %s -->' % TODAY, '',
         '## Row update — %s (1.5a-7 Version cell reconciled to the document`s head; b454, under (R17) as amended by (R64)(3))' % TODAY, '',
         'Row **1.5a-7** (`phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md`): the Version cell **v0.5 → v0.18** in the Phase 1.5A table (`REGISTRY.md:141`), read from the document’s own head (`INDEX_ARITY_AT_THE_CRITICAL_LINE.md:15`, *"v0.18, 2026-08-08"*). Nothing else on the row changed. **The pre-edit row, preserved verbatim:**', '',
         '```text', ru['original'], '```', '']
    for r in p1d['rows']:
        prov = ('Entered %s (b454) under (R17) as amended by (R64)(3), from the document’s own head read in full (lines 1–%d, to its first `## 1.` heading): Title from its `#` line; Version from *"%s"*; '
                % (TODAY, r['head_lines'], r['version_line'].strip('*')))
        prov += ('**the head carries no status word of the STATUS KEY or of the cluster’s Status cells, so Status reads UNGRADED**; ' if r['status'] == 'UNGRADED' else 'Status the head’s own word `%s`; ' % r['status'])
        prov += ('the head carries no confidence mark, so Conf reads —; ' if not r['conf_marks'] else '')
        prov += ('ID the next in the cluster’s own sequence (`%s`, REGISTRY.md:%d, rows %s) — REGISTRY states no numbering rule in words; Words a whitespace count of the file on %s.' % (r['heading'], r['heading_line'], r['seq'], TODAY))
        b += ['<!-- b454 (R63)(d) ROW ADDITION, %s -->' % TODAY, '',
              '## Row addition — %s (%s; b454, under (R17) as amended by (R64)(3); fold into Phase 1.5 table at next hand edit)' % (TODAY, r['cluster']), '',
              '| ID | Title | File | Version | Conf | Status | Words | Provenance |',
              '|:---|:------|:-----|:--------|:-----|:-------|:------|:-----------|',
              '| %s | %s | `%s` | %s | %s | %s | %s | %s |' % (r['id'], r['title'], PATHOF[r['key']], r['version'], '—' if not r['conf_marks'] else ' '.join(r['conf_marks']),
                                                         r['status'], '{:,}'.format(r['words']), prov), '']
    return NL.join(b)


def removed_zero(pre, post, edited_originals):
    postlines = set(lines_of(post))
    missing = [l for l in lines_of(pre) if l not in postlines and not (l in edited_originals and l in post)]
    return len(missing) == 0, missing[:3]


def numstat(repo, rel):
    o = git(repo, 'diff', '--numstat', '--', rel).strip()
    return o.split()[:2] if o else ['0', '0']


# ### COMPONENT 3 -- THE REPAIR THE WORK-ORDER NAMES.
SPAN = os.path.join(T, 'b363_span.py')
C3_SUBS = [
    ("""def folds():
    \"\"\"### EVERY FOLD HEADING IN `FINDINGS.md`, WITH THE SPAN IT NAMES IN ITS OWN TITLE.\"\"\"
    txt = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    out = []
    for m in re.finditer(r'^## (.*?), b(\\d+)–b(\\d+) — THE FOLD\\s*$', txt, re.M):
        lo, hi = int(m.group(2)), int(m.group(3))
        out.append(dict(title=m.group(1), lo=lo, hi=hi, acts=hi - lo + 1))
    return out
""",
     """FORM_A = re.compile(r'^## (.*?), b(\\d+)–b(\\d+) — THE FOLD\\s*$')
FORM_B = re.compile(r'^## (.*?) — b(\\d+) through b(\\d+), folded at b(\\d+)\\s*$')
UNPARSED = []


def fold_headings(txt):
    \"\"\"### REPAIRED AT b454 (W-ORD-SPAN-HEADING): EVERY `## ` HEADING IN EITHER FOLD FORM -- `<title>, bNNN–bNNN — THE FOLD`
    ### and b434's `<title> — bNNN through bNNN, folded at bNNN` -- and every `## ` line carrying `fold` that neither parses.\"\"\"
    heads, bad = [], []
    for m in re.finditer(r'^## .*$', txt, re.M):
        line = m.group(0)
        a, b = FORM_A.match(line), FORM_B.match(line)
        if a or b:
            g = a or b
            heads.append((m.start(), g.group(1), int(g.group(2)), int(g.group(3))))
        elif re.search(r'(?i)fold', line):
            bad.append(line)
    return heads, bad


def folds():
    \"\"\"### EVERY FOLD HEADING IN `FINDINGS.md`, WITH THE SPAN IT NAMES IN ITS OWN TITLE.\"\"\"
    txt = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    heads, bad = fold_headings(txt)
    UNPARSED[:] = bad
    out = []
    for _pos, title, lo, hi in heads:
        out.append(dict(title=title, lo=lo, hi=hi, acts=hi - lo + 1))
    return out
"""),
    ("""    heads = [m.start() for m in re.finditer(r'^## .*— THE FOLD\\s*$', txt, re.M)]
""",
     """    heads = [h[0] for h in fold_headings(txt)[0]]
"""),
    ("""    for f in F:
        rec('    b%-4d - b%-4d  %2d acts   %s' % (f['lo'], f['hi'], f['acts'], f['title'][:62]))
""",
     """    for f in F:
        rec('    b%-4d - b%-4d  %2d acts   %s' % (f['lo'], f['hi'], f['acts'], f['title'][:62]))
    for u in UNPARSED:
        rec('    ### UNPARSED FOLD HEADING, PRINTED AND NOT SKIPPED : %s' % u[:90])
"""),
]


def span_read(tag):
    out = subprocess.run([sys.executable, SPAN, '--act', '454'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    io.open(os.path.join(D, 'b454_span_%s.txt' % tag), 'w', encoding='utf-8', newline=NL).write(out)
    return out


def c3_fixture():
    import importlib.util
    import tempfile
    fx = os.path.join(tempfile.gettempdir(), 'b454_span_fixture_FINDINGS.md')
    io.open(fx, 'w', encoding='utf-8', newline=NL).write(NL.join([
        '## THE FIRST ARC, b1–b9 — THE FOLD', '*Filed by b10.*', '## The second arc — b11 through b19, folded at b20', '*Filed by b20.*',
        '## A fold heading in neither form, b21 to b29', 'text', '## Not a heading about anything else', '']))
    spec = importlib.util.spec_from_file_location('span_under_test', SPAN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.FINDINGS = fx
    F = mod.folds()
    res = dict(parsed=[(f['lo'], f['hi']) for f in F], unparsed=list(mod.UNPARSED), filed_by=mod.filed_by(F[-1]['hi']) if F else None)
    res['ok'] = (res['parsed'] == [(1, 9), (11, 19)] and res['unparsed'] == ['## A fold heading in neither form, b21 to b29'] and res['filed_by'] == 20)
    os.remove(fx)
    return res


def do_plan_or_write(write):
    fj, V, control = verdicts()
    tg = fj['targets']
    raw = {k: read(pp(p)) for k, p in PATHOF.items()}
    crlf = {k: (chr(13) + NL) in v for k, v in raw.items()}
    texts = {k: v.replace(chr(13) + NL, NL) for k, v in raw.items()}
    R1a = plan_1a(texts)
    reg, P1d = plan_1d()
    print('  ### (1b) POSITIVE CONTROL (two-kinds windows verdict at %s:8431) returned and holds : %s' % (A2, control))
    for fid, v in V.items():
        print('  %s %-56s S1 %3d S2 %3d hits %3d FOUND %-5s %s' % (fid, v['finding'][:56], v['s1'], v['s2'], v['hits'], v['found'],
                                                             ['%s:%d returned %s verbatim %s' % (h['ledger'].split('/')[-1][:24], h['line'], h['returned'], h['verbatim']) for h in v['holds']]))
    found_t = [t for t in tg if V[t['fid']]['found']]
    notf_t = [t for t in tg if not V[t['fid']]['found']]
    print('  ### TARGETS FOUND (added) : %d ; CLAIMED BY THE KEYSTONE AND HELD BY NO LEDGER : %d ; sum %d of %d' % (len(found_t), len(notf_t), len(found_t) + len(notf_t), len(tg)))
    for r in R1a:
        print('  (1a) %-34s line %-4s edited %-5s %s' % (r['keystone'], r.get('line', r['survey_line']), r['edited'], r['why']))
    print('  (1d) row 1.5a-7 : ok %s ; head %r' % (P1d['row_update']['ok'], P1d['row_update']['head_line']))
    for r in P1d['rows']:
        print('  (1d) %s %-30s title %r version %s status words %s -> %s ; conf %s ; words %d ; next id %s ok %s ; heading ok %s'
              % (r['id'], r['key'], r['title'][:40], r['version'], r['status_words'], r['status'], r['conf_marks'], r['words'], r['next_id'], r['id_ok'], r['heading_ok']))
    if not write:
        return 0
    # ### THE WRITES.
    if not control:
        print('  ### (1b) HALTS: THE CONTROL WAS NOT RETURNED. NO ERA ANNOTATION IS WRITTEN.')
    diffs = []
    for key, rel in PATHOF.items():
        full = pp(rel)
        pre = texts[key]
        L = lines_of(pre)
        mine = [r for r in R1a if r['keystone'] == key and r['edited']]
        for r in mine:
            L[r['line'] - 1] = r['new']
        body = NL.join(L)
        add = currency_block(key, R1a)
        if control:
            for fid in sorted(set(t['fid'] for t in found_t if t['keystone'] == key)):
                add += era_block(fid, V[fid])
        if not mine and not add:
            continue
        post = body.rstrip(NL) + NL + add.rstrip(NL) + NL
        onfile = post.replace(NL, chr(13) + NL) if crlf[key] else post
        open(full + '.tmp', 'wb').write(onfile.encode('utf-8'))
        os.replace(full + '.tmp', full)
        ok, miss = removed_zero(pre, post, [r['original'] for r in mine])
        ns = numstat(PP, rel)
        diffs.append(dict(doc=rel, edited_lines=len(mine), added_blocks=add.count('<!-- b454'), numstat_added=ns[0], numstat_removed=ns[1], removed_zero=ok, missing=miss))
    # ### REGISTRY.
    rows_ok = P1d['row_update']['ok'] and all(r['id_ok'] and r['heading_ok'] and r['status'] and r['version'] and r['title'] for r in P1d['rows'])
    if rows_ok:
        RL = lines_of(reg)
        RL[140] = P1d['row_update']['new']
        post = NL.join(RL).rstrip(NL) + NL + registry_append(P1d).rstrip(NL) + NL
        reg_crlf = (chr(13) + NL) in read(pp('REGISTRY.md'))
        open(pp('REGISTRY.md') + '.tmp', 'wb').write((post.replace(NL, chr(13) + NL) if reg_crlf else post).encode('utf-8'))
        os.replace(pp('REGISTRY.md') + '.tmp', pp('REGISTRY.md'))
        ok, miss = removed_zero(reg, post, [P1d['row_update']['original']])
        ns = numstat(PP, 'REGISTRY.md')
        diffs.append(dict(doc='REGISTRY.md', edited_lines=1, added_blocks=3, numstat_added=ns[0], numstat_removed=ns[1], removed_zero=ok, missing=miss))
    else:
        print('  ### (1d) A ROW CONDITION FAILED -- REGISTRY NOT WRITTEN.')
    for d in diffs:
        print('  diff %-58s edited %d blocks %d numstat +%s -%s removed-zero %s %s' % (d['doc'], d['edited_lines'], d['added_blocks'], d['numstat_added'], d['numstat_removed'], d['removed_zero'], d['missing'] or ''))
    dump_json(os.path.join(D, 'b454_branch_lines.json'), dict(table=[dict((k, v) for k, v in r.items()) for r in R1a]))
    fj['verdicts'] = V
    fj['control'] = control
    fj['found_targets'] = found_t
    fj['held_by_no_ledger'] = notf_t
    fj['defect'] = DEFECT
    fj['counts'] = dict(found=len(found_t), held_by_no_ledger=len(notf_t), targets=len(tg),
                        found_if_defect_credited=len(found_t) + sum(1 for t in notf_t if t['fid'] == DEFECT['fid']))
    fj['diffs'] = diffs
    dump_json(FINDJ, fj)
    dump_json(os.path.join(D, 'b454_registry.json'), dict(P1d, written=rows_ok))
    # ### COMPONENT 3.
    before = span_read('before')
    src = read(SPAN)
    new = src.replace(chr(13) + NL, NL)
    applied = []
    for a, b in C3_SUBS:
        applied.append(new.count(a) == 1)
        if new.count(a) == 1:
            new = new.replace(a, b)
    if all(applied):
        open(SPAN + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(SPAN + '.tmp', SPAN)
    after = span_read('after')
    fx = c3_fixture() if all(applied) else dict(ok=False)
    ns = git(ROOT, 'diff', '--numstat', '--', 'tools/b363_span.py').strip().split()[:2]
    uni = git(ROOT, 'diff', '--', 'tools/b363_span.py')
    grab = lambda s, pat: [l.strip() for l in s.splitlines() if re.search(pat, l)]
    c3 = dict(applied=applied, numstat=ns, unified=uni, fixture=fx,
              before=grab(before, r'FOLDS RUN|the last fold covers|FILED BY|STARTS AT|CURRENT SPAN|UNPARSED'),
              after=grab(after, r'FOLDS RUN|the last fold covers|FILED BY|STARTS AT|CURRENT SPAN|UNPARSED|b423'),
              write_path_unchanged=("run_clock.write(D, '%s_span_notes' % emit, LINES)" in new and "'%s_span.json' % emit" in new))
    dump_json(os.path.join(D, 'b454_span_repair.json'), c3)
    print('  (3) applied %s ; numstat %s ; fixture %s ; write path unchanged %s' % (applied, ns, fx.get('ok'), c3['write_path_unchanged']))
    for l in c3['before']:
        print('      before | %s' % l)
    for l in c3['after']:
        print('      after  | %s' % l)
    return 0


# ### COMPONENT 2 -- THE GRADES, HAND-READ AGAINST (E1), BY README.md:54-:75.
E_REQ = [('E1', 'The seven-class catalogue is exhaustive.'),
         ('E2', "The Poisson Exhaustion Theorem (proved via Ostrowski's theorem) establishes n₂ = 3."),
         ('E3', 'Combined with n₁ = 2 (algebraic), n₃ = 2 (complex analysis), n₄ = 0 (Tate), the formation (2,3,2,0) = 7 is complete.'),
         ('E4', 'RH follows by SIDE Exclusion — *under the exhaustiveness premise `h2`, carried openly as open*')]
GRADES = {
    ('SIDE-kernel', 'Kernel/Layer1.lean', 30): dict(grade='INTERFACES', deciding='(cat : ExhaustiveCatalogue X P)',
        why='the exhaustive catalogue is the theorem`s named hypothesis `cat`; it concludes `Not (P x)` from it and proves no catalogue exhaustive',
        profile='NO SHIPPED PROFILE LOCATED -- the one window naming it within three lines of `axioms` (AGENTS.md:58) states the profile of the composed `riemann_hypothesis`, not of `SIDE_exclusion`'),
    ('SIDE-effects', 'SIDEEffects/Phase15/SIDEFramework.lean', 45): dict(grade='INTERFACES', deciding='(cat : ExhaustiveCatalogue X P)',
        why='the same statement in `SIDEEffects`: the exhaustive catalogue is a named hypothesis',
        profile='NO SHIPPED PROFILE LOCATED -- no tracked file names it within three lines of `axioms`'),
}
SECOND = dict(kernel='SIDE-kernel', path='Bridge/TheBridgeComplete.lean', line=249, name='structural_exhaustiveness_proved',
              statement='theorem structural_exhaustiveness_proved : StructuralExhaustiveness := ⟨seven_classes, none_produce, ostrowski_exhaustive_prime⟩',
              unfolds='StructuralExhaustiveness := (Fintype.card MechanismClass = 7) ∧ (forall c : MechanismClass, ¬(produces_offline c)) ∧ (every nontrivial absolute value on ℚ is equivalent to the real or a p-adic one)  [Bridge/TheBridgeComplete.lean:215]',
              grade='NOT THE CLAIM', deciding='Fintype.card MechanismClass = 7',
              why='sound and premise-free, and strictly weaker than (E1): it counts the constructors of the seven-constructor inductive it defines (`decide`) and classifies the places of ℚ (Mathlib`s Ostrowski); it does not state that every mechanism falls in one of the seven classes, nor n₂ = 3 or the formation`s completeness',
              profile='`[propext, Classical.choice, Quot.sound]` -- DEPOSIT_v1_2_NOTES.md:38, *"\'structural_exhaustiveness_proved\' depends on axioms: [propext, Classical.choice, Quot.sound]"*',
              defect='the word test reads a declaration through its `:=`; `StructuralExhaustiveness``s conjuncts are defined at Bridge/TheBridgeComplete.lean:215, so the name touched no clause and the rule`s nearest is `SIDE_exclusion`. Printed as a second figure, not substituted.')


def do_enumera_grade():
    ej = json.loads(read(ENUMJ))
    for h in ej['nearest']:
        g = GRADES.get((h['kernel'], h['path'], h['line']))
        h['graded'] = g
        h['deciding_in_decl'] = bool(g) and g['deciding'] in h['decl']
    src = git(os.path.join('D:' + os.sep, SECOND['kernel']), 'show', 'HEAD:%s' % SECOND['path'])
    SECOND['statement_verbatim'] = 'theorem structural_exhaustiveness_proved :' in src and '⟨seven_classes, none_produce, ostrowski_exhaustive_prime⟩' in src
    SECOND['deciding_verbatim'] = '(Fintype.card MechanismClass = 7) ∧' in src
    prof = git(os.path.join('D:' + os.sep, SECOND['kernel']), 'show', 'HEAD:DEPOSIT_v1_2_NOTES.md')
    SECOND['profile_verbatim'] = "'structural_exhaustiveness_proved' depends on axioms: [propext, Classical.choice, Quot.sound]" in prof
    ej['second'] = SECOND
    ej['requirement'] = E_REQ
    grades = [h['graded']['grade'] for h in ej['nearest'] if h.get('graded')] + [SECOND['grade']]
    ej['census'] = 'CLOSES AT SIXTEEN' if 'DERIVES' in grades else 'STAYS AT FIFTEEN OF SIXTEEN'
    ej['shortfall'] = ('no rostered terminal states (E1): the rule`s nearest, `SIDE_exclusion`, takes the exhaustive catalogue as its hypothesis '
                       '(INTERFACES), and `structural_exhaustiveness_proved` proves the card of a type it defines and the places of ℚ (NOT THE CLAIM)')
    ej['lean_runs'] = 0
    dump_json(ENUMJ, ej)
    for h in ej['nearest']:
        print('  nearest %s %s:%d %s -> %s (deciding words in decl %s)' % (h['kernel'], h['path'], h['line'], h['name'], h['graded']['grade'] if h.get('graded') else None, h['deciding_in_decl']))
    print('  second  %s %s -> %s ; statement verbatim %s ; deciding verbatim %s ; profile verbatim %s' % (SECOND['kernel'], SECOND['name'], SECOND['grade'], SECOND['statement_verbatim'], SECOND['deciding_verbatim'], SECOND['profile_verbatim']))
    print('  ### CENSUS : %s' % ej['census'])
    return 0


def residual_held():
    out = []
    for key in ('PATHS_TO_THE_CRITICAL_LINE', 'EXHAUSTIVENESS_LICENSE', 'THE_RESIDUE_OF_RH'):
        L = read(pp(PATHOF[key])).replace(chr(13) + NL, NL).split(NL)
        cut = next((i for i, l in enumerate(L) if l.startswith('<!-- b454 CURRENCY ANNOTATION')), len(L))
        for i, l in enumerate(L[:cut]):
            if re.search(r'\bheld\b|\bHELD\b|HELD-BRANCH|not merged|main untouched', l) and re.search(r'word-pairing-interface|w-ladder-skeleton|same branch|on branch', l):
                out.append((PATHOF[key].split('/')[-1], i + 1, l.strip()[:120]))
    return out


def do_report():
    fj = json.loads(read(FINDJ))
    ej = json.loads(read(ENUMJ))
    rj = json.loads(read(os.path.join(D, 'b454_registry.json')))
    bj = json.loads(read(os.path.join(D, 'b454_branch_lines.json')))
    cj = json.loads(read(os.path.join(D, 'b454_span_repair.json')))
    face = read(os.path.join(D, 'b454_registration_2026-09-14.txt'))
    sh = re.search(r'([0-9a-f]{64})', face.split('THE REGISTRATION LOCK')[-1])
    O = []
    r = O.append
    bar = lambda c='-': r(c * 100)
    bar('=')
    r('b454 -- THE COMPONENTS. ### (R63) EXECUTED UNDER (R64), AND THE SPAN-HEADING WORK-ORDER REPAIRED.')
    r('### the face, locked before any write : sha256 %s' % (sh.group(1) if sh else '?'))
    bar('=')
    r('')
    bar()
    r('### COMPONENT 1(a) -- THE BRANCH LINES, BY THE FACE`S TABLE.')
    bar()
    for x in bj['table']:
        r('  %-34s line %-4s edited %-5s tip %s (%s, fast-forward)%s' % (x['keystone'], x.get('line', x['survey_line']), x['edited'], x['tip'], x['repo'], ('' if x['edited'] else ' -- ' + x['why'])))
        for a, b in x.get('subs', []):
            r('        `%s` -> `%s`' % (a, b))
    r('  ### LINES EDITED : %d OF %d.' % (sum(1 for x in bj['table'] if x['edited']), len(bj['table'])))
    rh = residual_held()
    r('  ### OBSERVED, NOT EDITED (words outside the face`s named state terms): %d line(s) in the three documents still carry a held-state word beside a branch:' % len(rh))
    for f, ln, t in rh:
        r('        %s:%d | %s' % (f, ln, t))
    r('')
    bar()
    r('### COMPONENT 1(b) -- THE ERA FINDINGS, SEARCHED IN THE PRE-b450 LEDGERS.')
    bar()
    r('  ledgers : %s' % ' ; '.join(fj['ledgers']))
    r('  commits touching the archive split after 687aa24 : %s' % (len(fj['archive_commits_after'].splitlines()) if fj['archive_commits_after'] else 0))
    r('  withdrawn by (R64)(2): item(s) %s' % fj['withdrawn'])
    r('  ### THE POSITIVE CONTROL (two-kinds windows verdict at OPEN_TRAILS-archive-2:8431) RETURNED AND HOLDS : %s' % fj['control'])
    for fid, v in fj['verdicts'].items():
        r('  %s %-56s S1 yield %-3d S2 yield %-3d hits hand-read %-3d ### %s' % (fid, v['finding'], v['s1'], v['s2'], v['hits'], 'FOUND' if v['found'] else 'HELD BY NO LEDGER'))
        for h in v['holds']:
            r('        HOLDS  %s:%d -- *"%s"*' % (h['ledger'], h['line'], h['words'][:200]))
        r('        not holding: %s' % v['not_read'])
    r('  ### THE DEFECTIVE PREDICATE, PRINTED AND NOT PATCHED: %s at %s:%d, returned by %s -- *"%s"*; %s.'
      % (fj['defect']['fid'], fj['defect']['ledger'], fj['defect']['line'], fj['defect']['returned_by'], fj['defect']['words'], fj['defect']['why']))
    r('')
    r('  per target:')
    for t in fj['targets']:
        v = fj['verdicts'][t['fid']]
        r('    item %-3d %-34s %-56s %s' % (t['n'], t['keystone'], t['finding'][:56], 'ADDED' if v['found'] else 'CLAIMED BY THE KEYSTONE AND HELD BY NO LEDGER'))
    c = fj['counts']
    r('')
    r('  ### ### **THE TWO COUNTS: ADDED %d ; CLAIMED BY THE KEYSTONE AND HELD BY NO LEDGER %d ; SUM %d OF %d.**' % (c['found'], c['held_by_no_ledger'], c['found'] + c['held_by_no_ledger'], c['targets']))
    r('  ### with the defective predicate`s line credited, the figure would be ADDED %d, HELD BY NO LEDGER %d -- printed, not adopted.' % (c['found_if_defect_credited'], c['targets'] - c['found_if_defect_credited']))
    r('')
    bar()
    r('### COMPONENT 1(d) -- THE REGISTRY.')
    bar()
    ru = rj['row_update']
    r('  row 1.5a-7 at REGISTRY.md:141 : Version v0.5 -> v0.18 ; head %r ; pre-edit row preserved verbatim in the appended row-update section ; written %s' % (ru['head_line'], rj['written']))
    for x in rj['rows']:
        r('  %s  %-24s title %r ; version %s ; Conf %s ; Status words in head (lines 1-%d) %s -> %s ; words %d ; next id %s (%s, REGISTRY.md:%d) ; unused %s'
          % (x['id'], x['key'], x['title'], x['version'], x['conf_marks'] or '—', x['head_lines'], x['status_words'], x['status'], x['words'], x['next_id'], x['heading'], x['heading_line'], x['id_ok']))
    r('')
    bar()
    r('### EVERY WRITE, AS A DIFF COUNT.')
    bar()
    for d in fj['diffs']:
        r('  %-58s numstat +%-3s -%-2s  lines edited %d  blocks appended %d  ### LINES REMOVED 0 BY THE FACE`S PREDICATE : %s'
          % (d['doc'], d['numstat_added'], d['numstat_removed'], d['edited_lines'], d['added_blocks'], d['removed_zero']))
    r('  ### numstat counts an edited line once removed and once added; every pre-edit line is present in the post-edit file or, if edited, verbatim inside its annotation.')
    r('')
    bar()
    r('### COMPONENT 2 -- ENUMERA.')
    bar()
    r('  THE REQUIREMENT, IN THE KEYSTONE`S OWN WORDS (ENUMERA.md:73, "The load-bearing claim"):')
    for k, s in ej['requirement']:
        r('    (%s) %s' % (k, s))
    r('  rostered kernels searched : %d ; yield : %d ; most clauses touched : %d ; nearest by the rule : %d' % (len(ej['kernels']), ej['yield_'], ej['best'], len(ej['nearest'])))
    for h in ej['nearest']:
        g = h['graded']
        r('  NEAREST %s %s:%d `%s` clauses %s' % (h['kernel'], h['path'], h['line'], h['name'], h['clauses']))
        for ln in h['decl'].split(NL):
            r('        %s' % ln)
        r('        profile as shipped : %s' % g['profile'])
        r('        ### GRADE AGAINST (E1) : %s -- deciding words `%s`; %s' % (g['grade'], g['deciding'], g['why']))
    s2 = ej['second']
    r('  SECOND FIGURE (the defective predicate named): %s %s:%d `%s`' % (s2['kernel'], s2['path'], s2['line'], s2['name']))
    r('        %s' % s2['statement'])
    r('        unfolds: %s' % s2['unfolds'])
    r('        profile as shipped : %s' % s2['profile'])
    r('        ### GRADE AGAINST (E1) : %s -- deciding words `%s`; %s' % (s2['grade'], s2['deciding'], s2['why']))
    r('        why a second figure: %s' % s2['defect'])
    r('  lean runs : %d' % ej['lean_runs'])
    r('  ### ### **THE TERMINAL VERDICT: NO RELATION IS DERIVES. THE CENSUS %s.** ### SHORTFALL: %s.' % (ej['census'], ej['shortfall']))
    r('')
    bar()
    r('### COMPONENT 3 -- W-ORD-SPAN-HEADING, THE NAMED REPAIR.')
    bar()
    r('  substitutions applied : %s ; numstat +%s -%s ; write path unchanged : %s' % (cj['applied'], cj['numstat'][0], cj['numstat'][1], cj['write_path_unchanged']))
    r('  fixture (both forms and an unparseable fold heading, by import against a scratch copy) : %s' % cj['fixture'])
    for l in cj['before']:
        r('    before | %s' % l)
    for l in cj['after']:
        r('    after  | %s' % l)
    r('  unparsed fold headings in FINDINGS.md after the repair : %d' % sum(1 for l in cj['after'] if 'UNPARSED' in l))
    r('  the diff:')
    for l in cj['unified'].splitlines():
        r('    %s' % l)
    r('')
    bar()
    r('### THE EXPECTATIONS.')
    bar()
    f15 = c['found']
    r('  (N1) fewer than half of the twenty-eight have a pre-b450 ledger line')
    r('        over the 15 findings : %d of 15 -> %s ; over the twenty-eight : %d of 28 -> %s' % (f15, 'HELD' if f15 * 2 < 15 else 'REFUTED', f15, 'HELD' if f15 * 2 < 28 else 'REFUTED'))
    fc = c['found_if_defect_credited']
    r('        with the defective predicate`s line credited: %d of 15 -> %s ; %d of 28 -> %s' % (fc, 'HELD' if fc * 2 < 15 else 'REFUTED', fc, 'HELD' if fc * 2 < 28 else 'REFUTED'))
    r('  (N2) a nearest terminal exists in a rostered kernel and proves something narrower; the census stays at fifteen')
    r('        exists : HELD (%d by the rule) ; narrower : REFUTED for the rule`s nearest (INTERFACES -- it assumes the claim) and HELD for the second figure (NOT THE CLAIM) ; census stays at fifteen : %s'
      % (len(ej['nearest']), 'HELD' if ej['census'].startswith('STAYS') else 'REFUTED'))
    r('  (N3) the span-heading repair is a single-line change')
    r('        numstat +%s -%s -> %s' % (cj['numstat'][0], cj['numstat'][1], 'HELD' if cj['numstat'] == ['1', '1'] else 'REFUTED'))
    r('  ### the seat`s own from the face: (N1) HELD -- HELD over both populations by the face`s figure; (N2) HELD -- HELD on existence and the census, split on "narrower" as above; (N3) REFUTED -- HELD.')
    bar('=')
    io.open(os.path.join(D, 'b454_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(O) + NL)
    print(NL.join(O))
    return 0


def main(argv):
    mode = argv[0] if argv else ''
    if mode == 'search':
        return do_search()
    if mode == 'enumera':
        return do_enumera()
    if mode == 'grade':
        return do_enumera_grade()
    if mode == 'plan':
        return do_plan_or_write(False)
    if mode == 'write':
        return do_plan_or_write(True)
    if mode == 'report':
        return do_report()
    print('modes: search | enumera | plan | write | report')
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
