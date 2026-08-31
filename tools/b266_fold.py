# -*- coding: utf-8 -*-
"""b266_fold.py -- THE STATE OF THE SHADOW. ### THE RUN.

### **A FILINGS ACT. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED. ### NO NEW MATHEMATICS.**
### Every bar was fixed in `data/b266_registration_2026-08-31.txt`, SEALED `dbb5cb0d...`,
### term-scanned and satisfiability-checked BEFORE the seal.

### ### **THE DESIGN POINT, AND IT IS THE WHOLE REASON THIS FILE EXISTS:**
### ### **THE OBSTACLE TABLE BELOW IS THE SINGLE SOURCE OF TRUTH, AND THIS RUNNER ### EMITS ###
### ### THE MARKDOWN THE FOLD PASTES.** ### So a quotation that fails F-QUOTE never reaches
### `FINDINGS.md` at all -- the check is not a review of the document, it is the document's
### generator. ### **A CHECK THAT RUNS AFTER THE WRITING CAN ONLY REPORT A PARAPHRASE; ONE THAT
### GENERATES THE WRITING CANNOT EMIT ONE.**
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
TC = r'D:\MY-DOwnloads\TECHNE-Core'
BANK = os.path.join(D, 'b266_run.txt')
ROWS = os.path.join(D, 'b266_rows.json')
FOLD_MD = os.path.join(D, 'b266_fold_emitted.md')
LORE = os.path.join(TC, 'modules', '2026-08', 'HARNESS_LORE.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')

ARC = ['b256', 'b257', 'b258', 'b259', 'b260', 'b261', 'b262', 'b263', 'b264', 'b265']

SRC = {
    'b256': 'b256_contribution_map.txt',
    'b257': 'b257_methodology_sweep.txt',
    'b258': 'b258_history_inventory.txt',
    'b259': 'b259_blob_sensitivity.txt',
    'b260': 'b260_junction_sign.txt',
    'b261': 'b261_e2even_monotone.txt',
    'b262': 'b262_junction_limit.txt',
    'b263': 'b263_top_level_silence.txt',
    'b264': 'b264_eps_even_decay.txt',
    'b265': 'b265_nq_ceiling_sweep.txt',
}

# ### THE OBSTACLE TABLE. ### (act, what it is, the QUOTATION, the grade as its act left it)
# ### ### **EVERY QUOTATION IS CHECKED VERBATIM AGAINST `SRC[act]` BEFORE IT IS EMITTED.**
OBSTACLES = [
    ('b260', 'J1 -- the per-term inequality',
     'DERIVES BY TERMWISE DOMINATION',
     '**DERIVES** -- the arc\u2019s first derived limit'),
    ('b260', 'J1 -- why the ferry\u2019s expected mechanism was refused',
     '`2 log p` IS ON BOTH SIDES.',
     'refuted **by reading the two instruments**, not by a measurement'),
    ('b261', 'J2 -- the monotone reading',
     '`E2even` DOES NOT DECREASE MONOTONICALLY',
     '**REFUTED**'),
    ('b261', 'J2 -- where the turn sits',
     'SO THERE IS AN `a_0 > 1` BELOW WHICH `E2even` RISES, AND J2 AS STATED IS FALSE.',
     '`a_0` in `(1.75, 2]`; b255\u2019s ladder starts at `a^2 = 2`'),
    ('b262', 'J3 -- the junction along the cutoff limit',
     'THE JUNCTION DIVERGES ALONG THE CUTOFF LIMIT.',
     '**(GROWS)**'),
    ('b263', 'the branch the specification is about',
     'THE SPECIFICATION BELOW IS FOR THE FIRST BRANCH ONLY AND IS VACUOUS ON THE SECOND.',
     '**SPECIFICATION, CONDITIONAL** -- the branch is not decided'),
    ('b264', 'J4 -- the envelope, and the wall it routes around',
     'IT CONTAINS NO ENDPOINT VALUE `xi_n(1)^2`, SO THE',
     '**(DECAYS, rate/envelope derived)**'),
    ('b265', 'the certification of the arc\u2019s instrument',
     'ZERO CELLS FALL ABOVE THE CEILING, ACROSS BOTH ACTS.',
     '**MEASUREMENT, NOT VERDICT**'),
    ('b256', 'the map\u2019s own limit on itself',
     'THE MAP *STATES* GRADES AND CONFERS NONE',
     'no grade moved'),
    ('b257', 'the guard exception, in the author\u2019s words',
     'A hook constrains a habit; it does not constrain a decision.',
     'author-ruled exception; the act resumed and closed'),
    ('b258', 'the custody measurement\u2019s subject',
     'ADDED BY `df2f54d` (2026-08-18)',
     '**READ-ONLY THROUGHOUT**; no recommendation made'),
    ('b259', 'the six blobs, graded',
     'ALL SIX REBUILT BYTE-FOR-BYTE: sha256 EQUAL, SIZE EQUAL, SIX FOR SIX.',
     '**READ-ONLY THROUGHOUT**; no recommendation made'),
]


def norm(s):
    """### WHITESPACE ONLY. ### **NO CASE FOLDING, NO PUNCTUATION STRIPPING, NO NEAR-MATCHING** --
    ### the registration fixed that and a looser normaliser would be a different check."""
    return re.sub(r'\s+', ' ', s).strip()


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b266 RUN -- THE STATE OF THE SHADOW. ### THE CONTROLS.')
    rec('### Registration SEALED (`dbb5cb0d...`), TERM-SCANNED and SATISFIABILITY-CHECKED')
    rec('### ### **BEFORE** ### the seal. ### Bars fixed there.')
    rec('### ### **A FILINGS ACT. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED.**')
    rec('=' * 100)

    # ============================================================ F-QUOTE
    rec('')
    rec('### F-QUOTE -- EVERY OBSTACLE VERBATIM IN ITS OWNING ACT. ### **THE FOLD RULES FORBID')
    rec('###          PARAPHRASE, AND THIS IS THAT RULE MECHANIZED.**')
    rec('=' * 100)
    cache = {}
    for act, f in SRC.items():
        cache[act] = norm(io.open(os.path.join(D, f), encoding='utf-8', errors='replace').read())
    rec('  %-7s %-46s %s' % ('act', 'obstacle', 'verbatim in its owning act?'))
    rec('  ' + '-' * 92)
    bad = []
    for act, what, quote, grade in OBSTACLES:
        ok = norm(quote) in cache[act]
        if not ok:
            bad.append((act, what, quote))
        rec('  %-7s %-46s %s' % (act, what[:46], 'YES' if ok else '### NOT FOUND ###'))
    fquote = (len(bad) == 0)
    rec('  ### **%d quotations checked, %d unfindable.**' % (len(OBSTACLES), len(bad)))
    for act, what, quote in bad:
        rec('    ### NOT FOUND in %s : %r' % (SRC[act], quote[:90]))
    rec('  ### ### **F-QUOTE %s**'
        % ('DID NOT FIRE -- every obstacle is a quotation, checked and not asserted.'
           if fquote else 'FIRED. ### THE FOLD IS WRONG AND NOTHING IS EMITTED.'))

    # ### POSITIVE CONTROL: an altered quotation MUST be unfindable.
    tampered = OBSTACLES[0][2].replace('DOMINATION', 'DOMINATIONX')
    ctrl = norm(tampered) not in cache[OBSTACLES[0][0]]
    rec('  (C1) THE CHECKER DISCRIMINATES -- a deliberately altered quotation is reported')
    rec('       unfindable : ### **%s** ### (must be YES)' % ('YES' if ctrl else 'NO'))
    rec('       ### **A MATCHER THAT NEVER MISSES IS NOT MATCHING.**')

    # ============================================================ F-COUNT
    rec('')
    rec('=' * 100)
    rec('### F-COUNT -- THE ARC RECONCILES.')
    rec('=' * 100)
    nums = sorted(int(a[1:]) for a in ARC)
    contiguous = (nums == list(range(nums[0], nums[-1] + 1)))
    covered = sorted({o[0] for o in OBSTACLES})
    fcount = bool(len(ARC) == 10 and contiguous and covered == sorted(ARC))
    rec('  arc span declared          : ### **b%d .. b%d** ### (%d acts)' % (nums[0], nums[-1], len(nums)))
    rec('  contiguous, nothing skipped: ### **%s**' % contiguous)
    rec('  acts carrying an obstacle  : ### **%d of %d**' % (len(covered), len(ARC)))
    rec('  ### ### **F-COUNT %s**'
        % ('DID NOT FIRE -- ten acts, contiguous, every one represented.'
           if fcount else 'FIRED. ### THE ARC AND THE ROWS DISAGREE.'))

    # ============================================================ F-INCIDENT
    rec('')
    rec('=' * 100)
    rec('### F-INCIDENT -- EVERY LORE RULE CARRIES ITS SCAR.')
    rec('=' * 100)
    finc, nrules, missing = True, 0, []
    if os.path.exists(LORE):
        txt = io.open(LORE, encoding='utf-8', errors='replace').read()
        blocks = re.split(r'\n## ', txt)
        for b in blocks[1:]:
            head = b.split('\n', 1)[0]
            nrules += 1
            if not re.search(r'\bb\d{2,3}\b', b):
                missing.append(head[:60])
        finc = (len(missing) == 0)
        rec('  rules in HARNESS_LORE.md            : ### **%d**' % nrules)
        rec('  rules with NO owning-act citation   : ### **%d**' % len(missing))
        for m in missing:
            rec('    ### NO INCIDENT : %s' % m)
    else:
        finc = False
        rec('  ### **HARNESS_LORE.md NOT FOUND -- F-INCIDENT CANNOT BE READ.**')
    rec('  ### ### **F-INCIDENT %s**'
        % ('DID NOT FIRE -- every rule names an act. ### *"a rule without its incident is a '
           'preference."*' if finc else 'FIRED. ### A RULE CARRIES NO INCIDENT.'))

    # ============================================================ F-NOGRADE
    rec('')
    rec('=' * 100)
    rec('### F-NOGRADE -- THE FOLD IS PURELY ADDITIVE. ### **A FOLD THAT EDITED AN EXISTING GRADE')
    rec('###            WOULD BE A RE-VERDICT WEARING A FOLD\'S CLOTHES.**')
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
        % ('DID NOT FIRE -- no line deleted, no tag rewritten; the change is PURELY ADDITIVE.'
           if fnograde else 'FIRED. ### A LINE WAS DELETED OR REWRITTEN.'))

    # ============================================================ F-NOSHADOW
    rec('')
    rec('=' * 100)
    rec('### F-NOSHADOW -- THE SCOPE HELD. ### **FILINGS ONLY; NO NEW MATHEMATICS.**')
    rec('=' * 100)
    lean = []
    for repo in (ROOT, r'D:\SIDE-global-section', PP):
        q = subprocess.run(['git', '-C', repo, 'status', '--porcelain'],
                           capture_output=True, text=True)
        lean += [l for l in q.stdout.splitlines() if l.strip().endswith('.lean')]
    fnoshadow = (len(lean) == 0)
    rec('  `.lean` files moved across all three repos : ### **%d**' % len(lean))
    for l in lean:
        rec('    ### MOVED : %s' % l)
    rec('  ### ### **F-NOSHADOW %s**'
        % ('DID NOT FIRE -- this act compiles nothing and formalizes nothing, as registered.'
           if fnoshadow else 'FIRED. ### A LEAN FILE MOVED IN A FILINGS-ONLY ACT.'))

    # ============================================================ EMIT
    rec('')
    rec('=' * 100)
    rec('### THE EMISSION. ### **THE FOLD\'S OBSTACLE TABLE, GENERATED FROM THE VERIFIED QUOTES.**')
    rec('=' * 100)
    if fquote:
        md = ['| act | obstacle | quoted from its owning act | grade as its act left it |',
              '|:--|:--|:--|:--|']
        for act, what, quote, grade in OBSTACLES:
            md.append('| **%s** | %s | *"%s"* | %s |'
                      % (act, what, quote.replace('|', '\\|'), grade))
        io.open(FOLD_MD, 'w', encoding='utf-8').write('\n'.join(md) + '\n')
        rec('  emitted %d rows to `data/b266_fold_emitted.md`' % len(OBSTACLES))
        rec('  ### **THE FOLD PASTES THIS TABLE. ### IT DOES NOT RETYPE IT.**')
    else:
        rec('  ### **NOTHING EMITTED -- F-QUOTE FIRED.**')

    rec('')
    rec('=' * 100)
    rec('### THE RUN\'S VERDICTS.')
    rec('=' * 100)
    rec('  F-QUOTE    (obstacles verbatim)  : ### **%s**' % ('DID NOT FIRE' if fquote else 'FIRED'))
    rec('  F-COUNT    (arc reconciles)      : ### **%s**' % ('DID NOT FIRE' if fcount else 'FIRED'))
    rec('  F-INCIDENT (lore carries scars)  : ### **%s**' % ('DID NOT FIRE' if finc else 'FIRED'))
    rec('  F-NOGRADE  (purely additive)     : ### **%s**' % ('DID NOT FIRE' if fnograde else 'FIRED'))
    rec('  F-NOSHADOW (nothing formalized)  : ### **%s**' % ('DID NOT FIRE' if fnoshadow else 'FIRED'))
    rec('  ### **QUOTED-N: %d obstacles across %d acts; %d lore rules read.**'
        % (len(OBSTACLES), len(covered), nrules))
    rec('=' * 100)

    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump(dict(arc=ARC, n_obstacles=len(OBSTACLES), unfindable=len(bad),
                   acts_covered=covered, n_rules=nrules, rules_missing_incident=missing,
                   findings_added=added, findings_removed=removed, lean_moved=len(lean),
                   f_quote=fquote, f_count=fcount, f_incident=finc,
                   f_nograde=fnograde, f_noshadow=fnoshadow, control_discriminates=ctrl),
              io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    return 0 if (fquote and fcount and fnograde and fnoshadow) else 1


if __name__ == '__main__':
    sys.exit(main())
