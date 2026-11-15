# -*- coding: utf-8 -*-
"""b756_constellation.py -- COMPONENT 2 OF b756, UNDER (R366)(4)(i): THE RERUN OF THE CONSTELLATION MAP OVER THE ROSTER'S CURRENT EDITIONS.

Carried from tools/b589_constellation.py by tools/standing/carry.py (data/b756_carry_constellation.txt: the substitution b589 -> b756, the
tool's own name at :2 and the usage line shifted past what existed, written by --shifted) and committed before its run ((R366)(4)(i): "carried
from tools/b589_constellation.py and committed before its run"; the ferry's N2). ### THE SEAT'S REPAIRS OF THE CARRIED FORM, by the Edit tool
before any run:
###   (a) THE POPULATION. b589's twenty keys (b586's census, a current version and an edition a key) give way to the roster's current
###       editions, read at run time from `tools/standing/roster.py json` (the builder's roster; 83 files at b755's mirror). A document of it
###       CARRIES A CORRESPONDENCE TABLE when its table sections (rule (1) below) hold at least one row naming a terminal (b589's
###       terminal_names); each such document is read once, at the edition the roster carries, so b589's second version per key falls away.
###       A file with a table section and no row naming a terminal is listed in the summary bank with its counts and not read further.
###   (b) THE FOUR TABLES OF ANOTHER NAME (b586's start lines, b589's keys BALPOS, FACES, LEDGER, IDC): each start line located in today's
###       file by the text b589's start line held at PLACE-papers b378167 (PRE_PP), found exactly once or HELD; its sections are the start
###       line's range together with every Correspondence heading the file now carries (b589 read the start range alone).
###   (c) THE KERNELS: b586's kernels and pins columns (data/b586_corroboration.txt) read by the document's family, its `_v<n>` suffix removed
###       on both sides; a document b586 does not name takes the defaults and the federation-wide fall-back, as at b589.
###   (d) NO FETCH: each kernel's main read as the host holds it (`main`, else HEAD); the tool's git calls read (grep, show, rev-parse,
###       cat-file, merge-base, branch --contains, ls-tree); nothing is fetched and nothing written in any repository ((R366)(8); the seat's
###       read at step zero, data/b756_stepzero.txt :127-:129).
###   (e) b589's `b454` route (b454's ledger table re-searched, the other half of (R199)(3)) is not ordered by (R366)(4)(i) and is removed with
###       its shapes and its hand-read; the substitution's four citations of b589's own defect (c) set back to b589.
###   (f) THE CONTROLS, b589's (data/b589_registration_2026-10-01.txt :18-:20, "the constellation re-read of REPARAMETERIZATION_BARRIERS_v0_1
###       alone, with every write captured -- no subcommand's bank written, the PLACE-papers worktree's status printed unchanged afterwards"):
###       `control <KEY>` runs one document's re-read with every write captured and no document bank written, PLACE-papers' status, the
###       refs and FETCH_HEAD of every repository the tool reads, and the relay's data listing printed before and after. Beside it, the seat's
###       planted pair, beyond b589's: a row naming a declaration that stands at its cited tag reads with no MISSING flag, and a row naming one
###       that no repository holds reads MISSING. Banked as data/b756_constellation_control.txt, printed before any figure.
###   (g) each document's run timed and the seconds banked (data/b756_stepzero.txt :105: "timed at its first run").

### ### Per document (`doc <KEY>`, or `docs <KEY> ...` one after another), at the edition the roster carries:
###   (1) the table sections: every heading carrying "Correspondence" down to the next heading of its level or above (b557's tier
###       block and b558's line excluded), and, for a table of another name, b586's start line down to the next heading;
###   (2) rowgen's four source-only checks at each row's pin (rowgen IMPORTED: `extract_doc_body`, `definition_encoded`, `LEAN_NAME`) --
###       MISSING at the pin, STATUS-vs-DOC, DEFINITION-ENCODED; the rounded-profile check printed NOT EXERCISED (no build);
###   (3) the declaration's signature at the row's pin against the kernel's current main (SIG-MOVED, or GONE-AT-MAIN);
###   (4) constellation mode proper (rowgen.constellation, IMPORTED) over the whole file, its flags inside the table sections printed;
###   (5) every moved cell printed and superseded in the table's own row form, IN THIS BANK ONLY ((R366)(4)(i): "No keystone is written by it").
### `list` prints the population; `summary` writes one line per table. Writes only data/b756_constellation_*.
###   python -X utf8 -u tools/b756_constellation.py list | control <KEY> | doc <KEY> | docs <KEY> ... | summary
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

# ### b589's keys, kept unedited as the source of the four start lines (b586's, at PLACE-papers b378167) and of b589's reading; the
# ### population is population() below. key: (b586 name, current version path, edition path or None, start line or None)
B589_DOCS = {
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
ACT = 'b756'
VER = re.compile(r'_v\d+(?:_\d+)*$')   # ### tools/standing/roster.py's family rule, on a name without its .md


def family(name):
    return VER.sub('', name)


def roster_files():
    """### the roster's current editions: `tools/standing/roster.py json`, the builder's roster (a read of PLACE-papers main; writes nothing)."""
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'standing', 'roster.py'), 'json'], capture_output=True)
    if r.returncode != 0:
        sys.exit('### roster.py json exit %d: %s' % (r.returncode, r.stderr.decode('utf-8', 'replace')[:400]))
    return [p.replace('\\', '/') for p in json.loads(r.stdout.decode('utf-8'))['files']]


def start_now(path, start):
    """### (b): b589's start line located in today's file by the text it held at PLACE-papers PRE_PP; (line, text) or (None, text)."""
    old = g(PP, 'show', '%s:%s' % (PRE_PP, path))[1].split(NL)
    t = old[start - 1] if 0 < start <= len(old) else ''
    now = io.open(os.path.join(PP, *path.split('/')), encoding='utf-8', errors='replace').read().replace(chr(13), '').split(NL)
    hits = [i + 1 for i, l in enumerate(now) if t and l == t]
    return (hits[0] if len(hits) == 1 else None), t


def is_row(l):
    return l.strip().startswith('|') and not re.match(r'^\|[\s:|-]+\|?$', l.strip())


_POP = []


def population():
    """### (a): every roster file with a table section, [dict(key, path, start, start589, held, secs, rows, pipe, lines)], in the roster's
    ### order; `rows` the rows naming a terminal, `pipe` the table rows; a document carries a correspondence table when rows > 0."""
    if _POP:
        return _POP
    starts = dict((cur, st) for (_nm, cur, _ed, st) in B589_DOCS.values() if st)
    for p in roster_files():
        fp = os.path.join(PP, *p.split('/'))
        if not p.endswith('.md') or not os.path.exists(fp):
            continue
        lines = io.open(fp, encoding='utf-8', errors='replace').read().replace(chr(13), '').split(NL)
        st, held = None, False
        if p in starts:
            st, _t = start_now(p, starts[p])
            held = st is None
        secs = sections(lines, st)
        if not secs and not held:
            continue
        seen, rows, pipe = set(), 0, 0
        for a, b in secs:
            for i in range(a, b + 1):
                if i in seen or i - 1 >= len(lines):
                    continue
                seen.add(i)
                if is_row(lines[i - 1]):
                    pipe += 1
                    rows += 1 if terminal_names(lines[i - 1]) else 0
        _POP.append(dict(key=os.path.basename(p)[:-3], path=p, start=st, start589=starts.get(p), held=held, secs=secs, rows=rows,
                         pipe=pipe, lines=len(lines)))
    keys = [d['key'] for d in _POP if d['rows']]
    if len(keys) != len(set(keys)):
        sys.exit('### TWO DOCUMENTS OF THE POPULATION SHARE A KEY: %s' % sorted(k for k in keys if keys.count(k) > 1))
    return _POP


def listing():
    pop = population()
    read = [d for d in pop if d['rows']]
    print('### THE ROSTER`S CURRENT EDITIONS (tools/standing/roster.py json): %d files ; with a table section %d ; carrying a correspondence '
          'table (a row naming a terminal) %d' % (len(roster_files()), len(pop), len(read)))
    for d in pop:
        print('  %-4s %-52s rows naming a terminal %-4d table rows %-4d sections %s%s' % (
            'READ' if d['rows'] else '--', d['key'][:52], d['rows'], d['pipe'], [':%d-:%d' % s for s in d['secs']][:6],
            (' ; b586`s start :%d at %s, now %s' % (d['start589'], PRE_PP, (':%d' % d['start']) if d['start'] else 'HELD')) if d['start589'] else ''))
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
        out.append((start, e))   # ### b756 (b): the start line's range together with the headings below (b589 returned it alone)
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
# ### THE SEAT'S HAND-READ AT b589, carried unedited, of the backticked names a first run flagged MISSING that are not terminals (each row read whole):
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
            res.append(dict(name=n, repo=None, pin=None, flags=[], notes=['b589`s hand-read: not a terminal cell -- %s' % HAND_NOT_TERMINAL[n]]))
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


def meta_for(key):
    """### (c): b586's row for the document's family, (b586 name, dict(kernels, pins)); (None, empty) where b586 names none."""
    for nm, m in b586_rows().items():
        if family(nm) == family(key):
            return nm, m
    return None, dict(kernels=[], pins=[])


def doc(key):
    pop = dict((x['key'], x) for x in population() if x['rows'])
    if key not in pop:
        sys.exit('### %s is not a document of the population carrying a correspondence table (`list` prints the population)' % key)
    t0 = time.time()
    dd = pop[key]
    name, start = key, dd['start']
    b586, meta = meta_for(key)
    kernels = meta['kernels'] + [r for r in DEFAULT_REPOS if r not in meta['kernels']]
    if not _INDEX:
        _INDEX.append(rowgen.build_corpus_index(PP))
    files, reg = _INDEX[0]
    L = ['b756 -- COMPONENT 2: THE CONSTELLATION RE-READ OF %s, (R366)(4)(i). ### A BANK; NO KEYSTONE IS WRITTEN BY IT ((R366)(4)(i)).' % name, '',
         '### the roster`s current edition %s (tools/standing/roster.py json), at PLACE-papers HEAD %s ; each kernel`s main as the host holds it, '
         'nothing fetched' % (dd['path'], g(PP, 'rev-parse', '--short=7', 'HEAD')[1].strip()),
         '### b586`s row: %s ; kernels searched (b586`s column, then the defaults): %s ; the document`s pins (b586): %s' % (
             b586 or 'NONE (a document b586 does not name)', kernels, meta['pins'])]
    if dd['start589']:
        L.append('### a table of another name: b586`s start line :%d at PLACE-papers %s, located now at %s' % (
            dd['start589'], PRE_PP, (':%d' % start) if start else 'HELD (its text not found exactly once)'))
    L += ['### the rounded-profile check: NOT EXERCISED (source only, no build).', '']
    summ = dict(doc=name, path=dd['path'], b586=b586, versions={}, moved=0, rows=0, names=0, flag_kinds={})
    for which, p in (('current edition', dd['path']),):
        fp = os.path.join(PP, *p.split('/'))
        lines = io.open(fp, encoding='utf-8', errors='replace').read().replace(chr(13), '').split(NL)
        secs = sections(lines, start)
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
                for x in fl:
                    for fx in x['flags']:
                        k = fx.split(':')[0]
                        summ['flag_kinds'][k] = summ['flag_kinds'].get(k, 0) + 1
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
            sup = sup[:-1].rstrip() + ' *(superseded at b756: %s)* |' % '; '.join('%s -- %s' % (x['name'], x['flags'][0][:200]) for x in fl)
            L.append('      superseding  : %s' % sup[:900])
        summ['versions'][which] = dict(path=p, rows=len(rows), names=nnames, moved=[(i, [x['name'] for x in fl], [x['flags'] for x in fl]) for i, l, fl in moved],
                                       constellation=len(cflags), constellation_in_table=len(in_tab), kinds=kinds)
        summ['moved'] += len(moved)
        summ['rows'] += len(rows)
        summ['names'] += nnames
        L.append('')
    summ['seconds'] = round(time.time() - t0, 1)
    L.append('### ### **%s: ROWS NAMING A TERMINAL %d ; NAMES READ %d ; ROWS MOVED OR GONE %d %s ; %.1f s.**' % (
        name, summ['rows'], summ['names'], summ['moved'], summ['flag_kinds'], summ['seconds']))
    put_txt('b756_constellation_%s.txt' % name, L)
    put_json('b756_constellation_%s.json' % name, summ)
    print(name, 'rows', summ['rows'], 'names', summ['names'], 'moved', summ['moved'], summ['flag_kinds'], '%.1f s' % summ['seconds'])


# ### b756 (e): b589's `b454` route (its shapes, its fixed ledgers, its hand-read and the route) removed here, not ordered by (R366)(4)(i).
def _repos_read():
    """### every repository the tool may read: PLACE-papers, each D:/SIDE-* clone, the two TECHNE-Core clones, the Mathlib checkout."""
    rs = [PP] + sorted('D:/' + d for d in os.listdir('D:/') if d.startswith('SIDE-') and os.path.isdir('D:/%s/.git' % d)) + \
        [r for r in FED_EXTRA if os.path.isdir(r + '/.git')] + ([MATHLIB] if os.path.exists(MATHLIB + '/.git') else [])
    return rs


def _state():
    """### the read state the control compares: each repository's refs and FETCH_HEAD time, PLACE-papers' status, the relay's data listing."""
    st = {}
    for r in _repos_read():
        gd = g(r, 'rev-parse', '--git-dir')[1].strip()
        gd = gd if os.path.isabs(gd) else os.path.join(r, gd)
        fh = os.path.join(gd, 'FETCH_HEAD')
        st[r] = (g(r, 'for-each-ref', '--format=%(refname) %(objectname)')[1], os.path.getmtime(fh) if os.path.exists(fh) else None)
    st['__pp_status__'] = g(PP, 'status', '--porcelain')[1]
    st['__data__'] = sorted(os.listdir(D))
    return st


PLANTED_OK = '| planted | `zq_offline_zero` | SIDE-explicit-formula `v0.38` |'
PLANTED_MISS = '| planted | `zz_b756_planted_absent_decl` | SIDE-kernel |'


def control(key):
    """### (f): b589's control, one document's re-read with every write captured, and the seat's planted pair; banked, before any figure."""
    t0 = time.time()
    g_ = globals()
    cap = []
    keep = (g_['put_txt'], g_['put_json'])
    before = _state()
    g_['put_txt'] = lambda name, lines: cap.append((name, len(NL.join(lines))))
    g_['put_json'] = lambda name, obj: cap.append((name, len(json.dumps(obj))))
    try:
        doc(key)
    finally:
        g_['put_txt'], g_['put_json'] = keep
    after = _state()
    want = ['b756_constellation_%s.txt' % key, 'b756_constellation_%s.json' % key]
    moved = [r for r in before if r not in ('__pp_status__', '__data__') and before[r] != after.get(r)]
    c1 = [n for n, _ in cap] == want
    c2 = before['__pp_status__'] == after['__pp_status__']
    c3 = not moved
    c4 = before['__data__'] == after['__data__']
    ok_r = check_row(PLANTED_OK, terminal_names(PLANTED_OK), ['SIDE-explicit-formula'], [])
    miss_r = check_row(PLANTED_MISS, terminal_names(PLANTED_MISS), ['SIDE-kernel'], [])
    c5 = len(ok_r) == 1 and ok_r[0]['repo'] == 'SIDE-explicit-formula' and not any(f.startswith('MISSING') for f in ok_r[0]['flags'])
    c6 = len(miss_r) == 1 and any(f.startswith('MISSING') for f in miss_r[0]['flags'])
    cases = [
        ('b589`s (1)', 'the re-read of %s with every write captured: the writes it would make are its two banks and nothing else' % key, c1,
         '%s' % cap),
        ('b589`s (2)', 'PLACE-papers` status printed unchanged afterwards', c2, '%d status lines before, %d after' % (
            len(before['__pp_status__'].split(NL)) - 1, len(after['__pp_status__'].split(NL)) - 1)),
        ('the seat`s (3)', 'no repository the tool reads moved: refs and FETCH_HEAD equal before and after, over %d repositories (nothing fetched)' % (
            len(before) - 2), c3, 'moved %s' % moved),
        ('the seat`s (4)', 'the relay`s data listing equal before and after (no bank written by the captured run)', c4,
         '%d files before, %d after' % (len(before['__data__']), len(after['__data__']))),
        ('the seat`s (5)', 'the planted row naming a declaration at its cited tag reads with no MISSING flag: %s' % PLANTED_OK, c5,
         '%s' % [(x['name'], x['repo'], x['pin'], x['flags'][:1]) for x in ok_r]),
        ('the seat`s (6)', 'the planted row naming a declaration no repository holds reads MISSING: %s' % PLANTED_MISS, c6,
         '%s' % [(x['name'], x['repo'], x['pin'], [f[:80] for f in x['flags']]) for x in miss_r]),
    ]
    L = ['b756 -- COMPONENT 2: THE CONTROLS OF tools/b756_constellation.py, PRINTED BEFORE ITS FIGURES ((R366)(4)(i): "its controls as b589 ran '
         'them"; the ferry`s N2) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### b589`s control (data/b589_registration_2026-10-01.txt :18-:20): one document`s re-read with every write captured, no bank written,',
         '### PLACE-papers` status unchanged afterwards; at b756 the document %s (the edition the roster carries of b589`s REPARAMETERIZATION_BARRIERS).' % key,
         '### The seat`s, beyond b589`s: the repositories` refs and FETCH_HEAD, the data listing, and a planted pair for the MISSING flag.', '']
    for tag, what, ok, got in cases:
        L.append('  %s %s: %s' % ('AS WANTED' if ok else 'NOT AS WANTED', tag, what))
        L.append('      read: %s' % got[:600])
    n = sum(1 for c in cases if c[2])
    L += ['', '### ### **THE CONTROLS: %d OF %d AS WANTED ; %.1f s.**' % (n, len(cases), time.time() - t0)]
    put_txt('b756_constellation_control.txt', L)
    print(NL.join(L))
    return n == len(cases)


# ### THE SEAT'S HAND-READ AT b756 OF EVERY ROW THE FIRST RUN MOVED (b589's form: each row read whole, by the hand, after the run printed it;
# ### the facts read by git at 14:14:47Z, scratch hand756.py, nothing fetched). (document, line): (counted, class, reading). A row the first run
# ### moved and this table does not name prints NOT YET READ. The document banks stand as run; the summary prints both totals.
HAND_READ = {
    ('ADDITIVE_MULTIPLICATIVE_CONSPIRACY', 412): (True, 'GONE AT MAIN, AS THE ROW SAYS',
        'the three names stand at SIDE-effects c66f3c5 and are absent at its main db0575c; the row reads "Placeholder — retired from the claim structure"'),
    ('FACES_OF_H2_AT_FINITE_INSTANCE', 205): (True, 'SIG-MOVED',
        '`T3_perClass_to_combinations`, a theorem carrying its sorry at the row`s pin v0.10.0, is at SIDE-lv-conservation main 305a87c a def of type '
        'Prop (SIDELvConservation/T3_StepNineBridge.lean :90); the row reads it OPEN and CARRIED'),
    ('FACES_LEDGER', 31): (True, 'SIG-MOVED', 'the same declaration at the row`s pin 93c27ec, the same def at main'),
    ('THE_UNCONDITIONAL_SURROUND', 227): (True, 'SIG-MOVED',
        'the same declaration at the row`s pin v0.2.0, named twice in the row; the row reads "the pin ... carries sorryAx; the closure step has no terminal"'),
    ('THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS_v0_3', 207): (True, 'GONE AT MAIN, READ MISSING BY THE FALL-BACK',
        '`all_gapped` stands at SIDE-effects c66f3c5 (SIDEEffects/Structural.lean :49) and is absent at a27415d and at main db0575c; b586 names no '
        'row for the document, so the defaults were searched, and the federation-wide fall-back indexes each repository at its main alone; the row '
        'reads "retired at the later pin"'),
    ('THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS_v0_3', 259): (True, 'GONE AT MAIN, READ MISSING BY THE FALL-BACK',
        'the same name at the same pin c66f3c5'),
    ('THE_CLAUSE_AND_ITS_COMPILED_FACES', 267): (True, 'DEFINITION-ENCODED BY b589`S RULE',
        'rowgen`s flag fires on `b321Norm := 1` (SIDEExplicitFormula/B321Identity.lean :41), a factor the statement carries by its own docstring (:11); '
        'b589`s rule counts a literal body, and the flag stands by the rule`s words'),
    ('SIMPLICITY_OF_RIEMANN_ZEROS', 446): (False, 'NOT A TERMINAL CELL',
        '`h_at_one` is a hypothesis binder of simplicity_from_trace_structure (SIDE-kernel v1.2 Kernel/PerpendicularCrossing.lean :54), as b589 read '
        '`h_conserved`; the row`s three terminals read ok'),
    ('SIMPLICITY_OF_RIEMANN_ZEROS', 707): (False, 'NOT ON THE HOST, AS THE ROW SAYS',
        '`Zeta23.thmB₀_mult` is named by the row in an upstream repository, "not vendored"; SIDE-explicit-formula names it in a docstring alone '
        '(SIDEExplicitFormula/Simplicity.lean :11 at main, and at 40 local refs)'),
    ('THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION_v0_2', 52): (False, 'NOT A TERMINAL CELL',
        '`native_decide` is a tactic name (the row: "by `decide`, not `native_decide`"), as b589 read `field_simp`'),
    ('THE_LOAD_BEARING_MAP', 54): (False, 'HELD ON A BRANCH, THE ROW CITING NO PIN',
        '`no_onLine_double_iff_transversal` stands in SIDE-kernel on the branch derivative-engine alone (01e5633, Kernel/DerivativeEngine.lean :81), '
        'at no tag and not at main, over the five kernels of SIMPLICITY`s row read at every local branch tip and tag; the row cites no pin'),
    ('THE_LOAD_BEARING_MAP', 162): (False, 'NOT A MOVE AT THE ROW`S LAST PIN',
        'the tool read the row`s first tag v1.1; the row reads "v1.1 -> v1.4 (repaired) -> v1.7", and at v1.4, v1.7 and main the signature is one '
        '(Kernel/Cascade/SieveCeiling.lean)'),
}


def hand_lines(pop):
    """### the hand-read section of the summary: every row a document bank moved, with its reading; (lines, counted, unread)."""
    out, counted, unread = [], 0, 0
    for dd in [x for x in pop if x['rows']]:
        p = os.path.join(D, 'b756_constellation_%s.json' % dd['key'])
        if not os.path.exists(p):
            continue
        s = json.load(io.open(p, encoding='utf-8'))
        for v in s['versions'].values():
            for m in (v.get('moved') or []) if isinstance(v, dict) else []:
                h = HAND_READ.get((dd['key'], m[0]))
                if h is None:
                    unread += 1
                    out.append('  %s :%d -- ### NOT YET READ -- %s' % (dd['key'], m[0], m[2]))
                    continue
                counted += 1 if h[0] else 0
                out.append('  %s :%d -- %s -- %s -- %s' % (dd['key'], m[0], 'COUNTED' if h[0] else 'NOT COUNTED', h[1], h[2]))
    return out, counted, unread


def summary():
    pop = population()
    rows, tot, kinds, secs = [], 0, {}, 0.0
    for dd in [x for x in pop if x['rows']]:
        name = dd['key']
        p = os.path.join(D, 'b756_constellation_%s.json' % name)
        if not os.path.exists(p):
            rows.append('| %s | ### NOT RUN -- HELD | | | | |' % name)
            continue
        s = json.load(io.open(p, encoding='utf-8'))
        tot += s['moved']
        secs += s.get('seconds') or 0
        for k, v in (s.get('flag_kinds') or {}).items():
            kinds[k] = kinds.get(k, 0) + v
        where = []
        for w, v in s['versions'].items():
            if isinstance(v, dict) and v['moved']:
                where.append(':%s' % ', :'.join(str(m[0]) for m in v['moved']))
        rows.append('| %s | %d | %d | %d | %s | %s |' % (name, s['rows'], s['names'], s['moved'], s.get('flag_kinds') or '--', '; '.join(where) or '--'))
    rest = ['  %-56s table rows %-4d sections %d%s' % (x['key'][:56], x['pipe'], len(x['secs']),
                                                     ' ; HELD: b586`s start line :%d not found once' % x['start589'] if x['held'] else '')
            for x in pop if not x['rows']]
    nread = sum(1 for r in rows if 'NOT RUN' not in r)
    hl, hc, hu = hand_lines(pop)
    L = ['b756 -- COMPONENT 2: THE CONSTELLATION RE-READ, ONE LINE PER TABLE, (R366)(4)(i). ### the banks data/b756_constellation_<document>.txt;'
         ' the controls data/b756_constellation_control.txt.', '',
         '### the population: the roster`s current editions (tools/standing/roster.py json, %d files); with a table section %d; carrying a '
         'correspondence table (a row naming a terminal) %d.' % (len(roster_files()), len(pop), len([x for x in pop if x['rows']])), '',
         '| table | rows naming a terminal | names read | rows moved or gone | flags by kind | where |', '|:--|--:|--:|--:|:--|:--|'] + rows + [
        '', '### THE FILES WITH A TABLE SECTION AND NO ROW NAMING A TERMINAL, listed and not read further ((a)): %d' % len(rest)] + rest + [
        '', '### THE SEAT`S HAND-READ OF EVERY ROW THE RUN MOVED (HAND_READ, b589`s form; each row read whole): %d rows, %d counted, %d not yet read' % (
            len(hl), hc, hu)] + hl + [
        '', '### ### **TABLES READ: %d OF %d. ### ROWS MOVED OR GONE BY THE TOOL: %d %s ; AFTER THE HAND-READ: %d COUNTED, %d NOT, %d UNREAD. '
            '### SECONDS SUMMED %.1f.**' % (nread, len([x for x in pop if x['rows']]), tot, kinds, hc, len(hl) - hc - hu, hu, secs)]
    put_txt('b756_constellation_summary.txt', L)
    put_json('b756_constellation_summary.json', dict(tables=nread, population=len([x for x in pop if x['rows']]), moved=tot, kinds=kinds,
                                                     hand_counted=hc, hand_not=len(hl) - hc - hu, hand_unread=hu,
                                                     unread=[x['key'] for x in pop if not x['rows']], seconds=round(secs, 1)))
    for l in L[-3:]:
        print(l)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'list':
        listing()
    elif cmd == 'control':
        sys.exit(0 if control(sys.argv[2]) else 1)
    elif cmd == 'doc':
        doc(sys.argv[2])
    elif cmd == 'docs':
        for k_ in sys.argv[2:]:
            doc(k_)
    elif cmd == 'summary':
        summary()
    else:
        print('usage: b756_constellation.py list | control <KEY> | doc <KEY> | docs <KEY> ... | summary')
        sys.exit(2)
