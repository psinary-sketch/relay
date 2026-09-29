# -*- coding: utf-8 -*-
"""b560_record.py -- LANE TWO, ACT TWO: THE LI-WEIL BRIDGE, STAGED; b559`S CLEAN GAIN MERGED AS v0.3; THE DETECTION REGION
RE-SCOPED; THE SUITE`S FILE-TIME ARMS MOVED TO DIGESTS: THE RECORD, UNDER (R170) AND ITS (4) AMENDMENT.
### `python tools/b560_record.py reads | suite | clean | e0clean | rescope | stage | e0 | rowgen | findings | row | trail |
### components | desk`
### The branches, their commits, merges, tags, pushes and read-backs, the commits, pushes and branch commands of the ritual
### are the seat`s. This file deletes nothing.
"""
import io, json, os, re, subprocess, sys, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b551_record as P  # noqa: E402
DD = 'D:' + os.sep
PP = P.PP
FIND, OT = P.FIND, P.OT
CORR = P.CORR
EF = os.path.join(DD, 'SIDE-explicit-formula')
LV = P.LV
NL = chr(10)
rd, g, append_to, guard_absent, poss, outside_bt = P.rd, P.g, P.append_to, P.guard_absent, P.poss, P.outside_bt
line_of = P.line_of
PRIOR_RELAY = 'f8017036'   # ### b559`s table housekeeping -- relay`s tip before this act
PRIOR_PP = 'b132b5e'       # ### b559`s PLACE-papers commit
PRIOR_GS = '3268b94'       # ### SIDE-global-section before this act
MAIN0 = '81ae1758f28e280f4e924e8acd76b4b76ae4ac9d'   # ### SIDE-explicit-formula main before this act
V02 = '5c72cad24303f23d92256ebd466d3a3d32424a4b'
HELD = 'detection-region-b559'
HELD_TIP = '8faf7ded8754870669547c9caa54ee5f0275e7c1'
CLEAN = 'detection-region-clean'
LIW = 'li-weil-b560'
NS = 'SIDEExplicitFormula.B321.'
NSL = 'SIDEExplicitFormula.LiWeil.'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    open(os.path.join(D, n), 'wb').write((json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def put_txt(n, lines):
    open(os.path.join(D, n), 'wb').write((NL.join(lines) + NL).encode('utf-8'))


def at(rev, rel, repo=EF):
    return subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, rel)], capture_output=True).stdout.decode('utf-8', 'replace').replace(chr(13), '')


def decl_at(text, name):
    """### the first line declaring `name` (theorem, lemma, def, structure), 1-based; None if absent."""
    pat = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|noncomputable\s+)?(?:theorem|lemma|def|structure|abbrev)\s+' + re.escape(name) + r'(?=[\s:({\[]|$)')
    for i, l in enumerate(text.split(NL)):
        if pat.match(l):
            return i + 1
    return None


def statement(text, n, cap=14):
    """### the statement from its declaring line to the line carrying `:=` or `where` (inclusive), verbatim."""
    ### ### a `def` or `structure` whose body follows on later lines is printed to its next blank line (its fields, its
    ### ### hypotheses verbatim); a theorem stops at the line carrying `:=` (b560`s first reads run cut EF_lit and ZeroConfig).
    ls = text.split(NL)
    out = []
    body = re.match(r'^(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+)?(?:def|structure|abbrev)\b', ls[n - 1]) is not None
    for l in ls[n - 1:n - 1 + cap]:
        if body and out and (not l.strip() or l.startswith('/--')):
            break
        out.append(l)
        if not body and (':=' in l or re.search(r'\bwhere\s*$', l)):
            break
    return out


# ------------------------------------------------------------------------------ READING (1): the reads
DECLS = [
    # (rev, file, name, what)
    (HELD_TIP, 'SIDEExplicitFormula/DetectionRegion.lean', n, 'the HELD branch module') for n in
    ('h2_sign_upto', 'h2_sign_upto_mono', 'h2_sign_imp_upto', 'upto_all_imp_h2_sign', 'h2_sign_iff_forall_upto',
     'forall_upto_iff_rh', 'ellOf', 'j₀', 'detection_region')
] + [
    (MAIN0, 'Zeta23/ExplicitFormula.lean', 'literatureRHS', 'the literature right-hand side'),
    (MAIN0, 'Zeta23/ExplicitFormula.lean', 'EF_lit', 'H-EF, literature form: the hypotheses on the test function'),
    (MAIN0, 'Zeta23/WeilEF/Main.lean', 'EF_lit_zetaZeroConfig', 'EF_lit for the genuine instance'),
    (MAIN0, 'Zeta23/Defs.lean', 'gammaOf', 'the ordinate map'),
    (MAIN0, 'Zeta23/Defs.lean', 'reflect', 'the configuration`s reflection'),
    (MAIN0, 'Zeta23/Defs.lean', 'ZeroConfig', 'the configuration type'),
    (MAIN0, 'Zeta23/Statement.lean', 'IsNontrivialZero', 'membership'),
    (MAIN0, 'Zeta23/Statement.lean', 'zeroMult', 'multiplicity'),
    (MAIN0, 'Zeta23/Statement.lean', 'ZetaSeam', 'the seam'),
    (MAIN0, 'Zeta23/Statement.lean', 'zetaZeros', 'the instance from the seam'),
    (MAIN0, 'Zeta23/Statement/SeamClosed.lean', 'zetaSeam', 'the seam discharged'),
    (MAIN0, 'Zeta23/Statement/SeamClosed.lean', 'zetaZeroConfig', 'the genuine instance'),
    (MAIN0, 'Zeta23/ZetaReflect.lean', 'riemannZeta_conj', 'conjugation fact (set)'),
    (MAIN0, 'Zeta23/ZetaReflect.lean', 'analyticOrderAt_zeta_conj', 'conjugation fact (multiplicity)'),
    (MAIN0, 'Zeta23/ZetaReflect.lean', 'zeta_reflect_zero', 'reflection fact (set)'),
    (MAIN0, 'Zeta23/ZetaReflect.lean', 'zeta_mult_reflect', 'reflection fact (multiplicity)'),
    (MAIN0, 'Zeta23/RvM/LocalCount.lean', 'zeta_local_zero_count', 'the count bound'),
    (MAIN0, 'Zeta23/RvM/LocalCount.lean', 'zetaZeroConfig_local_count', 'the count bound, H-RvM`s vocabulary'),
    (MAIN0, 'Zeta23/WeilEF/ZeroSummability.lean', 'zero_sum_inv_sq_gen', 'the log-form grouping (Stage B`s input)'),
    (MAIN0, 'Zeta23/WeilEF/ZeroSummability.lean', 'zero_sum_inv_sq', 'the same, for the zeros of zeta'),
    (MAIN0, 'Zeta23/WeilEF/ZeroSummability.lean', 'EF_zero_sum_summable_gen', 'the finite window handled (its pattern)'),
    (MAIN0, 'SIDEExplicitFormula/PowerLimit.lean', 'weighted_summable', 'the fourth-power grouping'),
    (MAIN0, 'SIDEExplicitFormula/DecayBound.lean', 'paperFT_decay', 'the decay bound'),
    (MAIN0, 'SIDEExplicitFormula/Seam.lean', 'h2_sign_iff_rh', 'the seam`s equivalence'),
]
BALPOS = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
ARMS_FILETIME = ('G-PEEK-DECLARED', 'G-WRITELIST-KINDS', 'G-PRIORBANK-UNCHANGED')


def reads():
    L = ['b560 -- READING (1): THE READS, PRINTED VERBATIM BY PATH AND LINE (COMPONENT 3), BEFORE ANY NEW FILE IS WRITTEN',
         '### SIDE-explicit-formula main = %s ; the HELD branch %s = %s' % (MAIN0[:7], HELD, HELD_TIP[:7]), '']
    L.append('### main against v0.2 (git diff --stat v0.2 main): ' + ' ; '.join(
        x.strip() for x in g(EF, 'diff', '--stat', V02, MAIN0).split(NL) if x.strip()))
    rows = []
    for rev, rel, name, what in DECLS:
        t = at(rev, rel)
        n = decl_at(t, name)
        L.append('')
        if n is None:
            L.append('### %s @%s %s -- %s -- ### NOT FOUND' % (rel, rev[:7], name, what))
            rows.append(dict(rev=rev[:7], file=rel, name=name, line=None))
            continue
        st = statement(t, n)
        L.append('### %s:%d @%s -- %s (%s)' % (rel, n, rev[:7], name, what))
        for i, l in enumerate(st):
            L.append('    %5d | %s' % (n + i, l))
        rows.append(dict(rev=rev[:7], file=rel, name=name, line=n, text=NL.join(st)))
    held = at(HELD_TIP, 'SIDEExplicitFormula/DetectionRegion.lean').split(NL)
    L.append('')
    L.append('### the two sorry bodies on the HELD branch, by line:')
    for i, l in enumerate(held):
        if re.search(r'\bsorry\b', l) and not l.lstrip().startswith(('--', '/-', '`')) and 'sorry`' not in l and 'sorry` ' not in l:
            L.append('    DetectionRegion.lean:%d | %s' % (i + 1, l))
    # ### the document reads
    B = rd(BALPOS).split(NL)
    L.append('')
    L.append('### BALANCE_AND_POSITIVITY.md -- C.7.3 as it stands, and the Bombieri-Lagarias formula where the document quotes it:')
    for n in (498, 500, 504):
        L.append('    BALPOS:%d | %s' % (n, B[n - 1][:260]))
    for n in (70, 422):
        L.append('    BALPOS:%d | %s' % (n, B[n - 1][:400]))
    L.append('    BALPOS:68 (the on-line term, compiled in another kernel) | ...%s...' % B[67][B[67].index('One half'):B[67].index('One half') + 330])
    lvt = at('HEAD', 'SIDELvConservation/PartialPositivity.lean', LV)
    n = decl_at(lvt, 'blTerm_nonneg_of_onLine')
    L.append('### SIDE-lv-conservation @%s SIDELvConservation/PartialPositivity.lean:%s -- blTerm_nonneg_of_onLine (cited, not imported):'
             % (g(LV, 'rev-parse', '--short', 'HEAD').strip(), n))
    for i, l in enumerate(statement(lvt, n)):
        L.append('    %5d | %s' % (n + i, l))
    n2 = decl_at(lvt, 'blTerm')
    if n2:
        for i, l in enumerate(statement(lvt, n2)):
            L.append('    %5d | %s' % (n2 + i, l))
    pr = rd(os.path.join(D, 'b549_premise.txt')).split(NL)
    L.append('### relay data/b549_premise.txt:12 -- inequalityToPositivity (the eventual consumer, cited, not imported):')
    L.append('    ' + pr[11])
    O = rd(OT).split(NL)
    L.append('')
    L.append('### OPEN_TRAILS:')
    for n in (3548, 11203, 11265, 11290, 11294, 11295, 11296, 11297, 11298, 11299, 11300, 11301, 11302, 11424, 11491, 11493):
        L.append('    OPEN_TRAILS.md:%d | %s' % (n, O[n - 1][:300]))
    S = rd(os.path.join(T, 'b559_checks.py')).split(NL)
    L.append('')
    L.append('### THE SUITE`S FILE-TIME ARMS, tools/b559_checks.py (each arm, and every line reading a file time):')
    for a in ARMS_FILETIME:
        ln = [i + 1 for i, l in enumerate(S) if ("('%s'" % a) in l]
        L.append('    %-24s declared at :%s' % (a, ln))
    for i, l in enumerate(S):
        if 'getmtime' in l:
            L.append('    b559_checks.py:%d | %s' % (i + 1, l.strip()[:200]))
    # ### H11a, from the prints alone
    have = {r['name']: r for r in rows if r.get('line')}
    zc = have.get('ZeroConfig', {}).get('text', '')
    conj_set = 'riemannZeta (conj s) = conj (riemannZeta s)' in have.get('riemannZeta_conj', {}).get('text', '')
    conj_mult = 'analyticOrderAt riemannZeta (conj w) = analyticOrderAt riemannZeta w' in have.get('analyticOrderAt_zeta_conj', {}).get('text', '')
    carrier = 'IsNontrivialZero' in at(MAIN0, 'Zeta23/Statement.lean') and 'zetaZeros zetaSeam' in have.get('zetaZeroConfig', {}).get('text', '')
    reflect_only = ('reflect_mem' in rd_all(MAIN0, 'Zeta23/Defs.lean', 'ZeroConfig')) and ('conj' not in rd_all(MAIN0, 'Zeta23/Defs.lean', 'ZeroConfig'))
    refl_def = have.get('reflect', {}).get('text', '')
    L.append('')
    L.append('### ### **H11a, SCORED FROM THE PRINTS ALONE, BEFORE ANY BUILD:**')
    L.append('    the type`s symmetry fields : reflect_mem, mult_reflect only (no conjugation field) : %s' % reflect_only)
    L.append('    reflect ρ = 1 - (starRingEnd ℂ) ρ  (Defs.lean:124) : %s -- at ρ.re = 1/2 it is ρ itself (1 - (1/2 - iγ) = 1/2 + iγ)'
             % ('1 - (starRingEnd ℂ) ρ' in refl_def))
    L.append('    H11a AS FIRST WORDED (reflection sufficient for pairing) : REFUTED ON THE TYPE -- the configuration`s only symmetry fixes the line')
    L.append('    the conjugation facts printed : riemannZeta_conj %s ; analyticOrderAt_zeta_conj %s ; the instance`s carrier and mult are IsNontrivialZero and zeroMult : %s'
             % (conj_set, conj_mult, carrier))
    w = 'HOLDS FROM THE PRINTS' if (conj_set and conj_mult and carrier) else 'NOT SUPPORTED BY THE PRINTS'
    L.append('    ### H11a AS AMENDED (conjugation; the author`s (R170)(4) amendment) : %s -- ζ(conj ρ) = conj ζ(ρ) = 0 for ρ ≠ 1, the open strip'
             ' is conjugation-invariant, and the order agrees; the compile is Stage A`s' % w)
    put_txt('b560_reads.txt', L)
    put_json('b560_reads.json', dict(rows=rows, h11a_first='REFUTED', h11a_amended=w, reflect_only=reflect_only,
                                     conj_set=conj_set, conj_mult=conj_mult, carrier=carrier))
    print(NL.join(L[-8:]))
    print('  written: b560_reads.txt (%d lines), b560_reads.json' % len(L))


def rd_all(rev, rel, name):
    t = at(rev, rel)
    n = decl_at(t, name)
    return NL.join(statement(t, n, 20)) if n else ''



# ------------------------------------------------------------------------------ the prints and the rowgen record, shared
SCR = os.environ.get('B560_SCRATCH') or os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp')
STD3 = ['propext', 'Classical.choice', 'Quot.sound']


def parse_prints(text):
    """### Lean's own `#print axioms` lines -> {name: [axioms]}; 'does not depend on any axioms' -> []."""
    out = {}
    for l in text.split(NL):
        m = re.match(r"'([^']+)' depends on axioms: \[(.*)\]", l.strip())
        if m:
            out[m.group(1)] = [x.strip() for x in m.group(2).split(',') if x.strip()]
        m = re.match(r"'([^']+)' does not depend on any axioms", l.strip())
        if m:
            out[m.group(1)] = []
    return out


def check_line(prints_text, n):
    pl = prints_text.split(NL)
    for j, l in enumerate(pl):
        if l.startswith(n + ' :') or l.startswith('@' + n + ' :'):   # ### `#check @name` prints the `@` (b560 defect (i))
            chk = l
            k = j + 1
            while k < len(pl) and pl[k].startswith(' '):
                chk += ' ' + pl[k].strip()
                k += 1
            return chk
    return ''


def rowgen_record(names, rel, rev, prints_text):
    """### rowgen's own source-side functions, IMPORTED (extract_doc_body, definition_encoded), at the pin; the check and
    ### axioms lines are the stdin prints of the same declarations -- rowgen's lean_check_axioms is NOT RUN: its
    ### `import <module>` needs an olean this act does not build ((Z): no `lake build`)."""
    sys.path.insert(0, os.path.join(T, 'rowgen'))
    import rowgen as RG
    src = at(rev, rel)
    recs = []
    for n in names:
        short = n.split('.')[-1]
        chk = check_line(prints_text, n)
        doc, body1 = RG.extract_doc_body(src, n)
        concl = chk.split(':', 1)[1] if ':' in chk else short
        de, why = RG.definition_encoded(src, concl)
        ax = parse_prints(prints_text).get(n)
        recs.append(dict(name=n, pin=rev[:7], file=rel, check=chk, axioms=ax, doc=doc, body1=body1, defenc=de, defenc_why=why))
    ctl = RG.definition_encoded('def b560_ctl_stub : Prop := True', 'b560_ctl_stub')
    return recs, ctl


# ------------------------------------------------------------------------------ READING (3): the clean merge
CLEAN_NAMES = [NS + x for x in ('h2_sign_upto', 'h2_sign_imp_upto', 'upto_all_imp_h2_sign', 'h2_sign_iff_forall_upto', 'forall_upto_iff_rh')]
CLEAN_GRADES = {
    'h2_sign_upto': ('A DEFINITION -- NO GRADE IN THE THREE-GRADE VOCABULARY (it is not a terminal)',
                     'a Prop over `classK` windows and b321`s `poleTerm`, `primeSum`, `archTerm`; it names no zero of zeta and no real part: the salt-check passes'),
    'h2_sign_imp_upto': ('DERIVES', 'the restriction of `h2_sign` to the windows vanishing outside [-L0, L0]; one line'),
    'upto_all_imp_h2_sign': ('DERIVES', 'compact support of a classK window gives a bound r; the finite positivity at r is the sign'),
    'h2_sign_iff_forall_upto': ('DERIVES', '`h2_sign <-> forall L0, h2_sign_upto L0`: both sides the kernel`s Props, the join proved'),
    'forall_upto_iff_rh': ('DERIVES', 'the join composed with `h2_sign_iff_rh` (Seam.lean:101); its right side is Mathlib`s `RiemannHypothesis`'),
}


def clean():
    rel = 'SIDEExplicitFormula/DetectionRegion.lean'
    tip = g(EF, 'rev-parse', CLEAN).strip()
    pr = rd(os.path.join(SCR, 'clean_prints.txt'))
    P0 = parse_prints(pr)
    src = at(tip, rel)
    L = ['b560 -- READING (3): THE CLEAN MERGE -- THE BRANCH, THE ELABORATION, THE PRINTS, THE E0 READ, THE ROWGEN RECORD', '']
    L.append('### the branch %s = %s ; its parent %s (main before this act = %s)' % (
        CLEAN, tip[:7], g(EF, 'rev-parse', '--short', CLEAN + '^').strip(), MAIN0[:7]))
    L.append('### its files against main before the act (name-status): ' + ' ; '.join(
        x.replace('\t', ' ') for x in g(EF, 'diff', '--name-status', MAIN0, tip).split(NL) if x.strip()))
    L.append('### the declarations it carries: %s' % re.findall(r'^(?:def|theorem)\s+(\S+)', src, re.M))
    L.append('### not carried from %s (absent here): %s' % (HELD, [n for n in ('h2_sign_upto_mono', 'ellOf', 'j₀', 'detection_region')
                                                            if decl_at(src, n) is None]))
    L.append('### the bodies against the HELD branch`s, declaration by declaration:')
    held = at(HELD_TIP, rel)
    same = {}
    for n in CLEAN_NAMES:
        s = n.split('.')[-1]
        a, b = decl_at(src, s), decl_at(held, s)
        same[s] = statement_block(src, a) == statement_block(held, b)
        L.append('    %-26s identical to 8faf7de`s: %s' % (s, same[s]))
    code = re.sub(r'/-.*?-/', '', src, flags=re.S)
    L.append('### sorry in the carried file (code, prose stripped): %d' % len(re.findall(r'\bsorry\b', code)))
    L.append('')
    L.append('### THE ELABORATION (data/b560_clean_elab.txt):')
    L += ['    ' + x for x in rd(os.path.join(D, 'b560_clean_elab.txt')).split(NL) if x.strip()]
    L.append('')
    L.append('### LEAN`S PRINTS (the module fed on stdin with its own header import, then AxiomCheckDetection.lean`s lines):')
    L += ['    ' + x for x in pr.split(NL) if x.strip()]
    L.append('')
    L.append('### THE E0 READ, PER DECLARATION (statement-read, the three-grade vocabulary; the salt-check on each):')
    grades = {}
    for n in CLEAN_NAMES:
        s = n.split('.')[-1]
        gr, why = CLEAN_GRADES[s]
        ax = P0.get(n)
        std = ax is not None and set(ax) <= set(STD3)
        grades[s] = dict(grade=gr, why=why, axioms=ax, std3_or_fewer=std)
        L.append('    %-26s %-12s prints %s -- %s' % (s, gr.split(' --')[0], ax, why))
    thm = [s for s in grades if grades[s]['grade'] == 'DERIVES']
    ok = all(grades[s]['std3_or_fewer'] for s in grades) and len(thm) == 4 and all(same.values())
    L.append('### ### **EVERY CARRIED THEOREM DERIVES, EVERY PRINT IS THE STANDARD THREE OR FEWER, EVERY BODY IS THE BRANCH`S: %s**'
             ' -- the merge gate of (R170)(1)' % ok)
    recs, ctl = rowgen_record(CLEAN_NAMES, rel, tip, pr)
    L.append('')
    L.append('### THE ROWGEN RECORD (tools/rowgen/rowgen.py`s extract_doc_body and definition_encoded IMPORTED, at %s):' % tip[:7])
    for r in recs:
        L.append('    %-26s defenc %-5s %s | doc: %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_why'], r['doc'][:110]))
    L.append('    control: definition_encoded on `def b560_ctl_stub : Prop := True` -> %s (must be True)' % (ctl,))
    L.append('    ### rowgen`s lean_check_axioms NOT RUN: its `import <module>` needs an olean this act does not build ((Z)); the')
    L.append('    ### check and axioms above are the stdin prints of the same declarations.')
    put_txt('b560_clean.txt', L)
    put_json('b560_clean.json', dict(branch=CLEAN, tip=tip, parent=g(EF, 'rev-parse', CLEAN + '^').strip(), grades=grades,
                                     same_as_held=same, gate=ok, rowgen=recs, rowgen_control=ctl[0]))
    print(NL.join(L[-14:]))
    print('  written: b560_clean.txt, b560_clean.json ; gate %s' % ok)


def statement_block(text, n):
    """### a declaration with its body: from its line to the next blank line."""
    out = []
    for l in text.split(NL)[n - 1:]:
        if not l.strip():
            break
        out.append(l)
    return NL.join(out)



# ------------------------------------------------------------------------------ READINGS (3) and (4): the ledger lines
HELD_LINE = ('*Appended 2026-09-29 by b560, under the author`s ruling `(R170)`(1), to the DETECTION-REGION record (:11491, :11493) -- '
             'THE HELD BRANCH AND ITS CLEAN PART:*')
RESCOPE_H = ('### `W-ORD-DETECTION-REGION` (the entry at :11151, the price corrected at :11491) -- RE-SCOPED ON THE MEASURED OBSTACLE, '
             'appended 2026-09-29, b560, under the author`s ruling (R170)(2)')
ARC_LINE = '- **Research-arc line, 2026-09-29 (b560, `(R170)`(2); owner: the author).**'
CLEAN_FH = ('## The detection region`s clean part merged: h2_sign as the conjunction over every support bound of its finite '
            'restrictions, and that conjunction as Mathlib`s RiemannHypothesis -- SIDE-explicit-formula v0.3')


def ledger1():
    cj = jl('b560_clean.json')
    tip = cj['tip']
    v03 = g(EF, 'rev-parse', 'v0.3').strip()
    out = {}
    for h in (HELD_LINE, RESCOPE_H, ARC_LINE):
        guard_absent(OT, h)
    guard_absent(FIND, CLEAN_FH)
    held_txt = (NL + HELD_LINE + ' the branch `detection-region-b559` stays as it is at `8faf7de` (pushed by name, HELD: `j₀` and '
                '`detection_region` with `sorry` bodies). Its clean part -- `h2_sign_upto`, `h2_sign_imp_upto`, `upto_all_imp_h2_sign`, '
                '`h2_sign_iff_forall_upto`, `forall_upto_iff_rh`, their bodies unchanged -- is on SIDE-explicit-formula `main` at '
                '`%s`, tagged **v0.3** (tag object `%s`, peeled `%s`, read back from the remote), cut from `main` = `81ae175` and not '
                'from v0.2: `(R170)`(1) wrote "from v0.2" assuming `main` sat at v0.2, and it sits one commit past it (b538`s '
                'RegisterDepth) -- the navigator`s, corrected by the author (relay `data/b560_ferry.txt`, paste two). v0.3 carries both '
                'contents: RegisterDepth (b538) and DetectionRegion-clean (b559/b560). `h2_sign_upto_mono` and `ellOf` stay on the '
                'HELD branch alone. Relay `data/b560_clean.txt`, `data/b560_v03.txt`.' % (tip[:7], v03[:7], tip[:7]) + NL)
    out['held'] = append_to(OT, held_txt)
    res = (NL + RESCOPE_H + NL + NL +
           'The trail entry at :11151 is rewritten by this append on the obstacle b559 measured (relay `data/b559_constants.txt`; '
           '`PowerLimit.lean`:1092 at v0.2); no byte above changes.' + NL + NL +
           '- **(E1) the configuration-relative rate** -- a rate for `rest_tendsto_zero` given the largest ratio `offScore / M` off '
           'the tie and kill sets: one lemma of moderate weight, giving an index for the whole zero configuration, not for (γ, δ). '
           'A future lane-two act.' + NL +
           '- **(E2) the per-(γ, δ) region** -- the configuration`s constants (the dominant score, the tie and kill sets, the '
           'interpolation bound over the tie nodes) bounded by (γ, δ) alone: it needs a separation estimate for the zeros near the '
           'dominant score that no compiled lemma carries. Research grade; entered as a research-arc line, the author its owner.' + NL +
           '- **The alternative beside them** -- the closed-form bench route (b554, :11332, C1-C5, three lemmas of substance). '
           'Neither (E1), (E2) nor the closed form is attempted at b560.' + NL +
           '- **The navigator`s mis-statements at `(R169)`(2), recorded as the navigator`s:** a fixed base width (the route takes its '
           'half-support ℓ = 1/(4(‖gammaOf ρ₁‖ + 1)) from the excluded zero, PowerWindow.lean:276; `PWSetup` fixes none); and '
           '"j-fold" for 2^j-fold (`power g j` is the j-fold iterated self-convolution, the 2^j-fold power, PowerWindow.lean:121, '
           ':129, so the window of index j is supported in [-2^(j+1)·ℓ, 2^(j+1)·ℓ]).' + NL + NL +
           ARC_LINE + ' The per-(γ, δ) detection region of W-ORD-DETECTION-REGION (E2): a separation estimate for the zeros of ζ '
           'near the dominant score of a power window, of a kind no compiled lemma carries. Research grade; queued, not an act.' + NL)
    out['rescope'] = append_to(OT, res)
    fnd = (NL + CLEAN_FH + NL + NL +
           '*Filed at b560 on the author`s ruling `(R170)`(1). Banks: relay `data/b560_clean.txt`, `data/b560_v03.txt`; '
           'SIDE-explicit-formula v0.3 = `%s`. Nothing about ζ`s zeros is claimed beyond the compiled statements` own words.*' % tip[:7]
           + NL + NL +
           '**What is compiled.** `h2_sign_upto L₀` is `h2_sign`’s sign on the `classK` windows that vanish outside [−L₀, L₀]. '
           '`h2_sign_iff_forall_upto : h2_sign ↔ ∀ L₀, h2_sign_upto L₀`, and `forall_upto_iff_rh : (∀ L₀, h2_sign_upto L₀) ↔ '
           'RiemannHypothesis` through `h2_sign_iff_rh` (Seam.lean:101). The two theorems and the two between them print '
           '`[propext, Classical.choice, Quot.sound]` and read DERIVES; `h2_sign_upto` is a definition, which the three-grade '
           'vocabulary does not grade, and it names no zero of ζ (the salt-check).' + NL + NL +
           '**The reading, descriptive voice.** The single located clause is a limit of bounded obligations. Each restriction '
           '`h2_sign_upto L₀` is a statement about windows of support at most L₀, finite in support; they are nested (a larger L₀ '
           'asks more); and only their conjunction over every L₀ is equivalent to Mathlib`s `RiemannHypothesis`. None of them '
           'alone is sufficient in the compiled record, and the upward direction runs through one fact: a `classK` window has '
           'compact support, so it lies under some bound. What a single bound would detect -- an explicit region of (γ, δ) -- '
           'is the part b559 held (`detection_region`, `j₀`), and it stays on the HELD branch.' + NL + NL +
           '*Nothing deposits; nothing at Zenodo written; no `sorry` on any `main`; nothing here is a statement about RH or any zero '
           'of ζ.*' + NL)
    out['findings'] = append_to(FIND, fnd)
    out['lines'] = dict(held=line_of(OT, HELD_LINE), rescope=line_of(OT, RESCOPE_H), arc=line_of(OT, ARC_LINE), findings=line_of(FIND, CLEAN_FH))
    put_json('b560_ledger1.json', out)
    print(json.dumps(out, indent=1, ensure_ascii=False))



def ledger1_lines():
    """### b560 defect (f): `ledger1`'s appends were written and its record was not (a NameError after the appends). The
    ### record is rebuilt from the files: each ledger's committed blob a byte prefix of its working bytes, and the lines."""
    out = {}
    for f in ('FINDINGS.md', 'OPEN_TRAILS.md'):
        before = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + f], capture_output=True).stdout
        now = open(os.path.join(PP, f), 'rb').read().replace(bytes([13, 10]), bytes([10]))
        out[f] = dict(before=len(before), added=len(now) - len(before), prefix=now.startswith(before))
    out['lines'] = dict(held=line_of(OT, HELD_LINE), rescope=line_of(OT, RESCOPE_H), arc=line_of(OT, ARC_LINE), findings=line_of(FIND, CLEAN_FH))
    out['rebuilt'] = 'defect (f): the appends were made by ledger1; this record is rebuilt by ledger1_lines'
    put_json('b560_ledger1.json', out)
    print(json.dumps(out, indent=1, ensure_ascii=False))


# ------------------------------------------------------------------------------ READING (5): the stages, banked as each lands
STAGES = {
    'A': dict(title='THE TERMS -- the conjugation stability of the genuine instance; liTerm, pairTerm; the pair real; the line nonnegative',
              names=['ne_one_of_mem', 'conj_mem', 'mult_conj', 'liTerm', 'pairTerm', 'liTerm_conj', 'pairTerm_eq', 'pairTerm_im',
                     'pairTerm_re', 'norm_sub_one_of_re_half', 'norm_one_sub_inv_of_re_half', 'liTerm_re_nonneg_of_re_half',
                     'pairTerm_re_nonneg_of_re_half']),
    'B': dict(title='THE DECAY -- the second-order remainder; the bound on the pair with its constant named; the summability over the genuine zeros',
              names=[]),
    'C': dict(title='THE COEFFICIENT AND THE FORWARD HALF -- LiCoeff over the genuine zeros; rh_imp_li_nonneg',
              names=[]),
    'D': dict(title='THE IDENTITY, PRICED AND PROBED -- the Bombieri-Lagarias test function; the truncation family; one truncation lemma; the limit exchange stated',
              names=[]),
}
GRADES = {}   # ### filled per stage: name -> (grade, why)


def stage():
    X = sys.argv[2]
    st = STAGES[X]
    names = st['names'] or [x for x in sys.argv[3].split(',')]
    rel = 'SIDEExplicitFormula/LiWeil.lean'
    src = rd(os.path.join(EF, rel)).replace(chr(13), '')
    att = sorted(f for f in os.listdir(SCR) if re.match(r'st%s_\d+\.txt$' % X, f))
    pr = rd(os.path.join(SCR, 'st%s_prints.txt' % X))
    P0 = parse_prints(pr)
    L = ['b560 -- READING (5): STAGE %s -- %s' % (X, st['title']), '']
    L.append('### the branch %s at the working tree of %s (from v0.3 = %s) ; the module %s' % (
        LIW, EF, g(EF, 'rev-parse', '--short', 'v0.3^{}').strip(), rel))
    L.append('')
    L.append('### THE ELABORATION ATTEMPTS OF THIS STAGE (lake env lean %s from the checkout), each with its exit and error count:' % rel)
    for f in att:
        t = rd(os.path.join(SCR, f)).split(NL)
        head = [x for x in t if x.startswith('### Stage %s attempt' % X)]
        L.append('    %s' % (head[0] if head else f))
        for x in t:
            if x.strip() and not x.startswith('### Stage'):
                L.append('        | ' + x[:230])
    L.append('')
    L.append('### THE DECLARATIONS OF THIS STAGE, AS THE SOURCE STATES THEM:')
    for n in names:
        k = decl_at(src, n)
        if k is None:
            L.append('    ### %s NOT IN THE MODULE' % n)
            continue
        for i, l in enumerate(statement(src, k, 10)):
            L.append('    %5d | %s' % (k + i, l))
    L.append('')
    L.append('### LEAN`S PRINTS (the module on stdin, then #print axioms for each and #check for the headline):')
    L += ['    ' + x for x in pr.split(NL) if x.strip()]
    L.append('')
    rows = {}
    for n in names:
        ax = P0.get(NSL + n)
        rows[n] = dict(axioms=ax, std3_or_fewer=ax is not None and set(ax) <= set(STD3), sorry=ax is not None and 'sorryAx' in ax)
    allok = all(r['std3_or_fewer'] for r in rows.values()) and len(rows) == len(names)
    L.append('### ### **PRINTED %d OF %d ; THE STANDARD THREE OR FEWER, NO sorryAx : %s**' % (
        sum(1 for r in rows.values() if r['axioms'] is not None), len(names), allok))
    put_txt('b560_stage%s.txt' % X, L)
    put_json('b560_stage%s.json' % X, dict(stage=X, names=names, rows=rows, all_std3=allok, attempts=len(att)))
    print(NL.join(L[-3:]))
    print('  written: b560_stage%s.txt (%d lines)' % (X, len(L)))



# ------------------------------------------------------------------------------ READING (6): the E0 read on the stages
DEF = 'A DEFINITION -- NO GRADE (the vocabulary grades terminals)'
LIW_GRADES = {
    'ne_one_of_mem': ('DERIVES', 'a member of the open strip is not 1'),
    'conj_mem': ('DERIVES', 'the conjugate of a nontrivial zero of `riemannZeta` is one, from `riemannZeta_conj` (ZetaReflect.lean:78) -- the instance`s conjugation stability, not a field of the type'),
    'mult_conj': ('DERIVES', 'its multiplicity agrees, from `analyticOrderAt_zeta_conj` (ZetaReflect.lean:160)'),
    'liTerm': (DEF, '`1 - (1 - ρ⁻¹) ^ n` over ℂ'),
    'pairTerm': (DEF, 'the term plus the term at the conjugate'),
    'liTerm_conj': ('DERIVES', 'the term at the conjugate is the conjugate of the term'),
    'pairTerm_eq': ('DERIVES', 'the pair is `2 Re (liTerm n ρ)`, real by construction'),
    'pairTerm_im': ('DERIVES', 'its imaginary part is zero'),
    'pairTerm_re': ('DERIVES', 'its real part is twice the term`s'),
    'norm_sub_one_of_re_half': ('DERIVES', 'on the line `‖ρ - 1‖ = ‖ρ‖`'),
    'norm_one_sub_inv_of_re_half': ('DERIVES', 'on the line `‖1 - ρ⁻¹‖ = 1`'),
    'liTerm_re_nonneg_of_re_half': ('DERIVES', 'on the line the real part of the term is nonnegative -- algebra over ℂ, no fact about zeta'),
    'pairTerm_re_nonneg_of_re_half': ('DERIVES', 'on the line the pair is nonnegative'),
    'rem_bound': ('DERIVES', 'the second-order remainder `‖(1 - w) ^ n - 1 + n w‖ ≤ n 2 ^ n ‖w‖ ^ 2` for `‖w‖ ≤ 1`, by induction'),
    'liTerm_re_abs_le': ('DERIVES', '`|Re liTerm n ρ| ≤ (n + n 2 ^ n) / ‖ρ‖ ^ 2` for `1 ≤ ‖ρ‖`, `0 ≤ Re ρ ≤ 1`'),
    'liConst': (DEF, 'the named constant `2 (n + n 2 ^ n)`'),
    'liConst_nonneg': ('DERIVES', 'the constant is nonnegative'),
    'pairTerm_norm_le': ('DERIVES', 'Stage B`s bound `‖pairTerm n ρ‖ ≤ liConst n / ‖ρ‖ ^ 2` -- exponent 2, constant named'),
    'pair_summable': ('DERIVES', 'absolute summability over the genuine zeros, from `zero_sum_inv_sq` (the log-form count)'),
    'LiCoeff': (DEF, '`(1/2) Σ_ρ m_ρ Re (pairTerm n ρ)` over `zetaZeroConfig` -- the genuine zeros, the salt-check below'),
    'LiCoeff_eq': ('DERIVES', 'the coefficient is `Σ_ρ m_ρ Re (1 - (1 - ρ⁻¹) ^ n)`, the Bombieri-Lagarias sum as the document writes it (BALPOS :70, :422)'),
    'liTerm_re_summable': ('DERIVES', 'the unpaired real-part sum converges absolutely'),
    'rh_imp_li_nonneg': ('DERIVES', 'Mathlib`s `RiemannHypothesis` implies `0 ≤ λ_n` for every `n`, over the genuine zeros -- the forward half'),
    'blPoly': (DEF, 'the Bombieri-Lagarias polynomial `Σ_{j=1}^n C(n,j) y^{j-1}/(j-1)!`'),
    'blSmooth': (DEF, '`e^{u/2} P_n(u)`'),
    'blTest': (DEF, 'the test function `1_{u<0} e^{u/2} P_n(u)` in the kernel`s variable'),
    'blTransform': (DEF + ' -- A Prop, STATED, NOT PROVED', 'T1: `paperFT (blTest n) (gammaOf ρ) = liTerm n ρ` for `Re ρ > 0`'),
    'truncMember': (DEF, 'the truncation family: a smooth bump times `e^{u/2} P_n(u)`'),
    'blPoly_contDiff': ('DERIVES', 'the polynomial is C²'),
    'blSmooth_contDiff': ('DERIVES', 'the profile is C²'),
    'truncMember_classEF': ('DERIVES', 'THE TRUNCATION LEMMA: every member is `ContDiff ℝ 2` with compact support -- EF_lit`s class'),
    'truncMember_eq': ('DERIVES', 'on a bump supported left of 0 the member is the bump times `k_n`'),
    'truncMember_EF': ('DERIVES', 'EF_lit at each member: the zero sum absolute and equal to the literature right-hand side'),
    'LiLimitExchange': (DEF + ' -- A Prop, STATED, NOT PROVED: THE HELD POINT', 'the zero side at the truncations tends to `LiCoeff n`'),
    'li_identity_of_exchange': ('INTERFACES', 'the literature right-hand sides tend to `LiCoeff n` GIVEN `LiLimitExchange n` -- the premise named at the site and discharged nowhere'),
}
HEADLINE = ['conj_mem', 'mult_conj', 'pairTerm_eq', 'liTerm_re_nonneg_of_re_half', 'pairTerm_norm_le', 'pair_summable',
            'LiCoeff_eq', 'rh_imp_li_nonneg', 'truncMember_classEF', 'truncMember_EF', 'li_identity_of_exchange']


def e0():
    rel = 'SIDEExplicitFormula/LiWeil.lean'
    src = rd(os.path.join(EF, rel)).replace(chr(13), '')
    pr = rd(os.path.join(SCR, 'stD_prints.txt'))
    P0 = parse_prints(pr)
    names = re.findall(r"^(?:theorem|def)\s+([A-Za-z_']+)", src, re.M)
    L = ['b560 -- READING (6): THE E0 READ ON THE STAGES -- EVERY DECLARATION OF LiWeil.lean GRADED, THE SALT-CHECK, THE ROWGEN RECORD', '']
    L.append('### declarations in the module: %d ; graded here: %d ; printed by Lean: %d' % (
        len(names), len([n for n in names if n in LIW_GRADES]), len([n for n in names if (NSL + n) in P0])))
    rows = {}
    for n in names:
        gr, why = LIW_GRADES.get(n, ('### UNGRADED', ''))
        ax = P0.get(NSL + n)
        rows[n] = dict(grade=gr, why=why, axioms=ax, std3_or_fewer=ax is not None and set(ax) <= set(STD3))
        L.append('    %-30s %-12s %s -- %s' % (n, gr.split(' --')[0][:12] if gr != DEF else 'DEFINITION', ax, why[:150]))
    counts = {}
    for r in rows.values():
        k = 'DEFINITION' if r['grade'].startswith('A DEFINITION') else r['grade']
        counts[k] = counts.get(k, 0) + 1
    L.append('### the grades counted: %s' % counts)
    L.append('')
    L.append('### THE SALT-CHECK (EXCLUSION_ENGINE.md :28-:34; FINDINGS :57): no Prop of the module encodes a conclusion it is')
    L.append('### cited for, and the coefficient is over the GENUINE configuration. Lean`s #print of LiCoeff and of what it names:')
    blk = pr[pr.index('def SIDEExplicitFormula.LiWeil.LiCoeff'):] if 'def SIDEExplicitFormula.LiWeil.LiCoeff' in pr else ''
    L += ['    ' + x for x in blk.split(NL)[:6]]
    stc = rd(os.path.join(SCR, 'stC_prints.txt'))
    for key in ('def Zeta23.zetaZeroConfig', 'def Zeta23.zetaZeros', 'def Zeta23.IsNontrivialZero', 'def Zeta23.zeroMult'):
        if key in stc:
            L += ['    ' + x for x in stc[stc.index(key):].split(NL)[:4] if x.strip()][:4]
    over_genuine = 'Zeta23.zetaZeroConfig.carrier' in blk and 'zetaZeros zetaSeam' in stc.replace('Zeta23.', '')
    param = re.search(r'def LiCoeff\s*\(Z\s*:\s*ZeroConfig\)', src) is not None or re.search(r'def LiCoeff\s*\{?Z', src) is not None
    L.append('    ### LiCoeff is over zetaZeroConfig (zetaZeros zetaSeam: carrier IsNontrivialZero of riemannZeta, mult the analytic')
    L.append('    ### order of riemannZeta): %s ; LiCoeff takes a configuration parameter: %s' % (over_genuine, param))
    ctl = re.search(r'def LiCoeff\s*\(Z\s*:\s*ZeroConfig\)', 'def LiCoeff (Z : ZeroConfig) (n : ℕ) : ℝ := 0') is not None
    L.append('    ### control: the parameter test on `def LiCoeff (Z : ZeroConfig) (n : ℕ) : ℝ := 0` -> %s (must be True)' % ctl)
    rhc = check_line(pr, NSL + 'rh_imp_li_nonneg')
    L.append('    rh_imp_li_nonneg as Lean prints it: %s' % rhc)
    L.append('    ### its conclusion unfolds to Mathlib objects over the genuine zeros: `RiemannHypothesis` (Mathlib), `LiCoeff n` a `tsum`')
    L.append('    ### over `{ρ | riemannZeta ρ = 0 ∧ 0 < ρ.re ∧ ρ.re < 1}` weighted by `(analyticOrderAt riemannZeta ρ).toNat` of')
    L.append('    ### `Re (1 - (1 - ρ⁻¹) ^ n)`: ### **THE SALT-CHECK PASSES: %s**' % (over_genuine and not param))
    recs, ctl2 = rowgen_record([NSL + n for n in HEADLINE], rel, g(EF, 'rev-parse', 'HEAD').strip(), pr)
    L.append('')
    L.append('### THE ROWGEN RECORD (rowgen.py`s extract_doc_body and definition_encoded IMPORTED, at the branch tip %s):'
             % g(EF, 'rev-parse', '--short', 'HEAD').strip())
    for r in recs:
        L.append('    %-30s defenc %-5s %s | doc: %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_why'], r['doc'][:100]))
    L.append('    control: definition_encoded on `def b560_ctl_stub : Prop := True` -> %s (must be True)' % (ctl2,))
    L.append('    ### rowgen`s lean_check_axioms NOT RUN (its `import <module>` needs an olean this act does not build); the check and')
    L.append('    ### axioms lines are the stdin prints of the same declarations.')
    theorems_ok = all(r['std3_or_fewer'] for r in rows.values())
    no_encodes = not any(r['grade'].startswith('ENCODES') for r in rows.values())
    gate = theorems_ok and no_encodes and over_genuine and not param and all(n in LIW_GRADES for n in names) and ctl and ctl2[0]
    L.append('')
    L.append('### ### **THE GATE (R170)(6): EVERY PRINT THE STANDARD THREE OR FEWER %s ; NO ENCODES %s ; THE SALT-CHECK %s ; => MERGE %s**'
             % (theorems_ok, no_encodes, over_genuine and not param, gate))
    L.append('### ### `li_identity_of_exchange` is INTERFACES: it lands on main as a conditional whose premise, `LiLimitExchange n`, is')
    L.append('### ### named and discharged nowhere; `blTransform` and `LiLimitExchange` land as Prop definitions, stated and not proved.')
    put_txt('b560_e0.txt', L)
    put_json('b560_e0.json', dict(rows=rows, counts=counts, salt=over_genuine and not param, param=param, control=ctl,
                                  gate=gate, rowgen=recs, rowgen_control=ctl2[0], names=names))
    print(NL.join(L[-6:]))


STAGE_D_PRICE = [
    '',
    '### ### **STAGE D -- WHERE IT STOPS, BY LINE, AND WHAT REMAINS, PRICED IN LEMMAS** (the truncation route, OPEN_TRAILS :11294-:11302)',
    '    REACHED: the statement of the family and ONE truncation lemma -- `truncMember_classEF` (every member `ContDiff ℝ 2` with',
    '    compact support, EF_lit`s class), EF_lit applied to it (`truncMember_EF`), and the identity conditional on the exchange',
    '    (`li_identity_of_exchange`, INTERFACES). T2 (the smoothing of the jump at 0) is absorbed: the bump supported left of 0',
    '    multiplies the everywhere-smooth `e^{u/2} P_n(u)`, so the member is smooth whatever `k_n` does at 0 (`truncMember_eq`).',
    '    ### **THE OBSTACLE (LiWeil.lean, `LiLimitExchange`): THE LIMIT EXCHANGE, AND THE PAIRING HAZARD IS EXACTLY THERE.** At each',
    '    member the zero sum is absolutely convergent (EF_lit, ExplicitFormula.lean:98-99), with a dominant `C/(1 + ‖γ_ρ‖²)` whose',
    '    constant C grows with the second derivative of the member (ZeroSummability.lean:192-195: `C = 2 e^{Λ/2} ∫‖k``‖`); along a',
    '    family tending to `1_{u<0}` the bumps steepen at 0 and C is unbounded, so no dominant uniform in the family comes from',
    '    EF_lit`s own bound. The target `LiCoeff n` is a sum of real parts (the paired sum): the unpaired Li terms decay only like',
    '    `n/ρ` (`liTerm_re_abs_le` bounds the REAL part at `‖ρ‖⁻²`; the imaginary part is first order). The exchange needs the',
    '    grouped (conjugate-paired) transforms dominated uniformly in the family.',
    '    PRICED, NOT FORCED:',
    '      (D1) `blTransform` -- the transform of `k_n` is the Li term (T1): the Mellin integral of `x^{ρ-1} (log x)^{j-1}` on (0,1),',
    '           an improper integral per power -- one lemma of moderate weight.',
    '      (D2) the transform at a member converges to the transform of `k_n` at each fixed ρ (dominated convergence in u,',
    '           `|k_n(u) e^{(ρ-1/2)u}| ≤ e^{Re ρ u}|P_n(u)|` on u < 0) -- one lemma, moderate.',
    '      (D3) THE LEMMA OF SUBSTANCE: a dominant for the PAIRED truncated transforms, uniform in the family and summable over',
    '           the zeros -- an integration by parts that keeps the jump`s boundary term (`n/ρ`, first order, cancelling in',
    '           the real part) separate from a remainder `O(‖ρ‖⁻²)` uniform in the bump -- T6.',
    '      (D4) Tannery over the zeros through (D3)`s dominant (the pattern of `rest_tendsto_zero`, PowerLimit.lean:1025) -- T7.',
    '      (D5) the prime side`s limit (a finite sum for compact support; the Λ(n) n^{-1/2} (k(log n) + k(-log n)) terms converge',
    '           termwise and the family`s support grows -- the tail needs k_n`s decay e^{u/2}|u|^{n-1}) and the Γ-integral`s limit',
    '           -- T8, two lemmas.',
    '      (D6) λ_n identified with the Bombieri-Lagarias arithmetic formula in the kernel`s objects -- T9, a statement once',
    '           (D1)-(D5) are in; not re-read at source (BL 1999 is not in the relay`s banks).',
    '    ### the exchange is (D2)+(D3)+(D4); (D3) is where the pairing hazard lives and is the next act`s item if the bridge',
    '    ### continues ((R170)(7)).',
    '',
    '### ### **THE CONVERSE, PRICED AND NOT ATTEMPTED** (λ_n ≥ 0 for all n → RH; Bombieri-Lagarias Theorem 1, Voros`s growth):',
    '      (V1) at an off-line zero ρ₀ (Re ρ₀ ≠ 1/2) one of ρ₀, 1 - conj ρ₀ has `‖1 - 1/ρ‖ > 1`, so its term grows like',
    '           `‖1 - 1/ρ₀‖^n`: a lemma over ℂ, the reverse of `norm_one_sub_inv_of_re_half` -- light.',
    '      (V2) the phase: the real part of `-(1 - 1/ρ₀)^n` is negative and of size `‖1 - 1/ρ₀‖^n` for infinitely many n',
    '           (an argument on `n·arg(1 - 1/ρ₀)` mod 2π, Dirichlet approximation) -- moderate.',
    '      (V3) the rest of the sum bounded by a quantity of smaller exponential order: the zeros with `‖1 - 1/ρ‖` below the',
    '           largest, uniformly in n -- it needs the maximum of `‖1 - 1/ρ‖` over the zeros to be attained and the others',
    '           separated from it, a configuration estimate of the kind b559 met at the detection region -- substance.',
    '      (V4) assembled: some λ_n < 0; contraposition gives RH. BL 1999 does this for an arbitrary multiset satisfying their',
    '           growth condition; the kernel`s count bound supplies the multiset`s summability (`pair_summable`).',
]


def stageD_price():
    p = os.path.join(D, 'b560_stageD.txt')
    t = rd(p)
    if 'WHERE IT STOPS, BY LINE' in t:
        sys.exit('### ALREADY PRESENT in b560_stageD.txt')
    open(p, 'ab').write((NL.join(STAGE_D_PRICE) + NL).encode('utf-8'))
    print('  appended the obstacle, the prices and the converse`s price to b560_stageD.txt')



# ------------------------------------------------------------------------------ the kernel state, the scores, the desk
PRE_HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': '3268b94',
             'SIDE-effects': 'ef4cff7', 'SIDE-silence-principle': '667c254', 'SIDE-compression': 'e9a5a36', 'SIDE-structural-error-correction': '6a4f482',
             'SIDE-cosmo': 'c5cba30'}
NEW_FILES = ['AxiomCheckDetection.lean', 'AxiomCheckLiWeil.lean', 'SIDEExplicitFormula/DetectionRegion.lean', 'SIDEExplicitFormula/LiWeil.lean']


def w_(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def mains():
    return {k: sorted(x for x in g(os.path.join(DD, k), 'diff', '--name-only', h, 'main').split(NL) if x.strip()) for k, h in PRE_HEADS.items()}


def kstate():
    ls = {}
    for l in g(EF, 'ls-remote', 'origin').split(NL):
        if '\t' in l:
            h, r = l.split('\t')
            ls[r.strip()] = h.strip()
    return dict(main=g(EF, 'rev-parse', 'main').strip(), remote=ls,
                v03=g(EF, 'rev-parse', 'v0.3^{}').strip(), v04=g(EF, 'rev-parse', 'v0.4^{}').strip(),
                v03obj=g(EF, 'rev-parse', 'v0.3').strip(), v04obj=g(EF, 'rev-parse', 'v0.4').strip(),
                liw=g(EF, 'rev-parse', LIW).strip(), held=g(EF, 'rev-parse', HELD).strip(),
                status=sorted(set(x.split('\t')[0] for x in g(EF, 'diff', '--name-status', MAIN0, 'main').split(NL) if x.strip())),
                files=sorted(x.split('\t')[1] for x in g(EF, 'diff', '--name-status', MAIN0, 'main').split(NL) if x.strip()),
                ff=subprocess.run(['git', '-C', EF, 'merge-base', '--is-ancestor', MAIN0, 'main']).returncode == 0,
                clean_branch=g(EF, 'branch', '--list', CLEAN).strip())


def scores():
    rj, cj, ej = jl('b560_reads.json'), jl('b560_clean.json'), jl('b560_e0.json')
    sa, sb, sc, sd = (jl('b560_stage%s.json' % x) for x in 'ABCD')
    k = kstate()
    rr = rd(os.path.join(D, 'b560_b559_postpush_rerun.txt'))
    # ### the arm's own ROW (`  G-X   PASS  PASS  FAIL  OK`), not the header line that names it (b560, the needle's yield printed)
    def arm(a):
        m = re.search(r'^\s+' + re.escape(a) + r'\s+(PASS|FAIL)\s', rr, re.M)
        return bool(m) and m.group(1) == 'PASS'
    src = rd(os.path.join(EF, 'SIDEExplicitFormula', 'LiWeil.lean'))
    body = lambda n: statement_block(src, decl_at(src, n))
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b560_') and needle in rd(os.path.join(T, x))]
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    trial = dict(head=g(P.TRIAL, 'rev-parse', 'HEAD').strip(), status=g(P.TRIAL, 'status', '--porcelain', '--untracked-files=no').strip())
    mm = {k2: [f for f in v if f.endswith('.lean')] for k2, v in mains().items()}
    mm_other = {k2: v for k2, v in mm.items() if k2 != 'SIDE-explicit-formula'}
    held_ok = k['held'] == HELD_TIP and k['remote'].get('refs/heads/' + HELD) == HELD_TIP
    v03_ok = k['v03'] == cj.get('tip') and k['remote'].get('refs/tags/v0.3^{}') == k['v03']
    v04_ok = k['v04'] == k['main'] == k['liw'] and k['remote'].get('refs/tags/v0.4^{}') == k['v04'] == k['remote'].get('refs/heads/main')
    rows = ej.get('rows', {})
    h11d = (rows.get('rh_imp_li_nonneg', {}).get('std3_or_fewer') and ej.get('salt') is True)
    s = dict(
        h11a_first=False,
        h11a=(rj.get('h11a_amended') == 'HOLDS FROM THE PRINTS' and rows.get('conj_mem', {}).get('std3_or_fewer') and rows.get('mult_conj', {}).get('std3_or_fewer')),
        h11b=bool(sa.get('all_std3')) and rows.get('liTerm_re_nonneg_of_re_half', {}).get('std3_or_fewer', False),
        h11c=bool(sb.get('all_std3')) and 'liConst' in body('pairTerm_norm_le') and 'zero_sum_inv_sq' in body('pair_summable'),
        h11d=bool(h11d),
        h11e=bool(sd.get('all_std3')) and rows.get('truncMember_classEF', {}).get('grade') == 'DERIVES'
             and rows.get('LiLimitExchange', {}).get('grade', '').endswith('THE HELD POINT'),
        n1=(v03_ok and cj.get('gate') is True),
        n2=False,
        n3=(all(jl('b560_stage%s.json' % x).get('all_std3') for x in 'ABC') and bool(h11d)),
        n4=(bool(sd.get('all_std3')) and 'PAIRING HAZARD' in rd(os.path.join(D, 'b560_stageD.txt'))),
        n5=(arm('G-PEEK-DECLARED') and arm('G-WRITELIST-KINDS') and arm('G-PRIORBANK-UNCHANGED')),
        n6=(k['status'] == ['A'] and k['files'] == NEW_FILES and k['ff'] and all(v == [] for v in mm_other.values()) and zen == [] and dep
            and trial['head'].startswith('f22ff35') and trial['status'] == '' and held_ok),
        s1=('riemannZeta_conj' in body('conj_mem') and 'analyticOrderAt_zeta_conj' in body('mult_conj')
            and not re.search(r'riemannZeta_one_sub|zeta_reflect|zeta_mult_reflect|riemannZeta_ne_zero', body('conj_mem') + body('mult_conj') + body('ne_one_of_mem'))),
        s2=('zero_sum_inv_sq' in body('pair_summable') and 'weighted_summable' not in src),
        s3=(not arm('G-WRITELIST-KINDS') and "['terminal_table.json']" in (line_with(rr, 'NO (W) GLOB COVERS') or '')),
        _detail=dict(kernel=k, mains=mm, zen=zen, dep=dep, trial=trial, held_ok=held_ok, v03_ok=v03_ok, v04_ok=v04_ok,
                     rerun={a: arm(a) for a in ARMS_FILETIME}))
    return s


def line_with(text, needle):
    for l in (text or '').split(NL):
        if needle in l:
            return l
    return None


def desk():
    s = scores()
    d0 = s['_detail']
    k = d0['kernel']
    ej = jl('b560_e0.json')
    lines = ['=' * 104, 'b560 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
             '### (R170)(5)`S FIVE, H11a AS THE AMENDMENT RE-SCORES IT.', '-' * 104,
             '  **(H11a)** AS FIRST WORDED (reflection sufficient for pairing): ### **REFUTED** -- `ZeroConfig` carries `reflect ρ = 1 - conj ρ`'
             ' alone (Defs.lean:124, :143-:144), which fixes the line (data/b560_reads.txt).',
             '  **(H11a)** AS AMENDED (conjugation): ### **%s.** -- from the prints (%s) and compiled: conj_mem %s, mult_conj %s.'
             % (w_(s['h11a']), jl('b560_reads.json').get('h11a_amended'), ej['rows']['conj_mem']['axioms'], ej['rows']['mult_conj']['axioms']),
             '  **(H11b)** ### **%s.** -- liTerm_re_nonneg_of_re_half, pairTerm_re_nonneg_of_re_half at the standard three (data/b560_stageA.txt).' % w_(s['h11b']),
             '  **(H11c)** ### **%s.** -- pairTerm_norm_le with liConst n = 2 (n + n 2^n), exponent 2; pair_summable from zero_sum_inv_sq, the kernel`s'
             ' count bound in its log form (data/b560_stageB.txt).' % w_(s['h11c']),
             '  **(H11d)** ### **%s.** -- rh_imp_li_nonneg %s; LiCoeff over zetaZeroConfig, the salt-check %s (data/b560_e0.txt).'
             % (w_(s['h11d']), ej['rows']['rh_imp_li_nonneg']['axioms'], ej.get('salt')),
             '  **(H11e)** ### **%s.** -- the statement (blTest, blTransform, truncMember) and one truncation lemma (truncMember_classEF) reached;'
             ' HELD at the limit exchange (LiLimitExchange stated, not proved), as the navigator expected -- no clean landing refutes it.' % w_(s['h11e']), '',
             '### THE NAVIGATOR`S SIX.', '-' * 104,
             '  **(N1)** ### **%s.** -- v0.3 local %s, remote peeled %s ; the gate %s. THE GRADE CLAUSE, READ BY ITS WORDS: of the three named,'
             ' h2_sign_iff_forall_upto and forall_upto_iff_rh grade DERIVES; h2_sign_upto is a definition, which the vocabulary does not grade.'
             % (w_(s['n1']), k['v03'][:7], k['remote'].get('refs/tags/v0.3^{}', '')[:7], jl('b560_clean.json').get('gate')),
             '  **(N2)** ### **REFUTED.** -- the configuration exposes reflection only, and reflection is not sufficient for pairing on the line;'
             ' the pairing is by conjugation, from the genuine instance`s facts (the amendment).',
             '  **(N3)** ### **%s.** -- Stages A-C all at the standard three, no sorryAx; the salt-check %s.' % (w_(s['n3']), ej.get('salt')),
             '  **(N4)** ### **%s.** -- Stage D reached its statement and one truncation lemma and is HELD at the limit exchange; the obstacle'
             ' line names the pairing hazard (data/b560_stageD.txt).' % w_(s['n4']),
             '  **(N5)** ### **%s.** -- the re-run on b559`s push (data/b560_b559_postpush_rerun.txt): %s. G-WRITELIST-KINDS fails on'
             ' terminal_table.json by content, which b559`s face does not name (b559`s defect (h)); the other two pass on digests.'
             % (w_(s['n5']), d0['rerun']),
             '  **(N6)** ### **%s.** -- SIDE-explicit-formula main against 81ae175: %s %s, a fast-forward %s ; .lean files changed on the other'
             ' mains %s ; the HELD branch at 8faf7de local and remote %s ; tools naming the platform %s ; deposit clean %s ; trial %s.'
             % (w_(s['n6']), k['status'], k['files'], k['ff'], [x for x, v in d0['mains'].items() if v and x != 'SIDE-explicit-formula'] or 'NONE',
                d0['held_ok'], d0['zen'] or 'NONE', d0['dep'], d0['trial']), '',
             '### THE SEAT`S THREE.', '-' * 104,
             '  **(S1)** ### **%s.** -- conj_mem cites riemannZeta_conj, mult_conj cites analyticOrderAt_zeta_conj, and no other fact about zeta'
             ' appears in either or in ne_one_of_mem.' % w_(s['s1']),
             '  **(S2)** ### **%s.** -- pair_summable draws on zero_sum_inv_sq; weighted_summable does not appear in the module.' % w_(s['s2']),
             '  **(S3)** ### **%s.** -- the re-run: %s.' % (w_(s['s3']), line_with(rd(os.path.join(D, 'b560_b559_postpush_rerun.txt')), 'NO (W) GLOB COVERS')), '',
             '### THE TAGS.', '-' * 104,
             '  v0.3 object %s peeled %s (remote %s) ; v0.4 object %s peeled %s (remote %s) ; main %s (remote %s) ; li-weil-b560 %s (remote %s)'
             % (k['v03obj'][:7], k['v03'][:7], k['remote'].get('refs/tags/v0.3^{}', '')[:7], k['v04obj'][:7], k['v04'][:7],
                k['remote'].get('refs/tags/v0.4^{}', '')[:7], k['main'][:7], k['remote'].get('refs/heads/main', '')[:7], k['liw'][:7],
                k['remote'].get('refs/heads/' + LIW, '')[:7]), '']
    nav = [s[x] for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')]
    seat = [s[x] for x in ('s1', 's2', 's3')]
    lines.append('### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
                 % (nav.count(True), nav.count(False), nav.count(None), seat.count(True), seat.count(False)))
    lines.append('### ### **(R170)(5) : H11a %s (as amended; REFUTED as first worded) ; H11b %s ; H11c %s ; H11d %s ; H11e %s.**'
                 % tuple(w_(s[x]) for x in ('h11a', 'h11b', 'h11c', 'h11d', 'h11e')))
    d = rd(os.path.join(D, 'b560_defects.txt')) if os.path.exists(os.path.join(D, 'b560_defects.txt')) else ''
    if d:
        lines += ['', '### THIS ACT`S OWN DEFECTS.'] + d.rstrip().split(NL)
    put_txt('b560_desk_notes.txt', lines)
    put_json('b560_scores.json', {k2: v for k2, v in s.items() if not k2.startswith('_')})
    print(NL.join(lines[:40]))


# ------------------------------------------------------------------------------ READING (7): the entry, the row, the trail
FH = ('## The Li–Weil bridge, staged: the paired Li terms over the compiled zero configuration, the forward half under RH, the identity '
      'probed at the truncation lemma -- held at the limit exchange')
ROWNO = '395'
WO_LINE = ('*Appended 2026-09-29 by b560, under the author’s ruling `(R170)`(4), to the LI-WEIL-BRIDGE entry (:3548; the truncation route '
           'at :11290) -- THE WORK-ORDER’S LINE UPDATED:*')
HEADING = ('### b560 — lane two, act two under (R170): the Li–Weil bridge staged over the genuine zero configuration and held at the '
           'limit exchange; b559’s clean part merged as v0.3; the detection region re-scoped; the suite’s file-time arms moved to digests')


def findings():
    guard_absent(FIND, FH)
    s = jl('b560_scores.json')
    k = kstate()
    t = ['', FH, '',
         '*Filed at b560 on the author’s ruling `(R170)` and its (4) amendment. Lane two, act two. Banks: relay `data/b560_reads.txt`, '
         '`data/b560_stageA.txt` … `data/b560_stageD.txt`, `data/b560_e0.txt`, `data/b560_v04_push.txt`; SIDE-explicit-formula v0.4 = '
         '`%s` (`SIDEExplicitFormula/LiWeil.lean`), the branch `li-weil-b560` pushed by name. Nothing about ζ’s zeros is claimed beyond '
         'the compiled statements’ own words.*' % k['v04'][:7], '',
         '**The pairing, and the hypothesis it refuted.** The configuration type `ZeroConfig` (Zeta23/Defs.lean:136) carries one '
         'symmetry, `reflect ρ = 1 − conj ρ` (:124), and it fixes every point of the critical line; a term paired by it degenerates '
         'there. H11a as first worded (the configuration’s reflection sufficient for pairing) is REFUTED on the type. Under the author’s '
         'amendment the pairing is by conjugation, and the conjugation stability is a fact about the genuine instance, not a field of the '
         'type: `conj_mem` and `mult_conj` derive it from `riemannZeta_conj` and `analyticOrderAt_zeta_conj` (ZetaReflect.lean:78, :160), '
         'and no Zeta23 file is edited.', '',
         '**What is compiled, 35 of 35 at the standard three.** Stage A: `liTerm n ρ = 1 − (1 − ρ⁻¹)ⁿ`; `pairTerm n ρ = liTerm n ρ + '
         'liTerm n (conj ρ) = 2 Re (liTerm n ρ)`; on Re ρ = 1/2, ‖1 − ρ⁻¹‖ = 1 and Re (liTerm n ρ) ≥ 0 -- algebra over ℂ (the same '
         'per-term fact stands in SIDE-lv-conservation as `blTerm_nonneg_of_onLine`, on another toolchain). Stage B: the second-order '
         'remainder ‖(1 − w)ⁿ − 1 + nw‖ ≤ n·2ⁿ‖w‖² for ‖w‖ ≤ 1; `pairTerm_norm_le`, ‖pairTerm n ρ‖ ≤ liConst n / ‖ρ‖² with liConst n = '
         '2(n + n·2ⁿ), for ‖ρ‖ ≥ 1 in the closed strip -- the pair decays at exponent 2 because the first-order part n/ρ enters only '
         'through its real part; `pair_summable` over the genuine zeros from `zero_sum_inv_sq` (the kernel’s local count in its log form; '
         'the fourth-power grouping `weighted_summable` is not met by this decay). Stage C: `LiCoeff n` = ½ Σ_ρ m_ρ Re (pairTerm n ρ) = '
         'Σ_ρ m_ρ Re (1 − (1 − ρ⁻¹)ⁿ) over `zetaZeroConfig`, absolutely convergent; **`rh_imp_li_nonneg : RiemannHypothesis → ∀ n, 0 ≤ '
         'LiCoeff n`**, its conclusion unfolding to Mathlib’s `riemannZeta` and `analyticOrderAt` over the nontrivial zeros (the '
         'salt-check passes). Stage D: the Bombieri–Lagarias test function in the kernel’s variable, k_n(u) = 1_{u<0} e^{u/2} P_n(u); '
         'its transform identity `blTransform` stated as a Prop; the truncation family (a smooth bump supported left of 0 times e^{u/2} '
         'P_n(u)); the one truncation lemma `truncMember_classEF` (every member C² with compact support, EF_lit’s class) and EF_lit at '
         'each member (`truncMember_EF`); the identity conditional on the exchange, `li_identity_of_exchange`, graded INTERFACES.', '',
         '**Where it stops.** The limit exchange -- the zero side of EF_lit at the truncations tending to `LiCoeff n` -- is stated '
         '(`LiLimitExchange`) and not proved. The pairing hazard is there: at each member the zero sum is absolute, with a dominant whose '
         'constant grows with the member’s second derivative near 0, while the target is a paired sum whose unpaired terms decay only like '
         'n/ρ. The lemma of substance is a dominant for the conjugate-paired truncated transforms uniform along the family (relay '
         '`data/b560_stageD.txt`, (D3)); the rest -- the transform identity, the pointwise limit, Tannery, the prime and Γ sides -- is '
         'priced beside it at (D1), (D2), (D4)-(D6). The converse (λ_n ≥ 0 → RH) is not attempted; its price is (V1)-(V4) in the same '
         'bank, (V3) a configuration estimate of the kind met at the detection region.', '',
         '**The reading, descriptive voice.** The forward half of Li’s criterion now stands over the compiled zero configuration: the '
         'coefficient is defined over the zeros of Mathlib’s ζ, it converges absolutely by the kernel’s own count, and RH gives its sign '
         'term by term. That half is the classical easy direction and says nothing about the sign without RH. The Weil side meets it at '
         'EF_lit, compactly supported and absolutely summed; the Li side needs a one-sided test function with a jump, summed in pairs. '
         'Between them sits one exchange of limits, stated in the kernel’s objects.', '',
         '**The scores.** H11a REFUTED as first worded, %s as amended; H11b %s; H11c %s; H11d %s; H11e %s. (N1) %s, (N2) %s, (N3) %s, '
         '(N4) %s, (N5) %s, (N6) %s.' % tuple(w_(s.get(x)) for x in ('h11a', 'h11b', 'h11c', 'h11d', 'h11e', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6')), '',
         '**Next** (`(R170)`(7)): the bridge continued at (D1)-(D4) -- the exchange is priced and the next act can take its lemma of '
         'substance -- if the author so rules; otherwise W-ORD-GRH-WEIL.', '',
         '*Nothing deposits; nothing at Zenodo written; no `sorry` on any `main`; nothing here is a statement about RH or any zero of ζ '
         'beyond the compiled statements’ own words.*', '']
    o = append_to(FIND, NL.join(t))
    o['heading_line'] = line_of(FIND, FH)
    put_json('b560_findings.json', o)
    print('  FINDINGS.md:%(heading_line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


ROW_NAMES = ['conj_mem', 'mult_conj', 'pairTerm_eq', 'liTerm_re_nonneg_of_re_half', 'pairTerm_norm_le', 'pair_summable',
             'LiCoeff_eq', 'rh_imp_li_nonneg', 'truncMember_classEF', 'truncMember_EF', 'li_identity_of_exchange']


def row():
    k = kstate()
    ej = jl('b560_e0.json')
    n_std = sum(1 for r in ej['rows'].values() if r['std3_or_fewer'])
    cells = [ROWNO,
             '**THE LI–WEIL BRIDGE, STAGED, AND THE DETECTION REGION’S CLEAN PART** (b560, under (R170) and its (4) amendment). '
             'SIDE-explicit-formula v0.3 = %s (b538’s RegisterDepth and b559’s DetectionRegion-clean: h2_sign ↔ ∀ L₀, h2_sign_upto L₀ ↔ '
             'RiemannHypothesis) and v0.4 = %s (LiWeil.lean): the genuine zero configuration conjugation-stable with multiplicity; the '
             'Bombieri–Lagarias terms paired by conjugation, real, nonnegative on the line; their decay liConst n / ‖ρ‖² and absolute '
             'summability over the zeros of ζ; LiCoeff over the genuine zeros and RiemannHypothesis → ∀ n, 0 ≤ LiCoeff n; the '
             'truncation lemma for EF_lit’s class. The limit exchange is stated as a Prop and not proved. Nothing here proves RH.'
             % (k['v03'][:7], k['v04'][:7]),
             '`SIDE-explicit-formula/SIDEExplicitFormula/LiWeil.lean` (v0.4) : ' + ', '.join('`%s%s`' % (NSL, n) for n in ROW_NAMES)
             + ' ; `SIDE-explicit-formula/SIDEExplicitFormula/DetectionRegion.lean` (v0.3) : `%sh2_sign_iff_forall_upto`, `%sforall_upto_iff_rh`' % (NS, NS),
             '%d of %d LiWeil declarations and 5 of 5 DetectionRegion declarations: [propext, Classical.choice, Quot.sound], no sorryAx '
             '(relay data/b560_e0.txt, data/b560_clean.txt)' % (n_std, len(ej['rows'])),
             ' ; '.join('`%s` %s' % (n, ej['rows'][n]['grade']) for n in ROW_NAMES) + ' ; `h2_sign_iff_forall_upto` DERIVES ; `forall_upto_iff_rh` DERIVES',
             'LANDED on main by fast-forward, tagged v0.3 and v0.4; HELD at the limit exchange (LiLimitExchange stated, not proved; '
             'li_identity_of_exchange INTERFACES on it); detection-region-b559 kept HELD; h2 where the deposit left it; nothing deposits; '
             'nothing at Zenodo written.']
    r = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + cells, capture_output=True, text=True, encoding='utf-8')
    print(r.stdout[-700:], r.stderr[-400:])
    put_json('b560_rows.json', dict(cells=cells, exit=r.returncode))


def rowgen_diff():
    """### READING (6): rowgen's own `diff`, IMPORTED, over the merged records against the row as it now stands."""
    sys.path.insert(0, os.path.join(T, 'rowgen'))
    import rowgen as RG
    recs = jl('b560_e0.json').get('rowgen', []) + jl('b560_clean.json').get('rowgen', [])
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = "'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or [])) if isinstance(r.get('axioms'), list) else (r.get('axioms') or '')
        r['pin'] = r.get('pin') or ''
    corr = rd(CORR)
    rowtxt = [l for l in corr.split(NL) if l.startswith('| %s |' % ROWNO)]
    out = RG.diff(recs, NL.join(rowtxt))
    L = ['b560 -- READING (6): THE ROWGEN DIFF (rowgen.diff IMPORTED) OF THE MERGED RECORDS AGAINST CORRESPONDENCE ROW %s' % ROWNO, '',
         '### records: %d ; row found: %s' % (len(recs), bool(rowtxt))]
    L += ['    ' + str(x) for x in (out if isinstance(out, list) else [out])]
    put_txt('b560_rowgen.txt', L)
    print(NL.join(L))


def workorder():
    guard_absent(OT, WO_LINE)
    k = kstate()
    t = (NL + WO_LINE + ' of the truncation route T1-T9 (:11294-:11302), at SIDE-explicit-formula v0.4 = `%s` (`LiWeil.lean`): **T3, T4, T5 '
         'COMPILED** (the bump family; `truncMember_classEF`, every member in EF_lit’s class; `truncMember_EF`, EF_lit at each member); '
         '**T2 ABSORBED** (the bump supported left of 0 multiplies the everywhere-smooth e^{u/2} P_n(u)); **T1 STATED** (`blTransform`, a '
         'Prop); **T6-T9 OPEN**, priced at relay `data/b560_stageD.txt` (D1)-(D6), the lemma of substance (D3) a dominant for the '
         'conjugate-paired truncated transforms uniform along the family -- the paired-sum hazard :11424 names, now at `LiLimitExchange`. '
         'Beside the route: the Li coefficient over the genuine zeros compiled (`LiCoeff`, absolutely convergent, `pair_summable`) and '
         'its forward half (`rh_imp_li_nonneg`). The converse is priced at (V1)-(V4) and not attempted.' % k['v04'][:7] + NL)
    o = append_to(OT, t)
    o['line'] = line_of(OT, WO_LINE)
    put_json('b560_workorder.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes, prefix %(prefix)s)' % o)


def components():
    L = ['=' * 132, 'b560 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b560_reads.txt', 'b560_b559_postpush_rerun.txt', 'b560_clean_elab.txt', 'b560_clean.txt', 'b560_v03.txt',
              'b560_stageA.txt', 'b560_stageB.txt', 'b560_stageC.txt', 'b560_stageD.txt', 'b560_e0.txt', 'b560_v04_push.txt', 'b560_rowgen.txt'):
        L.append('### relay data/%s' % n)
        L.extend('  ' + x for x in rd(os.path.join(D, n)).rstrip().split(NL))
        L.append('')
    for n, key in (('b560_ledger1.json', 'lines'), ('b560_findings.json', 'heading_line'), ('b560_rows.json', 'exit'), ('b560_workorder.json', 'line')):
        L.append('### relay data/%s -- %s %s' % (n, key, jl(n).get(key)))
    L.append('### the suite change: relay %s' % g(ROOT, 'log', '-1', '--format=%h %s', '--', 'tools/b559_checks.py').strip()[:160])
    put_txt('b560_components.txt', L)
    print('  written: b560_components.txt (%d lines)' % len(L))


def trail():
    guard_absent(OT, HEADING)
    s = jl('b560_scores.json')
    f, l1, wo = jl('b560_findings.json'), jl('b560_ledger1.json'), jl('b560_workorder.json')
    k = kstate()
    hk = g(ROOT, 'log', '-1', '--format=%h', '--', 'tools/b559_checks.py').strip()
    t = ['', HEADING, '',
         '**(R170) ratified, and its (4) amendment.** (1) b559’s clean part split from the HELD branch and merged. (2) The detection region '
         're-scoped on the measured obstacle. (3) The suite’s file-time arms moved to digests. (4) The bridge staged, the reads before the '
         'build; amended: Stage A pairs by conjugation, from the genuine instance’s facts. (5) H11a-H11e fixed before any build. (6) The gates. '
         '(7) The next act by the landing point. The author’s answers before the face: the clean branch cut from `main` = `81ae175`, not '
         'from v0.2 -- `(R170)`(1) assumed `main` sat at v0.2 (the navigator’s, corrected); the pairing by conjugation.', '',
         '**Entered:** FINDINGS.md:%s (the clean merge’s reading) and :%s (the entry); OPEN_TRAILS.md:%s (the HELD branch’s line), :%s (the '
         're-scope), :%s (the research-arc line), :%s (the work-order’s line); SIDE-global-section CORRESPONDENCE.md row %s; '
         'SIDE-explicit-formula v0.3 = `%s` and v0.4 = `%s`, the branch `li-weil-b560` pushed by name.'
         % (l1['lines']['findings'], f.get('heading_line'), l1['lines']['held'], l1['lines']['rescope'], l1['lines']['arc'], wo.get('line'),
            ROWNO, k['v03'][:7], k['v04'][:7]), '',
         '**The suite:** relay `%s` (b559’s suite: `G-WRITELIST-KINDS` and `G-PRIORBANK-UNCHANGED` read by content digests after the push; '
         'the re-run flag carried; its test quoted); the re-run on b559’s push 62 of 64 -- `G-WRITELIST-KINDS` on terminal_table.json '
         '(b559’s defect (h), by content) and `G-NUMBER-UNCLAIMED` (this act’s face exists).' % hk, '',
         '**H11a REFUTED as first worded, %s as amended · H11b %s · H11c %s · H11d %s · H11e %s.** The stop: `LiLimitExchange` (the limit '
         'exchange; the pairing hazard), priced (D1)-(D6), the converse (V1)-(V4).'
         % tuple(w_(s.get(x)) for x in ('h11a', 'h11b', 'h11c', 'h11d', 'h11e')), '',
         '**The kernel:** `DetectionRegion.lean` (v0.3), `LiWeil.lean` (v0.4) and their axiom-check files, new files only; 40 declarations at '
         'the standard three, no `sorryAx`; `rh_imp_li_nonneg : RiemannHypothesis → ∀ n, 0 ≤ LiCoeff n` over the genuine zeros.', '',
         '**Next:** the bridge continued at (D1)-(D4) if the author so rules; otherwise W-ORD-GRH-WEIL (`(R170)`(7)).', '',
         '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s.'
         % tuple(w_(s.get(x)) for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
         '**Two fast-forwards onto `main`, two tags, no `sorry` on any `main`.** Nothing deposits; nothing at Zenodo written; no existing '
         '`.lean` file edited; no Zeta23 file edited; no monograph byte changed; no keystone body edited; ERRATA untouched; the ceiling '
         'unchanged; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH or any '
         'zero beyond the compiled statements’ own words.', '']
    o = append_to(OT, NL.join(t))
    o['line'] = line_of(OT, HEADING)
    put_json('b560_trail.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn):
        sys.exit('usage: b560_record.py <component>')
    fn()
