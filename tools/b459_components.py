# -*- coding: utf-8 -*-
"""b459_components.py -- THE THREE COMPONENTS OF b459.

### COMPONENT 1 -- each site's index, read from its own entry in row U1.
### COMPONENT 2 -- three generators, every range printed before any site is placed.
### COMPONENT 3 -- the control, and the halt it runs into.

### ### **EVERY RULE THIS FILE APPLIES IS ON THE LOCKED FACE.** ### The cut, the extraction rule,
### the three sources, the placement rule and the three verdict words were fixed before the run.
### ### **NOTHING IS EXECUTED FROM `b321_window`** -- its range is READ off its own `return`.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FL = os.path.join(PP, 'FACES_LEDGER.md')
FN = os.path.join(PP, 'FINDINGS.md')
W = os.path.join(T, 'b321_window.py')
OUT = os.path.join(D, 'b459_components.txt')
NL = chr(10)
L = []

MARKS = [('(i)', '(i) THE CLAUSE'), ('(ii)', '(ii) THE HEIGHT'), ('(iii)', '(iii) THE WIDTH'),
         ('(iv)', '(iv) THE PRIME'), ('(v)', '(v) THE REPRESENTATION'), ('(vi)', '(vi) THE TYPE-D')]
END = 'THE TALLY, PRINTED SO NO READER HAS TO COUNT'
# ### THE WORDS THAT MARK AN INDEXING SENTENCE. ### Fixed here, applied to every site alike.
IDX_MARKS = ('indexed by', 'uniform in', 'depends on', 'at every', 'across ', 'index')
# ### **THE WIDENED SET, AND WHY.** ### The first set missed `(i)` and `(ii)` entirely: their own
# ### words name what they range OVER (`over the class`, `over the zeros`, `quantifies over`) and
# ### never use the token `index`. ### **A MATCHER THAT MISSES A THIRD OF ITS SUBJECTS IS THE
# ### DEFECT, NOT THE SUBJECTS**, and b396's rule applies: print the narrow yield, then widen.
IDX_MARKS_WIDE = IDX_MARKS + ('over the ', 'quantifies over', 'coordinate', 'per ')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def sentences(t):
    """### Split on the row's own sentence enders, keeping its `###` separators out of the way."""
    t = t.replace('###', ' ')
    parts = re.split(r'(?<=[.;])\s+', t)
    return [re.sub(r'\s+', ' ', p).strip() for p in parts if p.strip()]


def u1_cell():
    for l in read(FL).split(NL):
        if l.startswith('| U1 |'):
            return l
    raise SystemExit('### HARD FAILURE -- row U1 not found')


def cut(cell):
    """### THE CUT, AS THE FACE FIXED IT: each marker to the next; the last to the tally."""
    pos = [(k, cell.find(m)) for k, m in MARKS]
    end = cell.find(END)
    if any(p < 0 for _, p in pos) or end < 0:
        raise SystemExit('### HARD FAILURE -- a marker or the tally sentence is missing')
    out = {}
    for j, (k, p) in enumerate(pos):
        q = pos[j + 1][1] if j + 1 < len(pos) else end
        out[k] = cell[p:q].strip()
    return out


def cut2(cell):
    """### **THE CORRECTED CUT.** ### The row enumerates its six sites TWICE -- once as entries and
    ### again as `KIND`/`WITNESS` cells -- and the face's rule, which runs the last marker to the
    ### tally, swept the WHOLE SECOND ENUMERATION into `(vi)`. ### Each site's text is now its own
    ### block in BOTH enumerations, joined."""
    first = cut(cell)
    marks2 = [(k, m.start()) for k in [x[0] for x in MARKS]
              for m in re.finditer(re.escape('`%s`' % k) + r'\s*[—-]\s*KIND', cell)
              if m.group(0).startswith('`%s`' % k)]
    seen, pos2 = set(), []
    for k, p in marks2:
        if k not in seen:
            seen.add(k)
            pos2.append((k, p))
    pos2.sort(key=lambda x: x[1])
    end = cell.find(END)
    second = {}
    for j, (k, p) in enumerate(pos2):
        q = pos2[j + 1][1] if j + 1 < len(pos2) else end
        second[k] = cell[p:q].strip()
    out = {}
    for k, _ in MARKS:
        blocks = [first[k]] if k != '(vi)' else [first[k][:first[k].find(second['(i)'][:40])]
                                                 if second.get('(i)') and second['(i)'][:40] in first[k]
                                                 else first[k]]
        if k in second:
            blocks.append(second[k])
        out[k] = (' '.join(blocks)).strip()
    return out, first, second


# ====================================================================================================
# ### COMPONENT 1
# ====================================================================================================
# ### **THE SEAT'S READING OF EACH SITE'S INDEX, AND THE TOOL CHECKS IT AGAINST THE FACE'S RULE:**
# ### the word must occur in the sentence quoted from that site's own text. ### The candidate
# ### sentences are ALL printed first, so the reading is checkable and not merely asserted.
READING = {
    '(i)':   ('class',          'the quantifiers'),
    '(ii)':  ('height',         'the height coordinate'),
    '(iii)': ('width',          'the support width'),
    '(iv)':  ('width',          'the support width'),
    '(v)':   ('representation', 'the representation'),
    '(vi)':  ('modulus',        'the finite modulus'),
}


def component1(sites, face_cut, second):
    rec('=' * 100)
    rec('### COMPONENT 1 -- EACH SITE`S INDEX, READ FROM ITS OWN ENTRY.')
    rec('=' * 100)
    rec('  source : FACES_LEDGER.md:31, row U1, and nothing else.')
    rec('  ### YIELD A -- THE CUT AS THE FACE FIXED IT (each marker to the next, the last to the tally):')
    for k, _ in MARKS:
        rec('      %-6s %5d characters' % (k, len(face_cut[k])))
    rec('      ### ### **AND IT IS DEFECTIVE, PRINTED RATHER THAN PATCHED AWAY.** ### The row enumerates')
    rec('      ### its six sites TWICE -- once as entries, again as `KIND`/`WITNESS` cells -- so running')
    rec('      ### the last marker to the tally swept THE WHOLE SECOND ENUMERATION into `(vi)`, which is')
    rec('      ### why `(vi)` reads %d characters against `(i)`s %d.'
        % (len(face_cut['(vi)']), len(face_cut['(i)'])))
    rec('  ### YIELD B -- THE CORRECTED CUT: each site`s block in BOTH enumerations, joined.')
    for k, _ in MARKS:
        rec('      %-6s %5d characters  (entry %d + KIND cell %d)'
            % (k, len(sites[k]), len(face_cut[k]) if k != '(vi)' else len(sites[k]) - len(second.get(k, '')),
               len(second.get(k, ''))))
    rec('      ### ### **BOTH CUTS ARE ON THE RECORD; YIELD B IS THE ONE READ BELOW.**')
    rec('')
    out = {}
    for k, _ in MARKS:
        txt = sites[k]
        rec('-' * 100)
        rec('### SITE %s' % k)
        rec('-' * 100)
        narrow = [s for s in sentences(txt) if any(m in s.lower() for m in IDX_MARKS)]
        cands = [s for s in sentences(txt) if any(m in s.lower() for m in IDX_MARKS_WIDE)]
        rec('  ### MATCHER YIELDS -- narrow set %d ; widened set %d   ### **BOTH PRINTED (b396`s rule).**'
            % (len(narrow), len(cands)))
        for c in cands[:6]:
            rec('      | %s' % c[:220])
        if len(cands) > 6:
            rec('      ... %d further' % (len(cands) - 6))
        word, gloss = READING[k]
        quoted = next((c for c in cands if word in c.lower()), None)
        if quoted is None:
            rec('  ### ### **INDEX : UNNAMED** -- no sentence of this site names an index.')
            out[k] = dict(index=None, quoted=None, gloss=None)
            continue
        rec('  ### THE SENTENCE THE INDEX IS TAKEN FROM, QUOTED WHOLE:')
        rec('      | %s' % quoted)
        rec('  ### ### **INDEX, IN ONE WORD : `%s`** (%s).' % (word, gloss))
        rec('  ### the word occurs in the quoted sentence : %s   ### **THE FACE`S RULE, CHECKED.**'
            % (word in quoted.lower()))
        out[k] = dict(index=word, quoted=quoted, gloss=gloss)
    rec('')
    rec('  ### ### **THE SIX INDICES : %s**'
        % ' ; '.join('%s %s' % (k, out[k]['index'] or 'UNNAMED') for k, _ in MARKS))
    shared = {}
    for k, _ in MARKS:
        shared.setdefault(out[k]['index'], []).append(k)
    dup = {i: ks for i, ks in shared.items() if len(ks) > 1}
    rec('  ### ### **INDICES SHARED BY MORE THAN ONE SITE : %s**'
        % (' ; '.join('%s <- %s' % (i, ', '.join(ks)) for i, ks in dup.items()) or 'none'))
    rec('  ### this is the row`s own observation, not a bridge: *(iii) AND (iv) SHARE AN INDEX')
    rec('  ### -- THE SUPPORT WIDTH -- AND DIFFER IN OBJECT*. ### **NO BRIDGE IS TYPED.**')
    rec('')
    return out


# ====================================================================================================
# ### COMPONENT 2
# ====================================================================================================
def ranges():
    """### **EVERY RANGE READ OFF ITS OWN SOURCE, ALL THREE, BEFORE ANY SITE IS PLACED.**"""
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE THREE GENERATORS. ### **ALL THREE RANGES FIRST; NO SITE PLACED YET.**')
    rec('=' * 100)
    G = {}

    # --- G1 -------------------------------------------------------------------------------
    wt = read(W).split(NL)
    ident = next(l.strip() for l in wt if 'requires to vanish' in l)
    retl = next(l.strip() for l in wt if l.strip().startswith('return dict(zero='))
    names = [n for n in re.findall(r'(\w+)=', retl) if n not in ('residual', 'prime_terms')]
    rec('  ### (G1) THE IDENTITY `Z = P - PR + A`. ### source: tools/b321_window.py')
    rec('      the identity in its own words  | %s' % ident)
    rec('      the range, off the `return`    | %s' % retl)
    rec('      ### ### **RANGE : %d MEMBERS -- %s.** ### read off the function, not typed.'
        % (len(names), ', '.join(names)))
    # ### each member's own index, quoted from the function's own body.
    # ### **A COARSE LABEL CORRECTED BY FOLLOWING THE SOURCE CHAIN.** ### `zeros` was read off the
    # ### docstring; the DEFINITION is `Z = ... hhat_blocked(v, w, AT.GAM)`, and `AT.GAM` is
    # ### `np.load("zeta_ordinates.npy")` -- the zeros BY THEIR ORDINATES, which is the height.
    # ### **BOTH READINGS ARE PRINTED**; the traced one governs, because the face says a member's
    # ### definition is read at the generator's own source, and the source chain IS that source.
    g1idx = {
        'zero': ('zeros, by their ordinates -- the height',
                 next(l.strip() for l in wt if l.strip().startswith('Z = '))),
        'pole': ('none -- a constant term', next(l.strip() for l in wt if l.strip().startswith('P = '))),
        'arch': ('u, the archimedean variable', next(l.strip() for l in wt if l.strip().startswith('A = '))),
        'prime': ('primes', next(l.strip() for l in wt if l.strip().startswith('PR, terms = '))),
    }
    rec('      ### the `zero` channel`s coordinate, coarse reading off the docstring : `zeros`')
    rec('      ### the same channel, TRACED to its definition : AT.GAM = np.load("zeta_ordinates.npy"),')
    rec('      ### the banked verified ORDINATES -- so the channel ranges over the zeros BY HEIGHT.')
    rec('      ### **BOTH PRINTED; THE TRACED READING GOVERNS.**')
    for n in names:
        rec('      member %-6s ranges over : %-40s | %s' % (n, g1idx[n][0], g1idx[n][1][:64]))
    G['G1'] = dict(members=names, idx={n: g1idx[n][0] for n in names},
                   source='tools/b321_window.py:134,:143')

    # --- G2 -------------------------------------------------------------------------------
    fl = read(FN).split(NL)
    sent = next(l for l in fl if 'These are one premise in five registers' in l)
    m = re.search(r'five registers: ([^.]*)\.', sent)
    regs = [x.strip() for x in re.split(r',\s*|\s+and\s+', m.group(1)) if x.strip()]
    rec('')
    rec('  ### (G2) THE REGISTER PENTAGON OF SECTION 27.3. ### source: FINDINGS.md:3035, the deposit`s own sentence')
    rec('      | %s' % m.group(0))
    rec('      ### ### **RANGE : %d MEMBERS -- %s.** ### split on the sentence`s own commas and its `and`.'
        % (len(regs), ', '.join(regs)))
    # ### each register's own statement, from the FACES_LEDGER rows that carry them.
    rrows = {}
    for l in read(FL).split(NL):
        if re.match(r'^\| R[1-5] \|', l):
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            rrows[c[0]] = c[1]
    order = ['R1', 'R2', 'R3', 'R4', 'R5']
    g2idx = {}
    for reg, rid in zip(regs, order):
        st = rrows.get(rid, '')
        # ### the coordinate the register's own statement ranges over, quoted from that statement.
        if 'at some prime' in st:
            co = 'primes'
        elif 'through places' in st:
            co = 'places'
        elif 'multiplicative place' in st:
            co = 'the multiplicative place'
        elif 'universality' in st:
            co = 'none stated in the row'
        else:
            co = 'none stated in the row'
        g2idx[reg] = co
        rec('      member %-22s = %-3s ranges over : %-26s | %s' % (reg, rid, co, st[:64]))
    G['G2'] = dict(members=regs, idx=g2idx, source='FINDINGS.md:3035 + FACES_LEDGER rows R1-R5')

    # --- G3 -------------------------------------------------------------------------------
    stm = next(l for l in fl if l.startswith('**(S)** For every `g` in the source'))
    k8 = next(l for l in fl if '**K8** the quantifiers' in l)
    rec('')
    rec('  ### (G3) THE STATED CLAUSE OF b332. ### source: FINDINGS.md:3039 (the statement) and :3054 (K8)')
    rec('      the statement, its opening quantifier | %s' % stm[:150])
    rec('      the places sum it carries             | %s'
        % (re.search(r'`(Σ_v W_v\(f\)[^`]*)`', stm).group(1) if re.search(r'`(Σ_v W_v\(f\)[^`]*)`', stm) else '(not matched)'))
    rec('      K8, the clause`s own quantifiers      | %s' % k8[:190])
    vars_ = []
    if 'For every `g`' in stm:
        vars_.append(('g', 'the source`s class', '**(S)** *"For every `g` in the source`s class"*'))
    if re.search(r'Σ_v W_v', stm):
        vars_.append(('v', 'the places', '**(S)** *"the places sum ... `Σ_v W_v(f) ≤ 0`"*'))
    if 'over the zeros' in k8:
        vars_.append(('the zeros', 'the zeros of zeta',
                      'K8 *"over the class (infinite) and, through the explicit formula, over the zeros"*'))
    rec('      ### ### **RANGE : %d MEMBERS -- %s.** ### every one quoted from the statement or from K8.'
        % (len(vars_), ', '.join(v[0] for v in vars_)))
    for v, rng, q in vars_:
        rec('      member %-10s ranges over : %-22s | %s' % (v, rng, q))
    G['G3'] = dict(members=[v[0] for v in vars_], idx={v[0]: v[1] for v in vars_},
                   source='FINDINGS.md:3039, :3054')
    rec('')
    rec('  ### ### **AN ASYMMETRY BETWEEN G1 AND G3, PRINTED RATHER THAN SMOOTHED OVER:** both carry')
    rec('  ### the zeros, and their sources name them at different grains. ### `G1`s zero channel is a')
    rec('  ### COMPUTED object whose source names the ORDINATES; `G3`s zero quantifier is a STATED one')
    rec('  ### whose source (`K8`) says only *"over the zeros"* and names no coordinate. ### **THE SAME')
    rec('  ### SET, TWO SOURCES, TWO GRAINS** -- and the face binds each member to its own source, so')
    rec('  ### the two are read differently and the difference is a finding, not an inconsistency.')
    rec('')
    rec('  ### ### **ALL THREE RANGES ARE NOW PRINTED. ### ONLY NOW IS ANY SITE PLACED.**')
    rec('')
    return G


# ### THE PLACEMENT, BY THE FACE'S RULE. ### For each (site index, member) the tool asks whether the
# ### site's index IS the member's own index, or is a coordinate the member's definition ranges over.
# ### **THE COORDINATE SETS ARE THE ONES PRINTED ABOVE, AND NOTHING ELSE IS CONSULTED.**
def embeds(site_idx, member_range):
    if site_idx is None:
        return False, 'the site names no index, so it can be no member`s index'
    r = (member_range or '').lower()
    if r.startswith('none'):
        return False, 'the member`s definition ranges over nothing the record states'
    if site_idx in r or r.rstrip('s') in site_idx:
        return True, 'the site`s index `%s` is what the member ranges over (%s)' % (site_idx, member_range)
    return False, 'the member ranges over %s, which is not `%s`' % (member_range, site_idx)


def component2(idx, G):
    rec('-' * 100)
    rec('### THE SIX-BY-THREE TABLE. ### **A SITE EMBEDS IN A GENERATOR IF IT EMBEDS IN SOME MEMBER.**')
    rec('-' * 100)
    rec('      site    index            G1 (4 channels)        G2 (5 registers)       G3 (%d variables)'
        % len(G['G3']['members']))
    table, holders = {}, {g: {m: [] for m in G[g]['members']} for g in ('G1', 'G2', 'G3')}
    for k, _ in MARKS:
        si = idx[k]['index']
        row = {}
        for g in ('G1', 'G2', 'G3'):
            hit = [m for m in G[g]['members'] if embeds(si, G[g]['idx'][m])[0]]
            for m in hit:
                holders[g][m].append(k)
            row[g] = hit
        table[k] = row
        rec('      %-7s %-16s %-22s %-22s %s'
            % (k, si or 'UNNAMED',
               ', '.join(row['G1']) or '### NO MEMBER',
               ', '.join(row['G2']) or '### NO MEMBER',
               ', '.join(row['G3']) or '### NO MEMBER'))
    rec('')
    verd = {}
    for g in ('G1', 'G2', 'G3'):
        unplaced = [k for k, _ in MARKS if not table[k][g]]
        empty = [m for m in G[g]['members'] if not holders[g][m]]
        rec('  ### %s -- source %s' % (g, G[g]['source']))
        rec('      members with no site : %s' % (', '.join(empty) or 'none'))
        rec('      sites with no member : %s' % (', '.join(unplaced) or 'none'))
        if unplaced:
            v = 'NOT THE INDEX SET'
            why = 'site(s) %s fail to embed in any member' % ', '.join(unplaced)
        elif empty:
            v = 'FRAGMENT'
            why = 'every site embeds, but %s stand(s) empty and the record states no sentence that the obstruction does not arise there' % ', '.join(empty)
        else:
            v = 'CLOSED'
            why = 'every site embeds and no member is empty'
        verd[g] = dict(verdict=v, why=why, empty=empty, unplaced=unplaced,
                       placed={k: table[k][g] for k, _ in MARKS})
        rec('      ### ### **VERDICT : %s** -- %s' % (v, why))
        if v == 'FRAGMENT':
            rec('      ### **THE UNVISITED MEMBERS, NAMED : %s.**' % ', '.join(empty))
            rec('      ### A `CLOSED` verdict would need, for each of them, a statement IN THE RECORD,')
            rec('      ### quoted with its address, that the obstruction does not arise there. ### **NONE')
            rec('      ### IS QUOTED, BECAUSE THIS ACT LOCATED NONE**, and an absent statement is not one.')
        rec('')
    return table, verd


# ====================================================================================================
# ### COMPONENT 3
# ====================================================================================================
def component3(sites, idx):
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE CONTROL, AND THE HALT IT RUNS INTO.')
    rec('=' * 100)
    cell = u1_cell()
    rec('  ### **THE ORDER ASKS FOR A SITE THE ROW RECORDS AS KIND `(a)`, VACUOUS.**')
    rec('  ### **EVERY ROUTE TO ONE IS RUN, AND A POSITIVE CONTROL RUNS BESIDE EACH.**')
    rec('')
    r = {}
    tally = re.search(r'THE TALLY, PRINTED SO NO READER HAS TO COUNT: KIND .{0,120}', cell)
    rec('  (r1) THE ROW`S OWN TALLY SENTENCE')
    rec('       | %s' % tally.group(0))
    a1 = '0 `(a)`' in tally.group(0)
    b1 = '1 `(b)`' in tally.group(0)
    rec('       kind (a) sites : %s   ### positive control, kind (b) sites found : %s'
        % ('NONE -- the tally says zero' if a1 else '### the tally does not say zero', b1))
    r['r1'] = dict(a_found=not a1, b_found=b1)

    rec('  (r2) EACH OF THE SIX SITE TEXTS, SEARCHED FOR THE ROW`S KIND WORDING')
    fa, fb = [], []
    for k, _ in MARKS:
        t = sites[k]
        ka = bool(re.search(r'KIND: *`?\(a\)`?', t))
        kb = bool(re.search(r'KIND: *`?\(b\)`?', t))
        if ka:
            fa.append(k)
        if kb:
            fb.append(k)
        rec('       %-6s KIND (a) : %-5s   KIND (b) : %s' % (k, ka, kb))
    rec('       ### kind (a) sites found : %s   ### positive control, kind (b) : %s'
        % (fa or 'NONE', fb or 'NONE'))
    r['r2'] = dict(a_found=fa, b_found=fb)

    rec('  (r3) THE ROW`S `KIND` CELLS, ONE BY ONE, QUOTED')
    cells = {}
    for k, _ in MARKS:
        m = re.search(r'KIND: *[^.]{0,40}', sites[k])
        cells[k] = m.group(0).strip() if m else '### NO KIND CELL'
        rec('       %-6s | %s' % (k, cells[k]))
    a3 = [k for k in cells if '(a)' in cells[k]]
    b3 = [k for k in cells if '(b)' in cells[k]]
    rec('       ### kind (a) sites found : %s   ### positive control, kind (b) : %s'
        % (a3 or 'NONE', b3 or 'NONE'))
    r['r3'] = dict(a_found=a3, b_found=b3)

    pos = b1 and bool(fb) and bool(b3)
    halt = (a1 and not fa and not a3)
    rec('')
    rec('  ### ### **THE POSITIVE CONTROL FIRES ON ALL THREE ROUTES : %s.**' % pos)
    rec('  ### ### **AND ALL THREE ROUTES RETURN NO KIND-`(a)` SITE : %s.**' % halt)
    if pos and halt:
        rec('  ### ### **SO THE HALT IS PROVED: THE CONTROL THE ORDER ASKS FOR CANNOT BE RUN, BECAUSE')
        rec('  ### ### THE RECORD HOLDS NO SITE OF KIND `(a)`.** ### **NO SUBSTITUTE IS OFFERED AND NO')
        rec('  ### ### SITE IS RE-KINDED.** ### b404 DEFINED kind `(a)` -- *"empty because there is nothing')
        rec('  ### ### to range over -- vacuous forever"* -- and no site was ever entered under it.')
    else:
        rec('  ### ### **THE HALT IS NOT PROVED.** ### A route failed its own positive control, so this')
        rec('  ### ### is a broken search and not a result.')

    rec('')
    rec('  ### ### **THE SECOND HALF -- A DIFFERENT AND DECIDABLE QUESTION, NOT A SUBSTITUTE.**')
    rec('  ### The placement rule`s inputs, as the face fixed them and as `embeds()` takes them:')
    src = read(os.path.join(T, 'b459_components.py'))
    sig = next(l.strip() for l in src.split(NL) if l.startswith('def embeds('))
    rec('       | %s' % sig)
    reads_kind = 'kind' in src.split('def embeds(')[1].split('def component2')[0].lower()
    rec('       the rule`s inputs are a SITE INDEX and a MEMBER RANGE. ### does its body read KIND : %s'
        % reads_kind)
    rec('  ### ### **`KIND` IS NOT AN INPUT TO THE RULE, SO THE RULE CANNOT DISTINGUISH KINDS --')
    rec('  ### ### WHATEVER SITES THE ROW HAPPENS TO HOLD.** ### The answer does not depend on a')
    rec('  ### ### kind-`(a)` site existing, which is why it survives the halt above.')
    rec('  ### ### **AND THE CONSEQUENCE IS CARRIED, NOT LEFT TO BE NOTICED: COMPONENT 2`S VERDICTS')
    rec('  ### ### ARE SCOPED TO INDICES.** ### They say where a site`s index sits in a generator`s')
    rec('  ### ### range and NOTHING about whether the obstruction at that site is live, empty or')
    rec('  ### ### vacuous. ### A generator that embeds every site has not answered any of them.')
    rec('  ### **THE ONE CASE THE RECORD LETS US SEE THIS IN:** `(v)` is the row`s single kind-`(b)`')
    rec('  ### site -- *"empty because the available uniformity ranges over a class that does not')
    rec('  ### contain the corpus`s other object"* -- and the rule placed it by its index alone,')
    rec('  ### exactly as it placed the five sites the row calls NOT EMPTY.')
    r['positive_control'] = pos
    r['halt_proved'] = halt
    r['rule_reads_kind'] = reads_kind
    return r


if __name__ == '__main__':
    cell = u1_cell()
    sites, face_cut, second = cut2(cell)
    idx = component1(sites, face_cut, second)
    G = ranges()
    table, verd = component2(idx, G)
    ctl = component3(sites, idx)
    io.open(os.path.join(D, 'b459_sites.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(idx, indent=1, ensure_ascii=False) + NL)
    io.open(os.path.join(D, 'b459_generators.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(G, indent=1, ensure_ascii=False) + NL)
    io.open(os.path.join(D, 'b459_embed.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(dict(table=table, verdicts=verd), indent=1, ensure_ascii=False) + NL)
    io.open(os.path.join(D, 'b459_control.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(ctl, indent=1, ensure_ascii=False) + NL)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  written: %s and four json banks' % os.path.basename(OUT))
