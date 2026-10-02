# -*- coding: utf-8 -*-
"""b589_constellation.py -- COMPONENT 2 OF b589, UNDER (R199)(3): W-ORD-CONSTELLATION-RERUN OVER THE ROSTER TABLES.

### ### Per document (one per call, `doc <KEY>`), for the current version and the edition where one exists:
###   (1) the table sections: every heading carrying "Correspondence" down to the next heading of its level or above (b557's tier
###       block and b558's line excluded), or, for a table of another name, b586's start line down to the next heading;
###   (2) rowgen's four source-only checks at each row's pin (rowgen IMPORTED: `extract_doc_body`, `definition_encoded`, `LEAN_NAME`) --
###       MISSING at the pin, STATUS-vs-DOC, DEFINITION-ENCODED; the rounded-profile check printed NOT EXERCISED (no build);
###   (3) the declaration's signature at the row's pin against the kernel's current main (SIG-MOVED, or GONE-AT-MAIN);
###   (4) constellation mode proper (rowgen.constellation, IMPORTED) over the whole file, its flags inside the table sections printed;
###   (5) every moved cell printed and superseded in the table's own row form, IN THIS BANK ONLY (the author's answer: no keystone touched).
### `b454` re-searches b454's ledger table case-insensitively; `summary` writes one line per table. Writes only data/b589_constellation_*.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'rowgen'))
import rowgen  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'b378167'
MATHLIB = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# key: (b586 name, current version path, edition path or None, start line of a table of another name or None)
DOCS = {
    'PATHS': ('PATHS_TO_THE_CRITICAL_LINE', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md', None),
    'SIMP': ('SIMPLICITY_OF_RIEMANN_ZEROS', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', None, None),
    'SURR': ('THE_UNCONDITIONAL_SURROUND', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md', None),
    'GRH': ('GRH_CASCADE', 'phase1.5/spectral/GRH_CASCADE.md', 'phase1.5/spectral/GRH_CASCADE_v0_3_6.md', None),
    'RCURVE': ('R_CURVE_CRITERION', 'phase1.5/rcurve/R_CURVE_CRITERION.md', 'phase1.5/rcurve/R_CURVE_CRITERION_v0_2_2.md', None),
    'INDEX': ('INDEX_ARITY_AT_THE_CRITICAL_LINE', 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md',
              'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE_v0_19.md', None),
    'RESIDUE': ('THE_RESIDUE_OF_RH', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md', None, None),
    'AMC': ('ADDITIVE_MULTIPLICATIVE_CONSPIRACY', 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md',
            'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY_v0_2_4.md', None),
    'FOUND': ('FOUNDATIONS_OF_THE_SIDE_PROGRAMME', 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md',
              'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md', None),
    'TECHNE': ('TECHNE_TOOLKIT', 'phase1.5/method/TECHNE_TOOLKIT.md', 'phase1.5/method/TECHNE_TOOLKIT_v8_3.md', None),
    'SILENCE': ('SILENCE_STAGES_DEALIGNMENT', 'phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md', None, None),
    'LIC': ('EXHAUSTIVENESS_LICENSE', 'phase1.5/method/EXHAUSTIVENESS_LICENSE.md', 'phase1.5/method/EXHAUSTIVENESS_LICENSE_v0_2.md', None),
    'INVAR': ('INVARIANCE_BARRIERS', 'phase1.5/method/INVARIANCE_BARRIERS.md', 'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md', None),
    'REPARAM': ('REPARAMETERIZATION_BARRIERS_v0_1', 'phase2/method/REPARAMETERIZATION_BARRIERS_v0_1.md', None, None),
    'MONO': ('A_Place_to_Stand', 'day1/A_Place_to_Stand.md', None, None),
    'BALPOS': ('BALANCE_AND_POSITIVITY', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md', None, 343),
    'FACES': ('FACES_OF_H2_AT_FINITE_INSTANCE', 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md', None, 40),
    'LEDGER': ('FACES_LEDGER', 'FACES_LEDGER.md', None, 16),
    'IDC': ('THE_IDENTITY_CHAIN', 'phase2/method/THE_IDENTITY_CHAIN.md', None, 564),
    'EDIFF': ('E_DIFFICULTY_THEOREM', None, 'phase2/method/E_DIFFICULTY_THEOREM_v1_0_4.md', None),
}
DEFAULT_REPOS = ['SIDE-kernel', 'SIDE-explicit-formula', 'SIDE-lv-conservation']
DECL_KW = r'(theorem|lemma|def|abbrev|structure|class|instance|inductive|opaque|axiom)'


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def b586_rows():
    t = io.open(os.path.join(D, 'b586_corroboration.txt'), encoding='utf-8').read().replace(chr(13), '')
    out = {}
    for l in t.split(NL):
        if l.startswith('| ') and not l.startswith('| document') and not l.startswith('|:'):
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            if len(c) >= 6:
                out[c[0]] = dict(kernels=[k.strip() for k in c[4].split(',') if k.strip().startswith('SIDE-')],
                                 pins=[p.strip() for p in c[5].split(',') if re.fullmatch(r'[0-9a-f]{7,40}', p.strip())])
    return out


def sections(lines, start=None):
    """### [(first, last)] 1-based line ranges of the table sections."""
    out = []
    # ### every cascade tier block (b556's ACT TEN as well as b557's ACT ELEVEN) is the cascade's re-read, not the document's table
    stop_marks = ('<!-- b55', '#### THE CASCADE', '*Appended 2026-09-29 by b558', '*Appended 2026-09-28 by b55')
    if start:
        e = start
        while e < len(lines) and not (lines[e].startswith('#') and e + 1 > start):
            e += 1
        return [(start, e)]
    for i, l in enumerate(lines):
        m = re.match(r'^(#{1,6})\s+(.*)$', l)
        if m and 'correspondence' in m.group(2).lower() and not l.startswith('#### THE CASCADE'):
            lvl = len(m.group(1))
            e = i + 1
            while e < len(lines):
                m2 = re.match(r'^(#{1,6})\s', lines[e])
                if (m2 and len(m2.group(1)) <= lvl) or lines[e].startswith(stop_marks):
                    break
                e += 1
            out.append((i + 1, e))
    return out


def terminal_names(row):
    out = []
    for n in re.findall(r'`(' + rowgen.LEAN_NAME + r')`', row):
        if ('_' in n or '.' in n) and not re.search(r'\.(lean|md|json|txt|py|svg|pdf)$', n) and not re.fullmatch(r'v[\d.]+', n) \
                and not re.fullmatch(r'[0-9a-f._]+', n) and not n.isupper() and n not in out:
            out.append(n)
    return out


_CACHE = {}
# ### THE SEAT'S HAND-READ of the backticked names a first run flagged MISSING that are not terminals (each row read whole):
HAND_NOT_TERMINAL = {
    'm_k': 'a variable of the row`s formula (INDEX_ARITY :385)',
    'b_j': 'a variable of the row`s formula (INDEX_ARITY :385)',
    'field_simp': 'a tactic name (INDEX_ARITY :385)',
    'h_conserved': 'a hypothesis binder of `e_difficulty` (FOUNDATIONS :633)',
    'no_conspiracy': 'the row itself reads "NONE -- OPEN ... no verification exists" (ADDITIVE_MULTIPLICATIVE :451)',
    'padicFourierData_exists': 'the row names it "NOT compiled in Mathlib", the B-C debt (THE_IDENTITY_CHAIN :565)',
}


def find_decl(repo, rev, name):
    """### (file, line, signature) of `name` at `rev` in `repo`, by git grep; None when absent."""
    k = (repo, rev, name)
    if k in _CACHE:
        return _CACHE[k]
    short = name.split('.')[-1]
    rx = r'^[[:space:]]*(@\[[^]]*\][[:space:]]*)?((private|protected|noncomputable|nonrec|unsafe|partial)[[:space:]]+)*' + DECL_KW + \
         r'[[:space:]]+([^[:space:]]*\.)?' + re.escape(short).replace('\\', '\\\\') + r'([[:space:]]|$|:)'
    rc, out = g(repo, 'grep', '-n', '-E', rx, rev, '--', '*.lean')
    hits = [l for l in out.split(NL) if l.strip()]
    if not hits:
        # ### a structure field (b589 defect (c)): `  name : type` inside a structure of the file
        rcf, outf = g(repo, 'grep', '-n', '-E', r'^[[:space:]]+' + re.escape(short).replace('\\', '\\\\') + r'[[:space:]]*:[^=]', rev, '--', '*.lean')
        hits = [l for l in outf.split(NL) if l.strip()][:1]
    if '.' in name and len(hits) > 1:
        ns = name.split('.')[-2]
        pref = [h for h in hits if ns.lower() in h.lower()]
        hits = pref or hits
    if not hits:
        _CACHE[k] = None
        return None
    parts = hits[0].split(':', 3)
    f, ln = parts[1], int(parts[2])
    rc2, src = g(repo, 'show', '%s:%s' % (rev, f))
    sl = src.split(NL)
    sig = []
    j = ln - 1
    while j < len(sl) and len(sig) < 14:
        sig.append(sl[j])
        if ':=' in sl[j] or re.search(r'\bwhere\b', sl[j]):
            break
        j += 1
    s = ' '.join(x.strip() for x in sig)
    s = re.sub(r'\s+', ' ', s.split(':=')[0]).strip()
    _CACHE[k] = (f, ln, s, src)
    return _CACHE[k]


_FED = {}
FED_EXTRA = ['D:/MY-DOwnloads/TECHNE-Core', 'D:/MY-DOwnloads/TECHNE_Core']


def main_ref(repo):
    return 'main' if g(repo, 'rev-parse', '--verify', '-q', 'main')[0] == 0 else 'HEAD'


def current_ref(repo, pin):
    """### the kernel's current pin for a row's pin: main when the pin is main or an ancestor of it; otherwise the head of the branch
    ### that holds the pin (a branch-held terminal is current at its branch, never at main -- b589 defect (c))."""
    m = main_ref(repo)
    if pin in ('main', 'HEAD') or subprocess.run(['git', '-C', repo, 'merge-base', '--is-ancestor', pin, m]).returncode == 0:
        return m
    brs = [b.strip() for b in g(repo, 'branch', '--format=%(refname:short)', '--contains', pin)[1].split(NL) if b.strip()]
    brs = [b for b in brs if not b.startswith('push-')] or brs
    return brs[0] if brs else m


def fed_index():
    """### short name -> [repository] over every D:/SIDE-* kernel and the two local TECHNE-Core clones, from one git grep each at main."""
    if _FED:
        return _FED
    repos = sorted('D:/' + d for d in os.listdir('D:/') if d.startswith('SIDE-') and os.path.isdir('D:/%s/.git' % d)) + \
        [r for r in FED_EXTRA if os.path.isdir(r + '/.git')]
    rx = r'^[[:space:]]*(@\[[^]]*\][[:space:]]*)?((private|protected|noncomputable|nonrec|unsafe|partial)[[:space:]]+)*' + DECL_KW + r'[[:space:]]+'
    for r in repos:
        rc, out = g(r, 'grep', '-h', '-E', rx, main_ref(r), '--', '*.lean')
        for l in out.split(NL):
            m = re.search(DECL_KW + r'\s+([^\s(:{\[]+)', l)
            if m:
                _FED.setdefault(m.group(2).split('.')[-1], [])
                if r not in _FED[m.group(2).split('.')[-1]]:
                    _FED[m.group(2).split('.')[-1]].append(r)
    _FED['__repos__'] = repos
    return _FED


def resolve_pin(repo, tokens):
    for t in tokens:
        rc, _ = g(repo, 'cat-file', '-e', t + '^{commit}')
        if rc == 0:
            return t
    return None


def check_row(row, names, kernels, doc_pins):
    """### Each terminal name of the row: its repo and pin, the four source-only checks, the signature at main."""
    hexes = re.findall(r'\b([0-9a-f]{7,40})\b', row)
    tags = re.findall(r'\bv\d+(?:\.\d+)+\b', row)
    res = []
    for n in names:
        if n in HAND_NOT_TERMINAL:
            res.append(dict(name=n, repo=None, pin=None, flags=[], notes=['hand-read: not a terminal cell -- %s' % HAND_NOT_TERMINAL[n]]))
            continue
        found = None
        for repo in kernels:
            path = 'D:/' + repo
            if not os.path.isdir(path):
                continue
            # ### every cited pin resolving in the repository, in the row's order, then the document's, then main (defect (c))
            cands = [t for t in hexes + tags + doc_pins if g(path, 'cat-file', '-e', t + '^{commit}')[0] == 0] + [main_ref(path)]
            for pin in cands:
                d = find_decl(path, pin, n)
                if d:
                    found = (repo, pin, d)
                    break
            if found:
                break
        if not found:
            # ### the federation-wide fall-back (b589 defect (c)): the repositories whose declaration index at main holds the
            # ### short name, then the name at the row's pin there (or main when no cited pin resolves in that repository)
            for path in fed_index().get(n.split('.')[-1], []):
                if path.replace('D:/', '') in kernels:
                    continue
                pin = resolve_pin(path, hexes) or resolve_pin(path, tags) or resolve_pin(path, doc_pins) or 'main'
                d = find_decl(path, pin, n) or (find_decl(path, 'HEAD', n) if pin == 'main' else None)
                if d:
                    found = (path.replace('D:/', ''), pin, d)
                    break
        if not found:
            md = find_decl(MATHLIB, 'HEAD', n)
            res.append(dict(name=n, repo='Mathlib' if md else None, pin='de5ce8a9' if md else None,
                            flags=[] if md else ['MISSING: no declaration at the row`s pin in %s or Mathlib' % kernels]))
            continue
        repo, pin, (f, ln, sig, src) = found
        flags = []
        doc, body1 = rowgen.extract_doc_body(src, n)
        low = row.lower()
        if 'derives' in low and any(w in doc.lower() for w in ('stand-in', 'encoded', 'placeholder', 'deprecated', 'assigns')):
            flags.append('STATUS-vs-DOC: the row says DERIVES; the docstring says "%s"' % doc[:80])
        enc, why = rowgen.definition_encoded(src, sig.split(':', 1)[-1] if ':' in sig else sig)
        notes = []
        if enc and 'derives' in low and 'encodes' not in low:
            rhs = why.split(':=', 1)[-1].strip()
            if rhs in ('0', '1', 'true', 'false', 'True', 'False'):
                flags.append('DEFINITION-ENCODED: %s, the row reads DERIVES' % why)
            else:
                # ### rowgen's prefix rule `^(True|False|0|1)\b` reads a body beginning with 1 as the literal 1; its README defines the
                # ### flag as a body that IS a literal constant or True -- printed, read, not counted (b589 defect (c))
                notes.append('rowgen DEFINITION-ENCODED raised on `%s`, read: the body is not a literal constant, not counted' % why)
        mref = current_ref('D:/' + repo, pin)
        mm = find_decl('D:/' + repo, mref, n)
        main_sha = mref + ' ' + g('D:/' + repo, 'rev-parse', '--short=7', mref)[1].strip()
        if not mm:
            flags.append('GONE-AT-MAIN: the declaration is absent at %s main %s' % (repo, main_sha))
        elif mm[2] != sig:
            flags.append('SIG-MOVED: at %s main %s the signature reads "%s" (at %s: "%s")' % (repo, main_sha, mm[2][:160], pin, sig[:160]))
        res.append(dict(name=n, repo=repo, pin=pin, file=f, line=ln, sig=sig[:300], flags=flags, notes=notes))
    return res


_INDEX = []


def doc(key):
    name, curp, edp, start = DOCS[key]
    meta = b586_rows().get(name, dict(kernels=[], pins=[]))
    kernels = meta['kernels'] + [r for r in DEFAULT_REPOS if r not in meta['kernels']]
    if not _INDEX:
        _INDEX.append(rowgen.build_corpus_index(PP))
    files, reg = _INDEX[0]
    L = ['b589 -- COMPONENT 2: THE CONSTELLATION RE-READ OF %s, (R199)(3). ### A BANK; NO KEYSTONE IS TOUCHED (the author`s answer).' % name, '',
         '### kernels searched (b586`s column, then the defaults): %s ; the document`s pins (b586): %s' % (kernels, meta['pins']),
         '### the rounded-profile check: NOT EXERCISED (source only, no build).', '']
    summ = dict(doc=name, versions={}, moved=0, rows=0, names=0)
    for which, p in (('current', curp), ('edition', edp)):
        if not p:
            continue
        fp = os.path.join(PP, *p.split('/'))
        if not os.path.exists(fp):
            L.append('### %s %s : ### THE FILE IS ABSENT -- HELD for this version' % (which, p))
            summ['versions'][which] = 'ABSENT'
            continue
        lines = io.open(fp, encoding='utf-8', errors='replace').read().replace(chr(13), '').split(NL)
        secs = sections(lines, start if which == 'current' else None)
        L.append('### %s : %s (%d lines) ; table sections %s' % (which.upper(), p, len(lines), [':%d-:%d' % s for s in secs]))
        rows = []
        seen = set()
        for a, b in secs:
            for i in range(a, b + 1):
                l = lines[i - 1] if i - 1 < len(lines) else ''
                if i in seen:
                    continue
                seen.add(i)
                if l.strip().startswith('|') and not re.match(r'^\|[\s:|-]+\|?$', l.strip()):
                    nm = terminal_names(l)
                    if nm:
                        rows.append((i, l, nm))
        moved = []
        nnames = 0
        for i, l, nm in rows:
            r = check_row(l, nm, kernels, meta['pins'])
            nnames += len(r)
            fl = [x for x in r if x['flags']]
            L.append('    :%-5d %s' % (i, ' ; '.join('%s @ %s %s %s' % (x['name'], x['repo'], x['pin'], ('ok' if not x['flags'] else '### ' + ' | '.join(x['flags'])) + ''.join(' [%s]' % t for t in x.get('notes', [])))
                                                   for x in r)[:900]))
            if fl:
                moved.append((i, l, fl))
        cflags = rowgen.constellation(fp, files, reg)
        in_tab = [f for f in cflags if any(a <= f[0] <= b for a, b in secs)]
        kinds = {}
        for f in cflags:
            kinds[f[4]] = kinds.get(f[4], 0) + 1
        L.append('  ### constellation mode (cross-references) over the whole file: %d flag(s) %s ; inside the table sections %d' % (
            len(cflags), kinds, len(in_tab)))
        for f in in_tab:
            L.append('      :%d %s -- %s [%s]' % (f[0], f[1], f[2], f[4]))
        L.append('  ### rows naming a terminal %d ; names read %d ; cells moved %d' % (len(rows), nnames, len(moved)))
        for i, l, fl in moved:
            L.append('  ### MOVED :%d (%s)' % (i, which))
            L.append('      the row      : %s' % l[:600])
            sup = l.rstrip()
            sup = sup[:-1].rstrip() + ' *(superseded at b589: %s)* |' % '; '.join('%s -- %s' % (x['name'], x['flags'][0][:200]) for x in fl)
            L.append('      superseding  : %s' % sup[:900])
        summ['versions'][which] = dict(path=p, rows=len(rows), names=nnames, moved=[(i, [x['name'] for x in fl], [x['flags'] for x in fl]) for i, l, fl in moved],
                                       constellation=len(cflags), constellation_in_table=len(in_tab), kinds=kinds)
        summ['moved'] += len(moved)
        summ['rows'] += len(rows)
        summ['names'] += nnames
        L.append('')
    put_txt('b589_constellation_%s.txt' % name, L)
    put_json('b589_constellation_%s.json' % name, summ)
    print(name, 'rows', summ['rows'], 'names', summ['names'], 'moved', summ['moved'])


B454_SHAPES = [  # b454's registration :84-:91; S1 and S2 as predicates over a line, applied with and without case
    ('W_inf NOT sign-definite', lambda l, c: ('sign-definite' in c(l)) and (' not' in c(l) or 'not ' in c(l)), lambda l, c: 'sign-definite' in c(l) or 'sign definite' in c(l)),
    ('the Day-1 section I attribution pole-plus-archimedean', lambda l, c: 'pole-plus-archimedean' in c(l),
     lambda l, c: 'pole' in c(l) and 'archimedean' in c(l) and any(x in c(l) for x in (c('Day-1'), '§i', c('§I'), 'attribution'))),
    ('Face E / keyhole', lambda l, c: 'keyhole' in c(l), lambda l, c: c('Face E') in c(l)),
    ('the T3 Tier-1 scope', lambda l, c: c('T3') in c(l) and (c('Tier-1') in c(l) or c('Tier 1') in c(l)) and 'scope' in c(l),
     lambda l, c: c('T3') in c(l) and (c('Tier-1') in c(l) or c('Tier 1') in c(l))),
    ('the E-Difficulty cross-link verdict DISTINCT', lambda l, c: 'cross-link' in c(l) and c('DISTINCT') in c(l),
     lambda l, c: c('DISTINCT') in c(l) and (c('E-Difficulty') in c(l) or 'κ' in l)),
    ('the two-kinds windows verdict', lambda l, c: ('two-kinds' in c(l) or 'two kinds' in c(l)) and 'window' in c(l),
     lambda l, c: 'index truncation' in c(l) and 'support truncation' in c(l)),
    ('the S2 Ostrowski seal', lambda l, c: c('S2') in c(l) and c('Ostrowski') in c(l) and 'seal' in c(l), lambda l, c: c('S2') in c(l) and c('Ostrowski') in c(l)),
    ('the sign-face registers', lambda l, c: 'sign-face' in c(l) and 'register' in c(l), lambda l, c: 'sign-face' in c(l) or 'sign face' in c(l)),
]
B454_FIXED = '687aa24'


def _ledgers():
    fs = ['FINDINGS.md', 'OPEN_TRAILS.md'] + sorted(f for f in g(PP, 'ls-tree', '--name-only', B454_FIXED, 'archive/2026-08-24-ledger-split/')[1].split(NL)
                                                   if f.endswith('.md'))
    return [(f, g(PP, 'show', '%s:%s' % (B454_FIXED, f))[1].split(NL)) for f in fs]


# ### THE HAND-READ OF THE HITS THE CASE-INSENSITIVE SHAPES ADD, entered by the seat after `b454 dry` printed every one of them,
# ### by b454's rule (relay data/b454_registration_2026-09-14.txt :92-:94): a hit HOLDS only if the line states the finding's content.
_ARC2 = 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'
_VL1 = 'VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md'
_FA1 = 'FINDINGS-archive-1-entries-through-2026-08-20c.md'
HAND = {
    _ARC2 + ':8768': 'HOLDS -- the archimedean kernel negative at low frequency and positive at high, crossing at u = 2pi (the row was FOUND already)',
    _ARC2 + ':8770': 'HOLDS -- "Day-1 §II should read the positive POLE-PLUS-ARCHIMEDEAN term dominates the indefinite prime term" '
                     '(b450`s label says section I where the ledger says §II)',
    'OPEN_TRAILS.md:531': 'HOLDS -- the index line states the verdict: KEYHOLE (i)`s STATUS -- DISTINCT',
    'OPEN_TRAILS.md:2980': 'does not hold -- "check the dependents (dark-interface ...)": the shape matched inside a word',
    'OPEN_TRAILS.md:3822': 'does not hold -- "does a surface exist": the shape matched inside a word',
    _FA1 + ':357': 'does not hold -- "if a new face exists": the shape matched inside a phrase',
    _ARC2 + ':6609': 'HOLDS -- the section heading states the verdict: KEYHOLE (i)`s STATUS -- DISTINCT',
    _ARC2 + ':6613': 'HOLDS -- "Keyhole (i) is PRIMITIVE in the Face-E register ... DERIVED in the geometric register"',
    _VL1 + ':2027': 'does not hold -- a held-landing recommendation; the shape matched inside a phrase',
    _VL1 + ':5525': 'does not hold -- "a new rank-face either": the shape matched inside a phrase',
    'OPEN_TRAILS.md:773': 'HOLDS -- the index line states the verdict: THE E-DIFFICULTY CROSS-LINK: DISTINCT. THE DEFINITIONS DO NOT REACH',
    _FA1 + ':160': 'does not hold -- a register property; "distinct" and κ only',
    _FA1 + ':163': 'does not hold -- the κ = 0 property; "distinct" and κ only',
    _FA1 + ':265': 'does not hold -- a registered criterion; "distinct" and κ only',
    _ARC2 + ':1972': 'does not hold -- a three-arm probe; "distinct" and κ only',
    _ARC2 + ':2013': 'does not hold -- a gate-read package; "distinct" and κ only',
    _ARC2 + ':8839': 'HOLDS -- the landing`s section heading states the verdict: DISTINCT. THE DEFINITIONS DO NOT REACH',
    _VL1 + ':2406': 'does not hold -- the replication finding, another subject',
    _VL1 + ':3908': 'does not hold -- a cross-link list; "distinct" and κ only',
    'OPEN_TRAILS.md:606': 'HOLDS -- the sign-face literature table named (the row was FOUND already)',
    'OPEN_TRAILS.md:614': 'HOLDS -- the sign-face map named (the row was FOUND already)',
    _ARC2 + ':6453': 'does not hold -- the stop at the sign face, not the registers',
    _ARC2 + ':7402': 'HOLDS -- the sign-face literature table (the row was FOUND already)',
    _ARC2 + ':7472': 'HOLDS -- the sign-face map at its depth (the row was FOUND already)',
    _ARC2 + ':8740': 'HOLDS -- the sign face as deposited (the row was FOUND already)',
}


def b454(*a):
    """### b454's ledger table (OPEN_TRAILS :6755-:6766) re-searched case-insensitively at b454's own fixed ledgers (687aa24 and the archive)."""
    same = lambda s: s
    low = lambda s: s.lower()
    led = _ledgers()
    L = ['b589 -- COMPONENT 2 (b): b454`S LEDGER TABLE RE-SEARCHED CASE-INSENSITIVELY, (R199)(3). ### b454`s shapes (relay '
         'data/b454_registration_2026-09-14.txt :84-:91) at b454`s fixed ledgers (PLACE-papers %s and the archive); every hit the case-insensitive '
         'shapes add, beyond the case-sensitive ones b454 read, printed and hand-read.' % B454_FIXED, '']
    table = g(PP, 'show', '%s:OPEN_TRAILS.md' % PRE_PP)[1].split(NL)[6754:6766]
    state = {}
    for name, s1, s2 in B454_SHAPES:
        hs, hi = [], []
        for f, ls in led:
            for i, l in enumerate(ls, 1):
                if s1(l, same) or s2(l, same):
                    hs.append((f, i))
                if s1(l, low) or s2(l, low):
                    hi.append((f, i, l))
        added = [(f, i, l) for f, i, l in hi if (f, i) not in set(hs)]
        row = [r for r in table if r.startswith('| %s |' % name)]
        b454v = row[0].split('|')[5].strip() if row else '?'
        L.append('### %s -- b454: %s ; case-sensitive hits %d ; case-insensitive hits %d ; added %d' % (name, b454v, len(hs), len(hi), len(added)))
        holds = []
        for f, i, l in added:
            v = HAND.get('%s:%d' % (os.path.basename(f), i), '### NOT YET READ')
            if v.startswith('HOLDS'):
                holds.append('%s :%d' % (os.path.basename(f), i))
            L.append('      %s :%d -- %s -- %s' % (os.path.basename(f), i, v, l.strip()[:260]))
        st = ('LOCATED BY THE CASE-INSENSITIVE SHAPES at %s' % holds[0]) if holds and 'FOUND' not in b454v else (
            'FOUND, as b454 read it' if 'FOUND' in b454v else 'HELD BY NO LEDGER, the added hits read and none holding')
        state[name] = dict(b454=b454v, sensitive=len(hs), insensitive=len(hi), added=len(added), holds=holds, state=st,
                           unread=sum(1 for f, i, l in added if '%s:%d' % (os.path.basename(f), i) not in HAND))
        L.append('    ### STATE: %s' % st)
        L.append('')
    newly = [k for k, v in state.items() if v['state'].startswith('LOCATED')]
    L.append('### ### **ROWS NEWLY LOCATED: %d %s ; rows unread %d.**' % (len(newly), newly, sum(v['unread'] for v in state.values())))
    if 'dry' in a:
        for l in L:
            print(l[:400])
        return
    put_txt('b589_constellation_b454.txt', L)
    put_json('b589_constellation_b454.json', state)


def summary():
    rows = []
    tot = 0
    for key, (name, curp, edp, start) in DOCS.items():
        p = os.path.join(D, 'b589_constellation_%s.json' % name)
        if not os.path.exists(p):
            rows.append('| %s | ### NOT RUN -- HELD | | | |' % name)
            continue
        s = json.load(io.open(p, encoding='utf-8'))
        tot += s['moved']
        where = []
        for w, v in s['versions'].items():
            if isinstance(v, dict) and v['moved']:
                where.append('%s :%s' % (w, ', :'.join(str(m[0]) for m in v['moved'])))
        rows.append('| %s | %d | %d | %d | %s |' % (name, s['rows'], s['names'], s['moved'], '; '.join(where) or '--'))
    b = json.load(io.open(os.path.join(D, 'b589_constellation_b454.json'), encoding='utf-8')) if os.path.exists(os.path.join(D, 'b589_constellation_b454.json')) else {}
    newly = [k for k, v in b.items() if v['state'].startswith('LOCATED')]
    L = ['b589 -- COMPONENT 2: THE CONSTELLATION RE-READ, ONE LINE PER TABLE. ### the banks data/b589_constellation_<doc>.txt.', '',
         '| table | rows naming a terminal | names read | cells moved | where (current / edition) |', '|:--|--:|--:|--:|:--|'] + rows + [
        '', '### ### **TABLES READ: %d. ### CELLS MOVED: %d. ### b454`S TABLE: ROWS NEWLY LOCATED %d %s.**' % (
            sum(1 for r in rows if 'NOT RUN' not in r), tot, len(newly), newly)]
    put_txt('b589_constellation_summary.txt', L)
    put_json('b589_constellation_summary.json', dict(tables=sum(1 for r in rows if 'NOT RUN' not in r), moved=tot, newly=newly))
    for l in L[-3:]:
        print(l)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'doc':
        doc(sys.argv[2])
    elif cmd == 'b454':
        b454(*sys.argv[2:])
    elif cmd == 'summary':
        summary()
    else:
        print('usage: b589_constellation.py doc <KEY> | b454 [dry] | summary')
        sys.exit(2)
