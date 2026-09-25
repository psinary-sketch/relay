# -*- coding: utf-8 -*-
"""b524_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b524_record.py components | desk | trail`
### Every figure READ from the banks, not retyped; the scores are READING (9)'s; the step (9) note quotes b522`s and b523`s
### trail records VERBATIM, each line of the quotation a line of the trail as it stands (READING (8)).
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
NS = 'SIDEExplicitFormula.B321.'
ALLOWED_I = {'cosWin_contDiff', 'window_contDiff', 'windowC_contDiff', 'cosWin_hasCompactSupport', 'window_hasCompactSupport',
             'windowC_hasCompactSupport'}
MODULE_THMS = ['plateau_contDiff', 'plateau_even', 'plateau_hasCompactSupport', 'plateau_eq_one', 'cosWin_contDiff',
               'cosWin_hasCompactSupport', 'window_contDiff', 'window_hasCompactSupport', 'windowC_contDiff',
               'windowC_hasCompactSupport', 'weilTest_ofReal_even', 'kWin_classK', 'hasDerivAt_expIz', 'ibp_step',
               'paperFT_second_order', 'paperFT_window', 'paperFT_window_zero']
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


AT = json.loads(read('b524_attempts.json') or '[]')
PR = json.loads(read('b524_profile.json') or '{}')
RD = json.loads(read('b524_read.json') or '{}')
DEFS = read('b524_definitions.txt')
w = lambda v: 'HELD' if v else 'REFUTED'


def first_clean():
    ok = [a['attempt'] for a in AT if a['exit'] == 0 and a['errors'] == 0 and not a['sorry']]
    return ok[0] if ok else None


def body_of(name):
    m = re.search(r'^theorem %s\b[\s\S]*?(?=\n\n|\Z)' % re.escape(name), DEFS, re.M)
    return m.group(0) if m else ''


def scores():
    fc = first_clean()
    std = PR.get('std3', {})
    refs_i = {n for n in MODULE_THMS if n != 'kWin_classK' and re.search(r'\b%s\b' % n, body_of('kWin_classK').split(':=', 1)[-1])}
    # ### b524`s defect: the profile`s #check capture ran on into the #print lines (no blank line between them), so
    # ### the #check is read as its FIRST LINE alone.
    cp, pg = (PR.get('check_prop') or '').split(NL)[0], PR.get('print_growth') or ''
    return dict(
        first_clean=fc, refs_i=sorted(refs_i),
        n1=fc is not None and fc <= 2 and std.get(NS + 'paperFT_window') is True and std.get(NS + 'paperFT_window_zero') is True,
        n2=bool(body_of('kWin_classK')) and refs_i <= ALLOWED_I,
        n3=bool(RD) and RD.get('lemmas_beyond_b513') == [],
        n4=cp.rstrip().endswith('Prop') and '∫' in pg and 'Real.exp' not in pg,
        s1=fc is not None and fc <= 4 and bool(std) and all(std.values()),
        s2=not (bool(body_of('kWin_classK')) and refs_i <= ALLOWED_I),
        s3=not (bool(RD) and RD.get('lemmas_beyond_b513') == []))


def grades():
    std = PR.get('std3', {})
    out = {}
    for tag, name in (('(i)', 'kWin_classK'), ('(ii)', 'paperFT_window_zero'), ('(iii)', 'paperFT_window')):
        out[tag] = dict(name=name, grade=('DERIVES' if std.get(NS + name) is True else 'NOT COMPILED'))
    return out


def components():
    L = ['=' * 132, 'b524 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### THE INSTALL:', read('b524_install.json').rstrip(NL),
         '', '### ATTEMPT 0 -- STOPPED BY HOST ((R134)(2): not an attempt; no verdict from Lean):']
    L += ['    ' + l for l in read('b524_attempt0_stopped_by_host.txt').rstrip(NL).split(NL)]
    L += ['', '### THE ATTEMPTS (READING (4): each a whole-module run of lake env lean -o), numbered from the foreground run:']
    for a in AT:
        L.append('  attempt %d : exit %d ; %d error lines ; %.1f s ; source sha %s' % (a['attempt'], a['exit'], a['errors'], a['seconds'], a['source_sha'][:16]))
        L += ['      ' + e for e in a['first_errors']]
    L += ['', '### THE STATEMENTS, FROM THE DECLARATION LINE TO ITS := :'] + read('b524_statement.txt').rstrip(NL).split(NL)
    L += ['', '### THE READ (vendored references):']
    for r in RD.get('refs', []):
        L.append('  %-36s -> %s' % (r['name'], ['%(keyword)s in %(file)s' % h for h in r['resolved']]))
    L.append('  ### vendored lemmas referenced : %s ; beyond b513`s : %s' % (RD.get('lemma_refs'), RD.get('lemmas_beyond_b513') or 'NONE'))
    L += ['', '### THE PROFILE (AxiomCheckWindow.lean):'] + ['  ' + l for l in PR.get('lines', [])]
    L += ['  ### whole-string standard three : %s' % PR.get('std3'), '  ### #check : %s' % PR.get('check_prop'),
          '  ### #print : %s' % PR.get('print_growth'), '', '### THE GRADES, BY STATEMENT-READ (READING (6)):']
    for k, v in grades().items():
        L.append('  %s %s : %s' % (k, v['name'], v['grade']))
    L += ['  f_pair_hypothesis : STATED, NOT PROVED -- no grade.', '=' * 132]
    io.open(os.path.join(D, 'b524_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:40]))


def desk():
    sc = scores()
    L = ['=' * 104, 'b524 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FOUR.', '-' * 104,
         '  **(N1)** ### **%s.** -- first clean attempt : %s (against 2) ; (ii) std3 %s ; (iii) std3 %s.'
         % (w(sc['n1']), sc['first_clean'], PR.get('std3', {}).get(NS + 'paperFT_window_zero'), PR.get('std3', {}).get(NS + 'paperFT_window')),
         '  **(N2)** ### **%s.** -- the module theorems (i)`s proof cites : %s (allowed: the window`s ContDiff and support lemmas).'
         % (w(sc['n2']), sc['refs_i']),
         '  **(N3)** ### **%s.** -- vendored lemmas beyond b513`s : %s.' % (w(sc['n3']), RD.get('lemmas_beyond_b513') or 'NONE'),
         '  **(N4)** ### **%s.** -- #check : %s ; #print shows the integral : %s.'
         % (w(sc['n4']), (PR.get('check_prop') or '').replace(NL, ' ')[:160], '∫' in (PR.get('print_growth') or '')),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- first clean attempt %s, every theorem std3 : %s.' % (w(sc['s1']), sc['first_clean'], PR.get('std3')),
         '  **(S2)** ### **%s.** -- (N2) refuted.' % w(sc['s2']),
         '  **(S3)** ### **%s.** -- (N3) refuted.' % w(sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(True), [sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in read('b524_defects.txt').rstrip(NL).split(NL) if l] or ['    NONE FOUND.']) + ['=' * 104]
    io.open(os.path.join(D, 'b524_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b524_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b524 — (f)(i) stated on variant (B) in the kernel; (R133) entered'


def para(ot, heading, start):
    """### the paragraph of the record under `heading` that begins with `start`, its lines exactly as they stand."""
    i = ot.index(heading)
    j = ot.index(start, i)
    k = ot.find(NL + NL, j)
    return ot[j:k].split(NL)


def xi_words(name='b524_ferry.txt'):
    f = read(name)
    i = f.index('"positive for xi')
    j = f.index('numerical."', i) + len('numerical."')
    return ' '.join(f[i:j].split())


def trail():
    sc = scores()
    ot = open(OT, encoding='utf-8').read()
    q22 = para(ot, '### b522 —', '**COMPONENT 1 — Q0 with variant (B) at p = 7**')
    q23 = para(ot, '### b523 —', '**COMPONENT 5 — ')
    g = grades()
    st = PR.get('std3', {})
    body = [
        '', HEADING, '',
        '**(R133) ratified.** (1) b523\'s numbers are entered. (2) **(R118)(1)\'s bar lifts with the caveat named**: a window is',
        'exhibited — variant (B), p = 7, γ₀ = 16.290216, widths 34 to 60 — at which Q0\'s h2_sign quantity is negative beyond',
        'its bound on a bank complete below 150, the tail above 150 majorized under σ_max and the proved count, two of the',
        'count\'s constants numerical on grids. (3) The witness is announced in (R127)(2)\'s words and no other: exhibited',
        'numerically at one ρ, on a function whose off-line zeros are banked; not a statement about RH or zeta; the object',
        'column unchanged. (4) (f)(iii)\'s two ingredients, read off the witness: a bound on the real parts of the zeros above',
        'the bank and a bound on their count — for ζ, the strip and `zetaZeroConfig_local_count`. (5) The kernel lane opened for',
        'this act and shuts at its close; the fold follows at span nine.',
        '',
        '**By this appended note, the monograph\'s step (9) Epstein sentence — PROSE, NO BANK at `OPEN_TRAILS.md:9270` (b495,',
        'under (R106)), UNSUPPORTED BY THE CONTROL AT WIDTH ≤ 14.1 by b509\'s note — gains its bank, b522 and b523, quoted from',
        'their records as they stand; the NO BANK note and b509\'s note stay:**',
        ''] + ['> ' + l for l in q22] + ['>'] + ['> ' + l for l in q23] + [
        '',
        '**(R133)(2)\'s form of words for the ξ ladder, as pasted (line breaks collapsed):** %s' % xi_words(),
        '**(R134) ratified, in this act:** (1) the form is CORRECTED on the seat\'s two flags — ξ\'s 46 widths were read at b520',
        'at ramp order 5 and Q0\'s negative cells at b522 at order 7; ξ\'s tail at b520 was 1.6e-8 to 6.7e-8 of the bound, so',
        'ξ\'s cells are VERIFIED-EST, not tail-led — and reads from this act on: %s **`W-ORD-XI-P7` is filed:** ξ re-read at'
        % xi_words('b524_ferry_R134.txt'),
        'order 7 on the same widths, so the comparison is at one window; trigger: the next opening of the numerical lane.',
        '(2) A host stop is not an attempt: b524\'s first launch, stopped by the host for low memory with no verdict from Lean, is',
        'attempt 0, STOPPED BY HOST (`relay/data/b524_attempt0_stopped_by_host.txt`). (3) b524 resumed in the foreground.',
        'Nothing in this record cites the ladder.',
        '',
        '**COMPONENT 1 — `SIDEExplicitFormula/TwoPropertyWindow.lean`.** The plateau is Mathlib\'s smooth bump, flat on',
        '[−(1−F)L, (1−F)L], support (−L, L), C^n for every n, even; the b519 values the named instance `b519Plateau a`. **Its',
        'ramp is the smooth bump, not the numerical instrument\'s B-spline**; (i)–(iii) are proved for every real φ that is C⁴',
        'and compactly supported, and so hold for either ramp. (i) `kWin_classK` — k = weilTest h h is in classK, its',
        'evenness by translation invariance (`weilTest_ofReal_even`); (ii) `paperFT_window_zero` — paperFT h γ₀ = 0;',
        '(iii) `paperFT_window` — paperFT h z = (γ₀² − z²) · paperFT (cos(γ₀·)φ) z, by parts twice on the whole line.',
        'First clean attempt: %s of %d. Profiles: (i) %s, (ii) %s, (iii) %s. Grades by statement-read: (i) %s, (ii) %s, (iii) %s.'
        % (sc['first_clean'], len(AT), st.get(NS + 'kWin_classK'), st.get(NS + 'paperFT_window_zero'), st.get(NS + 'paperFT_window'),
           g['(i)']['grade'], g['(ii)']['grade'], g['(iii)']['grade']),
        '',
        '**COMPONENT 2 — the hypothesis of (f)(ii), a Prop, stated and not proved:** `f_pair_hypothesis` — the pair\'s term',
        'at ρ₀ = β + iγ₀ at most −4·δ²·|slope|²·G², δ = β − ½, the slope −2γ₀·paperFT(cos(γ₀·)φ)(γ₀), and G =',
        '`realizedGrowth φ δ` = ∫φ(u)cosh(δu)du / ∫φ, the integral and not e^{δL}; the instance G = 1.3607 at a = 34 cited',
        'from b522 and b523 for the B-spline ramp.',
        '',
        '**COMPONENT 3 — the remaining (f) lemmas, by the fold\'s names:** (f)(ii) = (f2), the pair\'s term bounded;',
        '(f)(iii) = (f3), the remaining zeros bounded — its two ingredients the strip and `zetaZeroConfig_local_count`;',
        '(f)(iv) = (f4), the assembly. None is attempted.',
        '',
        '**(N1) %s · (N2) %s · (N3) %s · (N4) %s.** The seat\'s own: (S1) %s, (S2) %s, (S3) %s. **The kernel lane shuts at this'
        % (w(sc['n1']), w(sc['n2']), w(sc['n3']), w(sc['n4']), w(sc['s1']), w(sc['s2']), w(sc['s3'])),
        'act\'s close.** The kernel is not tagged; nothing at Zenodo written; nothing deposits; row U1 unedited; `h2` where the',
        'deposit left it; the four lists stay OPEN; the object column unchanged; nothing here is a statement about RH.',
        '']
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(NL.join(body).encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING),
               q22_lines=len(q22), q23_lines=len(q23))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b524_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
