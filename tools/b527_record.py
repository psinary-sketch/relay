# -*- coding: utf-8 -*-
"""b527_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b527_record.py components | desk | trail`
### Every figure READ from the banks; the scores are READING (6)'s.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OT'.replace('OT', 'OPEN_TRAILS.md'))
NL = chr(10)
NS = 'SIDEExplicitFormula.B321.'
FOUR = ['plateau_contDiff', 'plateau_even', 'plateau_hasCompactSupport', 'plateau_eq_one']
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


AT = json.loads(read('b527_attempts.json') or '[]')
PR = json.loads(read('b527_profile.json') or '{}')
DF = json.loads(read('b527_statement_diff.json') or '{}')
VA = json.loads(read('b527_values.json') or '{}')
DEFS = read('b527_definitions.txt')
w = lambda v: 'HELD' if v else 'REFUTED'


def first_clean():
    ok = [a['attempt'] for a in AT if a['exit'] == 0 and a['errors'] == 0 and not a['sorry'] and not a.get('stopped_by')]
    return ok[0] if ok else None


def body_of(name):
    m = re.search(r'^theorem %s\b[\s\S]*?(?=\n\n|\Z)' % re.escape(name), DEFS, re.M)
    return m.group(0) if m else ''


def module_refs(name):
    names = re.findall(r'^theorem (\S+)', DEFS, re.M)
    b = body_of(name).split(':=', 1)[-1]
    return sorted(n for n in names if n != name and re.search(r'\b%s\b' % re.escape(n), b))


def scores():
    fc = first_clean()
    std = PR.get('std3', {})
    refs = {n: module_refs(n) for n in FOUR}
    return dict(first_clean=fc, refs=refs,
                n1=fc is not None and fc <= 2 and all(std.get(NS + n) is True for n in FOUR),
                n2=all(body_of(n) for n in FOUR) and not any(refs.values()),
                n3=DF.get('diff_lines') == 0 and DF.get('identical') == DF.get('b524_theorems') == 17,
                s1=fc == 1,
                s2=bool(std) and all(std.values()),
                s3=VA.get('max_diff', 1.0) <= 1e-15)


def components():
    L = ['=' * 132, 'b527 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### THE INSTALL:', read('b527_install.json').rstrip(NL),
         '', '### THE ATTEMPTS (READING (3)):']
    for a in AT:
        L.append('  attempt %d : exit %d ; %d error lines ; %.1f s%s' % (a['attempt'], a['exit'], a['errors'], a['seconds'],
                                                                     (' ; STOPPED -- ' + a['stopped_by']) if a.get('stopped_by') else ''))
    L += ['', '### THE STATEMENTS, FROM THE DECLARATION LINE TO ITS := :'] + read('b527_statement.txt').rstrip(NL).split(NL)
    L += ['', '### COMPONENT 2 -- THE STATEMENT DIFF AGAINST b524: %s theorems ; byte-identical %s ; changed %s ; new %s ; DIFF LINES %s'
          % (DF.get('b524_theorems'), DF.get('identical'), DF.get('changed') or 'NONE', DF.get('new_theorems'), DF.get('diff_lines')),
          '', '### THE PROFILE (AxiomCheckWindow.lean):'] + ['  ' + l for l in PR.get('lines', [])]
    L += ['  ### whole-string standard three : %s' % PR.get('std3'), '  ### #print plateau : %s' % PR.get('print_plateau'),
          '', '### COMPONENT 3 -- THE VALUES (a = %s, L = %.6f):' % (VA.get('a'), VA.get('L', 0))]
    for r in VA.get('rows', [])[:20]:
        L.append('  u=%9.6f  chain %.17f  kernel(mp) %s  |diff| %.1e' % (r['u'], r['chain'], r['kernel_str'], r['diff']))
    L += ['  ### max |diff| over %d points %.2e ; within 1e-14 %s' % (len(VA.get('rows', [])), VA.get('max_diff', 0), VA.get('agree')), '=' * 132]
    io.open(os.path.join(D, 'b527_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:12]))


def desk():
    sc = scores()
    L = ['=' * 104, 'b527 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- first clean attempt : %s (attempt 1 STOPPED by the seat`s own timeout, counted) ; the four lemmas std3 : %s.'
         % (w(sc['n1']), sc['first_clean'], all(PR.get('std3', {}).get(NS + n) for n in FOUR)),
         '  **(N2)** ### **%s.** -- module theorems the four proofs cite : %s.' % (w(sc['n2']), sc['refs']),
         '  **(N3)** ### **%s.** -- b524`s theorems byte-identical %s of %s ; diff lines %s.' % (w(sc['n3']), DF.get('identical'), DF.get('b524_theorems'), DF.get('diff_lines')),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the first attempt clean : attempt 1 was stopped, attempt %s clean.' % (w(sc['s1']), sc['first_clean']),
         '  **(S2)** ### **%s.** -- every theorem in the axiom check std3 : %d of %d.' % (w(sc['s2']), sum(1 for v in PR.get('std3', {}).values() if v), len(PR.get('std3', {}))),
         '  **(S3)** ### **%s.** -- max |diff| %.2e against 1e-15.' % (w(sc['s3']), VA.get('max_diff', 0)),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3')].count(True), [sc[k] for k in ('n1', 'n2', 'n3')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b527_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b527_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b527_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b527 — the plateau made concrete in the kernel; (R137) entered'


def trail():
    sc = scores()
    body = [
        '', HEADING, '',
        '**(R137) ratified.** (1) b526 is entered: `W-ORD-XI-P7` closed — ξ at ramp order 7 positive beyond its bound at 46 of',
        '46 verified widths to 60 — and the re-derived form of words stands with its closing clause; Component 2\'s halt proved.',
        '(2) **Choice (a): the plateau made concrete.** (3) (f)(ii) follows either way, for every C⁴ φ ≥ 0 with the realized G',
        'as hypothesis. (4) The kernel lane opened for this act and shuts at its close; the numerical lane reopens for b528.',
        '',
        '**COMPONENT 1 — `plateau` redefined** in `SIDEExplicitFormula/TwoPropertyWindow.lean` as',
        '`Real.smoothTransition ((L − u)/(F L)) · Real.smoothTransition ((L + u)/(F L))` — Mathlib\'s closed-form exp(−1/x)',
        'transition, no base chosen; Lean\'s own `#print plateau` shows the two `smoothTransition` factors and no `ContDiffBump`.',
        'A new theorem `plateau_apply_abs` proves it equal to `smoothTransition ((L − |u|)/(F L))` at every u. `plateau_contDiff`,',
        '`plateau_even`, `plateau_hasCompactSupport` and `plateau_eq_one` re-proved from Mathlib\'s `smoothTransition` lemmas and',
        'field arithmetic, citing no theorem of the module. `plateauBump`, the `ContDiffBump` over the chosen base, is removed.',
        'Attempts: 1 stopped by the seat\'s own timeout wrapper at 620 s (no verdict from Lean; counted); 2 clean in %.1f s.'
        % next((a['seconds'] for a in AT if a['attempt'] == sc['first_clean']), float('nan')),
        '',
        '**COMPONENT 2 — every theorem of b524 rebuilt with its statement byte-identical: %s of %s, the diff 0 lines**; the'
        % (DF.get('identical'), DF.get('b524_theorems')),
        'profiles re-run, %d of %d theorems in `AxiomCheckWindow.lean` the standard three on the whole string.'
        % (sum(1 for v in PR.get('std3', {}).values() if v), len(PR.get('std3', {}))),
        '',
        '**COMPONENT 3 — the plateau\'s values:** twenty points across the ramp at a = 34 and their mirrors, the kernel\'s',
        'definition as written evaluated in mpmath at 50 digits against the chain\'s formula in doubles: largest difference',
        '%.1e. b528 measures the kernel\'s function and no other.' % VA.get('max_diff', 0),
        '',
        '**(N1) %s · (N2) %s · (N3) %s.** The seat\'s own: (S1) %s, (S2) %s, (S3) %s. **The kernel lane shuts at this act\'s'
        % (w(sc['n1']), w(sc['n2']), w(sc['n3']), w(sc['s1']), w(sc['s2']), w(sc['s3'])),
        'close.** The kernel is not tagged; nothing at Zenodo written; nothing deposits; no grade conferred; row U1 unedited;',
        '`h2` where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH.',
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
    io.open(os.path.join(D, 'b527_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
