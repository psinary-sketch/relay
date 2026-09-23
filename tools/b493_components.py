# -*- coding: utf-8 -*-
"""b493_components.py -- THE COMPONENTS. ### THE 104 ROWS, DISPOSED AGAINST THE CEILING.

### ### **THE CEILING, QUOTED FROM (R102):** ### "Supportable: RH reduced to a single located
### clause, reduction machine-verified; not supportable: RH proved."
### ### **AN `EXCEEDS` ROW GETS NO REPLACEMENT.** ### The order is explicit: it is the author's to
### reword, and this act names it and stops.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CEILING = ('Supportable: RH reduced to a single located clause, reduction machine-verified; '
           'not supportable: RH proved')

# ### ### **THE CEILING MATCHER, VERSION 1 -- FIXED BEFORE THE READ.** ### A row EXCEEDS when it
# ### asserts RH as PROVED / VERIFIED / ESTABLISHED, rather than as REDUCED to a located clause.
EXC_V1 = re.compile(
    r'\bProof of the Riemann Hypothesis\b'
    r'|\bproof of the Riemann Hypothesis\b'
    r'|\b(?:Formal )?verification of the Riemann Hypothesis\b'
    # ### ### **`[^.]` COULD NOT CROSS THE PERIOD IN `MAIN THEOREM. The Riemann Hypothesis:`**
    # ### and so missed the very sentence (N2) names. ### Repaired to allow it.
    r'|\bMAIN THEOREM\b.{0,160}?Riemann Hypothesis'
    r'|\bproves that no off-line zero exists\b'
    r'|\bRH (?:is )?prove[dn]\b',
    re.I)
# ### ### **VERSION 2 ADDS THE FORMS VERSION 1 MISSED**, and BOTH yields are printed below.
EXC = re.compile(
    EXC_V1.pattern
    + r'|\bproof of the Riemann Hypothesis\b'
      r'|\bSIDE (?:Exclusion )?proof of the Riemann Hypothesis\b'
      r'|\bthe SIDE proof of the Riemann Hypothesis\b'
      r'|\bit proves that no off-line zero exists\b'
      r'|\bproves the mathematics\b',
    re.I)

# ### b487's CLAIM predicate, version 2, CARRIED UNCHANGED.
CLAIM = re.compile(r'machine.?(?:check|verif)|compil|verified|zero unproved|proof-check|'
                   r'formally (?:verif|proved)|#print axioms|lake build|sorry-free|no axioms|'
                   r'\b(?:kernel|we|it|this work)\b[^.]{0,40}\bproves\b|'
                   r'\bproves that\b|\bcertified\b', re.I)

# ### the two errata, and the sentences b487 found resting on them -- carried by their OWN words.
RESTS = {
    ('21539167', 'Proved and machine-checked around the argument'): 'E-2026-09-14-1',
    ('21539167', 'Section 27.3, "The One Premise,"'): 'E-2026-09-22-1',
    ('21520474', 'The kernel proves that no off-line zero exists'): 'E-2026-09-14-1',
}
R99 = {
    'E-2026-09-14-1|21539167': (
        'Proved and machine-checked around the argument, with the catalogue read exactly as its '
        'route terminal states it: the Lean terminal `structural_exhaustiveness_proved` proves '
        'that the kernel’s mechanism type has seven members, that none of them produces the '
        'off-line signature the kernel defines, and Ostrowski’s classification of the places '
        'of ℚ — that the seven classes exhaust the mechanisms is the manuscript’s '
        'theorem, and the kernel does not check it; and, as before, five independent compiled '
        'identifications of σ = 1/2 in five machineries; Conservation of Spectra from '
        'Tate’s thesis (Chapter 13); the Mechanism Theorem derived from the Independence, '
        'Determination and Symmetry principles (Chapter 10); h1 complete at the witness '
        '(`h1_complete_at_Phi`, SIDE-lv-conservation); the finite-range Li positivity certificate '
        'whose finite-set conjunct is itself proved (`lowFinset_mem_iff`, v0.10.0); and the step '
        '(9) assembly stated in its two-sentence form — the identity reading separated from '
        'the sign reading.'),
    'E-2026-09-14-1|21520474': (
        'The kernel compiles the exclusion architecture: the Lean terminal '
        '`structural_exhaustiveness_proved` proves that the kernel’s mechanism type has '
        'seven members, that none of them produces the off-line signature the kernel defines, and '
        'Ostrowski’s classification of the places of ℚ — that the seven classes '
        'exhaust the mechanisms is the manuscript’s theorem, and the kernel does not check '
        'it.'),
}


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    SV = json.loads(read(os.path.join(D, 'b493_survey.json')))
    recs = SV['records']
    DOI = {2: '21539167', 3: '21539068', 4: '21520474'}

    rec('=' * 122)
    rec('b493 -- THE COMPONENTS. ### THE EIGHT RECORDS READ WHOLE AGAINST THE CEILING.')
    rec('=' * 122)

    rec('')
    rec('### (1) THE CEILING, AND THE MATCHER`S LINEAGE.')
    rec('-' * 122)
    rec('    ### **"%s."**' % CEILING)
    rec('    ### ### **QUOTED FROM (R102). ### NEITHER SOFTENED NOR EXTENDED.**')
    rec('')
    rec('    ### the CLAIM matcher is b487`s version 2, ### **CARRIED UNCHANGED.**')
    rec('    ### the CEILING matcher is NEW to this act, and both its yields are printed:')
    allrows = []
    for r in recs:
        for j, s in enumerate(r['sentences'], 1):
            allrows.append((r['k'], 'sentence %d' % j, s))
        allrows.append((r['k'], 'TITLE', r['title']))
    v1 = [x for x in allrows if EXC_V1.search(x[2])]
    v2 = [x for x in allrows if EXC.search(x[2])]
    rec('      ### version 1 catches ### **%d** ### ; version 2 catches ### **%d**'
        % (len(v1), len(v2)))
    add = [x for x in v2 if x not in v1]
    for x in add:
        rec('      ### ### **VERSION 2 ADDS** ### record %d, %s' % (x[0], x[1]))
    if not add:
        rec('      ### ### **VERSION 2 ADDS NOTHING.** ### The widening changed no row, and that')
        rec('      ### is printed rather than left as a silent equality.')

    rec('')
    rec('### (2) THE 104 ROWS, ONE DISPOSITION EACH.')
    rec('-' * 122)
    disp = []
    for r in recs:
        doi = DOI.get(r['k'], '')
        rows = [('TITLE', r['title'])] + [('sentence %d' % j, s)
                                          for j, s in enumerate(r['sentences'], 1)]
        for kind, text in rows:
            d, why, erratum, repl = 'STANDS', '', None, None
            if EXC.search(text):
                d = 'EXCEEDS THE CEILING'
                why = 'asserts RH as proved or verified, not as reduced to a located clause'
            else:
                # ### ### **`startswith` FAILED ON A SENTENCE CARRYING ITS HEADLINE.** ### The
                # ### splitter keeps `WHAT THE MANUSCRIPT ESTABLISHES...` attached to the
                # ### sentence it heads, so the b487 text sits INSIDE the row, not at its start.
                for (rd, pre), e in RESTS.items():
                    if rd == doi and pre in text:
                        d, erratum = 'RESTS ON AN ERRATUM', e
                        repl = R99.get('%s|%s' % (e, rd))
                        why = 'the sentence rests on %s' % e
                        break
            disp.append(dict(k=r['k'], kind=kind, text=text, disposition=d, why=why,
                             erratum=erratum, replacement=repl, doi=doi))
    rec('    %-3s %-13s %-22s %s' % ('#', 'row', 'disposition', 'first 70 characters'))
    rec('    ' + '-' * 114)
    for x in disp:
        rec('    %-3d %-13s %-22s %s' % (x['k'], x['kind'], x['disposition'], x['text'][:70]))

    rec('')
    rec('### (3) THE COUNT PER DISPOSITION PER RECORD.')
    rec('-' * 122)
    rec('    %-3s %-60s %-9s %-9s %s' % ('#', 'record', 'STANDS', 'RESTS', 'EXCEEDS'))
    rec('    ' + '-' * 114)
    for r in recs:
        mine = [x for x in disp if x['k'] == r['k']]
        rec('    %-3d %-60s %-9d %-9d %d'
            % (r['k'], r['title'][:58],
               sum(1 for x in mine if x['disposition'] == 'STANDS'),
               sum(1 for x in mine if x['disposition'] == 'RESTS ON AN ERRATUM'),
               sum(1 for x in mine if x['disposition'] == 'EXCEEDS THE CEILING')))
    rec('    ' + '-' * 114)
    rec('    %-3s %-60s %-9d %-9d %d'
        % ('', 'TOTAL (of %d rows)' % len(disp),
           sum(1 for x in disp if x['disposition'] == 'STANDS'),
           sum(1 for x in disp if x['disposition'] == 'RESTS ON AN ERRATUM'),
           sum(1 for x in disp if x['disposition'] == 'EXCEEDS THE CEILING')))

    rec('')
    rec('### (4) THE `EXCEEDS` ROWS, IN FULL, WITH THE CEILING QUOTED BESIDE EACH.')
    rec('-' * 122)
    exc = [x for x in disp if x['disposition'] == 'EXCEEDS THE CEILING']
    for i, x in enumerate(exc, 1):
        rec('')
        rec('    ### **%d. RECORD %d -- %s**' % (i, x['k'], x['kind']))
        for chunk in [x['text'][c:c + 112] for c in range(0, len(x['text']), 112)]:
            rec('       %s' % chunk)
        rec('       ### the ceiling : *"%s."*' % CEILING)
        rec('       ### ### **NO REPLACEMENT IS DRAFTED.** ### %s' % x['why'])
    rec('')
    rec('    ### ### **%d ROWS EXCEED THE CEILING, AND NOT ONE CARRIES A DRAFT.**' % len(exc))
    rec('    ### The order is explicit: a title or headline that exceeds the ceiling is ### **THE')
    rec('    ### AUTHOR`S TO REWORD, AND THIS ACT NAMES IT AND STOPS.** ### A disposition that')
    rec('    ### refuses to draft is not an incomplete one.')

    rec('')
    rec('### (4b) A CORRECTION TO b487, FOUND BY READING THE DEPOSIT ITSELF.')
    rec('-' * 122)
    import subprocess
    z = subprocess.run(['git', '-C', os.path.join('D:', os.sep, 'SIDE-kernel'),
                        'show', 'v1.5:.zenodo.json'], capture_output=True, text=True,
                       encoding='utf-8').stdout
    try:
        zd = re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', json.loads(z).get('description', ''))).strip()
    except Exception:
        zd = ''
    scr = re.sub(r'\s+', ' ', recs[3]['desc']).strip()
    rec('    ### ### **THE KERNEL`S DEPOSITED DESCRIPTION IS NOT THE TEXT IN ITS REPOSITORY.**')
    rec('      `SIDE-kernel` at tag `v1.5`, `.zenodo.json` : ### **%d characters**' % len(zd))
    rec('        opening: *"%s..."*' % zd[:96])
    rec('      the author`s screen, record 4                : ### **%d characters**' % len(scr))
    rec('        opening: *"%s..."*' % scr[:96])
    rec('      ### ### **THEY ARE DIFFERENT TEXTS : %s**' % (zd != scr))
    rec('')
    rec('    ### ### **SO b487 DISPOSED A SENTENCE THAT IS NOT IN THE DEPOSIT.** ### b487 read the')
    rec('    ### kernel`s description from the repository`s `.zenodo.json` and graded its sentence')
    rec('    ### 2 -- *"The kernel proves that no off-line zero exists by exhaustively excluding')
    rec('    ### every mechanism class derivable from the specification"* -- as resting on')
    rec('    ### `E-2026-09-14-1`. ### **THAT SENTENCE IS PRESENT IN THE `.zenodo.json` AND ABSENT')
    rec('    ### FROM THE DEPOSITED RECORD:** ### in `.zenodo.json` %s ; on the screen %s.'
        % ('exhaustively excluding every mechanism class' in zd,
           'exhaustively excluding every mechanism class' in scr))
    rec('    ### ### **AND (R99) RULED THAT SENTENCE "APPLIED AS DRAFTED".** ### Applying it at')
    rec('    ### the platform would edit a sentence the record does not contain.')
    rec('    ### ### **THIS ACT NAMES IT AND STOPS.** ### The kernel`s `RESTS` row is therefore')
    rec('    ### NOT carried into the paste-ready block, and (R99)`s kernel text is held for the')
    rec('    ### author`s ruling -- it is a draft for a sentence that is not there.')
    rec('    ### ### **A SOURCE THAT SHIPS BESIDE A DEPOSIT IS NOT THE DEPOSIT.**')

    rec('')
    rec('### (5) THE PASTE-READY PLATFORM TEXTS -- `RESTS` ROWS ONLY, IN ONE BLOCK.')
    rec('-' * 122)
    rests = [x for x in disp if x['disposition'] == 'RESTS ON AN ERRATUM']
    rec('    ### ### **FOR A SINGLE PLATFORM SESSION UNDER (R102).** ### %d row(s).' % len(rests))
    rec('    ### ### **AND THE SESSION IS HELD UNTIL THE WHOLE DISPOSITION IS APPLIED AT ONCE** --')
    rec('    ### (R102) is explicit, and the EXCEEDS rows above must be reworded by the author')
    rec('    ### BEFORE any of this block is applied.')
    for i, x in enumerate(rests, 1):
        rec('')
        rec('    ' + '=' * 110)
        rec('    ### **%d. RECORD %d (%s) -- %s -- rests on %s**'
            % (i, x['k'], x['doi'], x['kind'], x['erratum']))
        rec('    ' + '-' * 110)
        rec('    ### REPLACE:')
        for chunk in [x['text'][c:c + 108] for c in range(0, len(x['text']), 108)]:
            rec('      %s' % chunk)
        rec('    ### WITH:')
        if x['replacement']:
            for chunk in [x['replacement'][c:c + 108]
                          for c in range(0, len(x['replacement']), 108)]:
                rec('      %s' % chunk)
        else:
            rec('      ### ### **NO (R99) TEXT EXISTS FOR THIS ROW.** ### (R99) supplied two')
            rec('      ### texts and ruled the third NOT APPLIED; this row carries no draft and')
            rec('      ### must not be edited on this pass.')
    rec('    ' + '=' * 110)

    rec('')
    rec('=' * 122)
    io.open(os.path.join(D, 'b493_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(rows=disp, n_rows=len(disp),
                   stands=sum(1 for x in disp if x['disposition'] == 'STANDS'),
                   rests=len(rests), exceeds=len(exc),
                   v1=len(v1), v2=len(v2),
                   per_record={str(r['k']): dict(
                       stands=sum(1 for x in disp if x['k'] == r['k']
                                  and x['disposition'] == 'STANDS'),
                       rests=sum(1 for x in disp if x['k'] == r['k']
                                 and x['disposition'] == 'RESTS ON AN ERRATUM'),
                       exceeds=sum(1 for x in disp if x['k'] == r['k']
                                   and x['disposition'] == 'EXCEEDS THE CEILING'))
                       for r in recs}),
              io.open(os.path.join(D, 'b493_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL + '  written: b493_components.txt, b493_results.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
