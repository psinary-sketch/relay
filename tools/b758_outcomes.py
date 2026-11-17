# -*- coding: utf-8 -*-
"""tools/b758_outcomes.py -- (R368)(4) AND (5): EACH RESULT'S SENTENCE, THE RULING'S TEXT WITH ITS FIELDS FILLED FROM THE ACT'S BANKS AND
NOTHING ELSE. Written whole by the Write tool at b758's Component 5, in the form of tools/b757_outcomes.py (sentences cut from the ferry bank at
run time, no sentence typed here, each field printed with the bank it came from); committed before it runs; its one write the pair
data/b758_outcomes.txt and data/b758_outcomes.json, written whole at each `bank`.

WHAT EACH RUN MUST SHOW, as (4) gives it (data/b758_ferry.txt :15) and (5) takes it ("as (4)", :17): the exit file 0; the print running with 0
error lines; an axioms line within propext, Classical.choice and Quot.sound for each line of print_targets.txt the filter passes; the refused
lines equal to (ii)'s (data/b758_presend.txt, by name: :358 and :359, each carrying the Greek capital lambda); no line naming sorryAx. (5) adds:
among the printed lines zq_coeff_not_multiplicative, cQ_forty_eight, cQ_not_nonneg, wide_detector and zq_arith_side_re_neg, each within the
standard three. Read from the controls tool's read row (data/b758_dispatch_rows.json) and, for (5)'s five, the run's axioms file.

THE OUTCOME: SHOWN where the run shows all of it; LANDED where, besides, the gated push's capture
(data/b758_SIDE-explicit-formula_<branch>_push_out.txt) reads the tag made at main's read-back and its peel read back equal at the remote --
the sentence IF IT COMPILES then composed with that peel; BROKE where the run does not show it, the sentence IF IT DOES NOT composed with
where it broke (the first error line's file and line, or the print's failed import); NOT READ where no run is read.

  control       the tool's controls, printed
  bank          both items read and composed, the pair written
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
import b757_join as J            # noqa: E402  (the module namer, as committed at b757)
import b758_controls as C        # noqa: E402  (the read rows and the axioms reader)
import figbank as FB             # noqa: E402

NL = '\n'
ACT = 'b758'
FERRY = os.path.join(D, 'b758_ferry.txt')
PRESEND = os.path.join(D, 'b758_presend.txt')
ROWS = os.path.join(D, 'b758_dispatch_rows.json')
BANK = os.path.join(D, 'b758_outcomes.txt')
BANKJ = os.path.join(D, 'b758_outcomes.json')
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')
EFKEY = 'SIDE-explicit-formula'
FIVE = ('zq_coeff_not_multiplicative', 'cQ_forty_eight', 'cQ_not_nonneg', 'wide_detector', 'zq_arith_side_re_neg')
# ### item: (clause, dispatch item, branch, tag, the compiled marker, the failing marker, the compiled fields, the failing fields)
ITEMS = (('join', 4, 'join', 'push-b758-land', 'v0.39', 'THE SENTENCE IF IT COMPILES:', 'THE SENTENCE IF IT DOES NOT:',
          ('peel', 'run id', 'n'), ('module', 'line', 'run id')),
         ('coeff', 5, 'coeff', 'push-b758-coeff', 'v0.40', 'THE SENTENCE IF IT COMPILES, one for the three:', 'THE SENTENCE IF IT DOES NOT:',
          ('peel', 'run id'), ('where', 'run id')))


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


def fill(t, vals):
    out = t
    for k, v in vals.items():
        if '<' in str(v) or '>' in str(v) or not str(v).strip():
            return None, ['<%s>' % k]
        out = out.replace('<%s>' % k, str(v))
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


def five_read(ax):
    """[(name, the printed full name or None, axioms or None, within)] for (5)'s five, each by its last component, one printed line each."""
    out = []
    for s in FIVE:
        hit = [n for n in ax if n.split('.')[-1] == s]
        a = ax[hit[0]] if len(hit) == 1 else None
        out.append((s, hit[0] if len(hit) == 1 else None, a, a is not None and set(a) <= set(STANDARD) and 'sorryAx' not in a))
    return out


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


def item(key):
    _k, n, ditem, branch, tag, yes_w, no_w, yes_f, no_f = [x for x in ITEMS if x[0] == key][0]
    ln, text = clause(n)
    yes, no = quoted_after(text, yes_w), quoted_after(text, no_w)
    out = ['## (%d) %s (the ferry bank :%d; the sentences cut from it at run time: compiled %d characters, its fields %s ; failing %d characters, its fields %s)' % (
        n, 'THE JOIN LANDED' if key == 'join' else 'T0, T1 AND THE WIDE DIRECTION LANDED', ln, len(yes or ''), list(fields_of(yes)), len(no or ''), list(fields_of(no)))]
    rec = dict(item=key, clause_line=ln, outcome='NOT READ', sentence=None)
    if not yes or not no or fields_of(yes) != yes_f or fields_of(no) != no_f:
        out.append('  ### A SENTENCE NOT CUT ONCE OR ITS FIELDS NOT AS READ -- nothing composed')
        return out, rec
    R = json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []
    disp = [r for r in R if r.get('kind') == 'dispatch' and r.get('kernel') == EFKEY and r.get('item') == ditem]
    if not disp:
        out.append('  ### NO DISPATCH OF ITEM %s ROWED -- nothing composed' % ditem)
        return out, rec
    d = disp[-1]
    rds = [r for r in R if r.get('kind') == 'read' and r.get('kernel') == EFKEY and int(r.get('run', 0)) == int(d['run'])]
    out.append('  the dispatch: %d of item %s, run %s at %s (data/b758_dispatch_rows.json)' % (d['n'], ditem, d['run'], d['sha'][:8]))
    if not rds:
        out.append('  ### THE RUN %s NOT READ -- nothing composed' % d['run'])
        return out, rec
    rd = rds[-1]
    refused = presend_refused()
    sh = shown(rd, refused)
    out.append('  THE RUN %s READ: exit file %s ; built %s, equal to the dispatched %s ; errors %d ; the print %s ; targets %s ; axioms lines %s, within %s ; '
               'without a line %s ; sorryAx %s ; runner low %s MB' % (d['run'], rd.get('build_exit'), (rd.get('built_ref') or '')[:8], rd.get('built_equal'),
                                                                    len(rd.get('errors') or []), rd.get('axioms_print'), rd.get('targets'), rd.get('axiom_lines'),
                                                                    rd.get('axiom_within'), rd.get('axiom_missing_n'), rd.get('sorryAx'), rd.get('runner_low_mb')))
    out.append('  (ii)`s refused, by name (data/b758_presend.txt): %s' % ', '.join(refused))
    for w, ok in sh:
        out.append('    %s: %s' % (w, 'SHOWN' if ok else 'NOT SHOWN'))
    ok = all(o for _w, o in sh)
    if key == 'coeff':
        ax = C.axioms_of(C._f(C._art('ef', d['run']), 'axioms.txt'))
        fr = five_read(ax)
        for s, full, a, w in fr:
            out.append('    (5)`s %s: %s [%s] -> %s' % (s, full or 'NO PRINTED LINE', ', '.join(a or ()), 'WITHIN THE STANDARD THREE' if w else 'NOT SHOWN'))
        ok = ok and all(w for _s, _f, _a, w in fr)
        rec['five'] = [dict(name=s, full=full, axioms=list(a or ()), within=w) for s, full, a, w in fr]
    rec.update(run=int(d['run']), sha=d['sha'], shown=ok)
    if ok:
        cap = os.path.join(D, '%s_%s_%s_push_out.txt' % (ACT, EFKEY, branch))
        peel, why = tag_read(_rd(cap), tag)
        out.append('  THE LANDING (%s, %s): %s' % (os.path.relpath(cap, RELAY).replace('\\', '/'), tag,
                                                    'made at main`s read-back %s, its peel read back equal at the remote' % peel if peel else 'NOT YET: %s' % why))
        if peel:
            vals = {'peel': peel[:8], 'run id': d['run']}
            if key == 'join':
                vals['n'] = rd.get('axiom_lines')
            s, left = fill(yes, vals)
            rec.update(outcome='LANDED', sentence=s, unfilled=left, tag=tag, peel=peel, tag_object=why, fields=vals)
        else:
            rec.update(outcome='SHOWN')
    else:
        mod, line, where = break_read(rd, d['sha'])
        vals = {'module': mod, 'line': line, 'run id': d['run']} if key == 'join' else {'where': where, 'run id': d['run']}
        if all(v not in (None, '') for v in vals.values()):
            s, left = fill(no, vals)
            rec.update(outcome='BROKE', sentence=s, unfilled=left, fields=vals)
        else:
            rec.update(outcome='BROKE, WHERE NOT READ')
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

    cut = []
    for key, n, _d, _b, _t, yw, nw, yf, nf in ITEMS:
        _ln, text = clause(n)
        y, no = quoted_after(text, yw), quoted_after(text, nw)
        cut.append((key, fields_of(y) == yf, fields_of(no) == nf))
    c('the four sentences cut once each from the ferry bank, their fields as read', cut, all(a and b for _k, a, b in cut))
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
    ax = dict(('A.B.%s' % s, STANDARD) for s in FIVE)
    c('(5)`s five on a planted print within the standard three; one with sorryAx and one absent refused',
      [all(w for *_x, w in five_read(ax)), all(w for *_x, w in five_read(dict(ax, **{'A.B.cQ_not_nonneg': ('propext', 'sorryAx')}))),
       all(w for *_x, w in five_read(dict((k, v) for k, v in ax.items() if not k.endswith('wide_detector'))))],
      all(w for *_x, w in five_read(ax)) and not all(w for *_x, w in five_read(dict(ax, **{'A.B.cQ_not_nonneg': ('propext', 'sorryAx')})))
      and not all(w for *_x, w in five_read(dict((k, v) for k, v in ax.items() if not k.endswith('wide_detector')))))
    a, b = 'a' * 40, 'b' * 40
    cap = 'push_gated: tag v0.39 made at the read-back %s (%s)\npush_gated: tag v0.39 peeled local %s remote %s\n' % (a, b, a, a)
    t1, t2 = tag_read(cap, 'v0.39'), tag_read(cap.replace('remote %s' % a, 'remote %s' % b), 'v0.39')
    c('the tag read from a planted capture, equal peels taken, a remote peel differing refused, another tag`s lines not read',
      (t1[0][:4] if t1[0] else t1[1], t2[0], tag_read(cap, 'v0.40')[0]), t1 == (a, b) and t2[0] is None and tag_read(cap, 'v0.40')[0] is None)
    br = break_read(dict(errors=['error: ././SIDEExplicitFormula/Schema/ZQ/OffZero/Time.lean:18:4: unknown identifier']), None)
    c('the break read from a planted error line', br, br[:2] == ('SIDEExplicitFormula.Schema.ZQ.OffZero.Time', 18))
    f1, f2 = fill('x <peel> y <run id>', {'peel': '1234abcd', 'run id': 7}), fill('x <peel>', {'peel': '<peel>'})
    c('a fill leaving no field taken; a value carrying a field mark refused', (f1, f2), f1 == ('x 1234abcd y 7', []) and f2[0] is None)
    return L, ok


def cmd_bank():
    L, ok = controls()
    if not all(ok):
        print(NL.join(L))
        sys.exit('### THE CONTROLS NOT AS WANTED -- nothing written')
    out = ['%s -- (R368)(4) AND (5): EACH RESULT`S SENTENCE, THE RULING`S TEXT WITH ITS FIELDS FILLED FROM THE ACT`S BANKS (%s, tools/b758_outcomes.py bank)' % (ACT, _now()),
           '', '## THE CONTROLS'] + L + ['']
    recs = []
    for key in ('join', 'coeff'):
        o, r = item(key)
        out += o + ['']
        recs.append(r)
    out.append('### ### **THE OUTCOMES: JOIN %s ; THE THREE %s ; CONTROLS %d OF %d.**' % (recs[0]['outcome'], recs[1]['outcome'], sum(ok), len(ok)))
    r = FB.write(BANK, NL.join(out))
    with open(BANKJ + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(recs, indent=1, ensure_ascii=False) + NL)
    os.replace(BANKJ + '.tmp', BANKJ)
    print(NL.join(out))
    print('written data/b758_outcomes.txt and data/b758_outcomes.json ; figbank: %s' % r['why'])


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
