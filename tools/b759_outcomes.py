# -*- coding: utf-8 -*-
"""tools/b759_outcomes.py -- (R369)(5): THE RESULT'S SENTENCE, THE RULING'S TEXT WITH ITS FIELDS FILLED FROM THE ACT'S BANKS AND NOTHING
ELSE. Carried from tools/b758_outcomes.py by tools/b759_carry.py (data/b759_carry_outcomes.txt) and set for b759 by the Edit tool before its
first run: (5)'s one item and its three sentences (sentences cut from the ferry bank at run time, no sentence typed here, each field printed
with the bank it came from); committed before it runs; its one write the pair data/b759_outcomes.txt and data/b759_outcomes.json, written
whole at each `bank`.

WHAT A RUN MUST SHOW, (5) (data/b759_ferry.txt :21): "the exit file 0; the print run with 0 error lines; an axioms line within propext,
Classical.choice and Quot.sound for each line the filter passes, the five new names among them; no line naming sorryAx." Read from the
controls tool's read row (data/b759_dispatch_rows.json): the exit file, the built commit, the build log's errors, the print's state, every
axioms line within the standard three, the targets without a line exactly the filter's refusals (data/b759_presend.txt, by name: :358 and :359,
each carrying the Greek capital lambda), no sorryAx; and from the run's axioms file the five new names by their full names: rQ_one, cQ_eq,
detector, h2_sign_iff_rh and zq_weil_positivity_fails.

A RUN'S STATE: ALL where it shows the list and the five; FOUR where it shows the list and the four print lines, zq_weil_positivity_fails not
among its targets (commit two reverted); BROKE otherwise.
THE OUTCOME, by (5)'s three sentences: COMPILED where a run reads ALL -- LANDED where, besides, the gated push's capture
(data/b759_SIDE-explicit-formula_push-b759-weil_push_out.txt) reads v0.41 made at main's read-back and its peel read back equal at the remote,
the sentence IF IT COMPILES then composed with that peel, the run and its axioms lines; SHOWN before the landing. NOT COMPILED where a run reads
FOUR -- the sentence IF IT DOES NOT COMPILE composed with where the last BROKE run naming the theorem broke and its run, and the landing's peel
and run. NOTHING LANDED where every read run is BROKE -- the sentence IF NO RUN SUCCEEDS composed with where the last read run broke and its
run. NOT READ where no run is read. Beside COMPILED: the compiled statement read against (5) at the run's commit (tools/b759_presend.py's salt
check, at the built commit), before the grade DERIVES is written anywhere.

  control       the tool's controls, printed
  bank          the item read and composed, the pair written
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
import b757_join as J            # noqa: E402  (the module namer, as committed at b757; the carry's shift to b758_join set back, b758_join
#   ### defining neither module_of nor libs_at)
import b759_controls as C        # noqa: E402  (the read rows and the axioms reader)
import figbank as FB             # noqa: E402

NL = '\n'
ACT = 'b759'
FERRY = os.path.join(D, 'b759_ferry.txt')
PRESEND = os.path.join(D, 'b759_presend.txt')
ROWS = os.path.join(D, 'b759_dispatch_rows.json')
BANK = os.path.join(D, 'b759_outcomes.txt')
BANKJ = os.path.join(D, 'b759_outcomes.json')
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')
EFKEY = 'SIDE-explicit-formula'
FIVE = ('SIDEExplicitFormula.Schema.ZQ.rQ_one', 'SIDEExplicitFormula.Schema.ZQ.cQ_eq', 'SIDEExplicitFormula.Schema.detector',
        'SIDEExplicitFormula.B321.h2_sign_iff_rh', 'SIDEExplicitFormula.Schema.ZQ.zq_weil_positivity_fails')   # ### (5)'s five new names, full
WEIL = FIVE[4]
CLAUSE, DITEM, BRANCH, TAG = 5, 'weil', 'push-b759-weil', 'v0.41'
# ### (5)'s three sentences: (the words standing once before each quoted sentence in :21, its fields in order)
SENTENCES = (('COMPILED', 'THE SENTENCE IF IT COMPILES:', ('peel', 'run id', 'n')),
             ('NOT COMPILED', 'the four lines land alone, and the sentence is', ('where', 'run id', 'peel', 'run id')),
             ('NOTHING LANDED', 'IF NO RUN SUCCEEDS:', ('where', 'run id')))


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _rd(p):
    return io.open(p, encoding='utf-8').read().replace('\r', '') if os.path.exists(p) else ''


def clause(n):
    hit = [(i + 1, l) for i, l in enumerate(_rd(FERRY).split(NL)) if l.startswith('(%d) ' % n)]
    if len(hit) != 1:
        sys.exit('### CLAUSE (%d) NOT READ ONCE IN THE FERRY BANK -- nothing written' % n)
    return hit[0]


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


def presend_refused():
    """the names (ii) refused, by the pre-send bank's REFUSED rows (each name once)."""
    return list(dict.fromkeys(m.group(1) for m in re.finditer(r'REFUSED print_targets\.txt :\d+ (\S+)', _rd(PRESEND))))


def shown(rd, refused):
    """[(what, ok)] of (4)'s list on a read row."""
    rtext = rd.get('axioms_refused') or ''
    rlines = [l for l in rtext.split(NL) if l.strip()]
    return [('the exit file 0', rd.get('build_exit') == '0'),
            ('the built commit the dispatched', bool(rd.get('built_equal'))),
            ('not stopped under the hold', not rd.get('stop')),
            ('the build log`s error lines 0', not rd.get('errors')),
            ('the print ran with 0 error lines', rd.get('axioms_print') == 'RAN'),
            ('every axioms line within the standard three', rd.get('axiom_lines') == rd.get('axiom_within') and not rd.get('axiom_outside')),
            ('the targets without a line exactly (ii)`s refused', sorted(rd.get('axiom_missing') or []) == sorted(refused)
             and rd.get('axiom_missing_n') == len(refused)),
            ('the lines the workflow refused (ii)`s, by name', len(rlines) == len(refused) and all(any(n in l for l in rlines) for n in refused)),
            ('no line naming sorryAx', not rd.get('sorryAx'))]


def five_read(ax, names=FIVE):
    """[(name, axioms or None, within)] for (5)'s five new names, each by its full name as the print names it."""
    out = []
    for s in names:
        a = ax.get(s)
        out.append((s, a, a is not None and set(a) <= set(STANDARD) and 'sorryAx' not in a))
    return out


def state_of(rd, ax, targets, refused):
    """(the run's state ALL | FOUR | BROKE, the list [(what, ok)], the five [(name, axioms, within)]), pure."""
    sh = shown(rd, refused) if rd else [('the run read', False)]
    fr = five_read(ax)
    base = all(o for _w, o in sh)
    four = all(w for _s, _a, w in fr[:4])
    if base and four and fr[4][2]:
        return 'ALL', sh, fr
    if base and four and WEIL not in (targets or []):
        return 'FOUR', sh, fr
    return 'BROKE', sh, fr


def tag_read(text, tag):
    """(peel, tag object) where the capture reads the tag made at main's read-back once and its peel local equal to remote; else (None, why)."""
    made = [m for m in re.finditer(r'(?m)^push_gated: tag (\S+) made at the read-back ([0-9a-f]{40}) \(([0-9a-f]{40})\)$', text or '') if m.group(1) == tag]
    peel = [m for m in re.finditer(r'(?m)^push_gated: tag (\S+) peeled local ([0-9a-f]{40}) remote ([0-9a-f]{40})$', text or '') if m.group(1) == tag]
    if len(made) != 1 or len(peel) != 1:
        return None, 'the tag`s making read %d times, its peel %d, not once each' % (len(made), len(peel))
    if not (made[0].group(2) == peel[0].group(2) == peel[0].group(3)):
        return None, 'the peel local %s, remote %s, the read-back %s, not equal' % (peel[0].group(2)[:8], peel[0].group(3)[:8], made[0].group(2)[:8])
    return made[0].group(2), made[0].group(3)


def break_read(rd, sha):
    """(module, line, where) of the break: the first error line naming a .lean file and line, else the print's failed import."""
    for l in (rd.get('errors') or []):
        m = re.search(r'([\w./-]+\.lean):(\d+):\d+', l)
        if m:
            path = re.sub(r'^(\./)+', '', m.group(1))
            mod = J.module_of(path, J.libs_at(sha)) if sha else None
            mod = mod or path[:-5].replace('/', '.')
            return mod, int(m.group(2)), '%s :%s' % (mod, m.group(2))
    m = re.search(r"import (\S+) failed", rd.get('axioms_print') or '')
    if m:
        return m.group(1), None, 'the print`s import of %s' % m.group(1)
    return None, None, None


def cut():
    """{key: (sentence or None, its fields)} for (5)'s three sentences, cut from the ferry bank's clause (5) at run time."""
    _ln, text = clause(CLAUSE)
    return dict((k, (quoted_after(text, w), fields_of(quoted_after(text, w)))) for k, w, _f in SENTENCES)


def item():
    ln, _text = clause(CLAUSE)
    sents = cut()
    out = ['## (5) THE STATEMENT AND THE PRINT LINES (the ferry bank :%d; the three sentences cut from it at run time: %s)' % (
        ln, ' ; '.join('%s %d characters, its fields %s' % (k, len(sents[k][0] or ''), list(sents[k][1])) for k, _w, _f in SENTENCES))]
    rec = dict(item=DITEM, clause_line=ln, outcome='NOT READ', sentence=None, runs=[])
    if any(sents[k][0] is None or sents[k][1] != f for k, _w, f in SENTENCES):
        out.append('  ### A SENTENCE NOT CUT ONCE OR ITS FIELDS NOT AS READ -- nothing composed')
        return out, rec
    R = json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []
    disp = [r for r in R if r.get('kind') == 'dispatch' and r.get('kernel') == EFKEY and r.get('item') == DITEM]
    if not disp:
        out.append('  ### NO DISPATCH OF ITEM %s ROWED -- nothing composed' % DITEM)
        return out, rec
    refused = presend_refused()
    out.append('  the filter`s refusals, by name (data/b759_presend.txt): %s' % ', '.join(refused))
    runs = []
    for d in disp:
        rds = [r for r in R if r.get('kind') == 'read' and r.get('kernel') == EFKEY and int(r.get('run', 0)) == int(d['run'])]
        out.append('  the dispatch: %d of item %s, run %s at %s (data/b759_dispatch_rows.json)' % (d['n'], DITEM, d['run'], d['sha'][:8]))
        if not rds:
            out.append('    THE RUN %s NOT READ' % d['run'])
            continue
        rd = rds[-1]
        art = C._art('ef', d['run'])
        ax, targets = C.axioms_of(C._f(art, 'axioms.txt')), C._targets(art)
        st, sh, fr = state_of(rd, ax, targets, refused)
        out.append('    THE RUN %s READ: exit file %s ; built %s, equal to the dispatched %s ; errors %d ; the print %s ; targets %s ; axioms lines %s, '
                   'within %s ; without a line %s ; sorryAx %s ; runner low %s MB' % (
                       d['run'], rd.get('build_exit'), (rd.get('built_ref') or '')[:8], rd.get('built_equal'), len(rd.get('errors') or []),
                       rd.get('axioms_print'), rd.get('targets'), rd.get('axiom_lines'), rd.get('axiom_within'), rd.get('axiom_missing_n'),
                       rd.get('sorryAx'), rd.get('runner_low_mb')))
        for w, ok in sh:
            out.append('      %s: %s' % (w, 'SHOWN' if ok else 'NOT SHOWN'))
        for s, a, w in fr:
            out.append('      the new name %s: %s -> %s' % (s, '[%s]' % ', '.join(a) if a is not None else 'NO PRINTED LINE%s' % (
                '' if s in targets else ', NOT AMONG THE RUN`S TARGETS'), 'WITHIN THE STANDARD THREE' if w else 'NOT SHOWN'))
        out.append('      THE RUN`S STATE: %s' % st)
        runs.append(dict(n=d['n'], run=int(d['run']), sha=d['sha'], state=st, axiom_lines=rd.get('axiom_lines'), weil_target=WEIL in targets,
                         five=[dict(name=s, axioms=list(a) if a is not None else None, within=w) for s, a, w in fr],
                         where=break_read(rd, d['sha'])[2] if st == 'BROKE' else None))
    rec['runs'] = runs
    if not runs:
        out.append('  THE OUTCOME: NOT READ')
        return out, rec
    cap = os.path.join(D, '%s_%s_%s_push_out.txt' % (ACT, EFKEY, BRANCH))
    good = [r for r in runs if r['state'] in ('ALL', 'FOUR')]
    if good:
        g = good[-1]
        peel, why = tag_read(_rd(cap), TAG)
        out.append('  THE LANDING (%s, %s): %s' % (os.path.relpath(cap, RELAY).replace('\\', '/'), TAG,
                                                    'made at main`s read-back %s, its peel read back equal at the remote' % peel if peel else 'NOT YET: %s' % why))
        if g['state'] == 'ALL':
            import b759_presend as PS
            sl, spass = PS.salt_at(g['sha'])
            out += ['  THE COMPILED STATEMENT READ AGAINST (5) AT THE BUILT COMMIT %s (tools/b759_presend.py`s salt check):' % g['sha'][:8]] + [
                '  ' + x for x in sl[1:]] + ['  THE GRADE: %s' % ('DERIVES, binding no premise' if spass else 'NOT WRITTEN: the compiled statement is not (5)`s')]
            rec.update(statement_as_ordered=spass, grade='DERIVES' if spass else None)
            seq = [('peel', (peel or '')[:8]), ('run id', g['run']), ('n', g['axiom_lines'])]
            key = 'COMPILED'
        else:
            bad = [r for r in runs if r['state'] == 'BROKE' and r['weil_target'] and r['n'] < g['n']]
            b = bad[-1] if bad else None
            seq = [('where', b['where'] if b else ''), ('run id', b['run'] if b else ''), ('peel', (peel or '')[:8]), ('run id', g['run'])]
            key = 'NOT COMPILED'
        rec.update(run=g['run'], sha=g['sha'], tag=TAG)
        if peel:
            s, left = fill(sents[key][0], seq)
            rec.update(outcome='LANDED, %s' % key, sentence=s, unfilled=left, peel=peel, tag_object=why, fields=seq)
        else:
            rec.update(outcome='SHOWN, %s' % key)
    else:
        last = runs[-1]
        seq = [('where', last['where'] or ''), ('run id', last['run'])]
        s, left = fill(sents['NOTHING LANDED'][0], seq)
        rec.update(outcome='NOTHING LANDED' if s else 'BROKE, WHERE NOT READ', sentence=s, unfilled=left, fields=seq, run=last['run'])
        if not s:
            out.append('  ### WHERE IT BROKE NOT READ FROM THE ROW -- no sentence composed')
    out.append('  THE OUTCOME: %s' % rec['outcome'])
    out.append('  THE SENTENCE: %s' % (rec.get('sentence') or 'NONE'))
    out.append('  fields left unfilled: %s' % (rec.get('unfilled') if rec.get('unfilled') is not None else '-'))
    return out, rec


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    cs = cut()
    got_c = [(k, cs[k][1] == f) for k, _w, f in SENTENCES]
    c('(5)`s three sentences cut once each from the ferry bank, their fields as read', got_c, all(x for _k, x in got_c))
    ref = presend_refused()
    c('(ii)`s refused by name from the pre-send bank', ref, len(ref) == 2 and all('Λ' in x for x in ref))
    good = dict(build_exit='0', built_equal=True, stop=[], errors=[], axioms_print='RAN', axiom_lines=417, axiom_within=417, axiom_outside={},
                axiom_missing=list(ref), axiom_missing_n=2, axioms_refused=NL.join('refused: %s' % x for x in ref), sorryAx=False)
    plants = [dict(good, sorryAx=True), dict(good, build_exit='1'), dict(good, axiom_missing=ref + ['X.y'], axiom_missing_n=3),
              dict(good, axioms_refused='refused: %s' % ref[0]), dict(good, axiom_within=416, axiom_outside={'X.z': ['sorryAx']}),
              dict(good, axioms_print='RAN WITH ERRORS (1 error lines, the first: x)')]
    got = [all(o for _w, o in shown(p, ref)) for p in plants]
    c('a planted row showing all of (4)`s list taken; six planted rows each failing one item refused', (all(o for _w, o in shown(good, ref)), got),
      all(o for _w, o in shown(good, ref)) and not any(got))
    ax = dict((s, STANDARD) for s in FIVE)
    less = dict((k, v) for k, v in ax.items() if k != FIVE[2])
    fv = [all(w for *_x, w in five_read(ax)), all(w for *_x, w in five_read(dict(ax, **{FIVE[1]: ('propext', 'sorryAx')}))),
          all(w for *_x, w in five_read(less)), all(w for *_x, w in five_read(dict(less, **{'X.' + FIVE[2]: STANDARD})))]
    c('the five new names on a planted print within the standard three taken; one with sorryAx, one absent, one printed under another prefix '
      'refused', fv, fv == [True, False, False, False])
    nw = dict((k, v) for k, v in ax.items() if k != WEIL)
    st = [state_of(good, ax, ['a', WEIL], ref)[0], state_of(good, nw, ['a'], ref)[0], state_of(good, nw, ['a', WEIL], ref)[0],
          state_of(dict(good, build_exit='1'), ax, ['a', WEIL], ref)[0], state_of(good, dict(nw, **{WEIL: ('propext', 'sorryAx')}), ['a', WEIL], ref)[0]]
    c('the run`s state on planted rows: ALL ; FOUR (the theorem not among the targets) ; BROKE (among them, no line) ; BROKE (the exit file 1) ; '
      'BROKE (the theorem`s line naming sorryAx)', st, st == ['ALL', 'FOUR', 'BROKE', 'BROKE', 'BROKE'])
    a, b = 'a' * 40, 'b' * 40
    cap = 'push_gated: tag v0.41 made at the read-back %s (%s)\npush_gated: tag v0.41 peeled local %s remote %s\n' % (a, b, a, a)
    t1, t2 = tag_read(cap, 'v0.41'), tag_read(cap.replace('remote %s' % a, 'remote %s' % b), 'v0.41')
    c('the tag read from a planted capture, equal peels taken, a remote peel differing refused, another tag`s lines not read',
      (t1[0][:4] if t1[0] else t1[1], t2[0], tag_read(cap, 'v0.40')[0]), t1 == (a, b) and t2[0] is None and tag_read(cap, 'v0.40')[0] is None)
    br = break_read(dict(errors=['error: ././SIDEExplicitFormula/Schema/ZQ/OffZero/Time.lean:18:4: unknown identifier']), None)
    c('the break read from a planted error line', br, br[:2] == ('SIDEExplicitFormula.Schema.ZQ.OffZero.Time', 18))
    f1 = fill('a <where> run <run id>; b <peel> (run <run id>)', [('where', 'M :3'), ('run id', 1), ('peel', '1234abcd'), ('run id', 2)])
    f2, f3 = fill('x <peel>', [('peel', '<peel>')]), fill('x <peel>', [('peel', 'a'), ('peel', 'b')])
    c('a fill in order, two run ids each its own, taken; a value carrying a field mark refused; a field filled twice refused', (f1, f2[0], f3[0]),
      f1 == ('a M :3 run 1; b 1234abcd (run 2)', []) and f2[0] is None and f3[0] is None)
    return L, ok


def cmd_bank():
    L, ok = controls()
    if not all(ok):
        print(NL.join(L))
        sys.exit('### THE CONTROLS NOT AS WANTED -- nothing written')
    out = ['%s -- (R369)(5): THE RESULT`S SENTENCE, THE RULING`S TEXT WITH ITS FIELDS FILLED FROM THE ACT`S BANKS (%s, tools/b759_outcomes.py bank)' % (ACT, _now()),
           '', '## THE CONTROLS'] + L + ['']
    o, r0 = item()
    out += o + ['']
    recs = [r0]
    out.append('### ### **THE OUTCOME OF (5): %s ; RUNS READ %d ; CONTROLS %d OF %d.**' % (r0['outcome'], len(r0.get('runs') or []), sum(ok), len(ok)))
    r = FB.write(BANK, NL.join(out))
    with open(BANKJ + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(recs, indent=1, ensure_ascii=False) + NL)
    os.replace(BANKJ + '.tmp', BANKJ)
    print(NL.join(out))
    print('written data/b759_outcomes.txt and data/b759_outcomes.json ; figbank: %s' % r['why'])


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
