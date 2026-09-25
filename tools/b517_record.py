# -*- coding: utf-8 -*-
"""b517_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b517_record.py components | desk | trail`
### Every figure READ from the banks, not retyped. ### THE TRAIL CARRIES GRADE WORDS ON TWO LINES ONLY, each beside its own
### theorem (READING (6)): the terminal table attaches a grade to the NEAREST backticked name in its line.
"""
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SUMMARY = ('the programme built and corrected instruments; it did not move a statement about zeta')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


P = json.loads(read('b517_profile.json') or '{}')
RD = json.loads(read('b517_read.json') or '{}')
w = lambda v: 'HELD' if v else 'REFUTED'


def attempts():
    out = []
    for p in sorted(glob.glob(os.path.join(D, 'b517_compile_log*.txt')), key=os.path.getmtime):
        t = io.open(p, encoding='utf-8').read()
        m = re.search(r'^exit (\d+) ; ([0-9.]+) s$', t, re.M)
        body = t.split('--- stdout ---', 1)[-1]
        ok = bool(m) and m.group(1) == '0' and 'error' not in body and 'sorry' not in body
        out.append(dict(file=os.path.basename(p), exit=int(m.group(1)) if m else None, secs=float(m.group(2)) if m else None, ok=ok))
    return out


def lines_of(name):
    return next((x['lines'] for x in RD.get('decls', []) if x['name'] == name), 10 ** 6)


def scores():
    A = attempts()
    first_ok = next((i + 1 for i, a in enumerate(A) if a['ok']), None)
    std3 = bool(P.get('std3')) and all(P['std3'].values()) and not P.get('sorry', True)
    return dict(n1=std3 and first_ok is not None and first_ok <= 2,
                n2=lines_of('paperFT_growth') < 40,
                n3=bool(RD.get('refs')) and not RD.get('lemma_refs') and 'Zeta23.paperFT' in (RD.get('def_refs') or []),
                s1=bool(A) and A[0]['ok'],
                s2=lines_of('paperFT_growth') < 30,
                s3=None), A, first_ok


def components():
    sc, A, first_ok = scores()
    L = ['=' * 104, 'b517 -- THE COMPONENTS, AS THEY RAN.', '=' * 104, '', '### COMPONENT 1 -- THE MODULE, EVERY DECLARATION WHOLE:']
    L += read('b517_definitions.txt').rstrip(NL).split(NL)
    L += ['', '### THE ATTEMPTS (READING (3)) : %d ; the first to succeed : %s' % (len(A), first_ok)]
    L += ['    %(file)s exit %(exit)s ; %(secs)s s ; Lean`s verdict %(ok)s' % a for a in A]
    L += ['', '### READING (4) -- LINES : ' + ' ; '.join('%s %d' % (x['name'], x['lines']) for x in RD.get('decls', [])),
          '### READING (5) -- VENDORED REFERENCES : ' + ' ; '.join('%s -> %s' % (r['name'], [h['keyword'] + ' in ' + h['file'] for h in r['resolved']])
                                                                 for r in RD.get('refs', [])),
          '    vendored lemmas referenced : %s' % (RD.get('lemma_refs') or 'NONE')]
    for p in sorted(glob.glob(os.path.join(D, 'b517_compile_log*.txt'))) + sorted(glob.glob(os.path.join(D, 'b517_profile_log*.txt'))):
        L += ['', '### RUN FILE %s:' % os.path.basename(p)] + io.open(p, encoding='utf-8').read().rstrip(NL).split(NL)
    L += ['', '### COMPONENT 2 -- THE PROFILE, EACH THEOREM ON THE WHOLE STRING : %s' % json.dumps(P.get('std3')), '=' * 104]
    io.open(os.path.join(D, 'b517_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[-4:]))


def desk():
    sc, A, first_ok = scores()
    L = ['=' * 104, 'b517 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- profiles %s ; sorry in Lean`s output %s ; attempts %d, the first to succeed %s.'
         % (w(sc['n1']), P.get('lines'), P.get('sorry'), len(A), first_ok),
         '  **(N2)** ### **%s.** -- paperFT_growth is %d lines by READING (4), against 40.' % (w(sc['n2']), lines_of('paperFT_growth')),
         '  **(N3)** ### **%s.** -- vendored lemmas referenced : %s ; vendored definitions : %s.'
         % (w(sc['n3']), RD.get('lemma_refs') or 'NONE', RD.get('def_refs')),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the first compile attempt`s verdict: %s.' % (w(sc['s1']), A[0]['ok'] if A else 'NO ATTEMPT'),
         '  **(S2)** ### **%s.** -- %d lines, against 30.' % (w(sc['s2']), lines_of('paperFT_growth')),
         '  **(S3)** ### **SCORED POST-PUSH.** -- the table rows are read after the push (G-TABLE-ROWS); the closing record carries the word.',
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d ; POST-PUSH 1.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3')].count(True), [sc[k] for k in ('n1', 'n2', 'n3')].count(False),
            [sc[k] for k in ('s1', 's2')].count(True), [sc[k] for k in ('s1', 's2')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b517_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b517_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(sc, attempts=len(A), first_ok=first_ok, proof_lines=lines_of('paperFT_growth')),
              io.open(os.path.join(D, 'b517_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b517 — (d), the growth bound, compiled; (R126) entered'


def trail():
    sc, A, first_ok = scores()
    ok = next((a for a in A if a['ok']), {})
    body = """
%(h)s

**(R126) ratified.** (1) The class shapes the converse: classK admits complex h but requires h ⋆ h~ even, so the
classical modulation e^{iγu}φ is not admitted and the real cosine is. The two-property window for (f)(i) is therefore
real — the zero factor applied to the cosine window, h = (γ₀² + d²/du²)(cos(γ₀u)φ) — the numerical candidate for the next
window act and the formal candidate for (f)(i), one object in two registers. (2) **The fold's object column is empty —
eight acts about the model, none about the object — and the week's honest summary is: %(summary)s.** (3) The kernel lane
opened for this act; the numerical lane reopens after it for the two-property window.

**COMPONENT 1.** `SIDEExplicitFormula/GrowthBound.lean`, importing `Zeta23.Defs` alone, proves (d): for h integrable with
support in [−L, L] and any complex z, ‖paperFT h z‖ ≤ (∫‖h‖)·exp(L·|Im z|), by the norm-of-integral bound and
‖exp(izu)‖ = exp(−u·Im z) ≤ exp(L|Im z|) on the support; and its form at a zero, exp(L·|Re ρ − 1/2|) at gammaOf ρ.
%(lines)d lines; compiled in %(secs)s s at attempt %(first)s of %(att)d; each profile the standard three on the whole
string; no sorry; vendored lemmas referenced: %(lemmas)s — only the definitions %(defs)s. By the order, each of its
model statement:

- `paperFT_growth` — DERIVES, of (d) as (R124)(2) words it.
- `paperFT_growth_at` — DERIVES, of (d)'s form at a zero.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s.** The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3) read post-push. **The kernel lane
shuts at this act's close.** The kernel is not tagged; REGISTRY is not written. Nothing at Zenodo written; nothing
deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; (f) is not attempted.
""" % dict(h=HEADING, summary=SUMMARY, lines=lines_of('paperFT_growth'), secs=ok.get('secs'), first=first_ok, att=len(A),
           lemmas=RD.get('lemma_refs') or 'none', defs=', '.join('`%s`' % d for d in RD.get('def_refs') or []),
           N1=w(sc['n1']), N2=w(sc['n2']), N3=w(sc['n3']), S1=w(sc['s1']), S2=w(sc['s2']))
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b517_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
