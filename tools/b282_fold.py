# -*- coding: utf-8 -*-
"""b282_fold.py -- THE FOLD, b266-b281. ### THE RUN.

### **A FILINGS ACT. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED. ### NO NEW MATHEMATICS.**

### ### **THE DESIGN POINT, INHERITED FROM b266 AND RESTATED BECAUSE IT IS THE WHOLE REASON THIS
### ### FILE EXISTS: ### THE OBSTACLE TABLE BELOW IS THE SINGLE SOURCE OF TRUTH, AND THIS RUNNER
### ### EMITS THE MARKDOWN THE FOLD PASTES.** ### So a quotation that fails F-QUOTE never reaches
### `FINDINGS.md` at all. ### **A CHECK THAT RUNS AFTER THE WRITING CAN ONLY REPORT A PARAPHRASE;
### ONE THAT GENERATES THE WRITING CANNOT EMIT ONE.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = r'D:\relay'
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
BANK = os.path.join(D, 'b282_run.txt')
ROWS = os.path.join(D, 'b282_rows.json')
FOLD_MD = os.path.join(D, 'b282_fold_emitted.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')

sys.path.insert(0, os.path.join(ROOT, 'tools'))
import lore_rules  # noqa: E402

ARC = ['b%d' % i for i in range(266, 282)]

# ### An act may own SEVERAL files. ### The quotation must be verbatim in ONE OF ITS OWN.
SRC = {
    'b266': ['b266_state_of_the_shadow.txt', 'b266_filings.txt'],
    'b267': ['b267_aggregation_source.txt', 'b267_filings.txt'],
    'b268': ['b268_generator_nonvanishing.txt', 'b268_filings.txt'],
    'b269': ['b269_m2_statement.txt', 'b269_filings.txt'],
    'b270': ['b270_ambient_pairing_properties.txt'],
    'b271': ['b271_top_level_no_go.txt'],
    'b272': ['b272_escape_class.txt'],
    'b273': ['b273_spec2_range.txt'],
    'b274': ['b274_straddle_generally.txt'],
    'b275': ['b275_the_rule_stated.txt'],
    'b276': ['b276_size_equivalence_tension.txt'],
    'b277': ['b277_aggregation_stated.txt'],
    'b278': ['b278_space_level_barrier.txt'],
    'b279': ['b279_the_local_space.txt'],
    'b280': ['b280_the_consequence.txt'],
    'b281': ['b281_the_compression.txt'],
}

# ### (act, what it is, the QUOTATION, the grade AS ITS ACT LEFT IT)
# ### ### **EVERY QUOTATION IS CHECKED VERBATIM AGAINST ITS ACT'S OWN FILES BEFORE EMISSION.**
# ### ### **THE FOURTH COLUMN IS TRANSCRIBED, NEVER DECIDED HERE. ### THIS ACT MOVES NO GRADE.**
OBSTACLES = [
    ('b266', 'the fold law it minted',
     'NO GRADE MOVED. ### NO ACT RE-VERDICTED.',
     '**(FILED)** -- a filings act'),

    ('b267', 'where the term cannot come from',
     'IT CANNOT COME FROM THE TRACE SIDE.',
     '**(PARTIAL)**, not (SUPPORTED)'),
    ('b267', 'the arithmetic at the top level, with the convention read above it',
     'AT `k = n`: THE EXPRESSION RETURNS `0` AT EVERY CELL.',
     '**(PARTIAL)**'),

    ('b268', "b226's owed step",
     'OWED STEP IS ### PAID',
     '**PAID** -- and (SPEC-1) is not touched'),
    ('b268', 'the support, derived rather than observed',
     'SO THE ZERO SET IS EXACTLY THE `q` MULTIPLES OF `q`, AND `support(u_p) = N - q`.',
     '**DERIVED**; the six-cell table is a control on the proof'),

    ('b269', 'the dossier verdict',
     '(HALT-WITH-DOSSIER). ### NO ROUTE CLOSES.',
     '**(HALT-WITH-DOSSIER)** -- nothing constructed'),
    ('b269', 'what the exclusions do and do not do',
     'THEY EXCLUDE; THEY DO NOT DETERMINE',
     '**(EXCLUSION)**, separated from "no map"'),

    ('b270', 'C1 dead by the operator\u2019s own index law',
     'THE PAIRING IS EXACTLY ZERO AT k = n',
     '**REFUTED** -- C1 struck'),
    ('b270', 'the scope it declined to claim, which b280 later supplied',
     "NOT A STATEMENT ABOUT THE INFINITE OBJECT, AND b10's OWN REGISTERED MODEL LIMITATION",
     'scope stated by its own act, not weakened'),

    ('b271', 'the escape',
     'MEMBERSHIP DOES NOT FORCE VANISHING ON THE BALL',
     '**(ESCAPE)** -- scoped to ambient `E_1`, one finite level'),
    ('b271', 'what the escape is not',
     'STATEMENT ABOUT SCOPE AND NOT A CHANGE OF VERDICT.',
     'b270 **NOT** re-verdicted'),

    ('b272', 'the class, characterized',
     '(CLASS NONEMPTY BUT BLOCKED). ### BLOCKED AT K5 -- (SPEC-2).',
     '**(CLASS NONEMPTY BUT BLOCKED)**'),
    ('b272', 'the orthogonality, and whose fact it is',
     'A FACT ABOUT `g_0`, NOT ABOUT THE CLASS',
     'scoped to the vector, not the class'),

    ('b273', 'the form, decided from its own definition',
     'THE FORM IS NEITHER HERMITIAN NOR',
     '**DECIDED** -- not assumed'),
    ('b273', 'the straddle, by the intermediate value theorem',
     '`2/3` IS ATTAINED',
     '**ATTAINED** at `(2,2)`'),

    ('b274', "where (SPEC-2) has content at all",
     "(SPEC-2)'s range is `1 <= k <= n-1`, which at `n = 1` is ### EMPTY",
     '**(STRADDLE PARTIAL)** -- only `(2,2)` carries content under b226\u2019s rule'),
    ('b274', 'the closed form for the escape vector',
     '`R(g_0) = (q - 1) / (2(q + 1))`, INDEPENDENT OF `k`.',
     '**DERIVED** generally'),

    ('b275', 'the rule',
     '(RULE STATED). ### ONE RULE, WRITTEN WHOLE, EVERY CONSTITUENT UNFOLDED.',
     '**(RULE STATED)** -- and its object is orthogonal'),
    ('b275', 'the index, derived and not picked',
     'the canonical index (`c = 0`, derived)',
     '**DERIVED**, not selected by taste'),

    ('b276', 'the trade',
     '(INCOMPATIBLE)',
     '**(INCOMPATIBLE)** -- equivalence and mass'),
    ('b276', 'the selection note',
     'THE SELECTION NOTE. ### PROMOTED, AT THE GRADE THE DERIVATION SUPPORTS.',
     '**PROMOTED**, with its inherited imports travelling'),

    ('b277', 'the block',
     "(BLOCKED). ### THE FAILING CONDITION IS von Neumann's Def 3.3.1 CLAUSE (i)",
     '**(BLOCKED)** at membership, every spec passing'),

    ('b278', 'the tower',
     '(ABSENT), WITH A POSITIVE CONTROL ON THE ABSENCE',
     '**(ABSENT)** -- and the search was controlled'),
    ('b278', "the owning act\u2019s own disclaimer",
     'nothing here constructs a limit object, and none is',
     'quoted, not paraphrased'),

    ('b279', 'the construction',
     'VERDICT: (CONSTRUCTED)',
     '**(CONSTRUCTED)** -- the `Son` tower, named by the keystone'),
    ('b279', 'the boundary the construction carries',
     'AT EVERY FINITE PLACE AND AT NO INFINITE ONE',
     'finite places only; `\u221e` specified separately'),

    ('b280', 'the barrier',
     'VERDICT: (BARRIER)',
     '**(BARRIER)** at grade **DERIVES**'),
    ('b280', 'the boundary, in the verdict\u2019s own words',
     'THIS REACHES THE FINITE PLACES AND NO OTHER',
     'scope carried, not footnoted'),

    ('b281', 'the compression',
     'VERDICT: (COMPRESSION ZERO)',
     '**(COMPRESSION ZERO)** at grade **DERIVES**'),
    ('b281', 'the stronger statement, and why the supports are complementary',
     'THE LEFT PROJECTION ALONE KILLS THE OPERATOR',
     '`P_S A = 0` -- disjoint supports'),
]


def norm(s):
    """### WHITESPACE ONLY. ### **NO CASE FOLDING, NO PUNCTUATION STRIPPING, NO NEAR-MATCHING.**
    ### A looser normaliser would be a different check, and a check nobody registered."""
    return re.sub(r'\s+', ' ', s).strip()


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b282 RUN -- THE FOLD, b266-b281. ### THE CONTROLS.')
    rec('### ### **A FILINGS ACT. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED.**')
    rec('=' * 100)

    # ==================================================================== F-QUOTE
    rec('')
    rec('### F-QUOTE -- EVERY OBSTACLE VERBATIM IN AN OWNING ACT\u2019S OWN FILE.')
    rec('=' * 100)
    cache = {}
    for act, files in SRC.items():
        blob = ''
        for f in files:
            p = os.path.join(D, f)
            if os.path.exists(p):
                blob += io.open(p, encoding='utf-8', errors='replace').read() + '\n'
        cache[act] = norm(blob)
    bad = []
    for act, what, quote, grade in OBSTACLES:
        ok = norm(quote) in cache[act]
        if not ok:
            bad.append((act, what, quote))
        rec('  %-6s %-52s %s' % (act, what[:52], 'YES' if ok else '### NOT FOUND ###'))
    fquote = (len(bad) == 0)
    rec('  ### **%d quotations checked, %d unfindable.**' % (len(OBSTACLES), len(bad)))
    for act, what, quote in bad:
        rec('    ### NOT FOUND in %s : %r' % (act, quote[:96]))

    # ### POSITIVE CONTROL: an altered quotation MUST be unfindable.
    tam = OBSTACLES[1][2].replace('TRACE SIDE', 'TRACE SIDEX')
    ctrl = norm(tam) not in cache[OBSTACLES[1][0]]
    rec('  (C1) THE CHECKER DISCRIMINATES -- a deliberately altered quotation is reported')
    rec('       unfindable : ### **%s** ### (must be YES)' % ('YES' if ctrl else 'NO'))
    rec('       ### **A MATCHER THAT NEVER MISSES IS NOT MATCHING.**')
    rec('  ### ### **F-QUOTE %s**'
        % ('DID NOT FIRE -- every obstacle is a quotation, checked and not asserted.'
           if fquote else 'FIRED. ### THE FOLD IS WRONG AND NOTHING IS EMITTED.'))

    # ==================================================================== F-COUNT
    rec('')
    rec('=' * 100)
    rec('### F-COUNT -- THE ARC RECONCILES.')
    rec('=' * 100)
    nums = sorted(int(a[1:]) for a in ARC)
    contiguous = (nums == list(range(nums[0], nums[-1] + 1)))
    covered = sorted({o[0] for o in OBSTACLES})
    fcount = bool(len(ARC) == 16 and contiguous and covered == sorted(ARC))
    rec('  arc span declared           : ### **b%d .. b%d** ### (%d acts)'
        % (nums[0], nums[-1], len(nums)))
    rec('  contiguous, nothing skipped : ### **%s**' % contiguous)
    rec('  acts carrying an obstacle   : ### **%d of %d**' % (len(covered), len(ARC)))
    if covered != sorted(ARC):
        rec('  ### ACTS WITH NO OBSTACLE : %s' % sorted(set(ARC) - set(covered)))
    rec('  ### ### **F-COUNT %s**'
        % ('DID NOT FIRE -- sixteen acts, contiguous, every one represented.'
           if fcount else 'FIRED. ### THE ARC AND THE ROWS DISAGREE.'))

    # ==================================================================== F-INCIDENT
    rec('')
    rec('=' * 100)
    rec('### F-INCIDENT -- EVERY LORE RULE CARRIES ITS SCAR.')
    rec('=' * 100)
    lore_ok, lore_out = lore_rules.self_test(verbose=False)
    nmech, njudge = len(lore_rules.MECHANIZED), len(lore_rules.JUDGEMENT)
    missing = [r['rule'] for r in lore_rules.MECHANIZED + lore_rules.JUDGEMENT
               if 'b' not in r['incident']]
    finc = lore_ok and not missing
    rec('  mechanized rules (gates that can fire) : ### **%d**' % nmech)
    rec('  judgement rules (NOTHING enforces)     : ### **%d**' % njudge)
    rec('  rules missing an incident              : ### **%d**' % len(missing))
    rec('  lore fixtures, both polarities         : ### **%s**' % ('PASS' if lore_ok else 'FAIL'))
    rec('  ### ### **F-INCIDENT %s**'
        % ('DID NOT FIRE -- every rule names an act. *"A rule without its incident is a '
           'preference."*' if finc else 'FIRED. ### A RULE CARRIES NO INCIDENT.'))

    # ==================================================================== F-NOGRADE
    rec('')
    rec('=' * 100)
    rec('### F-NOGRADE -- THE FOLD IS PURELY ADDITIVE.')
    rec('### ### **A FOLD THAT EDITED AN EXISTING GRADE WOULD BE A RE-VERDICT WEARING A FOLD\u2019S')
    rec('### ### CLOTHES.**')
    rec('=' * 100)
    p = subprocess.run(['git', '-C', PP, 'diff', '--numstat', 'HEAD', '--', 'FINDINGS.md'],
                       capture_output=True, text=True)
    added = removed = 0
    if p.stdout.strip():
        parts = p.stdout.split()
        added, removed = int(parts[0]), int(parts[1])
    fnograde = (removed == 0)
    rec('  FINDINGS.md vs HEAD : ### **+%d / -%d**' % (added, removed))
    rec('  ### ### **F-NOGRADE %s**'
        % ('DID NOT FIRE -- no line deleted, no tag rewritten; PURELY ADDITIVE.'
           if fnograde else 'FIRED. ### A LINE WAS DELETED OR REWRITTEN.'))

    # ==================================================================== F-NOSHADOW
    rec('')
    rec('=' * 100)
    rec('### F-NOSHADOW -- FILINGS ONLY; NO NEW MATHEMATICS.')
    rec('=' * 100)
    lean = []
    for repo in (ROOT, SIDE, PP):
        q = subprocess.run(['git', '-C', repo, 'status', '--porcelain'],
                           capture_output=True, text=True)
        lean += [l for l in q.stdout.splitlines() if l.strip().endswith('.lean')]
    fnoshadow = (len(lean) == 0)
    rec('  `.lean` files moved across all three repos : ### **%d**' % len(lean))
    for l in lean:
        rec('    ### MOVED : %s' % l)
    rec('  ### ### **F-NOSHADOW %s**'
        % ('DID NOT FIRE -- this act compiles nothing and formalizes nothing.'
           if fnoshadow else 'FIRED. ### A LEAN FILE MOVED IN A FILINGS-ONLY ACT.'))

    # ==================================================================== EMIT
    rec('')
    rec('=' * 100)
    rec('### THE EMISSION.')
    rec('=' * 100)
    if fquote and fcount:
        md = ['| act | obstacle | quoted from its owning act | grade as its act left it |',
              '|:--|:--|:--|:--|']
        for act, what, quote, grade in OBSTACLES:
            md.append('| **%s** | %s | *"%s"* | %s |'
                      % (act, what, quote.replace('|', '\\|'), grade))
        io.open(FOLD_MD, 'w', encoding='utf-8').write('\n'.join(md) + '\n')
        rec('  emitted %d rows to `data/b282_fold_emitted.md`' % len(OBSTACLES))
        rec('  ### **THE FOLD PASTES THIS TABLE. ### IT DOES NOT RETYPE IT.**')
    else:
        rec('  ### **NOTHING EMITTED -- A GATE FIRED.**')

    rec('')
    rec('=' * 100)
    rec('### THE RUN\u2019S VERDICTS.')
    rec('=' * 100)
    for nm, v in [('F-QUOTE    (obstacles verbatim)', fquote),
                  ('F-COUNT    (arc reconciles)', fcount),
                  ('F-INCIDENT (lore carries scars)', finc),
                  ('F-NOGRADE  (purely additive)', fnograde),
                  ('F-NOSHADOW (nothing formalized)', fnoshadow)]:
        rec('  %-34s : ### **%s**' % (nm, 'DID NOT FIRE' if v else 'FIRED'))
    rec('  DISCRIMINATION CONTROL             : ### **%s**' % ('PASS' if ctrl else 'FAIL'))
    rec('  ### **QUOTED-N: %d obstacles across %d acts; %d mechanized + %d judgement rules.**'
        % (len(OBSTACLES), len(covered), nmech, njudge))
    rec('=' * 100)

    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump(dict(arc=ARC, n_obstacles=len(OBSTACLES), unfindable=len(bad),
                   acts_covered=covered, n_mechanized=nmech, n_judgement=njudge,
                   rules_missing_incident=missing, findings_added=added,
                   findings_removed=removed, lean_moved=len(lean), f_quote=fquote,
                   f_count=fcount, f_incident=finc, f_nograde=fnograde,
                   f_noshadow=fnoshadow, control_discriminates=ctrl),
              io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    return 0 if (fquote and fcount and finc and fnograde and fnoshadow and ctrl) else 1


if __name__ == '__main__':
    sys.exit(main())
