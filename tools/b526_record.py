# -*- coding: utf-8 -*-
"""b526_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b526_record.py components | desk | trail`
### Every figure READ from the banks; (N2) and (N3) NOT SCORABLE by READING (5): their population does not exist.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


R = json.loads(read('b526_results.json') or '{}')
BP = json.loads(read('b526_bump.json') or '{}')
NT = json.loads(read('b526_notes.json') or '{}')
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def scores():
    return dict(
        n1=R['verified'] >= 1 and len(R['positive']) == R['verified'],
        n2=None, n3=None,
        s1=R['cells'] == 46 and R['within'] == 46 and R['verified'] == 46,
        s2=len(R['positive']) == 46,
        s3=BP['max_pointwise_diff'] > 0.01)


def components():
    L = ['=' * 132, 'b526 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, ''] + read('b526_report.txt').rstrip(NL).split(NL)
    L += ['', '### THE RUN LOG:'] + read('b526_run_log.txt').rstrip(NL).split(NL) + ['=' * 132]
    io.open(os.path.join(D, 'b526_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:6]))


def desk():
    sc = scores()
    L = ['=' * 104, 'b526 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- xi at order 7 : VERIFIED-EST %d of %d IN widths, positive beyond bound %d.'
         % (W(sc['n1']), R['verified'], R['within'], len(R['positive'])),
         '  **(N2)** ### **%s.** -- the population, Q0 cells on the kernel`s phi, does not exist: the kernel`s plateau is a ContDiffBump over a'
         % W(sc['n2']),
         '      base chosen by Classical.choice (someContDiffBumpBase := Nonempty.some), with no values to evaluate; Component 2 HALTED.',
         '  **(N3)** ### **%s.** -- no crossing read on the kernel`s phi, so no G there; the conflict is the same as (N2)`s.' % W(sc['n3']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- xi widths computed %d, IN %d, VERIFIED-EST %d.' % (W(sc['s1']), R['cells'], R['within'], R['verified']),
         '  **(S2)** ### **%s.** -- positive beyond bound at %d of 46.' % (W(sc['s2']), len(R['positive'])),
         '  **(S3)** ### **%s.** -- the two bases differ by %.4f pointwise.' % (W(sc['s3']), BP['max_pointwise_diff']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3')].count(True), [sc[k] for k in ('n1', 'n2', 'n3')].count(False),
            [sc[k] for k in ('n1', 'n2', 'n3')].count(None),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b526_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b526_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b526_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b526 — ξ at order 7; the kernel\'s φ found to be a choice; (R136) entered'


def trail():
    sc = scores()
    ta = BP['transforms']
    body = [
        '', HEADING, '',
        '**(R136) ratified.** (1) The fold\'s missing sentence is appended beside its summary in `FINDINGS.md` and beside the',
        'b525 block in the digest, prefixes proved: *%s* (2) (R135)(3)(a) ran as this act. (3) The numerical lane opened for'
        % NT['sentence'],
        'this act and shuts at its close; (f)(ii) in the kernel follows.',
        '',
        '**COMPONENT 1 — ξ on variant (B) at ramp order 7**, γ₀ = 14.1347, a = 15 … 60, the reach per width: %d of 46 widths IN,'
        % R['within'],
        '**VERIFIED-EST at %d, positive beyond its bound at %d**, negative at none; the tail at most %.1e of the rest of the bound'
        % (R['verified'], len(R['positive']), R['tail_over_bprime_max']),
        '— ξ\'s cells are VERIFIED-EST, not tail-led. The tail above the atlas\'s top takes the zeros there on the line, as b519',
        'and b520 read ξ.',
        '',
        '**COMPONENT 2 — HALTED, and why.** The kernel\'s `plateau` is Mathlib\'s `ContDiffBump`, whose function is',
        '`(someContDiffBumpBase ℝ).toFun`, and at the pin `someContDiffBumpBase E := Nonempty.some hb.out` with `HasContDiffBump`',
        'a `Prop` class: **the base is chosen by `Classical.choice` and fixed by no definition, so the kernel\'s named instance',
        'has no values to evaluate** — it is determined only by the properties the kernel proves. Two bases pass every field',
        '(Mathlib\'s `ofInnerProductSpace` base A and `smoothTransition` applied twice, B) and differ by up to %.3f pointwise; at'
        % BP['max_pointwise_diff'],
        'a = 34 the window would cite φ̂(γ₀) = %.1e on A and %.1e on B, G = %.4f and %.4f. A candidate with the wrong support'
        % (ta['A']['at_gamma0'], ta['B']['at_gamma0'], ta['A']['growth'], ta['B']['growth']),
        'is rejected by the same checks. **No number was taken "on the kernel\'s φ"**; measuring base A in its place would be',
        'the substitution (R136) exists to end.',
        '',
        '**COMPONENT 3 — the form of words, re-derived from Component 1 alone:** %s **The seat\'s reading:** %s.'
        % (R['form'] or 'NOT RE-DERIVED', R['instance_reading']),
        '',
        '**(N1) %s · (N2) %s · (N3) %s** — the last two have no population. The seat\'s own: (S1) %s, (S2) %s, (S3) %s.'
        % (W(sc['n1']), W(sc['n2']), W(sc['n3']), W(sc['s1']), W(sc['s2']), W(sc['s3'])),
        '**The numerical lane shuts at this act\'s close.** Nothing compiled; nothing at Zenodo written; nothing deposits; no',
        'grade conferred; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; no cell of this act is a',
        'statement about RH.',
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
    io.open(os.path.join(D, 'b526_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
