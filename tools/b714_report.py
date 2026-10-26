"""b714 -- THE STANDING REPORT TOOL, (R324)(3): data/b714_report.txt (.json). A REPORT, NOT AN ARM.

Carried from b713's standing report (tools/b713_report.py) at step zero and its lines rewritten at Component 5 by the Write tool: b713's
lines (the -15 list, the predictions and onsets, the coefficients, the source pin, the faces head :8, the re-cut's additive check) and its
throughstone (the author's word at b713's root, on b713's banks) read banks this act does not write, and are not carried; the lines are
b714's: the lv port's tag (KERNEL), pair 7's rectangle (CERTIFIED), the merge in keystone form, the law, the residual, the Sonin price and the
pilot (REGISTERED), and what the act holds (HELD), the pilot in one line as the author's word (2) sets it.
Three routes:
  bank    (before the root) each line's figures recomputed from the act's banks, beside each its SOURCE -- the bank's path, the row cited by
          line and the bank's sha256 now -- the lines printed in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), a footing no line stands
          on printed as NONE; written through the membrane to data/b714_report.txt and data/b714_report.json. Nothing else is written.
  dry     the lines printed, nothing written.
  scores  (after the root) the scores line: all eight from data/b714_scores_close.json, each HELD or BROKEN, and the root line from
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
import b714_worklist as K          # noqa: E402

NL = '\n'
ACT = 'b714'
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
    import b714_record as REC
    f = REC._figs()
    keys, seats = {}, []
    # ------------------------------------------------------------------ KERNEL: THE LV PORT'S TAG ((R324)(3)(i))
    st = seat('%s_lv_tag.txt' % ACT, '### ### **%s TAKEN' % K.LV_TAG_RULED)
    peel = g(K.LV_DIR, 'rev-parse', '%s^{}' % K.LV_TAG).strip()
    keys['TAG'] = ('KERNEL -- THE LV PORT TAGGED %s: SIDE-lv-conservation port-b707 at %s (compiled by the runner at b712, no commit this act), '
                   'the tag annotated, its peel read back %s and read now %s (equal %s); the ruled name %s found taken already (defect (f)); no GitHub release (%s); main %s and the deposit '
                   'untouched. SOURCE %s.' % (K.LV_TAG, K.PORT_TIP[:8], f['tag_peel'], peel[:8], peel == K.PORT_TIP, K.LV_TAG_RULED, f['tag_release'],
                                              K.LV_MAIN[:8], st['text']))
    seats.append(st)
    # ------------------------------------------------------------------ CERTIFIED: PAIR 7'S RECTANGLE ((R324)(9))
    sr = seat('%s_rect.txt' % ACT, '### ### **CONTROLS')
    keys['RECT'] = ('CERTIFIED -- PAIR 7`S RECTANGLE %s, wholly in Re s > 1: %s by an argument-principle count, controls %s, %s s; a certified '
                    'count of one zero of the -15 Epstein zeta in the box, no sentence locating a zero of zeta or of an L-function. SOURCE %s.' % (
                        f['rect_box'], f['rect'], f['rect_ctl'], f['rect_s'], sr['text']))
    seats.append(sr)
    # ------------------------------------------------------------------ REGISTERED: THE MERGE IN KEYSTONE FORM ((R324)(3)(ii))
    sa = seat('%s_recut_additive.txt' % ACT, '### ### **ORIGINAL LINES')
    parents = g(PP, 'rev-list', '--parents', '-n', '1', K.C2_PP_MERGE).split()
    keys['MERGE'] = ('REGISTERED -- THE MERGE IN KEYSTONE FORM: %s merged into PLACE-papers main at %s (--no-ff, parents %s), the additive check '
                     'found %s, missing %s, in order %s; the branch kept until b715`s step zero. SOURCE %s.' % (
                         K.RECUT_BRANCH, f['merge'], ' '.join(p[:8] for p in parents[1:]) or '### NOT READ', f['add_found'], f['add_missing'],
                         f['add_order'], sa['text']))
    seats.append(sa)
    # ------------------------------------------------------------------ REGISTERED: THE LAW ((R324)(7))
    sl = seat('%s_law.txt' % ACT, '### ### **CONTROLS')
    keys['LAW'] = ('REGISTERED -- THE LAW READ AS %s: the refined law and the -15 tool`s F2 read side by side, controls %s; a reading of two banked '
                   'formulas, nothing computed anew. SOURCE %s.' % (f['law'], f['law_ctl'], sl['text']))
    seats.append(sl)
    # ------------------------------------------------------------------ REGISTERED: THE RESIDUAL ((R324)(8))
    se = seat('%s_residual.txt' % ACT, '### ### **TEN PAIRS')
    keys['RESID'] = ('REGISTERED -- THE RESIDUAL: the onsets against the predictions equal %s to one decimal, the residual %s to %s in n, positive at '
                     '%s; read from the banks, no onset computed. SOURCE %s.' % (f['res_eq'], f['res_lo'], f['res_hi'], f['res_pos'], se['text']))
    seats.append(se)
    # ------------------------------------------------------------------ REGISTERED: THE SONIN PRICE ((R324)(10))
    ss = seat('%s_sonin_price.txt' % ACT, '### ### **PRICED AS A RESTRICTION')
    keys['SONIN'] = ('REGISTERED -- THE SONIN FACE PRICED AS A RESTRICTION: %s modules, %s dispatches, %s hours; priced, not written. SOURCE %s.' % (
        f['son_modules'], f['son_disp'], f['son_hours'], ss['text']))
    seats.append(ss)
    # ------------------------------------------------------------------ REGISTERED: THE PILOT, IN ONE LINE (the author's word (2))
    sp = seat('%s_pilot.txt' % ACT, '### ### **CONTROLS')
    keys['PILOT'] = 'REGISTERED -- THE PILOT, IN ONE LINE: %s. SOURCE %s.' % (REC.pilot_line(), sp['text'])
    seats.append(sp)
    # ------------------------------------------------------------------ HELD
    sh = seat('%s_heads_draft.txt' % ACT, '### ### **EIGHTEEN SENTENCES')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished; the heads draft of (R324)(4) (%s sentences footed, KERNEL %s, HELD %s) %s; the word '
                    'on the pilot`s %s FOR THE AUTHOR hits banked for b715, not applied here; the SIDESystem finding (Silence_of_Foundations :212 '
                    'names SIDE-kernel and a typeclass, the declaration a structure at SIDEMeta/Meta/SIDESystem.lean :99 in SIDE-meta) carried to b715, '
                    'the row not edited; the %s names with NO PIN STATED carried to b715 by keystone, file and line. SOURCE %s.' % (
                        K.DRAFT, f['heads_n'], f['heads_kernel'], f['heads_held'],
                        ('written to main at %s on the author`s word' % f['heads_commit']) if f['heads_commit'] else
                        'HELD on the author`s word at the root`s prompt (relay data/b714_author_words.txt), not written to main, carried to b715 with the '
                        'question whether a head carries its footings inline or in a companion correspondence',
                        f['pil_for'], f['pil_nopin'], sh['text']))
    seats.append(sh)
    order = [('KERNEL', ['TAG']), ('CERTIFIED', ['RECT']), ('REGISTERED', ['MERGE', 'LAW', 'RESID', 'SONIN', 'PILOT']), ('HELD', ['HELD'])]
    out = []
    for ft, ks in order:
        out += [keys[k] for k in ks]
    return out, keys, seats, order


def bank():
    import act_membrane as MEM
    import b714_record as REC
    out, keys, seats, order = lines()
    bad = [s['bank'] for s in seats if not s['ok']]
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE STANDING REPORT, (R324)(3): THE LINES IN FOOTING ORDER, EACH RECOMPUTED FROM ITS BANKS (%s)' % (ACT, at), '',
         '### rows are the report`s lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), each line`s figures recomputed from the act`s',
         '### banks, its SOURCE the bank by path, row and sha256. A report, not an arm: no verdict reads it. The scores line is printed after the',
         '### root by `tools/b714_report.py scores`, and written nowhere.', '']
    L += ['  (%d) %s' % (i + 1, l) for i, l in enumerate(out)]
    L += ['', '### SOURCES NOT SEATED (a needle not found or a bank absent): %s' % (bad or 'NONE'),
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
        print('usage: b714_report.py bank | dry | scores')
        sys.exit(2)
    dict(bank=bank, dry=dry, scores=scores)[r]()
