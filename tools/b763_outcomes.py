# -*- coding: utf-8 -*-
"""tools/b763_outcomes.py -- (R373)(6), (7) AND (8), AND THE AUTHOR'S WORD OF 2026-11-19 ON W-ORD-STATEMENT-FILE: EACH RESULT'S SENTENCE, THE
RULING'S TEXT WITH ITS FIELDS FILLED FROM THE ACT'S BANKS AND NOTHING ELSE; AND THE BUILD LINES FOR OPEN_TRAILS (data/b763_xlines.json, read by
tools/b763_rulings.py ledgers).

Carried from tools/b759_outcomes.py's form by the Write tool at b763's Component 2, while dispatch 3 built, and committed before its first run
(N2). The sentences are cut from the ferry bank at run time; no sentence is typed here. The two lines of the author's word stand in
tools/b763_rulings.py (SF_BUILT, SF_NOT), composed there from that word; this tool fills their fields. Each field is printed with the bank it
came from. Its writes: data/b763_outcomes.txt and .json and data/b763_xlines.json, whole at each `bank`.

WHAT A RUN MUST SHOW, (6) (data/b763_ferry.txt :19): "the exit file 0; the print run with 0 error lines; an axioms line within propext,
Classical.choice and Quot.sound for each new name; no line naming sorryAx." Read from the controls tool's read row
(data/b763_dispatch_rows.json): the exit file, the built commit, the build log's errors, the print's state, every axioms line within the
standard three, the targets without a line exactly the workflow grammar's two refusals (data/b763_presend_sf.txt, by name), no sorryAx; and
from the run's axioms file each new name by its full name.

(6). A RUN'S STATE: FILE where it shows the list, the 48 names of (6) (the six of [P1] and the 42 of (S1) to (S5)) and the 19 of the
statement file; FORM where it shows the list and the 48, the statement file's names not among its targets; BROKE otherwise. THE LANDING: the
gated push's capture of push-b763-form or push-b763-land reading v0.42 made at main's read-back once, its peel read back equal at the remote;
the landed run the FILE or FORM run built at that peel. Each statement's sentence is cut from (6) at run time, its "..." read as the field list
of (S1)'s sentence ("SIDE-explicit-formula <tag> = <peel>, run <run id>, <axioms>"), and filled from the landed run: <name> or <names> the
names the sentence cites (CITED), <axioms> the union of the axioms they print, in the standard order. THE GRADE: DERIVES where the salt check of
the statement's send at the landed commit (tools/b763_presend.py salt_at) passes, read before the grade is written anywhere; NOT WRITTEN
otherwise. A statement not compiled takes the failure sentence, with where the last run naming it broke and its price.

THE STATEMENT FILE, by the author's word (data/b763_author_words_preseal.txt :2-:7). BUILT where a FILE run shows each of its 19 names
within the standard three and main landed at that run's commit: the line SF_BUILT, its tag, peel, run and axioms. NOT BUILT where the run
that carries its names is BROKE: the line SF_NOT, with the build's reading. NOT READ where no run carries them; then no line.

(7). The statement's runs (item arith): STATEMENT COMPILED where a run shows the list and the ten names of its file within the standard
three. With no proof run, the sentence IF NO PROOF IS BUILT and the line [X2]: <names> ControlFailureB and ControlFailureA, <tag or branch>
push-b763-arith at the built commit, the prices of FORM A and FORM B from data/b763_price.json. A proof run is not composed here: the tool
stops, naming it.

(8). Each item of ITEMS8: BUILT where its run shows the list and its names within the standard three, and its branch's capture reads a tag
made at main's read-back once with its peel read back equal, the peel the run's built commit; the line [X3] for it. An item with no read run
takes no line, and is carried by name with its price in the entry ((8)).

  control       the tool's controls, printed
  bank          read and composed; data/b763_outcomes.txt, .json and data/b763_xlines.json written
"""
import io
import json
import os
import re
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b763_controls as C        # noqa: E402  (the read rows, the artifacts and the axioms reader)
import figbank as FB             # noqa: E402

NL = '\n'
ACT = 'b763'
FERRY = os.path.join(D, 'b763_ferry.txt')
PRESEND = os.path.join(D, 'b763_presend_sf.txt')
ROWS = os.path.join(D, 'b763_dispatch_rows.json')
PRICE = os.path.join(D, 'b763_price.json')
BANK = os.path.join(D, 'b763_outcomes.txt')
BANKJ = os.path.join(D, 'b763_outcomes.json')
XJSON = os.path.join(D, 'b763_xlines.json')
STANDARD = C.STANDARD
EFKEY = 'SIDE-explicit-formula'
TAG6 = 'v0.42'
B = 'SIDEExplicitFormula.B321.'
P1 = ('SIDEExplicitFormula.B321.b321_identity', 'SIDEExplicitFormula.GRHWeil.h2_sign_chi_iff_grh_chi',
      'SIDEExplicitFormula.Schema.h2_sign_cfg_iff_target', 'SIDEExplicitFormula.LiCriterionBridge.arith_limit_nonneg_iff_rh',
      'SIDEExplicitFormula.B321.h2_sign_iff_forall_upto', 'SIDEExplicitFormula.KeiperSign.liCoeff_one_pos')   # ### print_targets.txt :490-:495
# ### (6)'s statements: (key, the pre-send send that read it, its declarations by short name, the names its sentence cites)
STMTS = (
    ('S1', 's123', ('primeTermQ_window', 'primeSum_eq_primeTermQ', 'primeSum_window'), ('primeTermQ_window',)),
    ('S2', 's123', ('primeSum_eq_zero_of_lt_log_two',), ('primeSum_eq_zero_of_lt_log_two',)),
    ('S3', 's123', ('paperFT_neg_half_I', 'paperFT_half_I', 'poleTerm_weilTest', 'paperFT_real_neg_half_I', 'paperFT_real_half_I',
                    'poleTerm_weilTest_real', 'integral_mul_sinh_eq_zero_of_even', 'integral_mul_cosh_eq_zero_of_odd', 'poleTerm_weilTest_even',
                    'poleTerm_weilTest_odd', 'basePlateau', 'oddWindow', 'basePlateau_contDiff', 'basePlateau_nonneg', 'oddWindow_contDiff',
                    'oddWindow_hasCompactSupport', 'oddWindow_odd', 'oddWindow_sinh_pos', 'exists_classK_poleTerm_re_neg'),
     ('poleTerm_weilTest', 'poleTerm_weilTest_even', 'poleTerm_weilTest_odd', 'exists_classK_poleTerm_re_neg')),
    ('S4', 's4', ('paperFT_add', 'poleTerm_add', 'exists_window', 'primeSum_add', 'zeroSide_add', 'archTerm_add', 'weilTest_ofReal_apply',
                  'integral_parity_split', 'weilTest_parity_split', 'autocorr_facts', 'poleTerm_parity_split', 'primeSum_parity_split',
                  'archTerm_parity_split', 'form_parity_split'), ('form_parity_split',)),
    ('S5', 's5', ('admissibleWeights', 'primeTermQ_combo', 'admissibleWeights_convex', 'admissibleWeights_congr', 'h2_sign_upto_iff_mem'),
     ('admissibleWeights_convex', 'admissibleWeights_congr', 'h2_sign_upto_iff_mem')),
)
NEW48 = P1 + tuple(B + n for _k, _s, ns, _c in STMTS for n in ns)
OP19 = tuple('SIDEExplicitFormula.OnePage.' + n for n in (
    'classK_def', 'h2_sign_def', 'b321_identity', 'h2_sign_iff_rh', 'h2_sign_chi_iff_grh_chi', 'h2_sign_cfg_iff_target', 'li_nonneg_iff_rh',
    'arith_limit_nonneg_iff_rh', 'h2_sign_iff_forall_upto', 'liCoeff_one_pos', 'zeta_box', 'zq_explicit_formula_instance', 'zq_offline_zero',
    'zq_weil_positivity_fails', 'zq_li_nonneg_fails', 'zq_coeff_not_multiplicative', 'zeta_isMultiplicative_control', 'cQ_not_nonneg',
    'vonMangoldt_nonneg_control'))
CF10 = tuple(B + n for n in ('bsplineSix', 'witnessStep', 'witnessPhi', 'witnessFreq', 'witnessCos', 'witnessH', 'witnessK', 'witnessWidth',
                             'ControlFailureB', 'ControlFailureA'))
# ### (8)'s items as this act builds them: (the controls tool's item, the order, its branch, its full names, what compiled by name)
ITEMS8 = (('squares', 'W-ORD-SQUARES-AT-24', 'push-b763-squares',
           tuple('SIDEExplicitFormula.SquaresAt24.' + n for n in ('not_isSquare_two_zmod_three', 'isSquare_three_iff', 'squares_at_24')),
           'squares_at_24, with isSquare_three_iff and not_isSquare_two_zmod_three'),
          # ### b763 (8)'s third by its upper hours: a first file of W-ORD-KEIPER-FACE, the order not built in full by this act (events (66)),
          # ### so its branch's capture reads no tag and its outcome reads NOT BUILT whatever its run shows; its run read here beside it
          ('keiper', 'W-ORD-KEIPER-FACE', 'push-b763-keiper',
           tuple('SIDEExplicitFormula.KeiperPolygamma.' + n for n in (
               'rhp', 'mem_rhp', 'isOpen_rhp', 'ne_neg_nat_of_re_pos', 'differentiableOn_Gamma_rhp', 'analyticAt_Gamma_of_re_pos',
               'analyticAt_digamma', 'digamma_eventually_shift', 'iteratedDeriv_inv_apply', 'iteratedDeriv_digamma_shift',
               'iteratedDeriv_digamma_shift_nat', 'tendsto_partial_sums_of_tail')),
           'a first file, KeiperPolygamma.lean'))
SENT6 = tuple((k, 'for (%s), ' % k) for k in ('S1', 'S2', 'S3', 'S4', 'S5'))
FAIL6 = 'A statement that does not compile within its price: '
NOPROOF7 = 'IF NO PROOF IS BUILT: '
ELLIPSIS = ', ...)'


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _rd(p):
    return io.open(p, encoding='utf-8').read().replace('\r', '') if os.path.exists(p) else ''


def clause(n):
    """(the clause's first line, its text): the lines from the one opening `(n) ` to the line before the next clause's or the ruling's end."""
    ls = _rd(FERRY).split(NL)
    hit = [i for i, l in enumerate(ls) if l.startswith('(%d) ' % n)]
    if len(hit) != 1:
        sys.exit('### CLAUSE (%d) NOT READ ONCE IN THE FERRY BANK -- nothing written' % n)
    j = hit[0] + 1
    while j < len(ls) and not re.match(r'^\(\d+\) ', ls[j]) and not ls[j].startswith('RULING (R'):
        j += 1
    return hit[0] + 1, NL.join(ls[hit[0]:j])


def quoted_after(text, words):
    """the quoted sentence after `words`, the words standing once in the clause."""
    if text.count(words) != 1:
        return None
    m = re.match(r'\s*"(.*?)"', text[text.index(words) + len(words):])
    return m.group(1) if m else None


def fields_of(t):
    return tuple(re.findall(r'<([^<>]+)>', t or ''))


def fill(t, seq):
    """the sentence with its fields filled in order of their occurrence, each pair (field, value) filling the first field of its name left;
    (None, [the field]) where a value is empty or carries a field mark, or the field is not left to fill."""
    out = t
    for k, v in seq:
        if '<' in str(v) or '>' in str(v) or not str(v).strip() or ('<%s>' % k) not in out:
            return None, ['<%s>' % k]
        out = out.replace('<%s>' % k, str(v), 1)
    return out, re.findall(r'<[^<>]+>', out)


def tail_of(s1):
    """(S1)'s field list after its name: the words between '(<name>, ' and the sentence's closing ')'."""
    m = re.search(r'\(<name>, (.+)\)$', s1 or '')
    return m.group(1) if m else None


def expand(s, tail):
    """a sentence whose fields end '(<name>, ...)' or '(<names>, ...)' read with (S1)'s field list in place of the ellipsis; the ellipsis once."""
    if s is None or tail is None or s.count(ELLIPSIS) != 1:
        return None
    return s.replace(ELLIPSIS, ', %s)' % tail)


def cut6():
    """{key: (sentence or None, its fields)} for (6)'s five sentences, the ellipsis expanded, and FAIL for the failure sentence."""
    _ln, text = clause(6)
    raw = dict((k, quoted_after(text, w)) for k, w in SENT6)
    tail = tail_of(raw['S1'])
    out = {'S1': (raw['S1'], fields_of(raw['S1']))}
    for k, _w in SENT6[1:]:
        e = expand(raw[k], tail)
        out[k] = (e, fields_of(e))
    f = quoted_after(text, FAIL6)
    out['FAIL'] = (f, fields_of(f))
    return out


def cut7():
    _ln, text = clause(7)
    s = quoted_after(text, NOPROOF7)
    return s, fields_of(s)


def presend_refused():
    """the names the workflow's grammar refuses, by the pre-send bank's REFUSED rows (each name once)."""
    return list(dict.fromkeys(m.group(1) for m in re.finditer(r'REFUSED print_targets\.txt :\d+ (\S+)', _rd(PRESEND))))


def shown(rd, refused):
    """[(what, ok)] of (6)'s list on a read row."""
    rlines = [l for l in (rd.get('axioms_refused') or '').split(NL) if l.strip()]
    return [('the exit file 0', rd.get('build_exit') == '0'),
            ('the built commit the dispatched', bool(rd.get('built_equal'))),
            ('not stopped under the hold', not rd.get('stop')),
            ('the build log`s error lines 0', not rd.get('errors')),
            ('the print ran with 0 error lines', rd.get('axioms_print') == 'RAN'),
            ('every axioms line within the standard three', rd.get('axiom_lines') == rd.get('axiom_within') and not rd.get('axiom_outside')),
            ('the targets without a line exactly the grammar`s refused', sorted(rd.get('axiom_missing') or []) == sorted(refused)
             and rd.get('axiom_missing_n') == len(refused)),
            ('the lines the workflow refused the grammar`s, by name', len(rlines) == len(refused) and all(any(n in l for l in rlines) for n in refused)),
            ('no line naming sorryAx', not rd.get('sorryAx'))]


def names_read(ax, names):
    """[(name, axioms or None, within)] by full name as the print names it."""
    return [(s, ax.get(s), ax.get(s) is not None and set(ax[s]) <= set(STANDARD) and 'sorryAx' not in ax[s]) for s in names]


def state6(rd, ax, targets, refused):
    """(FILE | FORM | BROKE, the list, the 48 read, the 19 read), pure."""
    sh = shown(rd, refused) if rd else [('the run read', False)]
    n48, n19 = names_read(ax, NEW48), names_read(ax, OP19)
    if not (all(o for _w, o in sh) and all(w for *_x, w in n48)):
        return 'BROKE', sh, n48, n19
    if any(s in (targets or []) for s in OP19):
        return ('FILE' if all(w for *_x, w in n19) else 'BROKE'), sh, n48, n19
    return 'FORM', sh, n48, n19


def state_names(rd, ax, refused, names):
    """(COMPILED | BROKE, the list, the names read), pure: the list shown and every name within."""
    sh = shown(rd, refused) if rd else [('the run read', False)]
    nr = names_read(ax, names)
    return ('COMPILED' if all(o for _w, o in sh) and all(w for *_x, w in nr) else 'BROKE'), sh, nr


def tag_read(text, tag=None):
    """(tag, peel, tag object) where the capture reads one tag (the one named, or the only one) made at main's read-back once and its peel
    local equal to remote; else (None, None, why)."""
    made = [m for m in re.finditer(r'(?m)^push_gated: tag (\S+) made at the read-back ([0-9a-f]{40}) \(([0-9a-f]{40})\)$', text or '')
            if tag is None or m.group(1) == tag]
    if len(made) != 1:
        return None, None, 'a tag`s making read %d times, not once' % len(made)
    t = made[0].group(1)
    peel = [m for m in re.finditer(r'(?m)^push_gated: tag (\S+) peeled local ([0-9a-f]{40}) remote ([0-9a-f]{40})$', text or '') if m.group(1) == t]
    if len(peel) != 1:
        return None, None, 'the peel of %s read %d times, not once' % (t, len(peel))
    if not (made[0].group(2) == peel[0].group(2) == peel[0].group(3)):
        return None, None, 'the peel local %s, remote %s, the read-back %s, not equal' % (peel[0].group(2)[:8], peel[0].group(3)[:8], made[0].group(2)[:8])
    return t, made[0].group(2), made[0].group(3)


def break_read(rd):
    """where the run broke: the first error line naming a .lean file and line, else the print's state, else the exit file."""
    for l in (rd.get('errors') or []):
        m = re.search(r'([\w./-]+\.lean):(\d+):\d+', l)
        if m:
            return '%s :%s' % (re.sub(r'^(\./)+', '', m.group(1)), m.group(2))
    if rd.get('axioms_print') and rd.get('axioms_print') != 'RAN':
        return 'the axioms print, %s' % rd['axioms_print'][:120]
    return 'the exit file %s' % rd.get('build_exit')


def ax_union(nr):
    got = set(x for _s, a, _w in nr for x in (a or ()))
    return 'axioms [%s]' % ', '.join(x for x in STANDARD if x in got) if got <= set(STANDARD) else None


def and_join(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else '%s and %s' % (', '.join(xs[:-1]), xs[-1])


def price_of(key):
    r = dict((x['key'], x) for x in json.load(io.open(PRICE, encoding='utf-8'))['rows'])[key]
    return '%s to %s hours over %d to %d dispatches' % (r['lo_h'], r['hi_h'], r['dispatches'][0], r['dispatches'][1])


def runs_of(R, item, judge):
    """[(dispatch row, read row or None, the judge's reading or None, targets)] for the item's dispatches in order; the judge takes (read row,
    axioms, targets)."""
    out = []
    for d in [r for r in R if r.get('kind') == 'dispatch' and r.get('kernel') == EFKEY and r.get('item') == item]:
        rds = [r for r in R if r.get('kind') == 'read' and r.get('kernel') == EFKEY and int(r.get('run', 0)) == int(d['run'])]
        if not rds:
            out.append((d, None, None, []))
            continue
        art = C._art('ef', d['run'])
        ax, targets = C.axioms_of(C._f(art, 'axioms.txt')), C._targets(art)
        out.append((d, rds[-1], judge(rds[-1], ax, targets), targets))
    return out


def run_line(d, rd):
    return ('    dispatch %d, run %s at %s: exit file %s ; built %s, equal %s ; errors %d ; the print %s ; targets %s ; axioms lines %s, within %s ; '
            'without a line %s ; sorryAx %s ; runner low %s MB' % (
                d['n'], d['run'], d['sha'][:8], rd.get('build_exit'), (rd.get('built_ref') or '')[:8], rd.get('built_equal'), len(rd.get('errors') or []),
                rd.get('axioms_print'), rd.get('targets'), rd.get('axiom_lines'), rd.get('axiom_within'), rd.get('axiom_missing_n'), rd.get('sorryAx'),
                rd.get('runner_low_mb')))


# ================================================================================ (6) AND THE STATEMENT FILE
def item6(R, refused):
    ln, _t = clause(6)
    sents = cut6()
    out = ['## (6) BUILD ONE: THE FIVE STATEMENTS AND THE SIX NAMES OF [P1] (the ferry bank :%d; the sentences cut from it at run time, the ellipsis '
           'of (S2) to (S5) read as (S1)`s field list)' % ln]
    rec = dict(item='form', outcome='NOT READ', runs=[], statements=[])
    sf = dict(outcome='NOT READ', key=None, fields=None, runs=[])
    runs = runs_of(R, 'form', lambda rd, ax, tg: state6(rd, ax, tg, refused))
    for d, rd, J_, targets in runs:
        if rd is None:
            out.append('    dispatch %d, run %s at %s: NOT READ' % (d['n'], d['run'], d['sha'][:8]))
            continue
        st, sh, n48, n19 = J_
        out.append(run_line(d, rd))
        out += ['      %s: %s' % (w, 'SHOWN' if o else 'NOT SHOWN') for w, o in sh]
        bad48 = [s for s, _a, w in n48 if not w]
        out.append('      the 48 names of (6): %d within the standard three%s' % (48 - len(bad48), (' ; NOT: %s' % ', '.join(bad48[:6])) if bad48 else ''))
        if any(s in targets for s in OP19):
            bad19 = [s for s, _a, w in n19 if not w]
            out.append('      the 19 names of the statement file among the targets: %d within%s' % (19 - len(bad19), (' ; NOT: %s' % ', '.join(bad19[:6])) if bad19 else ''))
        out.append('      THE RUN`S STATE: %s%s' % (st, (' -- broke at %s' % break_read(rd)) if st == 'BROKE' else ''))
        rec['runs'].append(dict(n=d['n'], run=int(d['run']), sha=d['sha'], state=st, file_targets=any(s in targets for s in OP19),
                                where=break_read(rd) if st == 'BROKE' else None))
    if not rec['runs']:
        out.append('  THE OUTCOME: NOT READ')
        return out, rec, sf
    caps = [(b, os.path.join(D, '%s_%s_%s_push_out.txt' % (ACT, EFKEY, b))) for b in ('push-b763-form', 'push-b763-land')]
    tags = [(b, p) + tag_read(_rd(p), TAG6) for b, p in caps]
    landed = [x for x in tags if x[3]]
    good = dict((r['sha'], r) for r in rec['runs'] if r['state'] in ('FILE', 'FORM'))
    for b, p, t, peel, why in tags:
        out.append('  THE LANDING BY %s (%s): %s' % (b, os.path.relpath(p, RELAY).replace('\\', '/'),
                                                   '%s made at main`s read-back %s, its peel read back equal at the remote' % (t, peel[:8]) if peel else 'none: %s' % why))
    if len(landed) != 1 or landed[0][3] not in good:
        out.append('  THE OUTCOME: %s' % ('SHOWN, NOT LANDED' if good else 'NOT COMPILED'))
        rec['outcome'] = 'SHOWN, NOT LANDED' if good else 'NOT COMPILED'
        if not good:
            last = rec['runs'][-1]
            for k, send, _ns, cited in STMTS:
                s, left = fill(sents['FAIL'][0], [('statement', '(%s)' % k[1:]), ('where', '%s (run %s)' % (last['where'], last['run'])),
                                                  ('price', price_of('(6) %s' % k))])
                rec['statements'].append(dict(key=k, compiled=False, sentence=s, unfilled=left))
                out.append('  (%s) NOT COMPILED: %s' % (k, s))
        return out, rec, sf
    _b, _p, tag, peel, tobj = landed[0]
    g = good[peel]
    art = C._art('ef', g['run'])
    ax = C.axioms_of(C._f(art, 'axioms.txt'))
    import b763_presend as PS
    grades = {}
    for send in dict.fromkeys(s for _k, s, _n, _c in STMTS):
        L_, ok_, n_ok_, n_ = PS.salt_at(peel, send)
        grades[send] = ok_
        out.append('  THE SALT CHECK OF SEND %s AT THE LANDED COMMIT %s: %s (%d OF %d STATEMENTS)' % (send, peel[:8], 'PASSED' if ok_ else 'REFUSED', n_ok_, n_))
    for k, send, _ns, cited in STMTS:
        nr = names_read(ax, [B + c for c in cited])
        axu = ax_union(nr)
        word = 'names' if 'names' in sents[k][1] else 'name'
        seq = [(word, and_join(cited)), ('tag', tag), ('peel', peel[:8]), ('run id', g['run']), ('axioms', axu or '')]
        s, left = fill(sents[k][0], seq)
        rec['statements'].append(dict(key=k, compiled=True, cited=list(cited), axioms=axu, sentence=s, unfilled=left,
                                      grade='DERIVES' if grades[send] else None))
        out.append('  (%s) COMPILED, THE GRADE %s: %s' % (k, 'DERIVES, binding no premise' if grades[send] else 'NOT WRITTEN, the salt check refused', s))
    rec.update(outcome='LANDED, COMPILED', tag=tag, peel=peel, tag_object=tobj, run=g['run'], sha=g['sha'], landed_by=_b)
    out.append('  THE OUTCOME: LANDED, COMPILED -- %s = %s (tag object %s), run %s' % (tag, peel[:8], tobj[:8], g['run']))
    # ### the statement file, by the author's word
    fr = [r for r in rec['runs'] if r['file_targets']]
    if not fr:
        out.append('  THE STATEMENT FILE: NOT READ, no run carried its names')
        return out, rec, sf
    f = fr[-1]
    if f['state'] == 'FILE' and f['sha'] == peel:
        nr = names_read(ax, OP19)
        sf.update(outcome='BUILT', key='SF_BUILT', runs=[f['run']],
                  fields=[['<tag>', tag], ['<peel>', peel[:8]], ['<run id>', str(f['run'])], ['<axioms>', ax_union(nr) or '']])
    elif f['state'] == 'BROKE':
        sf.update(outcome='NOT BUILT', key='SF_NOT', runs=[f['run']],
                  fields=[['<reading>', 'dispatch %d, run %s at %s, broke at %s' % (f['n'], f['run'], f['sha'][:8], f['where'])]])
    else:
        sf.update(outcome='BUILT, NOT LANDED AT ITS COMMIT', runs=[f['run']])
    out.append('  THE STATEMENT FILE (the author`s word, data/b763_author_words_preseal.txt :2-:7): %s%s' % (
        sf['outcome'], (' -- the line %s, its fields %s' % (sf['key'], sf['fields'])) if sf['key'] else ' -- no line'))
    return out, rec, sf


# ================================================================================ (7)
def item7(R, refused):
    ln, _t = clause(7)
    s7, f7 = cut7()
    out = ['## (7) THE CENTRE: THE STATEMENT OF THE CONTROL`S FAILURE (the ferry bank :%d; the sentence IF NO PROOF IS BUILT cut at run time, its '
           'fields %s)' % (ln, list(f7))]
    rec = dict(item='arith', outcome='NOT READ', runs=[])
    if [r for r in R if r.get('kind') == 'dispatch' and r.get('item') in ('arith_a', 'arith_b')]:
        sys.exit('### A PROOF RUN OF (7) IS ROWED: NOT COMPOSED BY THIS TOOL -- nothing written')
    for d, rd, J_, _tg in runs_of(R, 'arith', lambda rd, ax, tg: state_names(rd, ax, refused, CF10)):
        if rd is None:
            out.append('    dispatch %d, run %s at %s: NOT READ' % (d['n'], d['run'], d['sha'][:8]))
            continue
        st, sh, nr = J_
        out.append(run_line(d, rd))
        out += ['      %s: %s' % (w, 'SHOWN' if o else 'NOT SHOWN') for w, o in sh]
        out.append('      the ten names of the statement`s file: %d within the standard three' % sum(1 for *_x, w in nr if w))
        out.append('      THE RUN`S STATE: %s' % st)
        rec['runs'].append(dict(n=d['n'], run=int(d['run']), sha=d['sha'], state=st, where=break_read(rd) if st == 'BROKE' else None))
    ok = [r for r in rec['runs'] if r['state'] == 'COMPILED']
    if not ok:
        rec['outcome'] = 'NOT READ' if not rec['runs'] else 'NOT COMPILED'
        out.append('  THE OUTCOME: %s' % rec['outcome'])
        return out, rec, None
    g = ok[-1]
    pa, pb = price_of('(7) A'), price_of('(7) B')
    s, left = fill(s7, [('names', 'ControlFailureB and ControlFailureA'), ('tag or branch', 'push-b763-arith at %s' % g['sha'][:8]),
                        ('run id', g['run']), ('price', pa), ('price', pb)])
    rec.update(outcome='STATEMENT COMPILED, NO PROOF SENT', run=g['run'], sha=g['sha'], sentence=s, unfilled=left, prices=dict(A=pa, B=pb))
    out.append('  THE OUTCOME: STATEMENT COMPILED, NO PROOF SENT')
    out.append('  THE SENTENCE: %s' % s)
    line = dict(key='X2', fields=[['<names>', 'ControlFailureB and ControlFailureA'], ['<price>', pa], ['<price>', pb]], runs=[g['run']])
    return out, rec, line


# ================================================================================ (8)
def item8(R, refused):
    out, recs, lines = ['## (8) THE ORDERS PRICED BESIDE IT, AS BUILT (each on a push-b763-* branch of its own)'], [], []
    for it, order, branch, names, what in ITEMS8:
        rec = dict(item=it, order=order, outcome='NOT BUILT', runs=[])
        for d, rd, J_, _tg in runs_of(R, it, lambda rd, ax, tg, names=names: state_names(rd, ax, refused, names)):
            if rd is None:
                out.append('    %s: dispatch %d, run %s at %s: NOT READ' % (order, d['n'], d['run'], d['sha'][:8]))
                continue
            st, sh, nr = J_
            out.append(run_line(d, rd))
            out.append('      %s ; its %d names within %d ; THE RUN`S STATE: %s' % (
                ' ; '.join('%s %s' % (w, 'SHOWN' if o else 'NOT SHOWN') for w, o in sh), len(names), sum(1 for *_x, w in nr if w), st))
            rec['runs'].append(dict(n=d['n'], run=int(d['run']), sha=d['sha'], state=st, axioms=ax_union(nr) if st == 'COMPILED' else None))
        cap = os.path.join(D, '%s_%s_%s_push_out.txt' % (ACT, EFKEY, branch))
        tag, peel, why = tag_read(_rd(cap))
        good = [r for r in rec['runs'] if r['state'] == 'COMPILED' and peel and r['sha'] == peel]
        if good and tag != TAG6:
            g = good[-1]
            rec.update(outcome='BUILT IN FULL', tag=tag, peel=peel, tag_object=why, run=g['run'])
            lines.append(dict(key='X3', fields=[["<the order's name>", order], ['<6 or 8>', '8'], ['<what compiled, by name>', what], ['<tag>', tag],
                                                ['<peel>', peel[:8]], ['<run id>', str(g['run'])], ['<axioms>', g['axioms'] or '']], runs=[g['run']]))
        out.append('  %s: %s%s' % (order, rec['outcome'], (' -- %s = %s, run %s' % (tag, peel[:8], rec['run'])) if rec.get('run') else
                                     (' -- no read run' if not rec['runs'] else ' -- the landing: %s' % (why if not peel else 'its peel %s not a compiled run`s commit' % peel[:8]))))
        recs.append(rec)
    return out, recs, lines


# ================================================================================ THE CONTROLS
def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    s6 = cut6()
    want6 = {'S1': ('name', 'tag', 'peel', 'run id', 'axioms'), 'S2': ('name', 'tag', 'peel', 'run id', 'axioms'),
             'S3': ('names', 'tag', 'peel', 'run id', 'axioms'), 'S4': ('name', 'tag', 'peel', 'run id', 'axioms'),
             'S5': ('names', 'tag', 'peel', 'run id', 'axioms'), 'FAIL': ('statement', 'where', 'price')}
    got6 = dict((k, s6[k][1]) for k in want6)
    c('(6)`s five sentences and its failure sentence cut once each from the ferry bank, the ellipsis read as (S1)`s field list, their fields',
      [k for k in want6 if got6[k] == want6[k]], got6 == want6)
    s7, f7 = cut7()
    c('(7)`s sentence IF NO PROOF IS BUILT cut once, its fields', f7, f7 == ('names', 'tag or branch', 'run id', 'price', 'price'))
    ex = expand('x (<names>, ...)', 'A <tag> = <peel>')
    c('the ellipsis expanded on a planted sentence; a sentence with two ellipses refused', (ex, expand('a, ...) b, ...)', 'T')),
      ex == 'x (<names>, A <tag> = <peel>)' and expand('a, ...) b, ...)', 'T') is None)
    ref = presend_refused()
    c('the grammar`s refused by name from the pre-send bank', ref, len(ref) == 2 and all('Λ' in x for x in ref))
    good = dict(build_exit='0', built_equal=True, stop=[], errors=[], axioms_print='RAN', axiom_lines=535, axiom_within=535, axiom_outside={},
                axiom_missing=list(ref), axiom_missing_n=2, axioms_refused=NL.join('print target refused: %s' % x for x in ref), sorryAx=False)
    plants = [dict(good, sorryAx=True), dict(good, build_exit='1'), dict(good, axiom_missing=ref + ['X.y'], axiom_missing_n=3),
              dict(good, axioms_refused='print target refused: %s' % ref[0]), dict(good, axiom_within=534, axiom_outside={'X.z': ['sorryAx']}),
              dict(good, axioms_print='RAN WITH ERRORS (1 error lines, the first: x)'), dict(good, errors=['error: x.lean:1:1: y'])]
    got = [all(o for _w, o in shown(p, ref)) for p in plants]
    c('a planted row showing all of (6)`s list taken; seven planted rows each failing one item refused', (all(o for _w, o in shown(good, ref)), got),
      all(o for _w, o in shown(good, ref)) and not any(got))
    ax = dict((s, STANDARD) for s in NEW48 + OP19)
    st = [state6(good, ax, list(NEW48 + OP19), ref)[0], state6(good, ax, list(NEW48), ref)[0],
          state6(good, dict((k, v) for k, v in ax.items() if k != P1[2]), list(NEW48), ref)[0],
          state6(good, dict((k, v) for k, v in ax.items() if k != OP19[5]), list(NEW48 + OP19), ref)[0],
          state6(dict(good, build_exit='1'), ax, list(NEW48), ref)[0],
          state6(good, dict(ax, **{NEW48[20]: ('propext', 'sorryAx')}), list(NEW48), ref)[0]]
    c('a run`s state on planted rows: FILE ; FORM (the file`s names not among the targets) ; BROKE (a [P1] name without a line) ; BROKE (a name '
      'of the file among the targets without a line) ; BROKE (the exit file 1) ; BROKE (a statement`s name naming sorryAx)', st,
      st == ['FILE', 'FORM', 'BROKE', 'BROKE', 'BROKE', 'BROKE'])
    a, b = 'a' * 40, 'b' * 40
    cap = 'push_gated: tag v0.42 made at the read-back %s (%s)\npush_gated: tag v0.42 peeled local %s remote %s\n' % (a, b, a, a)
    t1, t2, t3, t4 = tag_read(cap, 'v0.42'), tag_read(cap.replace('remote %s' % a, 'remote %s' % b), 'v0.42'), tag_read(cap, 'v0.43'), tag_read(cap)
    c('the tag read from a planted capture: equal peels taken; a remote peel differing refused; another tag`s lines not read; the only tag read '
      'unnamed', (t1[0], t2[0], t3[0], t4[0]), t1 == ('v0.42', a, b) and t2[0] is None and t3[0] is None and t4 == t1)
    c('two tags made in one capture refused unnamed', tag_read(cap + cap.replace('v0.42', 'v0.43'))[0], tag_read(cap + cap.replace('v0.42', 'v0.43'))[0] is None)
    br = break_read(dict(errors=['error: ././SIDEExplicitFormula/OnePageStatement.lean:41:4: unknown identifier']))
    c('the break read from a planted error line', br, br == 'SIDEExplicitFormula/OnePageStatement.lean :41')
    f1 = fill('a <where> run <run id>; b <peel> (run <run id>)', [('where', 'M :3'), ('run id', 1), ('peel', '1234abcd'), ('run id', 2)])
    f2, f3 = fill('x <peel>', [('peel', '<peel>')]), fill('x <peel>', [('peel', 'a'), ('peel', 'b')])
    c('a fill in order, two run ids each its own, taken; a value carrying a field mark refused; a field filled twice refused', (f1, f2[0], f3[0]),
      f1 == ('a M :3 run 1; b 1234abcd (run 2)', []) and f2[0] is None and f3[0] is None)
    au = [ax_union([('x', ('Quot.sound', 'propext'), True)]), ax_union([('x', (), True)]), ax_union([('x', ('sorryAx',), False)])]
    c('the axioms` union in the standard order; none printed as an empty list; one outside the three refused', au,
      au == ['axioms [propext, Quot.sound]', 'axioms []', None])
    c('the names: 48 of (6), 19 of the statement file, 10 of (7), each once', (len(NEW48), len(set(NEW48)), len(OP19), len(CF10)),
      len(NEW48) == len(set(NEW48)) == 48 and len(set(OP19)) == 19 and len(set(CF10)) == 10)
    return L, ok


def cmd_bank():
    L, ok = controls()
    if not all(ok):
        print(NL.join(L))
        sys.exit('### THE CONTROLS NOT AS WANTED -- nothing written')
    R = json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []
    refused = presend_refused()
    out = ['%s -- (R373)(6), (7) AND (8) AND THE AUTHOR`S WORD ON W-ORD-STATEMENT-FILE: EACH RESULT`S SENTENCE, THE RULING`S TEXT WITH ITS FIELDS '
           'FILLED FROM THE ACT`S BANKS (%s, tools/b763_outcomes.py bank)' % (ACT, _now()), '', '## THE CONTROLS'] + L + [
           '', '  the grammar`s refusals, by name (data/b763_presend_sf.txt): %s' % ', '.join(refused), '']
    o6, r6, sf = item6(R, refused)
    o7, r7, x7 = item7(R, refused)
    o8, r8, x8 = item8(R, refused)
    out += o6 + [''] + o7 + [''] + o8 + ['']
    lines = ([dict(key=sf['key'], fields=sf['fields'], runs=sf['runs'])] if sf.get('key') else []) + ([x7] if x7 else []) + x8
    out.append('## THE BUILD LINES FOR OPEN_TRAILS (data/b763_xlines.json, read by tools/b763_rulings.py ledgers): %s' % (
        ' ; '.join('%s %s' % (x['key'], x['runs']) for x in lines) or 'none'))
    c6 = sum(1 for s in r6.get('statements') or [] if s.get('compiled'))
    out.append('### ### **THE OUTCOMES: (6) %s, STATEMENTS COMPILED %d OF 5 ; THE STATEMENT FILE %s ; (7) %s ; (8) %s ; BUILD LINES %d ; CONTROLS %d OF %d.**' % (
        r6['outcome'], c6, sf['outcome'], r7['outcome'], ', '.join('%s %s' % (r['order'], r['outcome']) for r in r8), len(lines), sum(ok), len(ok)))
    r = FB.write(BANK, NL.join(out))
    for path, obj in ((BANKJ, dict(at=_now(), form=r6, statement_file=sf, arith=r7, orders=r8)), (XJSON, dict(at=_now(), lines=lines))):
        with open(path + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)
        os.replace(path + '.tmp', path)
    print(NL.join(out))
    print('written data/b763_outcomes.txt, data/b763_outcomes.json and data/b763_xlines.json ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        L_, ok_ = controls()
        print(NL.join(L_))
        print('### CONTROLS %d OF %d AS WANTED' % (sum(ok_), len(ok_)))
    elif a[:1] == ['bank']:
        cmd_bank()
    else:
        sys.exit(__doc__)
