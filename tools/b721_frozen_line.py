# -*- coding: utf-8 -*-
"""b721_frozen_line.py -- (R331)(7)(i): THE FROZEN LINE'S STATEMENTS QUOTED AT THEIR PINS AND GRADED AT E0 AGAINST EVERY SENTENCE OF
EACH KERNEL'S README (read at its HEAD) AND ITS GITHUB DESCRIPTION (read by gh).

  python -X utf8 -u D:/relay/tools/b721_frozen_line.py ids          prints every README sentence with its id; grades nothing
  python -X utf8 -u D:/relay/tools/b721_frozen_line.py [bank]       the controls, the statements, their E0 grades, every sentence graded
                                                                    -> data/b721_frozen_line.txt

THE STATEMENTS ((R331)(7)(i)): archimedean_forces_half (SIDE-archimedean v0.1.0 = 8019d9d), indicial_forces_half (SIDE-frobenius
v0.1.0 = 2efe9f2), spinor_forces_half and half_iff_centered_zero (SIDE-spinor v0.1.0 = b235bc6), monotone_unique_zero (SIDE-rcurve
v0.1.0 = d5f33b4). Each read by `git show <pin>:<file>` from the kernel's clone on D:, its header to `:=` graded by relay tools/e0_rule.py
(grade, unedited). The README by `git show HEAD:README.md`, its equality to the pin's printed; the description by
`gh repo view psinary-sketch/<repo> --json description` (no identifier of the author in the request beyond gh's own authentication).
The sentence grades are the seat's reading, by hand, against the statements quoted (HAND below), in the vocabulary printed before them.
Writes only data/b721_frozen_line.txt. Written by the Write tool at b721.
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import e0_rule as E0   # noqa: E402  ### the shared rule, unedited

OUT = os.path.join(ROOT, 'data', 'b721_frozen_line.txt')
K = [dict(repo='SIDE-archimedean', tag='v0.1.0', pin='8019d9d', file='SIDEArchimedean/Reflection.lean', names=['archimedean_forces_half']),
     dict(repo='SIDE-frobenius', tag='v0.1.0', pin='2efe9f2', file='SIDEFrobenius/Indicial.lean', names=['indicial_forces_half']),
     dict(repo='SIDE-spinor', tag='v0.1.0', pin='b235bc6', file='SIDESpinor/Spinor.lean', names=['spinor_forces_half', 'half_iff_centered_zero']),
     dict(repo='SIDE-rcurve', tag='v0.1.0', pin='d5f33b4', file='SIDERCurve/Criterion.lean', names=['monotone_unique_zero'])]

VOCAB = [
    '### THE SENTENCE VOCABULARY, printed before any sentence is graded (the seat`s, for (R331)(7)(i); E0 grades the statements, these grade',
    '### the sentences against them):',
    '###   STATED   -- what the sentence asserts of the kernel is the content of a compiled statement at the pin: its binders and conclusion,',
    '###               names and glosses aside.',
    '###   EXCEEDS  -- the sentence asserts of the kernel more than any compiled statement`s binders and conclusion carry: an object the',
    '###               statements do not name (zeta, xi, RH, an eigenvalue, a functional equation), a consequence they do not draw, or a',
    '###               definition`s name read as its content.',
    '###   OUTSIDE  -- the sentence speaks of a document, path, deposit or result outside the kernel, not of what it compiles.',
    '###   SCOPE    -- a non-claim (what the kernel does not do or claim), consistent with the statements.',
    '###   NO CLAIM -- a heading, author line, build or toolchain line, licence or disclosure.',
]


def git(repo, *a):
    p = subprocess.run(['git', '-C', 'D:/' + repo] + list(a), capture_output=True, text=True, encoding='utf-8')
    return p.stdout


def header(src, name):
    """the declaration's text from `theorem <name>` to its `:=` (the statement), and its line."""
    lines = src.split(NL)
    hits = [i for i, l in enumerate(lines) if re.match(r'^\s*(theorem|lemma)\s+' + re.escape(name) + r'\b', l)]
    if len(hits) != 1:
        return None, None, len(hits)
    i = hits[0]
    buf = []
    for l in lines[i:]:
        buf.append(l)
        if ':=' in l:
            break
    txt = ' '.join(x.strip() for x in buf)
    txt = txt[:txt.index(':=')].strip()
    return txt, i + 1, 1


def sentences(readme):
    """every sentence: each non-empty line; a prose line split after '.', '!' or '?' before a capital, a backtick or an asterisk."""
    out = []
    for n, l in enumerate(readme.split(NL), 1):
        s = l.strip()
        if not s:
            continue
        parts = re.split(r'(?<=[.!?])\s+(?=[A-Z`*(])', s) if not s.startswith('#') else [s]
        merged = []
        for p in parts:                       # ### an initial ("J.") is not a sentence: joined to what follows
            if merged and re.match(r'^[A-Z]\.$', merged[-1]):
                merged[-1] = merged[-1] + ' ' + p
            else:
                merged.append(p)
        for j, p in enumerate(merged, 1):
            out.append(('%d.%d' % (n, j), p))
    return out


def no_claim(s):
    """the rule's NO CLAIM lines, by form: a heading, the author line (orcid), a lake command, the toolchain line, the licence, the
    disclosure."""
    return bool(s.startswith('#') or 'orcid.org' in s or (s.startswith('lake ') and ' # ' not in s) or s.startswith('Toolchain ') or s == 'MIT.'
                or s.startswith('*Computational workflow') or s.startswith('Mathematical content, proof strategies'))


AUTHOR = lambda s: 'orcid.org' in s   # noqa: E731  ### the author line is graded, not quoted: the relay is public

S_ = 'STATED'
X_ = 'EXCEEDS'
O_ = 'OUTSIDE'
C_ = 'SCOPE'
IDK = 'the identification kernels` common lead-in'
HAND = {
    'SIDE-archimedean': {
        '3.1': (X_, 'names a sqrt / theta structure no statement compiles; the statements are rational arithmetic in sigma : Q'),
        '9.1': (O_, 'the path, outside the kernel'),
        '9.2': (X_, 'calls the compiled arithmetic the algebraic core of the theta/FE path; that relation is asserted, not compiled'),
        '11.1': (X_, 'theta_weight is the definition 1/2 and the theorem 2 * (1/2) = 1; theta(-1/tau), sqrt(-i tau) and an FE period are the '
                     'definition`s name read as content'),
        '12.1': (S_, 'fe_reflect_fixed_iff: (1 - sigma = sigma) iff sigma = 1/2 over Q; "functional-equation" a name'),
        '13.1': (X_, 'focus_codim is defined as 1 at sigma = 1/2 and 2 elsewhere; no zero, no codimension, no xi is compiled'),
        '14.1': (S_, 'archimedean_identifies_half: the two defined conditions coincide, as the definitions make them'),
        '15.1': (X_, 'the statement: sigma : Q, 1 - sigma = sigma gives sigma = 1/2; no FE structure enters it'),
        '19.1': (O_, 'a status comparison with other kernels'),
        '19.2': (X_, 'no Archimedean machinery (theta, FE) is compiled; the fixed point of sigma -> 1 - sigma is'),
        '19.3': (C_, 'a non-claim, consistent'),
        '23.1': (O_, 'the census'), '23.2': (O_, 'federation metadata'), '23.3': (O_, 'the Mathlib pin, build metadata'),
    },
    'SIDE-frobenius': {
        '3.1': (S_, 'the indicial polynomial`s double root and g(2,3) are compiled; indicial_forces_half concludes -r = 1/2'),
        '9.1': (O_, 'the path, outside the kernel'),
        '9.2': (S_, 'the listed algebra is compiled; its derivation from H = xp is not (the polynomial enters as a polynomial)'),
        '11.1': (S_, 'indicial_factor and indicial_root_unique, as stated'),
        '12.1': (S_, 'indicial_reflect_fixed_iff, and indicial_forces_half: r^2 + r + 1/4 = 0 gives -r = 1/2'),
        '13.1': (S_, 'g_two_three and g_two_three_minimal, as stated'),
        '14.1': (S_, 'S_squared and ST_cubed over integer matrices; PSL2 a gloss'),
        '18.1': (O_, 'a status comparison with other kernels'),
        '18.2': (S_, 'the indicial algebra compiled concludes -r = 1/2'),
        '18.3': (C_, 'a non-claim, consistent'),
        '22.1': (O_, 'the census'), '22.2': (O_, 'federation metadata'), '22.3': (O_, 'the Mathlib pin and the tactics, build metadata'),
        '27.1': (O_, 'an axiom print, not read here (no lean on the host); (7)(iii)`s rebuild runs AxiomCheck.lean'),
    },
    'SIDE-spinor': {
        '3.1': (X_, 'no spinor or information object is compiled; the statements are Complex.I * w = w gives w = 0, and sigma = 1/2 iff '
                    'sigma - 1/2 = 0'),
        '9.1': (O_, 'the path, outside the kernel'),
        '9.2': (X_, 'calls the compiled facts the algebraic core of the M = vv-dagger path; M is not compiled'),
        '11.1': (X_, 'spectral_volume: a list [3,2,1,0,1,2,3] sums to 12; no v, no norm, no M, no eigenvalue is compiled'),
        '12.1': (S_, 'aperture_decomp and aperture: the defined 1 + 6 = 7 and 1/7'),
        '13.1': (X_, 'phase_unit: normSq I = 1 is compiled; the invariance of M = vv-dagger it is said to make is not'),
        '14.1': (S_, 'spinor_sq and spinor_order_four: I^2 = -1, I^4 = 1 in C; "T", "720-degree" glosses'),
        '15.1': (X_, 'orbit_collapse_iff: I * w = w iff w = 0 is compiled; "w = s - 1/2 ... this is sigma = 1/2" is not: no s appears, and '
                     'w = 0 for complex w would fix t as well as sigma'),
        '16.1': (S_, 'half_iff_centered_zero, as stated (a real sigma, no hypothesis)'),
        '20.1': (O_, 'a status comparison with other kernels'),
        '20.2': (X_, 'the orbit collapse is compiled at w = 0; its link to sigma is not (half_iff_centered_zero binds an unrelated real)'),
        '20.3': (C_, 'a non-claim, consistent'),
        '24.1': (O_, 'the census'), '24.2': (O_, 'federation metadata'), '24.3': (O_, 'the Mathlib pin, build metadata'),
    },
    'SIDE-rcurve': {
        '3.1': (X_, 'no equivalence is compiled; the statements are lemmas on a strictly monotone real function and real algebra'),
        '9.1': (X_, 'no RH, no R-curve, no xi and no equivalence is compiled; "proven" is a status outside the kernel'),
        '11.1': (X_, 'monotone_unique_zero: a strictly monotone V vanishes at most once, compiled; "(ii) implies (i)" and "a second '
                     '(off-line) zero is impossible" are not'),
        '12.1': (X_, 'monotonicity_formula: alpha^2/beta + beta = (alpha^2 + beta^2)/beta for beta != 0; V`, xi` and |xi`|^2/beta are not compiled'),
        '13.1': (S_, 'beta_V_re: Re((alpha + beta i)/(V i)) = beta/V for V != 0; "xi`/xi", "xi = iV" names'),
        '14.1': (X_, 'singular_repulsion: 0 < n, 0 < beta give 0 < n/beta; the repulsion of an R-curve is not compiled'),
        '15.1': (X_, 'zero_codim is defined as 1 or 2 by a Bool; the codimension of a zero is the definition`s name read as content'),
        '19.1': (O_, 'a closure status of an analytic positivity, outside the kernel'),
        '19.2': (O_, 'a theorem of another document'),
        '19.3': (X_, '"this kernel verifies the equivalence machinery": no equivalence is compiled (the deposit named is outside)'),
        '19.4': (O_, 'a document`s framing'),
        '23.1': (C_, 'a non-claim, consistent'),
        '23.2': (X_, 'no RH and no geometric criterion is compiled; nothing connects them in the kernel'),
        '27.1': (O_, 'the census'), '27.2': (O_, 'federation metadata'), '27.3': (O_, 'the Mathlib pin, build metadata'),
    },
}
E0_NOTE = {
    'monotone_unique_zero': 'StrictMono V restricts V, a variable the statement binds universally ({V : R -> R}); under (R235)(2)(iii) '
                            '(a restriction on a universally quantified variable: support, parity, smoothness, continuity, ...) it '
                            'would read as a domain condition and the statement DERIVES, but StrictMono is not among the rule`s listed '
                            'restrictions, and the rule returns INTERFACES. The divergence is printed for the author; the rule`s grade stands.',
}
DESC = {
    'SIDE-archimedean': (X_, 'as README 3.1: a sqrt / theta structure no statement compiles'),
    'SIDE-frobenius': (S_, 'as README 3.1: the indicial algebra and {2,3} compiled'),
    'SIDE-spinor': (X_, 'as README 3.1: no spinor or information object compiled'),
    'SIDE-rcurve': (X_, 'as README 3.1: no equivalence and no sigma = 1/2 criterion compiled'),
}


def gh_desc(repo):
    p = subprocess.run(['gh', 'repo', 'view', 'psinary-sketch/' + repo, '--json', 'description'], capture_output=True, text=True,
                       encoding='utf-8')
    if p.returncode != 0:
        return None, p.stderr.strip()[:200]
    return json.loads(p.stdout).get('description'), ''


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def run():
    t0 = time.time()
    L = ['b721 -- (R331)(7)(i): THE FROZEN LINE`S STATEMENTS QUOTED AT THEIR PINS, GRADED AT E0, AND EVERY README SENTENCE AND GITHUB',
         'DESCRIPTION GRADED AGAINST THEM (%s)' % utc(), '']
    L += [l for l in E0.RULE_TEXT[:6]] + ['### (the rule in full: relay tools/e0_rule.py RULE_TEXT, unedited)', ''] + VOCAB + ['']
    ok = True
    st = E0.self_test()
    pl = E0.grade('(h : RiemannHypothesis) (s : ℂ) : s.re = 1 / 2', 'theorem')[0]
    L += ['## THE CONTROLS, BEFORE ANY STATEMENT',
          '  (C1) E0`s own self-test (e0_rule.self_test, both polarities): %s' % ('PASSES -- AS WANTED' if st else '### FAILS'),
          '  (C2) PLANT: a header with a premise binder (h : RiemannHypothesis) grades %s -- %s' % (
              pl, 'INTERFACES, AS WANTED' if pl == 'INTERFACES' else '### NOT AS WANTED')]
    ok = ok and st and pl == 'INTERFACES'
    neg = header(git('SIDE-frobenius', 'show', '2efe9f2:SIDEFrobenius/Indicial.lean'), 'archimedean_forces_half')[2]
    L.append('  (C3) NEG: archimedean_forces_half sought in SIDE-frobenius`s Indicial.lean at 2efe9f2: yield %d -- %s' % (
        neg, 'ABSENT, AS WANTED' if neg == 0 else '### NOT AS WANTED'))
    ok = ok and neg == 0
    L.append('')
    counts = {}
    for k in K:
        full = git(k['repo'], 'rev-parse', k['pin']).strip()
        tags = git(k['repo'], 'tag', '--points-at', k['pin']).split()
        src = git(k['repo'], 'show', '%s:%s' % (k['pin'], k['file']))
        L.append('## %s at %s = %s (%s; tags at the pin %s), %s' % (k['repo'], k['tag'], k['pin'], full[:12], tags, k['file']))
        decl = {}
        for n in k['names']:
            h, ln, y = header(src, n)
            if y != 1:
                L.append('  ### %s: yield %d at the pin -- STOPPED' % (n, y))
                ok = False
                continue
            g, why, _r = E0.grade(h[h.index(n) + len(n):], 'theorem')
            L += ['  THE STATEMENT, %s :%d (yield 1):' % (k['file'], ln), '    %s' % h,
                  '    E0: %s -- %s' % (g, why)]
            if n in E0_NOTE:
                L.append('    BESIDE IT, THE SEAT`S READING (not a grade; e0_rule.py not edited): ' + E0_NOTE[n])
            decl[n] = g
        rd = git(k['repo'], 'show', 'HEAD:README.md')
        rp = git(k['repo'], 'show', '%s:README.md' % k['pin'])
        head = git(k['repo'], 'rev-parse', '--short', 'HEAD').strip()
        L.append('  THE README at HEAD %s (%d lines; equal to the pin`s: %s), every sentence:' % (head, len(rd.split(NL)), rd == rp))
        hand = HAND[k['repo']]
        seen = set()
        for sid, s in sentences(rd):
            if no_claim(s):
                g, why = 'NO CLAIM', 'by form'
            elif sid in hand:
                g, why = hand[sid]
                seen.add(sid)
            else:
                g, why = '### UNGRADED', 'no hand grade for this sentence'
                ok = False
            names = re.findall(r'`(\w+)`', s)
            q = '(the author line, graded and not quoted)' if AUTHOR(s) else s
            L.append('    %-5s %-8s | %s' % (sid, g, q))
            if g not in ('NO CLAIM',):
                L.append('          %s' % why)
            for n in names:
                h, ln, y = header(src, n) if n in src else (None, None, 0)
                if y == 1:
                    L.append('          `%s` at the pin :%d -- %s' % (n, ln, h))
            counts.setdefault(k['repo'], {}).setdefault(g, 0)
            counts[k['repo']][g] += 1
        stale = sorted(set(hand) - seen, key=lambda x: [int(y) for y in x.split('.')])
        if stale:
            L.append('    ### HAND GRADES NAMING NO SENTENCE: %s' % stale)
            ok = False
        d, err = gh_desc(k['repo'])
        dg, dw = DESC[k['repo']]
        L += ['  THE GITHUB DESCRIPTION (gh repo view psinary-sketch/%s): %s' % (k['repo'], '"%s"' % d if d is not None else '### NOT READ ' + err),
              '    %-8s | %s' % (dg, dw), '']
        if d is None:
            ok = False
        counts[k['repo']].setdefault('DESC ' + dg, 0)
        counts[k['repo']]['DESC ' + dg] += 1
    L += ['## THE TALLY']
    for k in K:
        c = counts.get(k['repo'], {})
        L.append('  %s: %s' % (k['repo'], ' ; '.join('%s %d' % (g, c[g]) for g in sorted(c))))
    L += ['', '## THE GRADE',
          '  The five statements are quoted at their pins and graded by E0 as printed above. Every README sentence and description is graded',
          '  against them in the printed vocabulary, by the seat`s hand: a reading, not a rule; each EXCEEDS names what the sentence asserts',
          '  that no compiled statement carries. The drafts of (7)(ii) are written from these grades.',
          '', '### ### **CONTROLS %s ; FIVE STATEMENTS QUOTED AT THEIR PINS ; %s ; %d s.**' % (
              'ALL AS WANTED' if ok else '### NOT ALL AS WANTED',
              ' ; '.join('%s EXCEEDS %d, STATED %d' % (k['repo'], counts[k['repo']].get(X_, 0) + counts[k['repo']].get('DESC ' + X_, 0),
                                                       counts[k['repo']].get(S_, 0) + counts[k['repo']].get('DESC ' + S_, 0)) for k in K),
              int(time.time() - t0))]
    return L, ok


def run_ids():
    for k in K:
        rd = git(k['repo'], 'show', 'HEAD:README.md')
        print('=====', k['repo'])
        for sid, s in sentences(rd):
            print('  %s | %s' % (sid, '(the author line)' if AUTHOR(s) else s))


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'dry'
    if mode == 'ids':
        run_ids()
    else:
        L, ok = run()
        print(NL.join(L))
        if mode == 'bank':
            if not ok:
                sys.exit('### NOT ALL AS WANTED -- NOTHING WRITTEN')
            with open(OUT + '.tmp', 'wb') as fh:
                fh.write((NL.join(L) + NL).encode('utf-8'))
            os.replace(OUT + '.tmp', OUT)
            print('written data/b721_frozen_line.txt (%d lines)' % len(L))
