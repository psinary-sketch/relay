# -*- coding: utf-8 -*-
"""b580_record.py -- THE ACT'S RECORD TOOL, UNDER (R190). ### ONE SUBCOMMAND PER BANK.

### ### b580: LANE THREE, ACT EIGHT -- CP-7 ACT FIVE, THE EDITION OF ADDITIVE_MULTIPLICATIVE_CONSPIRACY; THE RE-PIN STEP.
### Subcommands write only `data/b580_*` unless the docstring names another file. Every bank is written through `put_txt` /
### `put_json` (encode first, then a temp file, then `os.replace`). This act makes no platform call. ### The template is
### b579_record.py.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'a1de9dc'
MIRROR_PIN = '192077f'
CUR = 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md'
ED = 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY_v0_2_4.md'
PATHS7 = 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md'
FOUND5 = 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md'
B578_BANK = 'b578_edition_PATHS.txt'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
WL = 'data/b558_editions/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.txt'
SE = 'D:/SIDE-effects'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def put_pp(rel, text):
    p = os.path.join(PP, *rel.split('/'))
    b = text.encode('utf-8')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (rel, len(b)))


def jl(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def _Q():
    import b566_record as R6
    return R6.Q


DEFECTS = [
    '(a) THE FIRST SCORING READ (N4) REFUTED ON A PREDICATE OF ITS OWN BUILDING: the check that PATHS v0.7`s diff is confined to its '
    'Correspondence rows tested each changed line for the row`s opening `| ` without stripping the diff`s own leading + or -, so no '
    'line could pass. The record lines had been appended with that score; being this act`s own and uncommitted, FINDINGS and '
    'OPEN_TRAILS were cut back to their pre-append byte length (each verified a prefix of its committed blob and of the file), the '
    'predicate corrected (the marker stripped, the 12 changed lines counted), and the scores and record re-run. The file itself was '
    'never in question: data/b580_repin.txt printed +2 on every row.',
    '(b) THE SUITE`S FIRST PRE-PUSH RUN READ 69 OF 70 ON AN ARM OF ITS OWN BUILDING: G-REPIN-FINAL expected one bank row per work-list '
    'row (13), and :249`s rewrite cites the zeta page, not a bank line, so the column carries 12 bank rows; each row`s lines matched the '
    'final file. The arm`s count was corrected to 12; nothing else changed.',
]


def defects():
    put_txt('b580_defects.txt', ['### b580 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


RELAY = ROOT.replace('\\', '/')
ROWLINES = [316, 319, 320, 323, 325, 327, 329, 332, 333, 335, 336, 337, 343]
READS = [
    ('relay the AMC work-list, whole', RELAY, 'HEAD', WL, list(range(1, 71))),
    ('PLACE-papers AMC, its head', PP, PRE_PP, CUR, list(range(1, 36))),
    ('PLACE-papers AMC, the marked, ceiling and stem lines', PP, PRE_PP, CUR, [231, 237, 241, 249, 279, 291, 292, 320, 334, 364, 366, 388, 396, 404, 446]),
    ('PLACE-papers AMC, the Correspondence', PP, PRE_PP, CUR, list(range(400, 421))),
    ('PLACE-papers AMC, the tier block', PP, PRE_PP, CUR, list(range(482, 520))),
    ('PLACE-papers the zeta page at the mirror`s pin, its pin line and nodes 8, 16, 20, 21', PP, MIRROR_PIN, PAGE, [3, 12, 20, 24, 25]),
    ('relay the CP-1b bank, its head and the 13 rows', RELAY, 'HEAD', 'data/b558_cp1b.txt', list(range(1, 9)) + ROWLINES),
    ('PLACE-papers OPEN_TRAILS, the form, its clauses, b579`s record', PP, PRE_PP, 'OPEN_TRAILS.md', [11864, 11902, 11904, 11906, 11908, 11914]),
    ('PLACE-papers FINDINGS, b579`s entry', PP, PRE_PP, 'FINDINGS.md', [6500]),
    ('PLACE-papers PATHS v0.7, its Correspondence', PP, PRE_PP, PATHS7, list(range(683, 691))),
    ('relay b578`s edition bank, its head', RELAY, 'HEAD', 'data/' + B578_BANK, list(range(1, 6))),
    ('PLACE-papers FOUNDATIONS v0.2.5, its Correspondence', PP, PRE_PP, FOUND5, list(range(740, 764))),
    ('relay tools/banned_terms.py, the stems and the exceptions', RELAY, 'HEAD', 'tools/banned_terms.py', list(range(1, 81))),
    ('relay b579`s closing push-out, its head', RELAY, 'HEAD', 'data/b579_closing_push_out.txt', list(range(1, 4))),
    ('SIDE-effects Module1.lean at a27415d, imports and statement', SE, 'a27415d', 'SIDEEffects/Phase15/Module1.lean', [11, 12, 154, 155, 156]),
    ('SIDE-effects Module1.lean at c66f3c5, imports and statement', SE, 'c66f3c5', 'SIDEEffects/Phase15/Module1.lean', [34, 35, 36, 37, 164, 165, 166, 167]),
]


def reads():
    L = ['b580 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    put_txt('b580_reads.txt', L)


# ================================================================================ COMPONENT 1 -- THE RE-PIN, THEN THE FORM LINES
CELL = re.compile(r'\| cited at :([0-9, :]+) of this edition \|$')
B578_HEAD = ('### b580 -- THE OFFSET, UNDER (R190)(3): +2 from :19 -- PATHS v0.7`s own lines from its :19 on sit two lower than when '
             'this bank was written (b579 inserted the v0.7 version line and a blank above the v0.6 version line); the v0.6 lines this '
             'bank cites are v0.6`s and do not move.')


def _nums(cell):
    return [int(x) for x in re.findall(r'\d+', cell)]


def _repin_file(rel, pins, bm_tag, banks):
    """### one edition's Correspondence column re-read against the file as it stands: (rows, new text or None)."""
    p = os.path.join(PP, *rel.split('/'))
    text = io.open(p, encoding='utf-8', newline='').read()
    ls = text.split(NL)
    cut = [i for i, l in enumerate(ls) if l.startswith(bm_tag)]
    if len(cut) != 1:
        sys.exit('### %s -- THE BACK-MATTER TAG IS NOT THERE EXACTLY ONCE' % rel)
    body = ls[:cut[0]]
    rows = []
    for i, l in enumerate(ls):
        if i < cut[0] or not CELL.search(l):
            continue
        m = re.match(r'^\| `(?:SIDEExplicitFormula\.\w+\.)?(\w+)` \|', l)
        mb = re.match(r'^\| `data/b558_cp1b\.txt` :(\d+) \|', l)
        if m and m.group(1) in pins:
            d = m.group(1)
            new = [k for k, x in enumerate(body, 1) if ('`%s`' % d) in x and pins[d] in x]
        elif mb and banks:
            n = int(mb.group(1))
            d = 'b558_cp1b.txt :%d' % n
            new = [k for k, x in enumerate(body, 1) if ('relay `data/b558_cp1b.txt` :%d' % n) in x]
        else:
            continue
        old = _nums(CELL.search(l).group(1))
        rows.append(dict(line=i + 1, decl=d, old=old, new=new, delta=[b - a for a, b in zip(old, new)] if len(old) == len(new) else None))
    out = list(ls)
    moved = False
    for r in rows:
        if r['old'] != r['new']:
            moved = True
            l = out[r['line'] - 1]
            out[r['line'] - 1] = CELL.sub('| cited at :%s of this edition |' % ', :'.join(str(x) for x in r['new']), l)
    return rows, (NL.join(out) if moved else None), text


def repin():
    """### PATHS v0.7's Correspondence column (PLACE-papers), b578's diff bank's head line (relay), FOUNDATIONS v0.2.5 checked."""
    import b578_record as R8
    import b579_record as R9
    pr, pnew, ptext = _repin_file(PATHS7, R8.PIN, '<!-- b578 (R188) THE v0.7 EDITION', False)
    if g(PP, 'show', '%s:%s' % (PRE_PP, PATHS7)) != ptext.replace(chr(13), ''):
        sys.exit('### PATHS v0.7 DIFFERS FROM ITS BLOB AT a1de9dc -- NOTHING WRITTEN')
    fr, fnew, _ = _repin_file(FOUND5, R9.PIN, R9.BM_TAG, True)
    plus2 = all(r['delta'] is not None and all(x == 2 for x in r['delta']) and all(o > 19 for o in r['old']) for r in pr)
    if not plus2:
        sys.exit('### THE PATHS COLUMN DOES NOT MOVE BY +2 ON EVERY LINE AFTER :19 -- NOTHING WRITTEN: %s' % pr)
    if pnew is not None:
        put_pp(PATHS7, pnew)
    if fnew is not None:
        put_pp(FOUND5, fnew)
    bank = io.open(os.path.join(D, B578_BANK), encoding='utf-8', newline='').read()
    if bank.startswith(B578_HEAD):
        sys.exit('### b578`s BANK IS ALREADY HEADED')
    b = (B578_HEAD + NL + bank).encode('utf-8')
    p = os.path.join(D, B578_BANK)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (one head line)' % B578_BANK)
    L = ['b580 -- COMPONENT 1: THE RE-PIN, (R190)(3)', '',
         '### PATHS v0.7 (PLACE-papers %s @ %s), its Correspondence column re-read against the file as it stands:' % (PATHS7, PRE_PP)]
    L += ['    :%d `%s` -- before :%s ; after :%s ; difference %s' % (r['line'], r['decl'], ', :'.join(map(str, r['old'])),
                                                                  ', :'.join(map(str, r['new'])), r['delta']) for r in pr]
    L += ['### ### **EVERY CITED LINE MOVES BY +2, EVERY ONE AFTER :19: %s ; rows rewritten %d.**' % (plus2, sum(r['old'] != r['new'] for r in pr)),
          '### relay data/%s headed: "%s"' % (B578_BANK, B578_HEAD), '',
          '### FOUNDATIONS v0.2.5 (PLACE-papers %s @ %s), its Correspondence column re-read the same way:' % (FOUND5, PRE_PP)]
    L += ['    :%d `%s` -- column :%s ; the file now :%s ; %s' % (r['line'], r['decl'], ', :'.join(map(str, r['old'])),
                                                               ', :'.join(map(str, r['new'])), 'UNMOVED' if r['old'] == r['new'] else '### MOVED')
          for r in fr]
    L += ['### ### **FOUNDATIONS v0.2.5`S COLUMN %s.**' % ('DID NOT MOVE -- NOT REWRITTEN' if fnew is None else 'MOVED -- RE-PINNED')]
    put_txt('b580_repin.txt', L)
    put_json('b580_repin.json', dict(paths=pr, paths_plus2=plus2, paths_written=pnew is not None, foundations=fr,
                                     foundations_moved=fnew is not None, b578_head=B578_HEAD))


H28B_TEXT = ('the body sentence count differs from the current version’s by at most the CREDIT count, the removals, the citations a '
             'ruling orders, and one version line; the back matter excluded and counted beside')
REPIN_TEXT = ('after every insertion the edition’s own Correspondence column and the act’s diff bank are re-read against the final '
              'file and cite its final lines; the bank states the offset from the current version once at its head')
EXC_TEXT = ('an object’s own name and a bibliography title are not live uses (relay `tools/banned_terms.py` :14, “CLAY / BIBLIOGRAPHY '
            'CITATIONS”, an exception the tool names part of the rule); each such use carries unchanged, is listed in the back matter '
            'with its line, and is printed as excepted when H28c is scored')
FORM_HEAD = '*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6), to the critical path’s lane three'
B579_TRAIL = '### b579 — lane three, act seven under (R189)'
B579_ENTRY = '## CP-7, act four: the edition of FOUNDATIONS_OF_THE_SIDE_PROGRAMME'


def c1_lines():
    """### PLACE-papers OPEN_TRAILS (three lines at the form, the navigator's wording at b579's record) and FINDINGS (b579's weight)."""
    Q = _Q()
    RP = jl('b580_repin.json')
    form, b579, entry = Q.line_of(Q.OT, FORM_HEAD), Q.line_of(Q.OT, B579_TRAIL), Q.line_of(Q.FIND, B579_ENTRY)
    if not (form == 11864 and b579 == 11914 and entry == 6500):
        sys.exit('### THE ADDRESSED LINES MOVED: form %s b579 %s entry %s -- NOTHING WRITTEN' % (form, b579, entry))
    heads = dict(
        h28b='*Appended 2026-10-01 by b580, under the author’s ruling `(R190)`(2), to the form of an edition (:%d) -- H28b, FINAL FORM FOR EVERY EDITION ACT:*' % form,
        repin='*Appended 2026-10-01 by b580, under the author’s ruling `(R190)`(3), to the form of an edition (:%d) -- THE RE-PIN STEP, THE FORM’S LAST:*' % form,
        exc='*Appended 2026-10-01 by b580, under the author’s answer before b580’s seal, to the form of an edition (:%d), beside the stem, ceiling and history clauses -- THE NAME-AND-TITLE EXCEPTION:*' % form,
        nav='*Appended 2026-10-01 by b580 to b579’s record (:%d), under the author’s ruling `(R190)`(2):*' % b579,
        weight='*Appended 2026-10-01 by b580 to b579’s entry (:%d), under `(R190)`(1) -- b579 AT ITS WEIGHT:*' % entry,
    )
    for k, h in heads.items():
        Q.guard_absent(Q.FIND if k == 'weight' else Q.OT, h)
    out = [Q.append_to(Q.OT, '\n%s %s.\n' % (heads['h28b'], H28B_TEXT))]
    out.append(Q.append_to(Q.OT, '\n%s %s. Run at b580 on PATHS v0.7, whose column moved by +2 on every cited line after :19 (relay '
                                 '`data/b580_repin.txt`), its diff bank headed “+2 from :19”; FOUNDATIONS v0.2.5’s column read the same '
                                 'way, %s.\n' % (heads['repin'], REPIN_TEXT, 'unmoved' if not RP['foundations_moved'] else 're-pinned')))
    out.append(Q.append_to(Q.OT, '\n%s %s. Applied at b580 to ADDITIVE_MULTIPLICATIVE_CONSPIRACY :231 (the object’s own name) and :388, '
                                 ':396 (two published titles).\n' % (heads['exc'], EXC_TEXT)))
    h28b_line = Q.line_of(Q.OT, heads['h28b'])
    out.append(Q.append_to(Q.OT, '\n%s `(R189)`(2)’s omission of the version line from H28b’s bound is recorded as the navigator’s; H28b '
                                 'stands in its final form at :%d.\n' % (heads['nav'], h28b_line)))
    out.append(Q.append_to(Q.FIND, '\n%s `phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md` beside v0.2.4 unedited: 16 rows '
                                   'as 15 sentences, 14 rewritten in place citing the five zeta-page declarations or the CP-1b bank line; '
                                   ':653’s dated entry carried with the v0.2.5 history line beneath; four ceiling corrections; the version '
                                   'line above v0.2.4’s; no credit, stem correction or removal; the diff banked. The stem, ceiling and '
                                   'history clauses stand at OPEN_TRAILS :11904-:11908. H28a and H28c held; H28b refuted in letter by the '
                                   'version line alone. PATHS v0.7 carries its version line and one back-matter section. The suite reads 66 '
                                   'of 66.\n' % heads['weight']))
    lines = {k: Q.line_of(Q.FIND if k == 'weight' else Q.OT, h) for k, h in heads.items()}
    put_json('b580_c1_lines.json', dict(form=form, b579=b579, entry=entry, lines=lines, heads=heads, appends=out))
    print(lines)


# ================================================================================ COMPONENT 2 -- THE EDITION
PIN = {'h2_sign_iff_rh': 'v0.2 = `5c72cad`', 'li_nonneg_iff_rh': 'v0.9 = `e5a5a83`', 'arith_limit_nonneg_iff_rh': 'v0.9 = `e5a5a83`'}
NS = {'h2_sign_iff_rh': 'B321', 'li_nonneg_iff_rh': 'LiCriterionBridge', 'arith_limit_nonneg_iff_rh': 'LiCriterionBridge'}
PAGE_NODE = {'h2_sign_iff_rh': 8, 'li_nonneg_iff_rh': 20, 'arith_limit_nonneg_iff_rh': 21}
EF = 'SIDE-explicit-formula'
H2 = '`h2_sign_iff_rh`, %s %s' % (EF, PIN['h2_sign_iff_rh'])
LI = '`li_nonneg_iff_rh`, %s %s' % (EF, PIN['li_nonneg_iff_rh'])
AL = '`arith_limit_nonneg_iff_rh`, %s %s' % (EF, PIN['arith_limit_nonneg_iff_rh'])
CPB = 'relay `data/b558_cp1b.txt` :%d'
PROF = 'over Mathlib, `[propext, Classical.choice, Quot.sound]` at `a27415d` and carrying `sorryAx` at `c66f3c5`'
TD = '`IsEmpty TypeD` over the programme’s own couplings'
LIT = 'two uncompiled literature premises (Bombieri–Lagarias `ExplicitFormulaDecomp`, Voros `TailBoundPremise`)'

REWRITES = [
    (25, 'The finite-modulus no-conspiracy is compiled: `Module1.no_type_d_conspiracies` (CRT exhaustiveness via periodic lift) in the '
         '`SIDE-effects` repository — vanilla Lean 4, `0 sorry, 0 axioms` — and it rules out finite-modulus-unexplained couplings only.',
     'The finite-modulus no-conspiracy is compiled as a programme-type statement: `Module1.no_type_d_conspiracies` (CRT exhaustiveness '
     'via periodic lift) in the `SIDE-effects` repository states %s, T2, %s (%s) — and it rules out finite-modulus-unexplained couplings '
     'only.' % (TD, PROF, CPB % 316)),
    (237, 'The genuine structural exclusion is `Module1.no_type_d_conspiracies` (CRT exhaustiveness via periodic lift), vanilla Lean 4, '
          'no sorry, no axioms.',
     'The structural exclusion is `Module1.no_type_d_conspiracies` (CRT exhaustiveness via periodic lift), which states %s, T2, the '
     'arithmetic reading carried by the programme’s definitions, %s (%s).' % (TD, PROF, CPB % 319)),
    (241, 'The genuine verification is `Module1.no_type_d_conspiracies` (CRT exhaustiveness);',
     'The verification is `Module1.no_type_d_conspiracies` (CRT exhaustiveness), which states %s, T2, so the arithmetic reading is '
     'carried by the programme’s definitions (%s);' % (TD, CPB % 320)),
    (249, '— both are the compiled-partial floor with the global residue left open.',
     '— but its finite range holds only under %s, T1-lit, while Li positivity at every n is RH itself (%s), equivalently the '
     'nonnegativity of the Bombieri–Lagarias arithmetic limits (%s).' % (LIT, LI, AL)),
    (279, '(2) **The structural exclusion is kernel-verified** as `Module1.no_type_d_conspiracies` (CRT exhaustiveness via periodic '
          'lift; vanilla Lean 4, 0 sorry, 0 axioms).',
     '(2) **The structural exclusion is compiled, programme-type,** as `Module1.no_type_d_conspiracies` (CRT exhaustiveness via '
     'periodic lift, stating %s, T2, %s, %s).' % (TD, PROF, CPB % 325)),
    (291, 'the `0 sorry, 0 axioms` claim holds of the structural theorems (`Module1.no_type_d_conspiracies`, `crt_exhaustiveness`, '
          '`no_type_d`);',
     'the structural theorems (`Module1.no_type_d_conspiracies`, `crt_exhaustiveness`, `no_type_d`) are programme-type, T2, over the '
     'programme’s own couplings, and at this pin `Module1.no_type_d_conspiracies` carries `sorryAx` and imports Mathlib (%s);' % (CPB % 327)),
    (292, '- `Module1.no_type_d_conspiracies` — the genuine structural exclusion (`crt_exhaustiveness` ⇒ `IsEmpty TypeD`), CRT '
          'exhaustiveness via periodic lift;',
     '- `Module1.no_type_d_conspiracies` — the structural exclusion over the programme’s own couplings (`crt_exhaustiveness` ⇒ '
     '`IsEmpty TypeD`), T2, the arithmetic reading carried by the programme’s definitions (%s), CRT exhaustiveness via periodic lift;'
     % (CPB % 329)),
    (334, 'The finite-modulus no-conspiracy is kernel-verified as `Module1.no_type_d_conspiracies` (CRT exhaustiveness) in '
          '`SIDE-effects`, vanilla Lean 4, `0 sorry, 0 axioms`.',
     'The finite-modulus no-conspiracy is compiled, programme-type, as `Module1.no_type_d_conspiracies` (CRT exhaustiveness) in '
     '`SIDE-effects`, stating %s, T2, %s (%s).' % (TD, PROF, CPB % 332)),
    (364, '`Module1.no_type_d_conspiracies` (genuine CRT exhaustiveness) and the general `no_type_d` lemma compile at `0 sorry, 0 axioms`;',
     '`Module1.no_type_d_conspiracies` (CRT exhaustiveness) and the general `no_type_d` lemma compile as programme-type statements over '
     'the programme’s own couplings, T2, `no_type_d` axiom-free and `Module1.no_type_d_conspiracies` %s (%s);' % (PROF, CPB % 333)),
    (404, '`no_type_d_conspiracies` is a **derivation-certificate** (scoped positive-modulus).',
     '`no_type_d_conspiracies` is a **derivation-certificate** (scoped positive-modulus) of a programme-type statement, %s, T2 whatever '
     'its profile (%s).' % (TD, CPB % 335)),
    (408, '| **DERIVES** — the modular-conversion discharge landed at `a27415d` (W-4).',
     '| **DERIVES** its own statement, %s, T2 whatever its profile (%s, :337) — the modular-conversion discharge landed at `a27415d` '
     '(W-4).' % (TD, CPB % 336)),
    (446, '| ### **`0 sorry, 0 axioms`** (vanilla Lean 4, no Mathlib) |', '| `[propext, sorryAx, Quot.sound]` at this pin, over Mathlib |'),
    (446, '| ### **COMPILED** |',
     '| ### **COMPILED, T2** — programme-type, %s, the clean profile `[propext, Classical.choice, Quot.sound]` at `a27415d` (%s) |'
     % (TD, CPB % 343)),
]
CEILS = [
    (33, '— mechanism identified, exclusion direct, problem closed (RH, GRH).',
     '— mechanism identified, exclusion direct, problem closed in the programme’s argument up to its open clause, `h2_sign`, '
     'equivalent to RH (%s) (RH, GRH).' % H2),
    (320, '— RH proof core;', '— RH-core;'),
    (366, '— RH proof core.', '— RH-core.'),
]
STEMX = [(231, 'gaps-between-primes', 'the object’s own name'), (388, 'Small gaps between primes', 'a published title (Maynard 2015)'),
         (396, 'Bounded gaps between primes', 'a published title (Zhang 2014)')]
VERSION = (17, '*v0.2.4 — 2026-10-01*')
OFFSET = '+2 from :17 (the v0.2.4 version line and a blank, inserted above the v0.2.3 version line); no other insertion'
ASSIGN = {'AMC:249:270': 0}
READING_NAME = {0: 'none -- resolved by the author`s answer before the seal', 2: '(b) a T2 terminal rewritten to what it states per its tier row'}
MATCHER = r'[Cc]ompiled|COMPILED|kernel-verified|genuine|0 axioms|no axioms|DERIVES|derivation-certificate'
CEILING = re.compile(r'RH proved|RH is proved|h2_sign proved|λ_n ≥ 0 proved|GRH reduced|GRH proved|reduction machine-verified|proof of RH|'
                     r'proves RH|RH proof|problem closed \(RH')
CEIL_RECORD = 'ceiling correction record:'
BM_TAG = '<!-- b580 (R190) THE v0.2.4 EDITION`S BACK MATTER, 2026-10-01 -->'


def _cp():
    import b558_record as CP
    return CP


def _segs(l):
    return [s for s in _cp().segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _rows():
    return [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'AMC' and r['verdict'] == 'MOVED-IN-MEANING']


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    """### the edition's final line for a current-version line: +2 from :17."""
    return n + 2 if n >= VERSION[0] else n


def edition(*a):
    """### PLACE-papers phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY_v0_2_4.md, created beside the current version from its blob at
    ### a1de9dc; the re-pin step run last over the final body. ### `again` rewrites an edition this act already wrote (never a committed one)."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE a1de9dc -- NOTHING WRITTEN')
    edp = os.path.join(PP, *ED.split('/'))
    if os.path.exists(edp) and 'again' not in a:
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    if g(PP, 'ls-files', ED).strip():
        sys.exit('### THE EDITION FILE IS COMMITTED -- NOTHING WRITTEN')
    new = list(cur)
    for ln, old, rep in REWRITES + CEILS:
        line = new[ln - 1]
        if line.count(old) != 1:
            sys.exit('### :%d -- THE FRAGMENT IS NOT ON ITS LINE EXACTLY ONCE (%d): %s' % (ln, line.count(old), old[:80]))
        n0 = len(_segs(line))
        new[ln - 1] = line.replace(old, rep)
        if len(_segs(new[ln - 1])) != n0:
            sys.exit('### :%d -- THE REWRITE CHANGED THE LINE`S SEGMENT COUNT %d -> %d' % (ln, n0, len(_segs(new[ln - 1]))))
    for ln, w, _ in STEMX:
        if w not in cur[ln - 1]:
            sys.exit('### :%d -- THE EXCEPTED USE IS NOT ON ITS LINE' % ln)
    if not cur[VERSION[0] - 1] == '*v0.2.3 — 2026-07-19*' or len(_segs(VERSION[1])) != 1:
        sys.exit('### THE VERSION ANCHOR IS NOT WHERE THE FACE SAYS')
    diff = []
    for r in _rows():
        ln = r['line']
        k = _segs(cur[ln - 1]).index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        cites = [d for d in PIN if ('`%s`' % d) in nw and PIN[d] in nw]
        banks = re.findall(r'relay `data/[^`]+` :\d+', nw)
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         reading=ASSIGN.get(r['id'], 2), matcher=bool(re.search(MATCHER, r['sentence'])),
                         cites=cites, banks=banks, supports=r['reading']))
    new[VERSION[0] - 1:VERSION[0] - 1] = [VERSION[1], '']
    body = list(new)
    if any(body[_edl(n) - 1] != new[_edl(n) - 1] for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL BROKEN')
    bm = ['', BM_TAG, '',
          '## Back matter of the v0.2.4 edition -- written 2026-10-01 by b580 under the author’s ruling `(R190)`(4), by the form of `(R187)`(5)',
          '',
          '*This file is v0.2.4 of ADDITIVE_MULTIPLICATIVE_CONSPIRACY, the CP-7 edition written beside v0.2.3 (`%s`, unedited) from v0.2.3’s '
          'tier block (its :482) and its CP-1b work-list (relay `%s`), the zeta page as its spine; it does not deposit and does not replace '
          'v0.2.3, and its promotion is CP-8’s. Its lines sit two below v0.2.3’s from v0.2.3’s :17 on (the version line); every line cited '
          'below is this file’s own.*' % (CUR, WL), '',
          '### Removals', '',
          'None: every one of the 13 work-list rows resolves to a sentence rewritten in place to what its compiled fact says.', '',
          '### Stem uses excepted', '',
          '| this edition’s line | the use | read as | Status |', '|:--|:--|:--|:--|']
    for ln, w, why in STEMX:
        bm.append('| :%d | %s (banned stem, excepted) | %s | carried unchanged under the name-and-title exception, the author’s answer '
                  'before b580’s seal |' % (_edl(ln), w, why))
    bm += ['', '### Ceiling corrections', '', '| this edition’s line | v0.2.3 wording | v0.2.4 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in CEILS:
        bm.append('| :%d | %s %s | %s | corrected under %s |' % (_edl(ln), CEIL_RECORD, old, rep,
                                                              'the author’s answer before b580’s seal' if ln == 33 else 'the ceiling clause'))
    bm += ['', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v0.2.4 | `%s` | written at b580 |' % ED,
           '| the current version, v0.2.3 | `%s` | unedited |' % CUR,
           '| the spine | `%s` at PLACE-papers `%s` | read, unedited |' % (PAGE, MIRROR_PIN),
           '| the work-list | relay `%s` | read |' % WL,
           '| the CP-1b readings | relay `data/b558_cp1b.txt` | read |',
           '| the sentence-by-sentence diff | relay `data/b580_edition_AMC.txt` | banked at b580 |',
           '', '### Correspondence', '',
           '| declaration or bank line | repository | pin as the zeta page prints it | the page’s line | Status |', '|:--|:--|:--|:--|:--|']
    # ### THE RE-PIN STEP, LAST: every cited line read against the final body
    ed_lines = {d: [i for i, l in enumerate(body, 1) if ('`%s`' % d) in l and PIN[d] in l] for d in PIN}
    bank_lines = sorted(set(int(x) for l in body for x in re.findall(r'relay `data/b558_cp1b\.txt` :(\d+)(?:, :(\d+))?', l) for x in x if x))
    for d in PIN:
        bm.append('| `SIDEExplicitFormula.%s.%s` | %s | %s | node %d, line %d | cited at :%s of this edition |' % (
            NS[d], d, EF, PIN[d].replace('`', ''), PAGE_NODE[d], PAGE_NODE[d] + 4, ', :'.join(str(x) for x in ed_lines[d]) or '### NONE'))
    for n in bank_lines:
        at = [i for i, l in enumerate(body, 1) if re.search(r'relay `data/b558_cp1b\.txt` :(?:\d+, :)?%d\b' % n, l)]
        bm.append('| `data/b558_cp1b.txt` :%d | relay | the CP-1b bank (b558) | not on the page | cited at :%s of this edition |' % (
            n, ', :'.join(str(x) for x in at)))
    bm.append('')
    full = body + bm
    b = (NL.join(full) + NL).encode('utf-8')
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    put_json('b580_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=0, removals=0, ruled_citations=1, version_lines=1, diff=diff, offset=OFFSET,
                                       ceils=CEILS, stemx=[dict(cur=l, ed=_edl(l), use=w, why=y) for l, w, y in STEMX],
                                       version=dict(above=VERSION[0], text=VERSION[1]),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full),
                                       cited_lines=ed_lines, bank_lines=bank_lines))
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))


def edition_bank():
    """### The diff with its offset line, the exceptions, the counts, the ceiling read, H28a-H28c: data/b580_edition_AMC.txt."""
    E = jl('b580_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    scan = rd('b580_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    live_lines = sorted(int(m) for m in re.findall(r'\.md :(\d+)\s+### LIVE USE', scan))
    exc_lines = sorted(s['ed'] for s in E['stemx'])
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            hits.append(dict(line=i, hit=m.group(0), ctx=l[max(0, m.start() - 60):m.end() + 20], record=l.startswith('| :') and CEIL_RECORD in l))
    beyond = [h for h in hits if not h['record']]
    h28a_bad = [d['id'] for d in E['diff'] if not d['changed'] or not (d['cites'] or d['banks'])]
    h28a = 'HELD' if not h28a_bad else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur']
    allowed = E['credit'] + E['removals'] + E['ruled_citations'] + E['version_lines']
    h28b = 'HELD' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HELD' if (live and int(live.group(1)) == len(exc_lines) and live_lines == exc_lines and not beyond) else 'REFUTED'
    al = [i for i, l in enumerate(ed[:E['lines_body']], 1) if '`arith_limit_nonneg_iff_rh`' in l and PIN['arith_limit_nonneg_iff_rh'] in l]
    cur0 = _cur()
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): %s -- every edition line below is the final file`s own.' % OFFSET, '',
         'b580 -- COMPONENT 2: THE EDITION OF ADDITIVE_MULTIPLICATIVE_CONSPIRACY, (R190)(4), BY THE FORM OF (R187)(5)', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :17 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0], cur0[16]),
         '### its tier block : :482 "%s"' % cur0[481][:110],
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE READINGS OF (R190)(4) AGAINST THIS DOCUMENT: (a) the prime side against the pole-plus-archimedean assembly -- NO '
         'OBJECT HERE (no such sentence, marked or unmarked; the sentence it described belongs to BALANCE_AND_POSITIVITY`s edition) ; '
         '(b) a T2 terminal called compiled -- 12 rows ; (c) h2 marked -- none ; (d) the T2-INTERFACES terminal -- none marked ; (e) T4 '
         '-- carried', '',
         '### THE WORK-LIST, ROW BY ROW (13 rows, 12 sentences, 11 lines) -- each row: v0.2.3`s line and the edition`s, the terminal, '
         'the reading (the seat`s hand-read), what its sentence cites, the sentence before and after.', '']
    for d in E['diff']:
        L += ['  %s v0.2.3 :%d -> v0.2.4 :%d `%s` -- %s ; cites %s%s' % (d['id'], d['line'], d['ed_line'], d['terminal'], READING_NAME[d['reading']],
                                                                     ['%s (%s)' % (c, PIN[c].replace('`', '')) for c in d['cites']],
                                                                     (' ; bank ' + ', '.join(d['banks'])) if d['banks'] else ''),
              '      work-list: %s' % d['supports'],
              '      v0.2.3 : %s' % d['old'], '      v0.2.4 : %s' % d['new'], '']
    cov = [d for d in E['diff'] if d['reading']]
    L += ['### (N1) COVERAGE BY THE READINGS OF (R190)(4), the seat`s hand-read: %d of %d rows -- (b) %d ; (a), (c), (d) none ; '
          'uncovered %s, resolved by the author`s answer' % (len(cov), len(E['diff']), len(cov),
                                                            [':%d `%s`' % (d['line'], d['terminal']) for d in E['diff'] if not d['reading']]),
          '### the matcher`s yield, printed as lineage and not the count: %d of %d rows' % (sum(d['matcher'] for d in E['diff']), len(E['diff'])),
          '### (N3) `arith_limit_nonneg_iff_rh` at its pin, cited at the edition`s :%s' % ', :'.join(map(str, al)), '',
          '### THE CEILING CORRECTIONS:']
    L += ['    v0.2.3 :%d -> v0.2.4 :%d  "%s" -> "%s"' % (c[0], _edl(c[0]), c[1], c[2]) for c in E['ceils']]
    L += ['### THE STEM USES EXCEPTED (the author`s answer): ' + ' ; '.join('v0.2.3 :%d -> v0.2.4 :%d %s (%s)' % (s['cur'], s['ed'], s['use'], s['why'])
                                                                   for s in E['stemx']),
          '### THE VERSION LINE: above v0.2.3 :%d: %s' % (E['version']['above'], E['version']['text']),
          '### CREDIT LINES: none (CREDIT 0). ### REMOVALS: none. ### HISTORY LINES: none.', '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (%+d: the '
          'version line) ; the back matter %d ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form (R190)(2): the body differs by %+d against CREDIT %d + removals %d + ruled citations %d (:33) + one version '
          'line = %d' % (body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']),
          '', '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], 'quoted in a ceiling correction record of the back matter, read by the seat'
                                          if h['record'] else '### BEYOND THE CEILING', h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### the banned-stem scan of the edition (relay data/b580_edition_termscan.txt): live uses %s at :%s ; excepted by the clause at '
          ':%s' % (live.group(1) if live else '?', ', :'.join(map(str, live_lines)), ', :'.join(map(str, exc_lines))), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing a declaration on the page at its pin, or a bank line%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- live banned stems %s, every one of them the three excepted uses; sentences beyond the ceiling %d.**' % (
              h28c, live.group(1) if live else '?', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b580_edition_AMC.txt', L)
    put_json('b580_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None, live_lines=live_lines,
                                   excepted=exc_lines, beyond=len(beyond), hits=hits, covered=len(cov),
                                   matcher=sum(d['matcher'] for d in E['diff']), arith_limit_at=al,
                                   uncovered=[d['id'] for d in E['diff'] if not d['reading']], held=None))
    H = jl('b580_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'covered', H['covered'], 'body_dn', body_dn, 'beyond', H['beyond'], 'arith', al, 'live', live_lines)


# ================================================================================ THE SCORING AND THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}


def scores():
    H, E, RP = jl('b580_h28.json'), jl('b580_edition.json'), jl('b580_repin.json')
    ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'ls-files', '--others', '--exclude-standard', 'phase1.5', 'phase2')).split(NL) if x.strip()))
    kmain = g('D:/SIDE-explicit-formula', 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    cur_same = g(PP, 'hash-object', CUR).strip() == E['cur_blob']
    p7diff = g(PP, 'diff', PRE_PP, '--unified=0', '--', PATHS7)
    p7ch = [l for l in p7diff.split(NL) if l[:1] in ('+', '-') and not l.startswith(('+++', '---'))]
    p7_only_rows = len(p7ch) == 12 and all(l[1:].startswith('| `SIDEExplicitFormula.') for l in p7ch)
    n2 = H['H28a'] == 'HELD' and H['H28b'] == 'HELD' and H['H28c'] == 'HELD' and H['held'] is None
    n4 = RP['paths_plus2'] and RP['paths_written'] and p7_only_rows
    allowed_pp = {'FINDINGS.md', 'OPEN_TRAILS.md', ED, PATHS7} | ({FOUND5} if RP['foundations_moved'] else set())
    bank_edited = bool(g(RELAY, 'diff', '--name-only', 'c34ef391', '--', 'data/' + B578_BANK).strip())
    n5_core = kmain == V015 and heads_ok and cur_same and set(ch) <= allowed_pp
    S = dict(
        N1=('HELD' if H['covered'] >= 9 else 'REFUTED', 'the readings of (R190)(4) cover %d of the 13 MOVED rows by the seat`s hand-read, '
            'all under (b); (a), (c), (d) find no object; uncovered %s, resolved by the author`s answer' % (H['covered'], H['uncovered'])),
        N2=('HELD' if n2 else 'REFUTED', 'H28a %s, H28b %s (the body %+d against at most %d), H28c %s (live %s, all excepted); no sentence '
            'held' % (H['H28a'], H['H28b'], H['body_dn'], H['allowed'], H['H28c'], H['live'])),
        N3=('HELD' if H['arith_limit_at'] else 'REFUTED', '`arith_limit_nonneg_iff_rh` cited at the edition`s :%s -- at :249`s rewrite by '
            'the author`s answer, not by reading (a)' % H['arith_limit_at']),
        N4=('HELD' if n4 else 'REFUTED', 'PATHS v0.7`s column: every cited line +2, every one after :19: %s ; the diff confined to the '
            'Correspondence rows: %s' % (RP['paths_plus2'], p7_only_rows)),
        N5=('HELD' if (n5_core and not bank_edited) else 'REFUTED', 'nothing deposits; no kernel touched (%s); the current AMC unedited (%s); '
            'PLACE-papers changed at %s -- %s' % ('held' if kmain == V015 and heads_ok else '### MOVED', 'held' if cur_same else '### EDITED', ch,
                                                  'and relay data/%s gained its head line, as (R190)(3) orders and the expectation`s '
                                                  'list does not name' % B578_BANK if bank_edited else 'nothing beyond the list')),
        S1=('HELD' if H['covered'] == 12 and H['uncovered'] == ['AMC:249:270'] else 'REFUTED', '12 of 13; uncovered :249'),
        S2=('HELD' if n2 and H['body_dn'] == 1 and H['allowed'] == 2 else 'REFUTED', 'H28a-H28c held; the body +1 against 2'),
        S3=('HELD' if H['arith_limit_at'] else 'REFUTED', 'at :249`s rewrite, by the author`s answer'),
        S4=('HELD' if n4 and not RP['foundations_moved'] else 'REFUTED', '+2 on every PATHS row; FOUNDATIONS unmoved'),
        S5=('HELD' if (n5_core and bank_edited) else 'REFUTED', '(N5) refuted in letter by b578`s bank head line; its other clauses hold'),
        counts=dict(pp_changed=ch, body_dn=H['body_dn'], covered=H['covered']),
    )
    put_json('b580_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], S[k][1][:150]))


TITLE_HEAD = ('## CP-7, act five: the edition of ADDITIVE_MULTIPLICATIVE_CONSPIRACY from its tier block and work-list, its RH-side '
              'twin cited to the Li and arithmetic-limit faces')
TITLE = TITLE_HEAD + '; written as v0.2.4 beside v0.2.3, no sentence held'
TRAIL_HEAD = ('### b580 — lane three, act eight under (R190): CP-7 act five -- the edition of ADDITIVE_MULTIPLICATIVE_CONSPIRACY '
              'written beside the current; H28b in its final form; the re-pin step; PATHS v0.7 re-pinned')
NAV_READING = ('reading (a) of `(R190)`(4) -- sentences stating the prime side against the pole-plus-archimedean assembly as RH -- has no '
               'object in this document, and is the navigator’s; the sentence it described belongs to BALANCE_AND_POSITIVITY’s edition')


def records_pp():
    Q = _Q()
    S, H, E, C1, RP = jl('b580_scores.json'), jl('b580_h28.json'), jl('b580_edition.json'), jl('b580_c1_lines.json'), jl('b580_repin.json')
    ln = C1['lines']
    Q.guard_absent(Q.FIND, TITLE_HEAD)
    e = ['', TITLE, '',
         '*Filed at b580 on the author’s ruling `(R190)`. Banks: relay `data/b580_edition_AMC.txt` (the sentence-by-sentence diff, its '
         'offset line at its head), `data/b580_edition.json`, `data/b580_repin.txt`. Nothing deposits.*', '',
         '**The edition** (`(R190)`(4)): `%s`, v0.2.4, written beside v0.2.3 (`%s`, unedited) from v0.2.3’s tier block and its CP-1b '
         'work-list, the zeta page as its spine. The 13 work-list rows resolve to 12 sentences on 11 lines, each rewritten in place: the '
         'twelve that called the finite-modulus no-conspiracy compiled, kernel-verified or genuine now say what its terminal states -- '
         'the empty conspiracy type over the programme’s own couplings, programme-type, over Mathlib, its profile clean at one pin and '
         'carrying the sorry axiom at the other -- each citing its CP-1b bank line; the RH-side twin sentence states its finite range '
         'as conditional on two literature premises and cites the Li and arithmetic-limit equivalences with RH at their pins. Three '
         'unmarked sentences beyond the ceiling are corrected, :33 citing the open clause’s equivalence with RH; three uses of the stem '
         'carry under the name-and-title exception. No CREDIT line (CREDIT 0); no removal; none held.' % (ED, CUR), '',
         '**The counts.** v0.2.3 %d sentences; v0.2.4 %d (the body %d, the back matter %d); the body differs by %+d against the final '
         'bound, %d.' % (E['n_cur'], E['n_full'], E['n_body'], E['n_backmatter'], H['body_dn'], H['allowed']), '',
         '**H28a %s · H28b %s · H28c %s.** Coverage of the 13 rows by the readings of `(R190)`(4): %d.' % (H['H28a'], H['H28b'], H['H28c'], H['covered']), '',
         '**The form’s changes** (`(R190)`(2)-(3)): H28b in its final form (OPEN_TRAILS :%d); the re-pin step, last (:%d); the '
         'name-and-title exception, the author’s answer (:%d); the navigator’s wording at b579’s record (:%d). **PATHS v0.7** re-pinned: '
         'its column moved +2 on every cited line after :19, nothing else, and relay `data/b578_edition_PATHS.txt` is headed with its '
         'offset; FOUNDATIONS v0.2.5’s column %s (relay `data/b580_repin.txt`).' % (
             ln['h28b'], ln['repin'], ln['exc'], ln['nav'], 'did not move' if not RP['foundations_moved'] else 'moved and was re-pinned'), '',
         '**A reading, the navigator’s:** %s.' % NAV_READING, '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s; the seat’s (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
         % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R190)`(5): the edition of THE_UNCONDITIONAL_SURROUND by the same form; the author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; v0.2.3, README, REGISTRY and both pages unwritten; nothing here is a statement about RH, GRH '
         'or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows = ['', TRAIL_HEAD, '',
            '**(R190) ratified.** (1) b579 at its weight. (2) H28b in its final form. (3) The re-pin step; PATHS v0.7 re-pinned. (4) The '
            'edition of ADDITIVE_MULTIPLICATIVE_CONSPIRACY by the form, five readings entered. (5) The act after.', '',
            '**Entered:** FINDINGS.md:%d (b579’s weight), :%d (the entry); OPEN_TRAILS.md:%d (H28b, final form), :%d (the re-pin step), :%d '
            '(the name-and-title exception), :%d (at b579’s record: the navigator’s wording), this record; PLACE-papers `%s` (created); '
            '`%s` (its Correspondence column re-pinned). Relay: `data/b578_edition_PATHS.txt` headed with its offset.' % (
                ln['weight'], Q.line_of(Q.FIND, TITLE_HEAD), ln['h28b'], ln['repin'], ln['exc'], ln['nav'], ED, PATHS7), '',
            '**Answered before the seal, by the author:** the RH-side twin sentence cites the Li and arithmetic-limit faces; the three '
            'stem uses carry as an object’s own name and two published titles; :33 takes the programme’s argument up to its open clause, '
            'cited. **Recorded as the navigator’s:** %s.' % NAV_READING, '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
            % tuple(S[k][0] for k in SCORE_KEYS), '',
            '**For the author:** two unmarked sentences of v0.2.3 still print “vanilla Lean 4” for the SIDE-effects pin (its :291 and '
            ':364), and the module imports Mathlib at both pins; neither names a terminal, so CP-1b did not read them and the form '
            'carries them. PATHS v0.7’s version-line section, appended at b579, still says its Correspondence column cites the lines as '
            'b578 wrote them; the column now cites the final lines, and the section was left as written because the re-pin is confined '
            'to the column.', '',
            '**Next:** per `(R190)`(5), CP-7 act six, b581 -- the edition of THE_UNCONDITIONAL_SURROUND by the same form, H28a-H28c '
            'scored; the author rules on the closing.', '',
            '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; the pages untouched; row U1 unedited; the four lists stay '
            'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows))
    put_json('b580_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE_HEAD), title=TITLE, append=r))
    put_json('b580_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r2))
    print(jl('b580_findings.json')['entry_line'], jl('b580_trail.json')['line'])


def desk():
    S = jl('b580_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b580 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b580_defects.txt').rstrip(NL).split(NL)
    put_txt('b580_desk_notes.txt', L)


def components():
    S, H, C1, RP, fj, tj = (jl('b580_scores.json'), jl('b580_h28.json'), jl('b580_c1_lines.json'), jl('b580_repin.json'),
                            jl('b580_findings.json'), jl('b580_trail.json'))
    ln = C1['lines']
    L = ['b580 -- THE COMPONENTS, BANKED UNDER (R190).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b579`s closing push-out relay c066701f ; push-b579* branches deleted by '
         'name (data/b580_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : OPEN_TRAILS :%d (H28b final), :%d (the re-pin step), :%d (the name-and-title exception), :%d (the navigator`s '
         'wording) ; b579`s weight FINDINGS :%d ; PATHS v0.7 re-pinned (+2 on every cited line: %s) and b578`s bank headed, two '
         'housekeeping commits ; FOUNDATIONS v0.2.5 %s (data/b580_repin.txt) ; N4 %s' % (
             ln['h28b'], ln['repin'], ln['exc'], ln['nav'], ln['weight'], RP['paths_plus2'],
             'unmoved' if not RP['foundations_moved'] else 're-pinned', S['N4'][0]),
         '### COMPONENT 2 : the edition %s ; 12 sentences rewritten, 3 ceiling corrections, 3 stem uses excepted, the version line, 0 '
         'credit lines, 0 removals ; data/b580_edition_AMC.txt ; H28a %s H28b %s H28c %s ; N1 %s N2 %s N3 %s' % (
             ED, H['H28a'], H['H28b'], H['H28c'], S['N1'][0], S['N2'][0], S['N3'][0]),
         '### COMPONENT 3 : FINDINGS :%d ; OPEN_TRAILS :%d (the record) ; next: the edition of THE_UNCONDITIONAL_SURROUND ; N5 %s'
         % (fj['entry_line'], tj['line'], S['N5'][0])]
    put_txt('b580_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b580_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
