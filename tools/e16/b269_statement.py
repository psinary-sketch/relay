# -*- coding: utf-8 -*-
"""b269_statement.py -- M-2 CAMPAIGN ACT 3 (A2). ### THE M-2 STATEMENT. ### THE RUN.

### **A DERIVATION ATTEMPT, AND -- ONLY IF IT HALTS -- A RULING DOSSIER.**
### ### **NOTHING IS CONSTRUCTED. ### NO NUMBER IS COMPUTED FOR ANY DOSSIER CANDIDATE
### ### (F-NOCONSTRUCT).** ### Bars fixed in `data/b269_registration_2026-08-31.txt`, SEALED
### `7a914743...`, term-scanned and satisfiability-checked BEFORE the seal.
"""
import io
import json
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = r'D:\relay'
D = os.path.join(ROOT, 'data')
BANK = os.path.join(D, 'b269_run.txt')
ROWS = os.path.join(D, 'b269_rows.json')

QUOTES = [
    ('b237, M-2 named', 'b237_left_side_assets.txt',
     'THIS IS THE ASSEMBLY STEP, NOT THE PER-PLACE OPERATOR.'),
    ('b237, the junction is at the assembly', 'b237_left_side_assets.txt',
     'THE JUNCTION IS AT THE ASSEMBLY.'),
    ('b227, omega_u cannot be evaluated', 'b227_the_trace.txt',
     "omega_u CANNOT BE EVALUATED ON ACT 9's CELL OPERATOR"),
    ('b227, E_1 does not exist on V_inv', 'b227_the_trace.txt',
     'ON V_inv THE TRANSFORM DOES NOT DESCEND, SO E_1 DOES NOT EXIST THERE.'),
    ('b227, the available operators', 'b227_the_trace.txt',
     'on Pi, or on M itself, whose state is 1 because u lies in E_1'),
    ('b227, the standing ruling', 'b227_the_trace.txt',
     'IT WANTS A RESULT OR A RULING; IT DOES NOT WANT A READ'),
    ('b10, V_inv defined', 'b10_2026-08-17.txt',
     'V_inv = { f supported off the ball'),
    ('b10, S_quot is an orthoprojection', 'b10_2026-08-17.txt',
     'S_quot = orthoprojection onto\nV_inv'),
    ('b10, the Fourier half does not descend', 'b10_2026-08-17.txt',
     'THE FOURIER HALF DOES NOT DESCEND -- the transform does not commute with x ~ px'),
    ('b10, the quantity', 'b10_2026-08-17.txt',
     'T_quot(k) = |Tr(U^k S_quot)|'),
    ('b228, READ 1 is ABSENT', 'b228_ledger_cell_statement.txt',
     'NO OWNER STATES AN ACTION. b10 STATES THE OBSTRUCTION AND CALLS IT INFORMATIVE.'),
    ('b228, the only connecting sentences', 'b228_ledger_cell_statement.txt',
     'THE ONLY SENTENCES CONNECTING V_inv AND Son ARE'),
    ('b263, SPEC-2', 'b263_top_level_silence.txt',
     "(SPEC-2) IT REDUCES TO `Theta_q`'s TERMS AT LEVELS `k <= n-1`."),
    ('b263, they exclude', 'b263_top_level_silence.txt',
     'THESE EXCLUDE; THEY DO NOT DETERMINE'),
]


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b269 RUN -- M-2 CAMPAIGN ACT 3 (A2). ### THE M-2 STATEMENT.')
    rec('### Registration SEALED (`7a914743...`), TERM-SCANNED and SATISFIABILITY-CHECKED')
    rec('### ### **BEFORE** ### the seal. ### `RULE M2-ORDER: A1 then A2`; A1 closed at b268.')
    rec('### ### **NOTHING IS CONSTRUCTED. ### NO CANDIDATE IS ADOPTED. ### NO NUMBER IS COMPUTED')
    rec('### ### FOR ANY CANDIDATE.**')
    rec('=' * 100)

    # ============================================================ F-QUOTE
    rec('')
    rec('### F-QUOTE -- EVERY OWNER SENTENCE VERBATIM, BEFORE ANY VERDICT IS EMITTED.')
    rec('=' * 100)
    cache, bad = {}, []
    for label, fn, q in QUOTES:
        path = os.path.join(D, fn)
        if path not in cache:
            cache[path] = norm(io.open(path, encoding='utf-8', errors='replace').read())
        ok = norm(q) in cache[path]
        if not ok:
            bad.append((label, fn, q))
        rec('  %-46s %s' % (label[:46], 'YES' if ok else '### NOT FOUND ###'))
    fquote = (len(bad) == 0)
    for label, fn, q in bad:
        rec('    ### NOT FOUND in %s : %r' % (fn, q[:80]))
    tam = norm(QUOTES[10][2]).replace('NO OWNER', 'NO OWNERX')
    ctrl = tam not in cache[os.path.join(D, QUOTES[10][1])]
    rec('  ### **%d quotations, %d unfindable.**' % (len(QUOTES), len(bad)))
    rec('  (C1) an altered quotation is reported unfindable : ### **%s**' % ('YES' if ctrl else 'NO'))
    rec('  ### ### **F-QUOTE %s**' % ('DID NOT FIRE.' if fquote else 'FIRED.'))

    # ============================================================ R1
    rec('')
    rec('=' * 100)
    rec('### R1 -- TRANSPORT. ### **DOES ANY OWNER STATE A MAP, IN EITHER DIRECTION?**')
    rec('=' * 100)
    files = sorted(f for f in os.listdir(D) if f.endswith('.txt'))
    OWN = ['b10_2026-08-17.txt', 'b10_registration_2026-08-17.txt', 'b36_registration_2026-08-18.txt']

    def hits(nd):
        r = []
        for f in files:
            if nd in io.open(os.path.join(D, f), encoding='utf-8', errors='replace').read():
                r.append(f)
        return r

    rec('  ### **NEEDLES DRAWN FROM THE ### OBJECTS ### , NOT FROM b237\'s SENTENCE NAMING THE')
    rec('  ### ABSENCE** -- F-ABSENCE, inheriting b267\'s own disclosure that a needle taken from')
    rec('  ### the naming finds only the naming.')
    h_sq, h_vi, h_op = hits('S_quot'), hits('V_inv'), hits('orthoprojection onto')
    rec('    `S_quot`               -> %d file(s); OWNING: %s'
        % (len(h_sq), ', '.join(f for f in h_sq if f in OWN)))
    rec('    `V_inv`                -> %d file(s)' % len(h_vi))
    rec('    `orthoprojection onto` -> %d file(s)' % len(h_op))
    rec('  ### **files searched : %d `data/*.txt`.**' % len(files))
    ctrl_r1 = bool(len(h_sq) > 0 and len(h_vi) > 0)
    rec('  (C2) POSITIVE CONTROL -- the matcher finds the objects it is looking for : ### **%s**'
        % ('YES' if ctrl_r1 else 'NO'))
    rec('')
    rec('  ### ── **DIRECTION B (`S-bar` side -> `V_inv`): A MAP EXISTS, AND IT IS THE CORPUS\'S.**')
    rec('  ### b10 states ### **"S_quot = orthoprojection onto V_inv"** ### -- an orthoprojection')
    rec('  ### from the ambient function space, and `Son(p,n)` sits in that ambient space.')
    rec('  ### **SO A MAP IS NOT MISSING IN THIS DIRECTION.** ### And b10 states the quantity as')
    rec('  ### an ### AMBIENT ### trace: ### **"T_quot(k) = |Tr(U^k S_quot)|"**.')
    rec('  ### ### ### **WHAT IS BLOCKED IS THEREFORE ### NOT THE MAP ### BUT THE STRUCTURE IT')
    rec('  ### ### ### WOULD HAVE TO CARRY.** ### b10: ### **"THE FOURIER HALF DOES NOT DESCEND"**')
    rec('  ### ### ### , and b227 draws the consequence: ### **"ON V_inv THE TRANSFORM DOES NOT')
    rec('  ### ### ### DESCEND, SO E_1 DOES NOT EXIST THERE."**')
    rec('  ### ### **"BLOCKED" DOES NOT MEAN "NO MAP". ### IT MEANS THE MAP EXISTS AND LOSES THE')
    rec('  ### ### SECTOR THAT DEFINES THE UNIT -- AND THOSE ARE DIFFERENT SENTENCES.**')
    rec('')
    rec('  ### ── **DIRECTION A (`V_inv` -> `S-bar` / `E_1`): (ABSENT), AND THE VERDICT IS AN')
    rec('  ###      OWNER\'S, NOT THIS ACT\'S GREP.**')
    rec('  ### **b228 ALREADY ASKED EXACTLY THIS QUESTION AND ANSWERED IT AT CONTENT:**')
    rec('  ###   READ 1 -- *"DOES ANY OWNER STATE HOW (OR WHETHER) THE QUOTIENT CHANNEL ACTS ON')
    rec('  ###   S-bar OR ON E_1?"* ### -> ### **ABSENT.** ### *"Searched at content."*')
    rec('  ###   ### **"THE ONLY SENTENCES CONNECTING V_inv AND Son ARE b10\'s OWN"**, and')
    rec('  ###   ### ### **"NO OWNER STATES AN ACTION. ### b10 STATES THE OBSTRUCTION AND CALLS IT')
    rec('  ###   ### ### INFORMATIVE."**')
    rec('  ### **SO R1 IS ANSWERED BY b228 AND CORROBORATED HERE AT A STATED SCOPE.** ### This act')
    rec('  ### adds one thing b228 did not separate: ### **THE PROJECTION AND THE ACTION ARE')
    rec('  ### DIFFERENT OBJECTS, AND ONLY THE SECOND IS ABSENT.**')
    r1 = 'ABSENT-FOR-THE-ACTION; PROJECTION EXISTS'

    # ============================================================ R2
    rec('')
    rec('=' * 100)
    rec('### R2 -- RE-DERIVATION ON `S-bar_v`. ### **HALT, AND THE MISSING CHOICE IS NAMED.**')
    rec('=' * 100)
    rec('  ### **WHAT act 9 COMPUTES, WITH ITS SPACE:** ### a ### FIXED-ORBIT COUNT ### *"on')
    rec('  ### V_inv"*, where `V_inv` is *"the model realization of functions on the orbit space')
    rec('  ### `x ~ px` of the non-ball part"* -- b10\'s own words.')
    rec('  ### ### ### **SO THE QUANTITY IS DEFINED ### RELATIVE TO AN ORBIT RELATION ### , AND THE')
    rec('  ### ### ### ORBIT RELATION IS PART OF `V_inv`\'s DEFINITION.**')
    rec('  ### **AND `S-bar_v` CARRIES NO SUCH RELATION IN THE RECORD.** ### It is *"the L^2-closure')
    rec('  ### of the tower\'s union"* with its `E_1` sector; ### **NO OWNER PUTS `x ~ px` ON IT**,')
    rec('  ### and b228\'s READ 1 is the measured statement of that.')
    rec('  ### ### ### **THE RESISTING STEP, NAMED: ### TO RE-DERIVE A FIXED-ORBIT COUNT ON')
    rec('  ### ### ### `S-bar_v` ONE MUST FIRST PUT AN ORBIT STRUCTURE ON `S-bar_v`. ### THAT IS A')
    rec('  ### ### ### CHOICE, IT IS NOT IN THE RECORD, AND CHOOSING IT IS A RULING.**')
    rec('  ### **R2 HALTS HERE AND OFFERS NO SUBSTITUTE** (b250\'s standard: where a step halts the')
    rec('  ### halt is named and no substitute is offered as though it were it).')
    r2 = 'HALT -- the orbit structure on S-bar_v is a choice not in the record'

    # ============================================================ R3
    rec('')
    rec('=' * 100)
    rec('### R3 -- THE STATE ROUTE. ### **DERIVED MISMATCH, NOT AN ARGUED ONE.**')
    rec('=' * 100)
    rec('  ### **THE OPERATORS THE CORPUS STATES ON `S-bar_v` ARE `Pi` AND `M`**, and b227 records')
    rec('  ### the state on them: ### **"on Pi, or on M itself, whose state is 1 because u lies in')
    rec('  ### E_1"**.')
    rec('  ### **WHAT (SPEC-2) DEMANDS:** ### **"IT REDUCES TO `Theta_q`\'s TERMS AT LEVELS')
    rec('  ### `k <= n-1`."**')
    rec('  ### **AND `Theta_q`\'s TERMS THERE ARE NOT CONSTANT:** from act 9\'s own closed form,')
    rec('  ### `tau_q(p,n,k) = p^{-k/2} (p^n - p^k)/(p^n - 1)`, which for `1 <= k <= n-1` lies')
    rec('  ### ### **STRICTLY BETWEEN 0 AND 1** ### -- the numerator is positive and smaller than')
    rec('  ### the denominator, and the prefactor `p^{-k/2} < 1`.')
    rec('  ### ### ### **A CONSTANT `1` DOES NOT REDUCE TO A FAMILY OF VALUES STRICTLY BELOW `1`.**')
    rec('  ### ### ### **(SPEC-2) FAILS FOR EVERY OPERATOR THE CORPUS STATES ON `S-bar_v`, AND THE')
    rec('  ### ### ### MISMATCH IS QUOTED RATHER THAN ARGUED.**')
    rec('  ### **AND b227 ALREADY REFUSED THE TEMPTATION THIS ROUTE OFFERS:** ### producing numbers')
    rec('  ### from `Pi` or `M` would be ### *"numbers about a different operator than the one the')
    rec('  ### ferry names, presented in a table headed by act 9\'s closed form"* ### -- the')
    rec('  ### double-name species. ### **THIS ACT DOES NOT PRODUCE THEM EITHER.**')
    r3 = 'REFUTED FOR THE AVAILABLE OPERATORS -- SPEC-2 fails against a constant state'

    # ============================================================ VERDICT
    rec('')
    rec('=' * 100)
    rec('### THE VERDICT.')
    rec('=' * 100)
    rec('  R1 : ### **%s**' % r1)
    rec('  R2 : ### **%s**' % r2)
    rec('  R3 : ### **%s**' % r3)
    rec('')
    rec('  ### ### ### **VERDICT: ### (HALT-WITH-DOSSIER) ### .**')
    rec('  ### **NO ROUTE CLOSES. ### M-2 IS NOT STATED. ### M-2 REMAINS SPECIFIED-NOT-STATED.**')
    rec('  ### **AND F-STATED WAS NEVER APPROACHED: no constituent of a statement was written,')
    rec('  ### because no route reached the point of writing one.**')
    rec('  ### **F-NOCONSTRUCT HOLDS: ### NO NUMBER WAS COMPUTED FOR ANY CANDIDATE.**')

    # ============================================================ DOSSIER
    rec('')
    rec('=' * 100)
    rec('### THE DOSSIER. ### **FOUR CANDIDATES, EACH WITH WHAT IT WOULD REQUIRE, WHAT IT WOULD')
    rec('###              ENTAIL FOR (SPEC-1)-(SPEC-3), AND ITS COST.**')
    rec('###              ### **NO RECOMMENDATION. ### NO CANDIDATE ADOPTED. ### THE AUTHOR RULES.**')
    rec('=' * 100)
    dossier = [
        dict(name='C1 -- THE AMBIENT PAIRING',
             what='Read the quotient channel as the AMBIENT operator b10 already writes, '
                  '`U^k S_quot`, and pair it against `u_v` in the ambient space: `<U^k S_quot '
                  'u_v, u_v>`.',
             requires='A RULING that this ambient object IS the intended per-place quantity. '
                      'It is arithmetically well-defined -- b10 writes `Tr(U^k S_quot)`, an '
                      'ambient trace -- but it is NOT act 9`s `tau_q`, which is a fixed-orbit '
                      'count ON `V_inv`.',
             entails='(SPEC-2) would have to be CHECKED, not assumed: nothing says the ambient '
                     'pairing reduces to `Theta_q`s terms at `k <= n-1`. (SPEC-1) unknown until '
                     'checked at `k = n`. (SPEC-3) inherits b268s `p = 2` step-up condition.',
             cost='A ruling, then one exact computation per cell. LOWEST COST OF THE FOUR.',
             risk='b227 refused numbers of exactly this shape as the DOUBLE-NAME species. The '
                  'ruling would have to say why this one is not that.'),
        dict(name='C2 -- EXTEND THE PROJECTION TO AN ACTION',
             what='Take b10`s `S_quot` as the transport and ask what survives of the sector '
                  'along it.',
             requires='A RESULT: what `S_quot` does to `E_1`. b10 says the Fourier half does '
                      'not descend, so the sector is not preserved; what is NOT stated is what '
                      'IS preserved.',
             entails='If nothing of the sector survives, `u_v`s defining property is gone and '
                     '(SPEC-2) has no anchor. If a residue survives, it would have to be named '
                     'before any SPEC is checked.',
             cost='A result on the image of `E_1` under `S_quot`. MEDIUM.',
             risk='b268s A1 result is about `u_v` IN `E_1`; it does not transfer to `S_quot u_v` '
                  'without this result.'),
        dict(name='C3 -- PUT AN ORBIT STRUCTURE ON `S-bar_v`',
             what='R2`s missing choice: equip `S-bar_v` with a relation playing the role of '
                  '`x ~ px`, then re-derive the fixed-orbit count there.',
             requires='A CONSTRUCTION and a RULING on WHICH relation. Neither is in the record.',
             entails='If it succeeded it would give a per-place number defined at `k = n` as '
                     'well as below -- which is exactly what (SPEC-1) needs and what act 9`s '
                     'range cannot supply.',
             cost='HIGHEST. New mathematics, and a choice that must be justified as canonical.',
             risk='b267s TEST 1 shows the `k = n` zero is the closed forms OWN arithmetic; a '
                  'new orbit structure would have to give a DIFFERENT count there, which means '
                  'it is not a re-indexing but a different object.'),
        dict(name='C4 -- CHANGE THE UNIT',
             what='Choose a reference vector that survives descent -- i.e. drop the `E_1` '
                  'characterisation.',
             requires='A RULING abandoning b226`s stated choice.',
             entails='b226`s `u_p` and b268`s nonvanishing would no longer be the object; A1 '
                     'would have to be re-run for the new unit. (SPEC-3)s `p = 2` condition '
                     'would have to be re-derived.',
             cost='Re-opens A1. HIGH, and it discards a result just paid.',
             risk='b226`s G-NORM and the C0 condition were established FOR that unit; a new '
                  'unit inherits none of it.'),
    ]
    for c in dossier:
        rec('')
        rec('  ### **%s**' % c['name'])
        rec('    WHAT     : %s' % c['what'])
        rec('    REQUIRES : %s' % c['requires'])
        rec('    ENTAILS  : %s' % c['entails'])
        rec('    COST     : %s' % c['cost'])
        rec('    RISK     : %s' % c['risk'])
    rec('')
    rec('  ### ### **THE FOUR ARE NOT RANKED AND NOT RECOMMENDED. ### THEY DIFFER IN KIND -- C1')
    rec('  ### ### AND C4 WANT A ### RULING ### , C2 WANTS A ### RESULT ### , C3 WANTS BOTH -- AND')
    rec('  ### ### WHICH KIND OF THING THE CAMPAIGN SHOULD SPEND NEXT IS THE AUTHOR\'S CALL, NOT')
    rec('  ### ### THIS SEAT\'S.**')

    # ============================================================ SIZE
    rec('')
    rec('=' * 100)
    rec('### THE SIZE TARGET, RESTATED AS A TARGET ONLY.')
    rec('=' * 100)
    rec('  b262\'s first-level family mass: ### **73.9594% at `a^2 = 1e2` to 99.9537% at')
    rec('  `a^2 = 1e8`.**')
    rec('  ### **IT IS COMPARED TO NOTHING HERE, BECAUSE NO STATEMENT WAS FIXED.** ### The')
    rec('  ### registration ordered the comparison as a CONTROL ### AFTER ### a statement, never')
    rec('  ### before, and there is no statement. ### **NO FIT, NO CANDIDATE VALUE, NO COMPARISON.**')

    rec('')
    rec('=' * 100)
    rec('### THE RUN\'S VERDICTS.')
    rec('=' * 100)
    rec('  F-QUOTE       : ### **%s**' % ('DID NOT FIRE' if fquote else 'FIRED'))
    rec('  F-NOCONSTRUCT : ### **DID NOT FIRE -- no candidate value computed**')
    rec('  F-STATED      : ### **NOT REACHED -- no statement was written**')
    rec('  ### **VERDICT: (HALT-WITH-DOSSIER). ### M-2 REMAINS SPECIFIED-NOT-STATED.**')
    rec('  ### **QUOTED-N: %d owner quotations; %d corpus files searched; %d dossier candidates.**'
        % (len(QUOTES), len(files), len(dossier)))
    rec('=' * 100)

    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump(dict(f_quote=fquote, unfindable=len(bad), control=ctrl, control_r1=ctrl_r1,
                   r1=r1, r2=r2, r3=r3, verdict='HALT-WITH-DOSSIER',
                   files_searched=len(files), n_candidates=len(dossier),
                   s_quot_files=h_sq, dossier=[c['name'] for c in dossier]),
              io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    return 0 if fquote else 1


if __name__ == '__main__':
    sys.exit(main())
