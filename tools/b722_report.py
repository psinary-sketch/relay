"""b722 -- THE STANDING REPORT TOOL, (R332)(3): data/b722_report.txt (.json). A REPORT, NOT AN ARM.

Carried from b721's standing report (tools/b721_report.py) by diff and its lines rewritten at Component 8: b721's lines (the rebuild, the
table over h = 3, 4, 5, the C2 halt, the predictions, the offset, the frozen line) read banks this act does not write, and are not carried;
the lines are b722's: the axiom step diagnosed from b721's runs by their ids (KERNEL), -31 and -55, the fourteen fields and the C2 statement
(CERTIFIED -- Python-checked, not compiled, N3), the research instruments and their reproduction (REGISTERED), and the propagation notes,
the LLM line's drafts and the draft (HELD).
Three routes:
  bank    (before the root) each line's figures recomputed from the act's banks, beside each its SOURCE -- the bank's path, the row cited by
          line and the bank's sha256 now -- the lines printed in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), a footing no line stands
          on printed as NONE; written through the membrane to data/b722_report.txt and data/b722_report.json. Nothing else is written.
  dry     the lines printed, nothing written.
  scores  (after the root) the scores line: all eight from data/b722_scores_close.json, each HELD or BROKEN, and the root line from
          data/act_roots.txt; PRINTED ONLY -- no bank is written after the root (N4), and the membrane refuses one.
The tool decides nothing: no verdict is gated on its lines (no arm reads its exit code), and a line it cannot recompute prints as such.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
import b722_worklist as K          # noqa: E402

NL = '\n'
ACT = 'b722'
FOOTINGS = ('KERNEL', 'CERTIFIED', 'REGISTERED', 'HELD')
PP = K.PP
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace')


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace('\r', '') if os.path.exists(p) else ''


def jl(name):
    t = rd(name)
    return json.loads(t) if t else {}


def sha(name):
    p = os.path.join(D, name)
    return hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None


def line_of(name, needle):
    for i, l in enumerate(rd(name).split(NL), 1):
        if needle in l:
            return i
    return None


def seat(name, needle):
    """the line's SOURCE: the bank's path, the row cited by line (the first line carrying the needle), its sha256 now."""
    ln, now = line_of(name, needle), sha(name)
    return dict(bank='data/' + name, row=ln, sha256=now, ok=bool(now) and ln is not None,
                text='relay data/%s :%s ; sha256 %s' % (name, ln if ln is not None else '### NEEDLE NOT FOUND', (now or '### ABSENT')[:16]))


def lines():
    import b722_record as REC
    f = REC._figs()
    keys, seats = {}, []
    # ### b722's lines (Component 8, the Edit tool), each from the record tool's figures over b722's banks
    # ------------------------------------------------------------------ KERNEL: THE AXIOM STEP ((R332)(10)), b721's runs read by their ids
    # ------------------------------------------------------------------ (N1: no lean on the host, no dispatch)
    sk = seat('%s_axiom_diag.txt' % ACT, '**THE AXIOM STEP AT FIVE PINS')
    keys['AXIOM'] = ('KERNEL -- THE AXIOM STEP AT FIVE WAVE 1 PINS, diagnosed from b721`s runs read by their ids: targets absent at the pin %s, '
                     'the build target not covering the axiom file`s imports %s, the step not the pin`s own %s, other %s; each route priced, '
                     'nothing committed, pushed or dispatched; the repair b723`s. SOURCE %s.' % (
                         f['ax_absent'], f['ax_cover'], f['ax_notown'], f['ax_other'], sk['text']))
    seats.append(sk)
    # ------------------------------------------------------------------ CERTIFIED: -31 AND -55 ((R332)(3)); THE FOURTEEN ((R332)(4)); THE C2
    # ------------------------------------------------------------------ STATEMENT ((R332)(5)) -- Python-checked, not compiled (N3)
    sc = seat('%s_coeffs.txt' % ACT, '**n0(-31) = ')
    keys['COEFFS'] = ('CERTIFIED -- -31 AND -55 UNDER e8c3dff4: n0(-31) = %s, b = %s, H-C3-31 %s; n0(-55) = %s, b = %s, H-C4-55 %s; the controls '
                      'first, each row with its prime clause; exact, Python-checked, not compiled (N3). SOURCE %s.' % (
                          f['n31'], f['b31'], f['h31'], f['n55'], f['b55'], f['h55'], sc['text']))
    seats.append(sc)
    sw = seat('%s_walk.txt' % ACT, '**H-C2-WALK: ')
    keys['WALK'] = ('CERTIFIED -- THE FOURTEEN REMAINING CLASS-NUMBER-2 FIELDS UNDER H-C2-WALK (15cb6cc4): %s of 14 HELD, REFUTED %s, NOT '
                    'SCORABLE %s, the control row -15 %s; %s. SOURCE %s.' % (
                        f['walk_held'], f['walk_refuted'], f['walk_unscor'], f['walk_ctl'], f['walk_grade'][:300].rstrip('.'), sw['text']))
    seats.append(sw)
    s2 = seat('%s_c2_price.txt' % ACT, '**THE C2 STATEMENT: ')
    keys['C2'] = ('CERTIFIED -- THE C2 STATEMENT FOR LEAN: E0 %s (the scope beside it: %s); as written, true in Python at %s of %s; priced per '
                  'field, the certificate route under %s at %s of %s; nothing compiled, nothing dispatched. SOURCE %s.' % (
                      f['c2_grade'], f['c2_scope'], f['c2_true'], f['c2_of'], f['c2_bound'], f['c2_under'], f['c2_under_of'], s2['text']))
    seats.append(s2)
    # ------------------------------------------------------------------ REGISTERED: THE RESEARCH INSTRUMENTS ((R332)(6)) AND THEIR
    # ------------------------------------------------------------------ REPRODUCTION ((R332)(7))
    si = seat('%s_instruments.txt' % ACT, '**THE RULE`S OUTPUT: ')
    keys['INSTR'] = ('REGISTERED -- THE RESEARCH INSTRUMENTS BY RULE: %s entered at PLACE-papers INSTRUMENTS.md as I-%s to I-%s in b618`s form '
                     '(the population %s, reused %s; the navigator`s %s, %s in the output). SOURCE %s.' % (
                         f['ins_n'], f['ins_first'], f['ins_last'], f['ins_pop'], f['ins_reused'], f['ins_nav'], f['ins_nav_in'], si['text']))
    seats.append(si)
    sr = seat('%s_reproduce.txt' % ACT, '**ROWS ')
    keys['REPRO'] = ('REGISTERED -- THE REPRODUCTION (tools/research/reproduce.py): %s rows, REPRODUCES %s, DIFFERS %s (%s), NOT RUN %s (%s), '
                     'the planted wrong figures as wanted %s of %s. SOURCE %s.' % (
                         f['rp_rows'], f['rp_rep'], f['rp_diff'], ', '.join(f['rp_differs']) or 'none', f['rp_notrun'],
                         ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr'], sr['text']))
    seats.append(sr)
    # ------------------------------------------------------------------ HELD: THE PROPAGATION NOTES; THE DRAFTS; THE DRAFT
    sg = seat('%s_propagation.txt' % ACT, '**THE PROPAGATION READ: ')
    keys['PROP'] = ('HELD -- THE PROPAGATION READ (standing clauses v8 row (82)): %s objects, %s hits, %s reading wrong and %s dated; %s notes '
                    'landed at FINDINGS :%s, no line rewritten. SOURCE %s.' % (
                        f['pg_obj'], f['pg_hits'], f['pg_wrong'], f['pg_dated'], f['pg_notes'], f['pg_line'], sg['text']))
    seats.append(sg)
    sh = seat('%s_ferry.txt' % ACT, 'THE DRAFT stands at v5, HELD')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits; the LLM-contribution line`s %s drafts for the release sitting '
                    '(SAME %s, DIFFERS %s, ABSENT %s), in the relay alone, nothing edited. SOURCE %s.' % (
                        K.DRAFT, f['ll_drafts'], f['ll_same'], f['ll_differs'], f['ll_absent'], sh['text']))
    seats.append(sh)
    order = [('KERNEL', ['AXIOM']), ('CERTIFIED', ['COEFFS', 'WALK', 'C2']), ('REGISTERED', ['INSTR', 'REPRO']), ('HELD', ['PROP', 'HELD'])]
    out = []
    for ft, ks in order:
        out += [keys[k] for k in ks]
    return out, keys, seats, order


def bank():
    import act_membrane as MEM
    import b722_record as REC
    out, keys, seats, order = lines()
    bad = [s['bank'] for s in seats if not s['ok']]
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE STANDING REPORT, (R332)(3): THE LINES IN FOOTING ORDER, EACH RECOMPUTED FROM ITS BANKS (%s)' % (ACT, at), '',
         '### rows are the report`s lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), each line`s figures recomputed from the act`s',
         '### banks, its SOURCE the bank by path, row and sha256. A report, not an arm: no verdict reads it. The scores line is printed after the',
         '### root by `tools/b722_report.py scores`, and written nowhere.', '']
    L += ['  (%d) %s' % (i + 1, l) for i, l in enumerate(out)]
    L += ['', '### FOOTINGS NO LINE STANDS ON: %s' % (', '.join(ft for ft, ks in order if not ks) or 'NONE')
          + ' (KERNEL: on the runner only, each by its run id; no lean on the host, N1)']
    L += ['### SOURCES NOT SEATED (a needle not found or a bank absent): %s' % (bad or 'NONE'),
          '### ### **THE STANDING REPORT: %d LINES IN FOOTING ORDER ; SOURCES %d, SEATED %d ; THE SCORES LINE AFTER THE ROOT.**' % (
              len(out), len(seats), len(seats) - len(bad))]
    J = dict(at=at, lines=out, keys=keys, seats=seats, unseated=bad, footing=dict(order))
    for name, b in (('%s_report.txt' % ACT, (NL.join(L) + NL).encode('utf-8')),
                    ('%s_report.json' % ACT, (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        p = os.path.join(D, name)
        MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(b)
        os.replace(p + '.tmp', p)
    print(NL.join(L[6:]))


def dry():
    out, _k, seats, _o = lines()
    print(NL.join('  (%d) %s' % (i + 1, l) for i, l in enumerate(out)))
    print('### SOURCES NOT SEATED: %s' % ([s['bank'] for s in seats if not s['ok']] or 'NONE'))


def scores():
    sc = jl('%s_scores_close.json' % ACT)
    keys = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    word = dict(HELD='HELD', REFUTED='BROKEN')
    roots = [l for l in rd('act_roots.txt').split(NL) if l.startswith(ACT + ' ')]
    print('### THE ROOT: %s' % (roots[-1] if roots else '### NOT APPENDED -- the scores line waits on the root'))
    print('### THE SCORES (relay data/%s_scores_close.json, sha256 %s…): %s' % (ACT, (sha('%s_scores_close.json' % ACT) or '### ABSENT')[:16],
          ' ; '.join('%s %s' % (k, word.get((sc.get(k) or ['?'])[0], (sc.get(k) or ['?'])[0])) for k in keys)))
    print('### ### **SCORES %d OF %d HELD -- PRINTED AFTER THE ROOT, WRITTEN NOWHERE.**' % (sum(1 for k in keys if (sc.get(k) or [''])[0] == 'HELD'), len(keys)))


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('bank', 'dry', 'scores'):
        print('usage: b722_report.py bank | dry | scores')
        sys.exit(2)
    dict(bank=bank, dry=dry, scores=scores)[r]()
