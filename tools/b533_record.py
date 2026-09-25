# -*- coding: utf-8 -*-
"""b533_record.py -- THE COMPONENTS, THE ROW, THE DESK AND THE TRAIL. ### `python tools/b533_record.py components | row | desk | trail`

### READING (10) of the sealed face: each compiled theorem among the fourteen named is graded by statement-read against the
### ferry`s model statement, the reading written in `GRADES` below beside the grade; a halted lemma takes none. READING (11):
### the navigator`s six and the seat`s three, scored on the banks (`b533_attempts.json`, `b533_profile.json`, the module`s
### source, the kernel`s git objects, PLACE-papers` git objects), never typed.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
MOD = os.path.join(KER, 'SIDEExplicitFormula', 'PowerWindow.lean')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
CORR = os.path.join('D:', os.sep, 'SIDE-global-section', 'CORRESPONDENCE.md')
NL = chr(10)
NS = 'SIDEExplicitFormula.B321.'
PRIOR_KERNEL = '7224b87'
PRIOR_PP = '810f944'
ROW = '382'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE GRADES, BY STATEMENT-READ (READING (10)). ### (grade ; the reading against the ferry`s model statement)
GRADES = [
    ('paperFT_conj_of_real_even', 'DERIVES', 'the model`s identity for every z, under evenness alone (continuity and compact support dropped)'),
    ('zero_term_sq', 'DERIVES', 'the model`s square, under the model`s three hypotheses'),
    ('weilTest_even_of_even', 'DERIVES', 'the model`s evenness, for every real g (evenness of g dropped)'),
    ('classK_of_real_even', 'DERIVES', 'the model`s membership, under C^2 and compact support (evenness of g dropped)'),
    ('selfConv_im_zero', 'DERIVES', 'the model`s vanishing imaginary part, for every real g'),
    ('paperFT_power', 'DERIVES', 'the model`s transform (paperFT g)^(2^j), for g even, continuous (C^n, any n) and supported in [-L, L] -- L1`s hypotheses; the support form is defect (d)`s reading'),
    ('power_contDiff', 'DERIVES', 'C^n for every n : ℕ∞ whenever g is, under L3`s window context (support in [-L, L]) -- defect (d)`s reading'),
    ('power_support', 'DERIVES', 'the model`s support [-2^j L, 2^j L] from [-L, L]'),
    ('paperFT_polyOp', 'DERIVES', 'the model`s factorisation, for g C^(2 length a) supported in [-L, L] (READING (5))'),
    ('base_nonzero_at', 'DERIVES', 'the model`s statement for every z and every plateau parameter F in (0, 1); no hypothesis on any zero'),
    ('off_finite_above', 'DERIVES', 'the model`s finiteness for every c > 0, for any C^4 window supported in [-L, L] and any configuration (READING (6))'),
    ('dominant_exists', 'DERIVES', 'the model`s dominant off-line zero, from the off-line rho_1 with offScore > 0 its route starts from; any C^4 window, any configuration'),
    ('real_even_interpolant', 'DERIVES', 'the model`s real interpolant with coefficients bounded by the nodes alone, over any conjugation-closed node set (the vanishing points are nodes with target 0), as a Polynomial ℝ (READING (7))'),
    ('rh_imp_rh_strip', 'DERIVES', 'the model`s statement exactly'),
]
RIGHT = 'riemannZeta_ne_zero_of_one_le_re'
w = lambda v: 'HELD' if v else 'REFUTED'


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


def git(repo, *a):
    return subprocess.run(['git'] + list(a), cwd=repo, capture_output=True, text=True, encoding='utf-8').stdout.strip()


def kread():
    return json.loads(read('b533_attempts.json') or '[]'), json.loads(read('b533_profile.json') or '{}')


def src():
    return io.open(MOD, encoding='utf-8').read()


def decl(s, name):
    """### the declaration`s whole text, from its keyword line to the next top-level keyword line."""
    m = re.search(r'^(?:theorem|def) %s\b' % re.escape(name), s, re.M)
    if not m:
        return None
    n = re.search(r'^(?:theorem|def|/-|end )', s[m.end():], re.M)
    return s[m.start():m.end() + (n.start() if n else len(s))].rstrip()


def head(s, name):
    t = decl(s, name)
    if t is None:
        return None
    i = t.find(':=')
    j = t.find(NL + '  |')
    cut = [x for x in (i, j) if x >= 0]
    return t[:min(cut)].rstrip() if cut else t


def first_clean(at):
    ok = [a['attempt'] for a in at if a['exit'] == 0 and a['errors'] == 0 and not a['sorry']]
    return ok[0] if ok else None


def failures(at):
    out = {}
    for a in at:
        for d in a.get('failed_decls', []):
            out[d] = out.get(d, 0) + 1
    return out


def scores():
    at, pr = kread()
    std = pr.get('std3', {})
    s = src()
    fc = first_clean(at)
    fl = failures(at)
    halted = sorted(d for d, n in fl.items() if n >= 2)
    l12 = ['paperFT_conj_of_real_even', 'zero_term_sq', 'weilTest_even_of_even', 'classK_of_real_even']
    bn_head, bn_all = head(s, 'base_nonzero_at') or '', decl(s, 'base_nonzero_at') or ''
    de_head = head(s, 'dominant_exists') or ''
    rb_now = git(KER, 'hash-object', 'SIDEExplicitFormula/RestBound.lean')
    rb_prior = git(KER, 'rev-parse', PRIOR_KERNEL + ':SIDEExplicitFormula/RestBound.lean')
    rb_head = git(KER, 'rev-parse', 'HEAD:SIDEExplicitFormula/RestBound.lean')
    er_prior = git(PP, 'rev-parse', PRIOR_PP + ':ERRATA.md')
    er_head = git(PP, 'rev-parse', 'HEAD:ERRATA.md')
    er_now = git(PP, 'hash-object', 'ERRATA.md')
    face = read('b533_registration_2026-09-25.txt')
    zen = [f for f in os.listdir(D) if f.startswith('b533_') and 'zenodo' in f.lower()]
    seam = decl(s, 'rh_strip_imp_rh') or ''
    seam_doc = s[max(0, s.find('def rh_strip_imp_rh') - 600):s.find('def rh_strip_imp_rh')]
    return dict(
        first_clean=fc, failures=fl, halted=halted,
        n1=fc is not None and fc <= 2 and all(std.get(NS + n) is True for n in l12),
        n2=std.get(NS + 'base_nonzero_at') is True and 'paperFT_decay' not in bn_all and 'carrier' not in bn_head
        and 'ZeroConfig' not in bn_head,
        n3=std.get(NS + 'dominant_exists') is True and '∀ ρ ∈ Z.carrier, ρ.re ≠ 1 / 2 →' in de_head and 'ρs.re ≠ 1 / 2' in de_head,
        n4=RIGHT in face and RIGHT in seam_doc and 'ABSENT' in face and 'ABSENT' in seam_doc and seam.startswith('def ')
        and not re.search(r'^theorem rh_strip_imp_rh\b', s, re.M),
        n5=bool(rb_now) and rb_now == rb_prior == rb_head,
        n6=bool(er_now) and er_now == er_prior == er_head and not zen,
        s1=not halted and fc is not None and fc <= 3,
        s2=std.get(NS + 'real_even_interpolant') is True,
        s3=std.get(NS + 'off_finite_above') is True,
        restbound=dict(now=rb_now, prior=rb_prior, head=rb_head), errata=dict(now=er_now, prior=er_prior, head=er_head),
        zenodo_files=zen)


def components():
    at, pr = kread()
    s = src()
    L = ['=' * 132, 'b533 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '',
         '### THE MODULE: `SIDEExplicitFormula/PowerWindow.lean` (NEW), `AxiomCheckPower.lean` (NEW).']
    for a in at:
        L.append('  attempt %d : exit %d ; %d error lines ; %.1f s ; declarations failing : %s'
                 % (a['attempt'], a['exit'], a['errors'], a['seconds'], a.get('failed_decls') or 'NONE'))
    fl = failures(at)
    L.append('  ### halted (two failures) : %s' % (sorted(d for d, n in fl.items() if n >= 2) or 'NONE'))
    L += ['', '### THE GRADED STATEMENTS, FROM THE SOURCE (declaration line to its := or its first equation):']
    for n, g, r in GRADES:
        L += ['', head(s, n) or ('### ABSENT : ' + n), '  -> %s -- %s' % (g, r)]
    L += ['', '### THE DEFINITIONS AND PROPS, WHOLE:']
    for n in ('selfConv', 'power', 'polyOp', 'polyEval', 'offScore', 'tieSet', 'killSet', 'nodes_distinct_nonreal',
              'rh_strip', 'rh_strip_imp_rh'):
        L += ['', decl(s, n) or ('### ABSENT : ' + n)]
    L += ['', '### THE PROFILE (AxiomCheckPower.lean):'] + ['  ' + l for l in pr.get('lines', [])]
    L += ['  ### whole-string standard three : %d of %d' % (sum(1 for v in pr.get('std3', {}).values() if v), len(pr.get('std3', {}))),
          '  ### #check : %s' % pr.get('checks')]
    for k, v in (pr.get('prints') or {}).items():
        L.append('  ### #print %s : %s' % (k, ' '.join((v or 'NONE').split())))
    L += ['', '### THE SEAM, PROBED: right half-plane `%s` (Mathlib NumberTheory/LSeries/Nonvanishing.lean:411, probe 2);' % RIGHT,
          '### left half-plane ("zeros with re <= 0 are the trivial zeros") ABSENT from Mathlib at this pin by name;',
          '### `riemannZeta_neg_two_mul_nat_add_one` and `riemannZeta_one_sub` present. `rh_strip_imp_rh` a Prop, not proved.',
          '### nodes_distinct_nonreal`s CAVEAT: (gamma - i delta)^2 is real when gamma = 0, so the square`s nonreality also needs',
          '### Im rho /= 0, which the kernel`s configuration does not record.', '=' * 132]
    io.open(os.path.join(D, 'b533_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:12]))


def grade_cell():
    return (' ; '.join('`%s` %s' % (n, g) for n, g, _ in GRADES)
            + ' -- each by statement-read against the ferry`s model statement; nodes_distinct_nonreal and rh_strip_imp_rh STATED, no grade')


def row():
    sc = scores()
    at, pr = kread()
    n_std = sum(1 for v in pr.get('std3', {}).values() if v)
    cells = [
        ROW,
        '**W-ORD-WEIL-CONVERSE f4, THE POWER-WINDOW ROUTE, ACT ONE OF TWO: THE WINDOW AND THE DOMINANT ZERO** (b533, under (R143)). '
        'In SIDE-explicit-formula, PowerWindow.lean (new): L1 the zero term of a real even window is the square of its transform; '
        'L2 weilTest g g is in classK for every real C^2 compactly supported g; L3 the powers power g j by self-convolution, '
        'transform (paperFT g)^(2^j), smooth, supported in [-2^j L, 2^j L]; L4 the even polynomial operator and its transform '
        'factor; L5 the plateau nonzero at any fixed z for small width, offScore, the off-line zeros above any level finite by '
        'paperFT_decay and the configuration`s finite_window field, the dominant off-line zero, tieSet and killSet finite; L6 a '
        'real interpolant over any conjugation-closed node set with coefficients bounded by the nodes alone; the seam rh_strip, '
        'RiemannHypothesis -> rh_strip compiled, the reverse a Prop (right half-plane %s in Mathlib; the left ABSENT by name). '
        'nodes_distinct_nonreal STATED, with its gamma = 0 caveat. Clean at attempt %s; halted NONE. L7-L8 are b534`s.'
        % (RIGHT, sc['first_clean']),
        '`SIDE-explicit-formula/SIDEExplicitFormula/PowerWindow.lean` : ' + ', '.join('`%s%s`' % (NS, n) for n, _, _ in GRADES)
        + ' ; `SIDE-explicit-formula/AxiomCheckPower.lean`',
        '%d of %d theorems of the module: each [propext, Classical.choice, Quot.sound]' % (n_std, len(pr.get('std3', {}))),
        grade_cell(),
        '(N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s; (S1) %s, (S2) %s, (S3) %s. The kernel lane shuts; the kernel is not '
        'tagged; nothing filed to ERRATA; nothing at Zenodo written; h2 where the deposit left it.'
        % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
    ]
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), CORR] + cells, capture_output=True, text=True,
                       encoding='utf-8')
    print(r.stdout[-3000:], r.stderr[-2000:])
    io.open(os.path.join(D, 'b533_rows.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(dict(cells=cells, exit=r.returncode), indent=1, ensure_ascii=False) + NL)
    return r.returncode


def desk():
    sc = scores()
    at, pr = kread()
    std = pr.get('std3', {})
    L = ['=' * 104, 'b533 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- first clean attempt %s (at most 2) ; L1-L2 std3 : %s.'
         % (w(sc['n1']), sc['first_clean'], [std.get(NS + n) for n in ('paperFT_conj_of_real_even', 'zero_term_sq',
                                                                      'weilTest_even_of_even', 'classK_of_real_even')]),
         '  **(N2)** ### **%s.** -- base_nonzero_at std3 %s ; `paperFT_decay` in its text : %s ; a zero in its statement : %s.'
         % (w(sc['n2']), std.get(NS + 'base_nonzero_at'), 'paperFT_decay' in (decl(src(), 'base_nonzero_at') or ''),
            'carrier' in (head(src(), 'base_nonzero_at') or '')),
         '  **(N3)** ### **%s.** -- dominant_exists std3 %s ; its statement: `%s`.'
         % (w(sc['n3']), std.get(NS + 'dominant_exists'), ' '.join((head(src(), 'dominant_exists') or '').split())),
         '  **(N4)** ### **%s.** -- right half-plane `%s` on the face and beside the Prop ; left ABSENT on both ; '
         '`rh_strip_imp_rh` a def.' % (w(sc['n4']), RIGHT),
         '  **(N5)** ### **%s.** -- RestBound.lean blob : working %s, at %s %s, at HEAD %s.'
         % (w(sc['n5']), sc['restbound']['now'][:12], PRIOR_KERNEL, sc['restbound']['prior'][:12], sc['restbound']['head'][:12]),
         '  **(N6)** ### **%s.** -- ERRATA.md blob : working %s, at %s %s, at HEAD %s ; b533 Zenodo files : %s.'
         % (w(sc['n6']), sc['errata']['now'][:12], PRIOR_PP, sc['errata']['prior'][:12], sc['errata']['head'][:12],
            sc['zenodo_files'] or 'NONE'),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- halted %s ; first clean attempt %s (at most 3) ; failures per declaration %s.'
         % (w(sc['s1']), sc['halted'] or 'NONE', sc['first_clean'], sc['failures'] or 'NONE'),
         '  **(S2)** ### **%s.** -- real_even_interpolant std3 : %s.' % (w(sc['s2']), std.get(NS + 'real_even_interpolant')),
         '  **(S3)** ### **%s.** -- off_finite_above std3 : %s.' % (w(sc['s3']), std.get(NS + 'off_finite_above')),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')].count(True),
            [sc[k] for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THE GRADES (READING (10)).'] + ['  `%s` %s -- %s' % g for g in GRADES] + [
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b533_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b533_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b533_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1, ensure_ascii=False)
    print(NL.join(L))


HEADING = '### b533 — f4, the power-window route, act one of two: the window and the dominant zero; (R143) entered'


def trail():
    sc = scores()
    at, pr = kread()
    s = src()
    n_std = sum(1 for v in pr.get('std3', {}).values() if v)
    body = [
        '', HEADING, '',
        '**(R143) ratified.** (1) The last step is attempted before any update: E-2026-09-25-1 stays drafted and not filed, the',
        'three (R110) description edits are not applied, and the ceiling\'s next wording is not ruled until the f4 attempt closes.',
        '(2) (R140)\'s dichotomy (H-MAX or a sequence toward the supremum of real parts) is withdrawn as the wrong dichotomy: the',
        'supremum f4 needs is of |k^(gamma_rho)| for one fixed window, and it is attained; `not_f4_needs` stands as a theorem about',
        'the widening route, not an obstruction to the power route. (3) The route is the classical proof of Weil\'s converse in the',
        'kernel\'s objects. (4) The converse lands on `rh_strip`; the seam to Mathlib\'s RH is probed and priced, not attempted.',
        '(5) The attempt takes two acts, L1-L6 here and L7-L8 at b534, under a halt rule per lemma.',
        '',
        '**The module, `SIDEExplicitFormula/PowerWindow.lean`** (new; imports RestBound, H2Bridge and Mathlib\'s Lagrange), clean',
        'at attempt %s of 2 run; %d of %d theorems the standard three on the whole string; no lemma halted (attempt 1 failed in'
        % (sc['first_clean'], n_std, len(pr.get('std3', {}))),
        '`neg_one_pow_mul_iz_pow` and `real_even_interpolant`, each once). L1-L2: the zero term of a real even window is the',
        'square of its transform, and `weilTest g g` is in classK for every real C^2 compactly supported g. L3: the powers by',
        'self-convolution, transform (paperFT g)^(2^j). L4: the even polynomial operator, transform factor `polyEval a z`.',
        'L5 and L6:',
        '',
        '```lean',
        head(s, 'base_nonzero_at') or '',
        '',
        head(s, 'dominant_exists') or '',
        '',
        head(s, 'real_even_interpolant') or '',
        '```',
        '',
        '`base_nonzero_at` goes by the estimate |g^(z) − ∫g| ≤ ½∫g once |z|L ≤ ¼, not by the change of variable and dominated',
        'convergence; `off_finite_above` bounds |Im ρ| by `paperFT_decay` at p = 4 and then uses the configuration\'s',
        '`finite_window` field. `tieSet` and `killSet` take the level M as a parameter; both are finite, and `tieSet` is nonempty at',
        'the dominant level. **`nodes_distinct_nonreal` is stated, not proved, with a caveat the ferry\'s one-line reason misses:**',
        '(γ − iδ)² is real when γ = 0, so the square\'s nonreality also needs Im ρ ≠ 0, which the configuration does not record.',
        '',
        '**The seam.** `rh_strip` defined; `rh_imp_rh_strip : RiemannHypothesis → rh_strip` compiled. The reverse, `rh_strip_imp_rh`,',
        'is a Prop: the right half-plane is Mathlib\'s `%s`; the left half-plane (zeros with re ≤ 0 are the trivial' % RIGHT,
        'zeros) is ABSENT from Mathlib at this pin by name, priced as derivable from `riemannZeta_neg_two_mul_nat_add_one` and',
        '`riemannZeta_one_sub`, not attempted.',
        '',
        '**Grades in this act\'s row (%s), by statement-read:** %s DERIVES. `power_contDiff` and `paperFT_power` carry the'
        % (ROW, ', '.join('`%s`' % n for n, _, _ in GRADES)),
        'window\'s support in [-L, L], which the face did not declare; they are read as L3\'s standing window context, and that',
        'reading is printed here for the author (relay `data/b533_desk_notes.txt`, defect (d)).',
        '',
        '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat\'s own: (S1) %s, (S2) %s, (S3) %s.'
        % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
        '**The kernel lane shuts at this act\'s close.** L7 and L8 not started; the kernel is not tagged; RestBound.lean',
        '(`not_f4_needs`, `HMax`) untouched; nothing filed to ERRATA; E-2026-09-25-1 drafted; nothing at Zenodo written; nothing',
        'deposits; no grade moved on any other row; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN;',
        'nothing here is a statement about RH. Span since b525\'s fold: b526-b533, eight.',
        '']
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(NL.join(body).encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b533_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


def main():
    return {'components': components, 'row': row, 'desk': desk, 'trail': trail}[sys.argv[1]]()


if __name__ == '__main__':
    sys.exit(main())
