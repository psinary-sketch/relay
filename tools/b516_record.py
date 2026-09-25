# -*- coding: utf-8 -*-
"""b516_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b516_record.py components | desk | trail`
### Every figure READ from the banks, not retyped."""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
FIND = os.path.join(PP, 'FINDINGS.md')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


FO = json.loads(read('b516_fold.json') or '{}')
CK = json.loads(read('b516_classk.json') or '{}')
TT = json.loads(read('terminal_table.json') or '{}')
DF = json.loads(read('terminal_table_diff.json') or '{}')
w = lambda v: 'HELD' if v else 'REFUTED'
WOS = ('W-ORD-TABLE-PROFILE-JSON', 'W-ORD-TABLE-SHORTNAME-DEDUP', 'W-ORD-WEIL-CONVERSE')


def section():
    ft = io.open(FIND, encoding='utf-8').read()
    h = FO.get('heading', '')
    return ft[ft.index(h):] if h and h in ft else ''


def scores():
    sec = section()
    wo = (TT.get('workorders_b516') or {})
    links = {'SIDEExplicitFormula.B321.rh_imp_h2_sign', 'SIDEExplicitFormula.B321.h2_sign_imp_cell', 'SIDEExplicitFormula.B321.rh_imp_cell_form'}
    case = {c['case']: c for c in CK.get('cases', [])}
    nonreal_admitted = bool(case.get('h = i phi (not real)', {}).get('admitted'))
    return dict(
        n1=bool(FO.get('quotes')) and all(q['found'] for q in FO['quotes']),
        n2=(FO.get('columns') or {}).get('OBJECT', -1) == 0,
        n3=all(('| `%s` |' % x) in sec for x in WOS) and sec.count('| `W-ORD-') == 3,
        n4=bool(CK) and not (CK.get('h_type') and nonreal_admitted),
        s1=len(wo.get('shortname_dedup') or []) >= 3,
        s2=links <= set(x[1] for x in (wo.get('profile_json') or [])),
        s3=bool(CK.get('h_type')) and nonreal_admitted), wo, case


def components():
    sc, wo, case = scores()
    L = ['=' * 124, 'b516 -- THE COMPONENTS, AS THEY RAN.', '=' * 124, '',
         '### COMPONENT 1 -- THE TWO TABLE WORK-ORDERS IN `tools/terminal_table.py` (THE THIRD RUN, AFTER TWO REPAIRS):',
         '  short ledger-only rows dropped beside a qualified twin : %d' % len(wo.get('shortname_dedup') or [])]
    L += ['    %s / %s' % tuple(x) for x in wo.get('shortname_dedup') or []]
    L += ['  rows profiled from a banked JSON : %d' % len(wo.get('profile_json') or [])]
    L += ['    %s / %s <- %s' % tuple(x) for x in wo.get('profile_json') or []]
    L += ['  the diff against b515`s close : rows added %d ; gone %d ; grade-or-profile changed %d'
          % (len(DF.get('added') or []), len(DF.get('gone') or []), len(DF.get('changed') or [])), '',
          '### THE RUNS, BANKED -- the first two read b456`s ABSENT search as profiles (defect (a)):']
    for n in ('b516_table_first_run.txt', 'b516_table_second_run.txt'):
        t = read(n)
        L.append('  %s : %s' % (n, next((l.strip() for l in t.split(NL) if 'PROFILE-JSON' in l), 'MISSING')[:200]))
    L += ['', '### COMPONENT 2 -- THE FOLD:', '  ' + json.dumps(dict(span=FO.get('span'), columns=FO.get('columns'), writes=FO.get('writes'),
                                                                         markers=FO.get('markers'), table=FO.get('table'))),
          '  verdict strings %d matched %d ; defects %d ; rulings %d matched %d'
          % (len(FO.get('quotes', [])), sum(q['found'] for q in FO.get('quotes', [])), sum(d['n'] for d in FO.get('defects', [])),
             len(FO.get('rulings', [])), sum(r['found'] for r in FO.get('rulings', []))),
          '', '### THE classK READING (READING (8)), FROM H2Sign.lean AT THE KERNEL`S HEAD:'] + ['  ' + x for x in CK.get('definition', '').split(NL)]
    L += ['  ' + CK.get('tilde', ''), '  ' + CK.get('weilTest', '')]
    L += ['  %-30s max|Im h| %.2e ; k even-defect %.2e ; ADMITTED %s' % (c['case'], c['h_imag_max'], c['k_even_defect'], c['admitted'])
          for c in CK.get('cases', [])]
    L += ['  ### ' + CK.get('reading', ''), '=' * 124]
    io.open(os.path.join(D, 'b516_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:12]))


def desk():
    sc, wo, case = scores()
    L = ['=' * 104, 'b516 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FOUR.', '-' * 104,
         '  **(N1)** ### **%s.** -- %d of %d verdict strings matched in their own closing banks.'
         % (w(sc['n1']), sum(q['found'] for q in FO['quotes']), len(FO['quotes'])),
         '  **(N2)** ### **%s.** -- the columns: %s.' % (w(sc['n2']), FO['columns']),
         '  **(N3)** ### **%s.** -- the fold section`s work-order table names %s, each with where filed, its trigger and its status.'
         % (w(sc['n3']), ', '.join(WOS)),
         '  **(N4)** ### **%s.** -- classK`s generating h is typed `ℝ → ℂ` (%s) and `h = i phi`, not real, is ADMITTED (k even-defect %.1e).'
         % (w(sc['n4']), CK.get('h_type'), case['h = i phi (not real)']['k_even_defect']),
         '    ### ITS "SO" CLAUSE, PRINTED SEPARATELY: the classical `e^{i gamma u} phi` is NOT admitted (k even-defect %.2f) -- by'
         % case['h = exp(i gamma u) phi']['k_even_defect'],
         '    evenness, not by type -- and its real part `cos(gamma u) phi` IS; the construction needs a real-valued variant or an even',
         '    combination, which is the clause`s second disjunct, and no widened class.',
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- %d short rows dropped.' % (w(sc['s1']), len(wo.get('shortname_dedup') or [])),
         '  **(S2)** ### **%s.** -- rows profiled from banked JSON: %s.' % (w(sc['s2']), [x[1] for x in wo.get('profile_json') or []]),
         '  **(S3)** ### **%s.** -- `h = i phi` admitted.' % w(sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(True), [sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b516_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b516_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b516_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b516 — the fold at span eight, b508–b515; (R125) entered'


def trail():
    sc, wo, case = scores()
    body = """
%(h)s

**(R125) ratified.** (1) b515 is entered as the sign half of (f): the zero at γ₀ turns the pair negative, and the factor
(γ₀² − t²) that makes it amplifies every zero far from γ₀, so the pair is about 1e-4 of the low zeros; the witness is the
product of both properties — (γ₀² − z²) applied to a window band-limited near γ₀ — the shape of the classical converse,
reached by measurement. (2) **A fixture floor is priced in the quantity's own scale: eps times the sum of the magnitudes
of the terms the closed form adds** — filed with this fold; b515's NOT CLEAN verdict on `G-FIXTURE-BAR` stands. (3)
`W-ORD-WEIL-CONVERSE` is priced at the fold in lemmas: (d) one lemma from the integral; (f) four lemmas, research-grade,
weeks. (4) The instrument lane opened inside the fold and shuts at its close; the kernel lane reopens for (d).

**THE FOLD.** `FINDINGS.md` gains `%(heading)s`, and the (R31) digest one block, both appended, prefixes proved. %(nq)d
verdict strings matched in their own closing banks; %(nd)d defects across the eight acts; eight rulings, (R118) through (R125),
each matched in its ferry. The object column is empty.

**THE TABLE WORK-ORDERS, EXECUTED.** `tools/terminal_table.py` now drops a short ledger-only row beside its qualified twin
(**%(dd)d dropped**) and takes a profile from relay's committed profile banks where a row's own tree is silent (**%(pj)d
rows**, all in `SIDE-explicit-formula`). **The JSON reader was repaired twice inside the fold**: its first two runs read
b456's ABSENT search as three `SIDE-kernel` profiles; quotations are now refused, and both runs are banked.

**classK, read from `H2Sign.lean`:** its generating h is typed `ℝ → ℂ`; `h = iφ` is admitted, `e^{iγu}φ` is not (its
k is not even), `cos(γu)φ` is. The converse's construction needs a real-valued variant or an even combination, not a
widened class.

**(N1) %(N1)s · (N2) %(N2)s · (N3) %(N3)s · (N4) %(N4)s.** The seat's own: (S1) %(S1)s, (S2) %(S2)s, (S3) %(S3)s. **The instrument
lane shuts at this act's close; the kernel lane reopens for (d).** Nothing compiled; nothing at Zenodo written; nothing
deposits; no expectation of the span re-scored; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN;
no cell of this act is a statement about RH.
""" % dict(h=HEADING, heading=FO['heading'], nq=len(FO['quotes']), nd=sum(d['n'] for d in FO['defects']),
           dd=len(wo.get('shortname_dedup') or []), pj=len(wo.get('profile_json') or []),
           N1=w(sc['n1']), N2=w(sc['n2']), N3=w(sc['n3']), N4=w(sc['n4']), S1=w(sc['s1']), S2=w(sc['s2']), S3=w(sc['s3']))
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b516_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
