# -*- coding: utf-8 -*-
"""b544_record.py -- E-6 FILED; THE :1109 NOTE; CP-2 THE T0 INVENTORY AND CP-3 THE INEQUALITY INDEX: THE RECORD, UNDER (R154).
### `python tools/b544_record.py reads | file | note | premises | index | table | findings | components | desk | trail`
### (the enumeration and the probes are `tools/b544_probe_part.py decls | probe <repo>`)

### ERRATA takes one append and one bullet; FINDINGS one line beneath :1109 and two appends; OPEN_TRAILS one append. The name on
### FINDINGS.md:1109 is never printed: this file masks it wherever it would appear. TECHNE-Core`s names never leave memory.
### This file deletes nothing.
"""
import hashlib, io, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b542_record as Q
import b544_probe_part as P
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
ERR, FIND, OT = os.path.join(PP, 'ERRATA.md'), os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
LIVE = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
NL = chr(10)
PRIV = Q.PRIV
STD = {'propext', 'Classical.choice', 'Quot.sound'}
ZOBJ = {'zetaZeroConfig', 'IsNontrivialZero', 'paperFT', 'weilTest'}   # the zeta objects (R154)(4) names; defect (e)
T2TITLE = ('## The T0 inventory of the federation: every premise-free terminal at the standard three, by subject -- about zeta, '
           'about arithmetic or logic, about a programme-defined type')
T3TITLE = ('## The inequality index: every compiled inequality about zeta or about test windows, with what it forces; the '
           'equality-shaped statements marked E')
HEADING = ("### b544 — E-2026-09-25-6 filed; the :1109 note; CP-2 the T0 inventory and CP-3 the inequality index fired, under (R154)")
WINDOW_FILES = ['SIDEExplicitFormula/B321Identity.lean', 'SIDEExplicitFormula/DecayBound.lean', 'SIDEExplicitFormula/GrowthBound.lean',
                'SIDEExplicitFormula/H2Sign.lean', 'SIDEExplicitFormula/PairTerm.lean', 'SIDEExplicitFormula/PowerLimit.lean',
                'SIDEExplicitFormula/PowerWindow.lean', 'SIDEExplicitFormula/RestBound.lean', 'SIDEExplicitFormula/TwoPropertyWindow.lean',
                'SIDELvConservation/PartialPositivity.lean']
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


def outside_bt(text):
    return sum(l.count('`') % 2 for l in text.split(NL))


def masked_name():
    """### the declaration name on FINDINGS.md:1109, read from SIDE-kernel v1.1 MetaKernel.lean:138 -- used only to MASK it"""
    m = re.search(r'(theorem|def|lemma)\s+([A-Za-z0-9_.]+)', Q.g('SIDE-kernel', 'show', 'v1.1:MetaKernel.lean').replace(chr(13), '').split(NL)[137])
    return m.group(2).split('.')[-1] if m else None


def mask(text):
    n = masked_name()
    return re.sub(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', '<the SIDE-kernel v1.1 MetaKernel.lean:138 name>', text) if n else text


def append_to(path, text):
    text = re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", text)
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE APPEND TO %s' % path)
    n = masked_name()
    if n and re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', text):
        sys.exit('### THE :1109 NAME WOULD BE WRITTEN -- REFUSED')
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


# ------------------------------------------------------------------------------ the reads
def reads():
    L = ['b544 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    d = rd(os.path.join(D, 'b543_erratum_draft.md'))
    L += ['### relay data/b543_erratum_draft.md : %d lines ; md5 %s ; rows %d' % (len(d.rstrip(NL).split(NL)), md5(os.path.join(D, 'b543_erratum_draft.md')),
                                                                              d.count('  - replacement: *"'))] + ['  :%d %s' % (i + 1, l) for i, l in enumerate(d.rstrip(NL).split(NL))]
    e = rd(ERR).split(NL)
    a = next(i for i, l in enumerate(e) if l.startswith('<!-- b337 partition -->'))
    b = next(i for i, l in enumerate(e) if l.startswith('**INTERNAL-RECORD**'))
    L += ['', '### ERRATA.md partition block, :%d-:%d' % (a + 1, b + 1)] + ['  :%d %s' % (i + 1, e[i][:220]) for i in range(a, b + 1)]
    f = rd(FIND).split(NL)
    L += ['', '### FINDINGS.md:1105-1112 (the name on :1109 masked)'] + ['  :%d %s' % (i + 1, mask(f[i])[:300]) for i in range(1104, 1112)]
    dj = jl('b544_decls.json')
    L += ['', '### the enumeration : b542 banked no file of its 5293 declarations (data/b542_census.json holds its 235 candidates and '
              'the digest); regenerated as relay data/b544_decls.json -- %d declarations, equal to b542`s count %s' % (dj.get('count', 0), dj.get('equal'))]
    L += ['', '### the banked axiom-profile files at the pins (AxiomCheck*.lean, AXIOM_PRINTS*.txt), each repository at its pin']
    for r, cited, _ in Q.REPOS:
        if r == PRIV:
            continue
        pin = cited or 'HEAD'
        fs = [x for x in Q.g(r, 'ls-tree', '-r', '--name-only', pin).split(NL) if re.search(r'(AxiomCheck[^/]*\.lean|AXIOM_PRINTS[^/]*\.txt|PrintAxioms[^/]*\.lean)$', x)]
        if fs:
            L.append('  %s %s (%s) : %s' % (r, pin, Q.g(r, 'rev-parse', '--short', pin + '^{commit}').strip(), ', '.join(fs)))
    L.append('  relay banks carrying captured `#print axioms` lines: %d files (data/*.txt)' % len([p for p in os.listdir(D) if p.endswith('.txt') and 'depends on axioms' in rd(os.path.join(D, p))]))
    m = rd(LIVE).split(NL)
    L += ['', '### day1/A_Place_to_Stand.md (v5.13) Chapter 19, steps (9)-(10) and the v5.10.2 recast']
    for i, l in enumerate(m):
        if l.startswith('**(9)**') or l.startswith('**(10)**') or l.startswith('v5.10.2 ('):
            L.append('  :%d %s' % (i + 1, l[:600]))
    p = rd(PATHS).split(NL)
    s = next(i for i, l in enumerate(p) if l.startswith('## ANNEX B'))
    L += ['', '### PATHS_TO_THE_CRITICAL_LINE.md §ANNEX B from :%d, the A-rows and B-rows' % (s + 1)]
    for i in range(s, min(len(p), s + 80)):
        if re.match(r'^\| [AB]\d+ \|', p[i]) or p[i].startswith('## ANNEX B'):
            L.append('  :%d %s' % (i + 1, p[i][:300]))
    io.open(os.path.join(D, 'b544_reads.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  reads banked : %d lines' % len(L))


# ------------------------------------------------------------------------------ COMPONENT 1-2
STATUS6 = ("**Filed 2026-09-26 by b544, on the author's ruling (R154)(1), as drafted at relay data/b543_erratum_draft.md, its bytes "
           "unchanged; the heading's words \"DRAFT, NOT FILED\" and the Status line's \"DRAFT. Not filed.\" are the draft's, retained as "
           "drafted. With it the monograph is read whole against the RH-anchor, and every RESTS row of the read has a filed erratum.**")
BULLET6 = ("- `E-2026-09-25-6` — *DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2* (appended to this list by b544 under `(R154)`(1))")
NOTE = ("*Note (b544, under (R154)(2)):* the declaration named here is public at SIDE-kernel v1.0/v1.1, MetaKernel.lean:138; b542's "
        "withholding of the name under (R152)(3) is lifted for it and stays for TECHNE-Core's own declarations.")


def file():
    raw = open(ERR, 'rb').read()
    if b'## E-2026-09-25-6 ' in raw:
        sys.exit('### E-2026-09-25-6 IS ALREADY IN ERRATA -- REFUSING TO FILE IT TWICE.')
    draft = io.open(os.path.join(D, 'b543_erratum_draft.md'), encoding='utf-8').read()
    lines = raw.decode('utf-8').split(NL)
    k = next(i for i, l in enumerate(lines) if l.startswith('- `E-2026-09-25-5` —'))
    before_lines = list(lines)
    lines = lines[:k + 1] + [BULLET6] + lines[k + 1:]
    open(ERR, 'wb').write(NL.join(lines).encode('utf-8'))
    kept = [l for i, l in enumerate(lines) if i != k + 1] == before_lines
    w = append_to(ERR, NL + draft.rstrip(NL) + NL + NL + STATUS6 + NL)
    t = rd(ERR).split(NL)
    first = next(i for i, l in enumerate(t) if l.startswith('## E-2026-09-25-6 ')) + 1
    last = next(i for i, l in enumerate(t) if l.startswith('**Filed 2026-09-26 by b544')) + 1
    entry = NL.join(t[first - 1:last])
    res = dict(bullet_line=k + 2, prior_lines_kept=kept, append=w, entry_lines=[first, last], entry_equals_draft=(draft.rstrip(NL) in entry),
               backticks=entry.count('`'), backticks_outside_code=outside_bt(entry), rows=draft.count('  - replacement: *"'))
    put_json('b544_file.json', res)
    print('  bullet at ERRATA.md:%d (prior lines kept %s) ; E-2026-09-25-6 at ERRATA.md:%d-%d ; draft carried %s ; %d rows ; backticks %d, outside code %d'
          % (k + 2, kept, first, last, res['entry_equals_draft'], res['rows'], res['backticks'], res['backticks_outside_code']))


def note():
    raw = open(FIND, 'rb').read().decode('utf-8')
    if 'Note (b544, under (R154)(2))' in raw:
        sys.exit('### THE NOTE IS ALREADY THERE')
    lines = raw.split(NL)
    n = masked_name()
    target = lines[1108].replace(chr(13), '')
    if not re.search(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', target):
        sys.exit('### FINDINGS.md:1109 DOES NOT CARRY THE NAME -- REFUSING')
    before = list(lines)
    eol = chr(13) if lines[1108].endswith(chr(13)) else ''
    lines = lines[:1109] + [NOTE + eol] + lines[1109:]
    open(FIND, 'wb').write(NL.join(lines).encode('utf-8'))
    kept = [l for i, l in enumerate(lines) if i != 1109] == before
    res = dict(line_before=1109, note_line=1110, following_line_before=1110, following_line_after=1111, prior_lines_kept=kept,
               line_1109_unchanged=(lines[1108] == before[1108]))
    put_json('b544_note.json', res)
    print('  the note at FINDINGS.md:1110, beneath :1109 (unchanged %s) ; the line that was :1110 is now :1111 ; prior lines kept %s'
          % (res['line_1109_unchanged'], kept))


# ------------------------------------------------------------------------------ CP-2: profiles and premises
PRINT_ANY = re.compile(r"'(.+?)'[ \t]+(does not depend on any axioms|depends on axioms: \[[^\]]*\])")


def profiles():
    """### parsed from each probe`s own banked output (a name may carry an apostrophe, so the quote is matched lazily)"""
    out = {}
    for r in ('SIDE-explicit-formula', 'SIDE-lv-conservation', 'SIDE-kernel', 'SIDE-spinor-calibration-mathlib'):
        p = os.path.join(D, 'b544_probe_%s.txt' % r)
        if not os.path.exists(p):
            continue
        txt = re.sub(r'\n\s+', ' ', rd(p).split(NL + '---' + NL, 1)[-1])
        for m in PRINT_ANY.finditer(txt):
            out[(r, m.group(1))] = m.group(2)
    return out


def prof_class(v):
    if v is None:
        return None
    if 'does not depend' in v:
        return 'none'
    ax = [x.strip() for x in v.split('[', 1)[1].rstrip(']').split(',') if x.strip()]
    return 'std3-or-fewer' if set(ax) <= STD else 'NON-STANDARD'


def fed_props(ds):
    props = set()
    for x in ds:
        if x['kw'] in ('def', 'abbrev', 'structure', 'class') and x.get('statement'):
            head = x['statement'].split(':=')[0].split(' where')[0]
            if re.search(r':\s*Prop\s*$', head.strip()) or re.search(r':\s*Prop\s*(where)?\s*$', x['statement'].split(NL)[0].strip()):
                props.add(x['name'].split('.')[-1])
    return props


def proved_props(ds, props):
    out = {}
    for x in ds:
        if x['kw'] in P.TERMKW and x.get('statement'):
            m = re.match(r'^\s*(?:@\[[^\]]*\]\s*)?(?:\w+\s+)*(?:theorem|lemma)\s+(\S+)\s*:\s*([A-Za-z0-9_.]+)\s*:=', ' '.join(x['statement'].split()))
            if m and m.group(2).split('.')[-1] in props:
                out.setdefault(m.group(2).split('.')[-1], x['name'])
    return out


def split_statement(st):
    """### (binders, conclusion) at the first top-level ':' after the name; the conclusion stops at a top-level ':='"""
    s = ' '.join(Q.blank_all_comments(st).split())
    m = re.match(r'^\s*(?:@\[[^\]]*\]\s*)?(?:\w+\s+)*(theorem|lemma|def|abbrev|instance|structure|class|inductive|opaque)\s+(\S+)', s)
    i = m.end() if m else 0
    depth, j = 0, i
    while j < len(s):
        c = s[j]
        if c in '([{⟨':
            depth += 1
        elif c in ')]}⟩':
            depth -= 1
        elif c == ':' and depth == 0 and s[j:j + 2] != ':=':
            break
        j += 1
    binders, rest = s[i:j], s[j + 1:]
    depth, k = 0, 0
    while k < len(rest):
        c = rest[k]
        if c in '([{⟨':
            depth += 1
        elif c in ')]}⟩':
            depth -= 1
        elif rest[k:k + 2] == ':=' and depth == 0:
            break
        k += 1
    return binders, rest[:k].strip(), rest[k + 2:].strip()


def hypotheses(binders):
    out = []
    depth, start, opener = 0, None, None
    for i, c in enumerate(binders):
        if c in '([{⦃' and depth == 0:
            start, opener = i, c
        if c in '([{⦃⟨':
            depth += 1
        elif c in ')]}⦄⟩':
            depth -= 1
            if depth == 0 and start is not None:
                b = binders[start + 1:i]
                if ':' in b and opener in '(':
                    nm, ty = b.split(':', 1)
                    out.append((nm.strip(), ty.strip()))
                start = None
    return out


def premises():
    dj = jl('b544_decls.json')
    ds = [x for x in dj['decls'] if x['repo'] != PRIV]
    props = fed_props(ds)
    proved = proved_props(ds, props)
    # ### the objects (R154)(4) itself names as zeta objects are not programme objects here (defect (e)); Phi stays one (READING (4))
    fednames = set(x['name'].split('.')[-1] for x in ds if x['kw'] in P.BODYKW and x['name'] != '(anonymous)' and len(x['name'].split('.')[-1]) > 2) - ZOBJ
    pr = profiles()
    rows = []
    for x in ds:
        if x['subject'] != 'ZETA' or x['kw'] not in P.TERMKW:
            continue
        v = pr.get((x['repo'], x['full']))
        klass = prof_class(v)
        skipped = next((s for s in jl('b544_probe_%s.json' % x['repo']).get('skipped', []) if s['full'] == x['full']), None)
        binders, concl, _ = split_statement(x['statement'])
        prem = []
        for nm, ty in hypotheses(binders):
            head = re.match(r'^[@(]*([A-Za-z0-9_.₀]+)', ty)
            h = head.group(1).split('.')[-1] if head else ''
            names = set(t.split('.')[-1] for t in re.findall(r'[A-Za-z_][A-Za-z0-9_₀.]*', ty))
            hp = h in props and h not in ZOBJ
            if hp or (names & fednames and (re.search(r'(=|≠|≤|<|∈|∉|→|↔)', ty) or nm.startswith('h') or nm.startswith('H'))):
                key = h if hp else sorted(names & fednames)[0]
                prem.append(dict(binder=nm, type=ty[:160], prop=key, proved=proved.get(key)))
        lead = re.match(r'^([A-Za-z0-9_.]+)\s*→', concl)
        if lead and lead.group(1).split('.')[-1] in props:
            key = lead.group(1).split('.')[-1]
            prem.append(dict(binder='(leading implication)', type=key, prop=key, proved=proved.get(key)))
        state = ('PREMISE-FREE' if not prem else 'PREMISE: ' + ', '.join(p['prop'] + (' (PROVED: %s)' % p['proved'] if p['proved'] else '') for p in prem))
        if klass:
            pclass = klass
        elif skipped:
            pclass = 'NOT PROFILED AT THE PIN (closure: %s)' % ', '.join(skipped['changed'])
        else:
            pclass = 'PRIVATE DECLARATION (not printable by name)' if x['private'] else 'NOT PRINTED'
        rows.append(dict(repo=x['repo'], pin=x['pin'], file=x['file'], line=x['line'], full=x['full'], profile=v, profile_class=pclass,
                         premises=prem, state=state, zeta=x['zeta'], t0=(klass in ('none', 'std3-or-fewer') and not prem)))
    res = dict(props=sorted(props), proved=proved, rows=rows,
               counts=dict(zeta_terminals=len(rows), profiled=sum(1 for r in rows if r['profile']), std3=sum(1 for r in rows if prof_class(r['profile']) in ('none', 'std3-or-fewer')),
                           t0=sum(1 for r in rows if r['t0']), with_premise=sum(1 for r in rows if r['premises'] and prof_class(r['profile']) in ('none', 'std3-or-fewer'))),
               premise_props=sorted(set(p['prop'] for r in rows for p in r['premises'])))
    put_json('b544_premises.json', res)
    print('  ZETA terminals %(zeta_terminals)d ; profiled %(profiled)d ; standard three or fewer %(std3)d ; T0 (premise-free) %(t0)d ; with a premise %(with_premise)d' % res['counts'])
    print('  the premises found : %s' % res['premise_props'])
    print('  federation Props proved by a theorem : %s' % proved)
    for r in rows:
        if not r['profile']:
            print('    unprofiled : %s %s:%d %s -- %s' % (r['repo'], r['file'], r['line'], r['full'], r['profile_class']))


# ------------------------------------------------------------------------------ CP-3: the marks
I_NEEDLES = [('≤', r'≤'), ('<', r'(?<![<-])<(?![-=])'), ('≥', r'≥'), ('>', r'(?<![-=])>(?!=)'), ('Nonneg', r'Nonneg'), ('Summable', r'Summable'),
             ('Tendsto to 𝓝 0', r'Tendsto[^\n]*𝓝 0'), ('IsBigO', r'IsBigO|=O\['), ('≠ 0', r'≠\s*0(?![.0-9])')]
E_SHAPES = [('↔', r'↔'), ('∈', r'∈'), ('Finite', r'\.Finite|Set\.Finite|Finite\b'), ('card', r'card|ncard'), ('=', r'(?<![<>≤≥!:])=(?![>])')]


def top_iff(concl):
    depth = 0
    for c in concl:
        if c in '([{⟨':
            depth += 1
        elif c in ')]}⟩':
            depth -= 1
        elif c == '↔' and depth == 0:
            return True
    return False


def mark_of(concl):
    if top_iff(concl):
        return 'E', '↔'
    for n, p in I_NEEDLES:
        if re.search(p, concl.replace('→', ' ').replace('↦', ' ').replace('=>', ' ')):
            return 'I', n
    for n, p in E_SHAPES:
        if re.search(p, concl):
            return 'E', n
    return 'E', 'other shape'


def range_of(binders, concl):
    s = binders + ' ' + concl
    tags = []
    if re.search(r'(1 / 2|1/2|½)', s) and re.search(r'\.re|⟨', s):
        tags.append('on the line')
    if re.search(r'1 < [a-z]\.re|1 ≤ [a-z]\.re|[a-z]\.re ≤ 0|2 ≤ [a-z]\.re|1 ≤ [a-z]', s):
        tags.append('a half-plane')
    if re.search(r'0 < [a-zρ]\.re', s) and re.search(r'\.re < 1', s):
        tags.append('the strip')
    if re.search(r'N₀|≤ n|n ≤|range|Finset', s):
        tags.append('a finite range')
    if re.search(r'\bPhi\b', s):
        tags.append('at the witness')
    if re.search(r'zetaZeroConfig|IsNontrivialZero|carrier|ρ', s):
        tags.append('over the zeros')
    return ', '.join(tags) or 'all arguments'


NAV = [('the on-line term`s nonnegativity', ['blTerm_nonneg_of_onLine']),
       ('the finite-range certificate', ['partialPositivity_finiteRange']),
       ('the order and growth bounds', ['norm_completedRiemannZeta₀_le', 'growth', 'Growth', 'C7_order', 'order_le', 'exp_bound']),
       ('the decay bound', ['decay', 'Decay']),
       ('the pair term`s near factor', ['pair', 'Pair', 'near']),
       ('the finite-type refutation`s bracket', ['C7_finite_type_false']),
       ('the local count', ['local_count', 'LocalCount']),
       ('h2_sign itself, a hypothesis', ['h2_sign'])]


def index():
    dj = jl('b544_decls.json')
    ds = [x for x in dj['decls'] if x['repo'] != PRIV]
    rows = []
    for x in ds:
        window = x['file'] in WINDOW_FILES and x['repo'] in ('SIDE-explicit-formula', 'SIDE-lv-conservation')
        if not (x['subject'] == 'ZETA' or window):
            continue
        binders, concl, body = split_statement(x['statement'])
        isdef = x['kw'] in P.BODYKW
        target = body if isdef else concl
        mk, shape = mark_of(target)
        zero = bool(re.search(r'zetaZeroConfig|IsNontrivialZero|carrier|zeroSide|\bρ\b|(riemannZeta|completedRiemannZeta₀?|(?<![A-Za-z_])ζ)\s*[a-zρ(⟨][^=≠\n]{0,40}=\s*0(?![.0-9])',
                                  x['statement']))
        concludes_loc = bool(re.search(r'\.re\s*=\s*1\s*/\s*2|RiemannHypothesis|rh_strip', concl))
        rows.append(dict(repo=x['repo'], file=x['file'], line=x['line'], full=x['full'], kw=x['kw'], subject=x['subject'], window=window,
                         mark=mk, shape=shape, flag=('DEF' if isdef else ''), conclusion=(target[:220]), range=range_of(binders, target),
                         forces=('%s -- %s' % (target[:180], range_of(binders, target))) if mk == 'I' else '', names_zero=zero,
                         concludes_location=concludes_loc))
    irows = [r for r in rows if r['mark'] == 'I']
    zI = [r for r in irows if r['names_zero']]
    nav = []
    for label, pats in NAV:
        hit = [r['full'] for r in irows if any(p in r['full'].split('.')[-1] for p in pats)]
        nav.append(dict(item=label, found=hit))
    anticipated = set(n for x in nav for n in x['found'])
    unanticipated = [r['full'] for r in irows if r['subject'] == 'ZETA' and r['full'] not in anticipated]
    loc = [r for r in irows if r['concludes_location']]
    res = dict(rows=rows, counts=dict(rows=len(rows), I=len(irows), E=len(rows) - len(irows), zeta=sum(1 for r in rows if r['subject'] == 'ZETA'),
                                      window=sum(1 for r in rows if r['window']), I_zeta=sum(1 for r in irows if r['subject'] == 'ZETA'),
                                      I_naming_zero=len(zI)),
               i_needles=[n for n, _ in I_NEEDLES], e_shapes=[n for n, _ in E_SHAPES] + ['other shape'], navigator=nav,
               unanticipated=unanticipated, i_concluding_location=[(r['full'], r['conclusion'][:160]) for r in loc])
    put_json('b544_index.json', res)
    ei = {}
    for r in rows:
        if r['subject'] == 'ZETA':
            ei['%s|%s' % (r['repo'], r['full'])] = '%s (%s)%s' % (r['mark'], r['shape'], ' DEF' if r['flag'] else '')
    put_json('b544_ei.json', dict(generated_by='tools/b544_record.py index', ruling='(R154)(4)', marks=ei))
    print('  CP-3 rows %(rows)d (ZETA %(zeta)d, window %(window)d) ; I %(I)d (ZETA %(I_zeta)d, naming a zero %(I_naming_zero)d) ; E %(E)d' % res['counts'])
    print('  I needles %s ; E shapes %s' % (res['i_needles'], res['e_shapes']))
    for x in nav:
        print('    navigator item %-42s found %s' % (x['item'], x['found'][:6] or 'NOT FOUND'))
    print('  unanticipated ZETA I rows : %d' % len(unanticipated))
    print('  I rows concluding re = 1/2, RiemannHypothesis or rh_strip : %s' % (res['i_concluding_location'] or 'NONE'))


# ------------------------------------------------------------------------------ the table, findings, desk, trail
def table():
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    tt = jl('terminal_table.json')
    zrows = [x for x in tt.get('rows', []) if x.get('ei') not in (None, '—')]
    blank = [x for x in tt.get('rows', []) if x.get('zeta_row') and not x.get('ei')]
    res = dict(exit=r.returncode, rows=len(tt.get('rows', [])), zeta_rows=sum(1 for x in tt.get('rows', []) if x.get('zeta_row')),
               marked=len(zrows), blank_zeta=len(blank), column=('ei' in (tt.get('rows') or [{}])[0]))
    put_json('b544_table.json', res)
    print('  terminal table regenerated exit %(exit)d ; rows %(rows)d ; ZETA rows %(zeta_rows)d ; marked %(marked)d ; blank ZETA cells %(blank_zeta)d ; column %(column)s' % res)


def findings():
    dj, pj, ij = jl('b544_decls.json'), jl('b544_premises.json'), jl('b544_index.json')
    tt = jl('terminal_table.json')
    aol_prof = {}
    for x in tt.get('rows', []):
        if x.get('profile_state') == 'PROFILED':
            aol_prof[(x['repo'], x['name'].split('.')[-1])] = x['profile']
    for (repo, full), v in profiles().items():
        aol_prof.setdefault((repo, full.split('.')[-1]), v)
    aol = []
    for x in dj['decls']:
        if x['repo'] == PRIV or x['subject'] != 'ARITHMETIC-OR-LOGIC' or x['kw'] not in P.TERMKW:
            continue
        v = aol_prof.get((x['repo'], x['name'].split('.')[-1]))
        aol.append(dict(repo=x['repo'], file=x['file'], line=x['line'], full=x['full'], profile=v, t0=(prof_class(v) in ('none', 'std3-or-fewer'))))
    zt0 = [r for r in pj['rows'] if r['t0']]
    at0 = [r for r in aol if r['t0']]
    put_json('b544_t0.json', dict(zeta=zt0, arithmetic_or_logic=at0, aol_unprofiled=sum(1 for r in aol if not r['profile']), aol_total=len(aol)))
    subj = dj['subjects']
    L = ['', T2TITLE, '',
         '*Filed at b544 on the author`s ruling `(R154)`(4): CP-2. The %d declarations of b542`s enumeration, regenerated at b542`s pins '
         '(relay `data/b544_decls.json`), each classified by the subject of its statement; the ZETA terminals probed fresh by `#print axioms` '
         '(relay `data/b544_probe_*.txt`), their hypotheses read. Bank: relay `data/b544_t0.json`, `data/b544_premises.json`.*' % dj['count'], '',
         '**The subjects.** ZETA %d · ARITHMETIC-OR-LOGIC %d · PROGRAMME-TYPE %d. The ZETA statements lie in %s.'
         % (subj.get('ZETA', 0), subj.get('ARITHMETIC-OR-LOGIC', 0), subj.get('PROGRAMME-TYPE', 0),
            '; '.join('%s %d' % (r, c.get('ZETA', 0)) for r, c in sorted(dj['per_repo'].items(), key=lambda kv: -kv[1].get('ZETA', 0)) if c.get('ZETA'))), '',
         '| repository | ZETA | ARITHMETIC-OR-LOGIC | PROGRAMME-TYPE |', '|:--|--:|--:|--:|']
    for r, c in sorted(dj['per_repo'].items(), key=lambda kv: (-kv[1].get('ZETA', 0), kv[0])):
        L.append('| %s | %d | %d | %d |' % (r, c.get('ZETA', 0), c.get('ARITHMETIC-OR-LOGIC', 0), c.get('PROGRAMME-TYPE', 0)))
    c = pj['counts']
    L += ['', '**The ZETA terminals.** %d theorems and lemmas; %d printed a profile, %d at the standard three or fewer; **%d PREMISE-FREE, the T0 '
              'part about zeta**; %d carry a premise (%s). A premise the federation proves is marked PROVED.' %
          (c['zeta_terminals'], c['profiled'], c['std3'], c['t0'], c['with_premise'], ', '.join('`%s`' % p for p in pj['premise_props'])), '']
    by = {}
    for r in zt0:
        by.setdefault(r['repo'], []).append(r)
    for repo in sorted(by):
        L += ['**%s** -- T0 about zeta:' % repo, '', '| terminal | module:line | subject | profile |', '|:--|:--|:--|:--|']
        for r in sorted(by[repo], key=lambda x: (x['file'], x['line'])):
            L.append('| `%s` | %s:%d | about zeta (%s) | %s |' % (r['full'], r['file'], r['line'], ', '.join(r['zeta']),
                                                                  'no axioms' if 'does not' in (r['profile'] or '') else 'the standard three'))
        L.append('')
    aby = {}
    for r in at0:
        aby[r['repo']] = aby.get(r['repo'], 0) + 1
    L += ['**The ARITHMETIC-OR-LOGIC terminals with a banked profile at the standard three or fewer** (no fresh probe; the rest are unprofiled): '
          '%d of %d, by repository: %s. They are listed in the bank; they are about natural numbers, integers, rationals, reals, finite sets '
          'and propositions, and say nothing about zeta.' % (len(at0), len(aol), ', '.join('%s %d' % kv for kv in sorted(aby.items()))), '',
          '**What the inventory says about the federation, in words.** Its premise-free facts about zeta are Mathlib`s objects handled '
          'directly: nonvanishing on half-planes and boxes, the functional-equation reflection of the zeros, counts and finiteness of the '
          'zeros in windows, the analytic identities of the explicit formula, and the transform bounds of the test functions. The '
          'statements that carry a premise carry a Prop or object the programme defines: %s; of these the federation proves %s. Nothing in '
          'the inventory states where the zeros lie.' % (', '.join('`%s`' % p for p in pj['premise_props']),
                                                         ', '.join('`%s` (by `%s`)' % (p, pj['proved'][p]) for p in pj['premise_props'] if p in pj['proved']) or 'none'), '']
    w1 = append_to(FIND, NL.join(L))
    ic = ij['counts']
    L2 = ['', T3TITLE, '',
          '*Filed at b544 on the author`s ruling `(R154)`(4): CP-3, the compiled census of the monograph`s step (9) identity/sign split and of '
          'PATHS §ANNEX B`s rows. The rows: every ZETA declaration and every declaration of the window modules. I marks: %s; E: %s. Bank: relay '
          '`data/b544_index.json`; the mark is a column of the terminal table.*' % (', '.join(ij['i_needles']), ', '.join(ij['e_shapes'])), '',
          '**The count.** %d rows: I %d (about zeta %d; naming a zero %d) · E %d.' % (ic['rows'], ic['I'], ic['I_zeta'], ic['I_naming_zero'], ic['E']), '',
          '| I row | module:line | what it forces (the conclusion, its range) |', '|:--|:--|:--|']
    for r in sorted([r for r in ij['rows'] if r['mark'] == 'I'], key=lambda x: (x['repo'], x['file'], x['line'])):
        L2.append('| `%s`%s | %s %s:%d | %s |' % (r['full'], ' (DEF)' if r['flag'] else '', r['repo'], r['file'], r['line'],
                                                 r['forces'].replace('|', '∣').replace('`', '')))
    loc = ij['i_concluding_location']
    L2 += ['', '**The I rows that name a zero** (%d). %s The others bound a quantity over the zeros (a count, a sum, a term`s sign on the line, the '
               'zero side of a test window, a nonvanishing near a zero) and none bears on location.'
           % (ic['I_naming_zero'], ('One concludes re = 1/2: %s, whose hypotheses include `RHHypothesis`, RH restated for completedRiemannZeta₀ '
                                    '(SIDEBridge.lean), so its conclusion is its hypothesis`s, not an inequality`s.' % ', '.join('`%s`' % x[0] for x in loc))
               if loc else 'None concludes re = 1/2, RiemannHypothesis or rh_strip.'), '',
           '**What the index says, in words.** The inequalities the federation holds about zeta are of three reaches. At the strip`s edge: '
           'zeta does not vanish on the half-plane re ≥ 1 and in the boxes near it, the edge Λ(n) ≥ 0 reaches and no further. At the fixed '
           'witness or in a finite range: the growth and order bounds of the completed function, the transform decay of the test windows, '
           'the pair term`s factor, the finite-range Li certificate and the on-line term`s sign. Over the zeros: counts in windows and '
           'summability of the zero sums. None of them moves a zero. The one inequality that would reach the centre of the strip is '
           '`h2_sign`, the sign of the zero side over the admissible class; it is a hypothesis, equivalent to RH (`h2_sign_iff_rh`), and no '
           'theorem of the federation proves it.', '']
    w2 = append_to(FIND, NL.join(L2))
    f = rd(FIND).split(NL)
    w1['heading_line'], w2['heading_line'] = f.index(T2TITLE) + 1, f.index(T3TITLE) + 1
    put_json('b544_findings.json', dict(cp2=w1, cp3=w2))
    print('  FINDINGS : CP-2 at line %d (+%d bytes) ; CP-3 at line %d (+%d bytes)' % (w1['heading_line'], w1['added'], w2['heading_line'], w2['added']))


# ------------------------------------------------------------------------------ desk, trail
def gitc(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout


PRIOR_PP = 'ba00159'
NAMED = ['SIDE-explicit-formula', 'SIDE-lv-conservation', 'SIDE-rcurve', 'SIDE-simplicity', 'SIDE-global-section']
N2_OK = {'h2_sign', 'ConservationHypothesis', 'conservationHypothesis', 'rh_strip_imp_rh', 'TailBoundPremise', 'ExplicitFormulaDecomp', 'Phi'}


def w(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def scores():
    dj, pj, ij, fj, tb = jl('b544_decls.json'), jl('b544_premises.json'), jl('b544_index.json'), jl('b544_file.json'), jl('b544_table.json')
    zper = {r: c.get('ZETA', 0) for r, c in dj.get('per_repo', {}).items() if c.get('ZETA')}
    others = sorted(r for r in zper if r not in NAMED)
    std_prem = [r for r in pj.get('rows', []) if r['premises'] and prof_class(r['profile']) in ('none', 'std3-or-fewer')]
    other_prem = sorted(set(p['prop'] for r in std_prem for p in r['premises'] if p['prop'] not in N2_OK))
    loc = ij.get('i_concluding_location', [])
    missing = [x['item'] for x in ij.get('navigator', []) if not x['found']]
    mono = {f: gitc(PP, 'hash-object', f) == gitc(PP, 'rev-parse', '%s:%s' % (PRIOR_PP, f)) for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')}
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b544_') and needle in rd(os.path.join(T, x))]
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(t) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b544_')) if t else None
    kernels = {k: gitc(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == '' for k in ('SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-explicit-formula', 'SIDE-global-section')}
    written = sorted(x for x in gitc(PP, 'diff', '--name-only', PRIOR_PP).split(NL) if x) if not gitc(PP, 'log', '-1', '--pretty=%s').startswith('b544 --') else \
        sorted(x for x in gitc(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x)
    return dict(
        n1=dj.get('subjects', {}).get('ZETA', 10 ** 6) * 10 < dj.get('count', 0) and len(others) <= 2, n1_zeta=dj.get('subjects', {}).get('ZETA'), n1_others=others,
        n2=not other_prem, n2_other=other_prem,
        n3=not loc, n3_rows=loc,
        n4=not missing, n4_missing=missing, n4_unanticipated=len(ij.get('unanticipated', [])),
        n5=tb.get('column') is True and tb.get('blank_zeta') == 0 and tb.get('exit') == 0,
        n6=(all(mono.values()) and not zen and tok == 0 and all(kernels.values()) and set(written) <= {'ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md'}
            and {'ERRATA.md', 'FINDINGS.md'} <= set(written) and fj.get('backticks_outside_code') == 0),
        mono=mono, zen=zen, token=tok, kernels=kernels, written=written,
        s1=zper.get('SIDE-kernel', 0) > 0 and len(others) > 2,
        s2=not [r for r in ij.get('rows', []) if r['mark'] == 'I' and r['subject'] == 'ZETA' and re.search(r'\.re\s*=\s*1\s*/\s*2', r['conclusion'])],
        s3=any(p['proved'] for r in pj.get('rows', []) for p in r['premises']))


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6'), ('s1', 's2', 's3')
    L = ['=' * 104, 'b544 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- ZETA %s of the declarations ; repositories outside (R154)(5)`s list contributing : %s.' % (w(sc['n1']), sc['n1_zeta'], sc['n1_others']),
         '  **(N2)** ### **%s.** -- premises at the standard three outside the expected kinds : %s.' % (w(sc['n2']), sc['n2_other'] or 'none'),
         '  **(N3)** ### **%s.** -- I rows concluding re = 1/2, RiemannHypothesis or rh_strip : %s.' % (w(sc['n3']), sc['n3_rows'] or 'none'),
         '  **(N4)** ### **%s.** -- navigator items not found : %s ; unanticipated ZETA I rows : %d.' % (w(sc['n4']), sc['n4_missing'] or 'none', sc['n4_unanticipated']),
         '  **(N5)** ### **%s.** -- the column, blank ZETA cells : %s.' % (w(sc['n5']), jl('b544_table.json')),
         '  **(N6)** ### **%s.** -- monograph %s ; PLACE-papers files written %s ; tools naming the platform %s ; token %s ; kernels clean %s.'
         % (w(sc['n6']), sc['mono'], sc['written'], sc['zen'] or 'NONE', sc['token'], sc['kernels']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- SIDE-kernel contributes ZETA rows outside the list.' % w(sc['s1']),
         '  **(S2)** ### **%s.** -- no I-marked ZETA row concludes about re = 1/2.' % w(sc['s2']),
         '  **(S3)** ### **%s.** -- a ZETA terminal`s premise is a Prop the federation proves.' % w(sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b544_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b544_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    io.open(os.path.join(D, 'b544_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    put_json('b544_scores.json', sc)
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b544 -- THE COMPONENTS, AS THEY RAN.', '=' * 132,
         '### COMPONENT 1 -- E-6 : ' + json.dumps(jl('b544_file.json'), ensure_ascii=False),
         '### COMPONENT 2 -- THE NOTE : ' + json.dumps(jl('b544_note.json'), ensure_ascii=False),
         '### THE ENUMERATION : ' + json.dumps({k: v for k, v in jl('b544_decls.json').items() if k != 'decls'}, ensure_ascii=False)]
    for r in ('SIDE-explicit-formula', 'SIDE-lv-conservation', 'SIDE-kernel', 'SIDE-spinor-calibration-mathlib'):
        pj = jl('b544_probe_%s.json' % r)
        L.append('### THE PROBE %s : rows %s ; printed %d ; skipped %d ; private %d ; exit %s ; %s s' % (r, pj.get('rows'), len(pj.get('profiles') or {}), len(pj.get('skipped') or []),
                                                                                                 len(pj.get('private_skipped') or []), pj.get('exit'), pj.get('seconds')))
    pj = jl('b544_premises.json')
    L += ['### COMPONENT 3 -- CP-2 : ' + json.dumps(pj.get('counts')), '  premises : %s' % pj.get('premise_props')]
    L += ['  %-14s %-40s %s %s:%d %s' % ('T0' if r['t0'] else r['profile_class'][:14], r['state'][:40], r['repo'], r['file'], r['line'], r['full']) for r in pj.get('rows', [])]
    ij = jl('b544_index.json')
    L += ['### COMPONENT 4 -- CP-3 : ' + json.dumps(ij.get('counts')), '  navigator : ' + json.dumps(ij.get('navigator'), ensure_ascii=False)[:2000]]
    L += ['  %s %-14s %s:%d %s -- %s' % (r['mark'], r['shape'], r['file'], r['line'], r['full'], r['forces'][:160]) for r in ij.get('rows', []) if r['mark'] == 'I']
    L += ['### THE TABLE : ' + json.dumps(jl('b544_table.json')), '### FINDINGS : ' + json.dumps(jl('b544_findings.json')),
          '### THE BRANCHES : see data/b544_branches.txt', '=' * 132]
    io.open(os.path.join(D, 'b544_components.txt'), 'w', encoding='utf-8', newline=NL).write(mask(NL.join(L)) + NL)
    print(NL.join(L[:6]))


def trail():
    sc, pj, ij, fj, fnd = scores(), jl('b544_premises.json'), jl('b544_index.json'), jl('b544_file.json'), jl('b544_findings.json')
    dj = jl('b544_decls.json')
    body = ['', HEADING, '',
            '**(R154) ratified.** (1) E-2026-09-25-6 filed; every RESTS row of the monograph read now has a filed erratum. (2) The note beneath '
            'FINDINGS.md:1109 (the declaration public at SIDE-kernel v1.0/v1.1). (3) The phase order, below. (4) CP-2 and CP-3, run here. (5) The '
            'navigator`s reading, scored.', '',
            '**Filed:** E-2026-09-25-6 at `ERRATA.md`:%s-%s, its bullet at :%s. **Entered:** the note at `FINDINGS.md`:1110; CP-2 at `FINDINGS.md`:%s; '
            'CP-3 at `FINDINGS.md`:%s; the E/I column in the terminal table.' % (fj['entry_lines'][0], fj['entry_lines'][1], fj['bullet_line'],
                                                                                fnd['cp2']['heading_line'], fnd['cp3']['heading_line']), '',
            '**CP-2 -- FIRED at b544.** Banks: relay `data/b544_decls.json`, `data/b544_probe_*.txt`, `data/b544_premises.json`, `data/b544_t0.json`. '
            'ZETA %d of %d declarations; %d ZETA terminals, %d premise-free at the standard three.' % (dj['subjects'].get('ZETA', 0), dj['count'],
                                                                                                 pj['counts']['zeta_terminals'], pj['counts']['t0']),
            '**CP-3 -- FIRED at b544.** Bank: relay `data/b544_index.json`, `data/b544_ei.json`. %d rows, I %d, E %d; no I row concludes re = 1/2.'
            % (ij['counts']['rows'], ij['counts']['I'], ij['counts']['E']),
            '**CP-1 -- OPEN, its order under (R154)(3):** the Phase 1.5 keystones` tables (the cascade as (R149)(3) lists them, BALANCE_AND_POSITIVITY '
            'next); then the Phase 1.2 presentations (THE_PROOF, MECHANISM_EXCLUSION, IDS_TO_RH, INTEGRATED_PROOF) and the six checkpoint kernels` '
            'papers; then the six Day-1 companions; Phase 2 (CP-6) after all of those. The 1.2 and companion sets are read when mirrored.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
            '**No kernel lane opened at this act.** Nothing deposits; nothing at Zenodo written; no kernel edited; no monograph byte changed; '
            'the ceiling unchanged; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH.', '']
    text = re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    before = open(OT, 'rb').read()
    if HEADING.encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b544_trail_notes.json', out)


if __name__ == '__main__':
    sys.exit({'reads': reads, 'file': file, 'note': note, 'premises': premises, 'index': index, 'table': table, 'findings': findings,
              'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]())
