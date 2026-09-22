# -*- coding: utf-8 -*-
"""b474_components.py -- THE FOLD AT TEN, b464 THROUGH b473. ### **PURELY ADDITIVE. AFTER THE LOCK.**

### Usage: `verify` -- every row's verdict strings matched in its own closing, into data/b474_fold.json
###        and data/b474_components.txt; `write` -- the FINDINGS section, the (R31) digest block and
###        (R84)'s lane entry, each appended with its HEAD blob proved a prefix, into b474_fold_run.txt.
### ### **A MARKER ALREADY PRESENT WRITES NOTHING. ### A FOLD RESTATES AND MINTS NOTHING.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
DIGEST = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
FOLDJ, COMP, RUN = (os.path.join(D, 'b474_fold.json'), os.path.join(D, 'b474_components.txt'),
                    os.path.join(D, 'b474_fold_run.txt'))
MARK_F = '<!-- b474 the fold: b464-b473, the external-reading arc -->'
MARK_D = '<!-- b474 orientation refresh: the external-reading arc -->'
MARK_L = '<!-- b474 (R84): the compression register entered as a research lane -->'
HEADING = '## THE EXTERNAL-READING ARC, b464–b473 — THE FOLD'
NL = chr(10)

sys.path.insert(0, T)
from b474_extract import ROWS, norm      # noqa: E402  ### THE ROWS AND THE NORMALISER, IMPORTED

ONE = ('**The record turned its own reading instruments outward — on the deposit’s own '
       'concordance and on two results by other hands — and every reading came back about the '
       'reading: the concordance assigns no row to any of the eight sentences that claim a machine '
       'check, the proportion theorem’s uniformity is in a coordinate no source can fire, the '
       'third party’s explicit formula contains the instrument’s own identity as a special '
       'case, and the axiom run that would have graded it was denied twice by this machine’s '
       'memory.**')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


def span(act):
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', str(act)],
                         capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    m = re.search(r'THE CURRENT SPAN : (\d+) ACT', out)
    return (m.group(1) if m else '?'), out


def verify():
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    rec('=' * 104)
    rec('b474 -- THE FOLD AT TEN, b464 THROUGH b473. ### VERIFY.')
    rec('=' * 104)
    rows, ok_all = [], True
    for act, subj, strings, col, note in ROWS:
        hay = norm(read(os.path.join(D, '%s_closing.txt' % act)))
        got = []
        for s in strings:
            c = hay.count(norm(s))
            got.append(dict(string=s, count=c))
            if c < 1:
                ok_all = False
        v = all(g['count'] >= 1 for g in got)
        rows.append(dict(act=act, subject=subj, bank='%s_closing.txt' % act, strings=got,
                         column=col, note=note, verified=v))
        rec('  %-6s [%-6s] strings %d ; all matched %s %s'
            % (act, col, len(got), v, '' if v else '### ROW NOT CARRIED'))
        for g in got:
            rec('        count %d  %s' % (g['count'], g['string'][:92]))
    cols = {}
    for r in rows:
        cols[r['column']] = cols.get(r['column'], 0) + 1
    n_strings = sum(len(r['strings']) for r in rows)
    n_ver = sum(len(r['strings']) for r in rows if r['verified'])
    sp, _ = span(474)
    rec('')
    rec('  ### ### **ROWS %d ; STRINGS %d ; VERIFIED %d ; ROWS NOT CARRIED %d.**'
        % (len(rows), n_strings, n_ver, sum(1 for r in rows if not r['verified'])))
    rec('  ### columns : %s ; ### **OBJECT %d**' % (' ; '.join('%s %d' % (k, cols[k]) for k in sorted(cols)),
                                                    cols.get('OBJECT', 0)))
    rec('  ### span by the tool through this filing act : %s ; the fold`s own span, filing act excluded : 10'
        % sp)
    rec('=' * 104)
    json.dump(dict(rows=rows, columns=cols, strings=n_strings, verified=n_ver,
                   span_tool=sp, one=ONE, all_matched=ok_all),
              io.open(FOLDJ, 'w', encoding='utf-8', newline=NL), indent=1, ensure_ascii=False)
    io.open(COMP, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0 if ok_all else 1


def blob(rel):
    r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:%s' % rel], capture_output=True)
    return (r.stdout or b'').decode('utf-8', 'replace')


def append(path, rel, mark, body, rec):
    before = read(path)
    if mark in before:
        rec('  %-46s ALREADY PRESENT -- nothing written' % rel)
        return 'DUPLICATE'

    def nz(s):
        return s.replace(chr(13) + NL, NL)

    hb = blob(rel)
    pre_ok = nz(before).startswith(nz(hb).rstrip(NL))
    if not pre_ok:
        rec('  %-46s ### WORKING COPY NOT A PREFIX-COPY OF ITS BLOB -- NOT WRITTEN' % rel)
        return 'NOT WRITTEN'
    new = before.rstrip(NL) + NL + NL + NL.join(body) + NL
    open(path + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(path + '.tmp', path)
    after = read(path)
    ok = nz(after).startswith(nz(before).rstrip(NL)) and after.count(mark) == 1
    rec('  %-46s WRITTEN +%d lines ; prior a TRUE PREFIX %s ; mark once %s ; lines removed 0'
        % (rel, len(after.splitlines()) - len(before.splitlines()), ok, after.count(mark) == 1))
    return 'WRITTEN' if ok else 'READ-BACK FAILED'


def write():
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    F = json.loads(read(FOLDJ))
    if not F['all_matched']:
        rec('  ### A VERDICT STRING IS NOT VERIFIED -- NOTHING WRITTEN.')
        io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
        return 1
    c = F['columns']
    body = [MARK_F, '', HEADING, '',
            '**Ten acts, b464 through b473 — one past `(R1)`’s declared threshold.** '
            '`b363_span.py` reads **%s** through this filing act; the fold’s own span, the filing '
            'act excluded as at b434, b444, b453 and b463, is **10**. **b465 is not a row**: it was '
            'stranded at step zero and re-issued as b467 under `(R75)`, and it has no closing bank to '
            'carry.' % F['span_tool'], '',
            '### The arc in one statement', '', ONE, '',
            '### The span, act by act, each verdict verified in its own closing bank', '',
            '| act | subject | its verdicts, as its bank prints them | column |', '|:--|:--|:--|:--|']
    for r in F['rows']:
        note = (' — *%s*' % r['note']) if r['note'] else ''
        body.append('| **%s** | %s%s | %s | %s |'
                    % (r['act'], r['subject'].replace('`', '’'), note,
                       ' · '.join('`%s`' % g['string'].replace('`', "'").replace('|', '/')
                                       for g in r['strings']), r['column']))
    body += ['',
             '**%d verdict strings across %d acts, every one matched in that act’s own closing '
             'bank, with both sides normalised for curly quotes, dashes, backticks and whitespace.** '
             'The match was rehearsed under `(R70)` **before** this fold’s face was sealed, and '
             'scored 23 of 23 there.' % (F['strings'], len(F['rows'])), '',
             '### The three columns, kept apart', '',
             '**Statements about the object** — the zeros, ξ, the Euler balance: **%d**. '
             '**About the model** — kernel terminals, their axiom profiles, the instrument’s '
             'channels and cells: **%d**. **About the record** — its documents, deposits, rulings, '
             'tools and grades: **%d**. Three rows are borderline and each says so in itself: b468r, '
             'b470 and b473.' % (c.get('OBJECT', 0), c.get('MODEL', 0), c.get('RECORD', 0)), '',
             '**The object column is empty for the tenth consecutive span, and it is carried as a '
             'property of the span rather than as an achievement.** What is new in this one is where '
             'the acts looked: outward, at a deposit’s own concordance and at two results by other '
             'hands. **The instruments reached them and still returned statements about the record.**',
             '',
             '### What the arc established, each at its own address', '',
             '- **The deposit’s concordance assigns no row to any of the eight sentences that '
             'claim a machine check** (b467), so the eight keep b464’s stand-in grades — six '
             '`NOT THE CLAIM`, one `INTERFACES`, one `SHELL`, none `DERIVES` — and '
             '`E-2026-09-22-1` says so in the errata without calling anything published wrong (b469).',
             '- **The six sites of row `U1` reduce to conditions on the test function, data of the '
             'representation, and the instrument’s truncation** (b467), which `(R76)` made the '
             'trigger’s coordinates and `(R78)` refined: on the representation coordinate the '
             'trigger fires only on an identity or a bound.',
             '- **The proportion theorem was read at its own address with its artefacts hash-matched** '
             '(b468r): `K1 CLASS BOUNDARY` at sites (v) and (vi) only, the trigger not fired, '
             '§24.4 annotated and the intake closed (b470).',
             '- **zeta23’s machine-checked explicit formula contains b321’s identity as its '
             'even case** — six declarations `CONTAINS`, two bridges `DOES NOT`, zero `MATCHES`, '
             'with no sign and no normalization difference and three of scope (b470). Its grade is '
             '`DERIVES, CONDITIONAL` on an axiom run that **this machine denied twice, both times for '
             'memory** (b470, b473).',
             '- **The price of vendoring it was read from the rules and not paid**: 57 of 316 modules, '
             '18,105 of 102,265 lines, 89 direct Mathlib imports, two attribution layers, and a copy '
             'that would have to be its own kernel (b471).',
             '- **The six statements a proof of RH would have to supply were written out from row '
             '`U1`’s own cells**, and the two external results placed against them: neither '
             'supplies any site in whole (b472).', '',
             '### The finding that was not asked for', '',
             '**`E0` and row `U1` are two frames that do not map onto each other.** The `E0` gate '
             'grades the eight **constituents** of the stated clause; row `U1` holds six **sites** of '
             'an obstruction. Under a threshold fixed before the read — a shared word-aligned run '
             'of at least six words — **one site of six reaches an `E0` row**, (i) to `K8`, and '
             'five reach none, with the mapping’s positive control recovering its row at 43 words '
             'and its negative control at three (b472). **So “the strongest statement the record '
             'holds at that site” is unavailable at five of the six sites, and the absence is '
             'structural rather than lexical.**', '',
             '### The rulings of the span, with their status', '',
             '| ruling | status |', '|:--|:--|',
             '| `(R74)` a grade is taken against the concordance terminal, the stand-in labelled | '
             '**executed at b467**; the concordance assigned `NO ROW` to all eight |',
             '| `(R75)` b465 re-issued as b467; the artefacts arrive by the author’s fetch | '
             '**executed at b467 and b468r** |',
             '| `(R76)` the `(R61)` trigger restated in the clause’s coordinates | **entered at '
             'b469**, `OPEN_TRAILS.md:7634` — one of two rulings of the span with an entry of its own |',
             '| `(R77)` the errata entry and the live note for the eight | **executed at b469** |',
             '| `(R78)` on the representation coordinate the trigger fires only on an identity or a '
             'bound | **entered at b470**, `OPEN_TRAILS.md:7791` |',
             '| `(R79)` the §24.4 annotation applied and the intake closed | **executed at b470** |',
             '| `(R80)` a detached build is authorized, the log read only at its end | **executed at '
             'b471 and read at b473**; the run it authorized failed for memory |',
             '| `(R81)` the ferry scan flags four words; as amended, a claim carries its check and a '
             'restriction carries `[procedural]` | **refused b472’s first issue, then amended and '
             'obeyed**; `ferry_scan.py` gained the flags at b472 |',
             '| `(R82)` the vendoring disposition, conditional on the three profiles | **VOID FOR WANT '
             'OF A RUN** at b473 — not on a bad profile: no profile was produced |',
             '| `(R83)` the vendored kernel would be `SIDE-explicit-formula`, created after the fold | '
             '**its trigger did not fire at b473**; nothing was created, named or pinned |',
             '| `(R84)` the `h2` lane is open as active research; the compression register is entered '
             'as a lane | **entered at b474**, this fold’s own act, in its own trail entry |', '',
             '*`(R66)` still stands from the previous span, and the wave stays parked under it.*', '',
             '### Errors entered as their owners’', '',
             '**The navigator’s, three, all named by the author’s own rulings:** the two '
             'overclaims of 2026-09-22, entered by `(R81)` with their record checks; **`(R81)` '
             'refusing its author’s own next ferry**, which the seat refused and banked at relay '
             '`eed5f8b` before the rule was amended; and **b360’s sentence carried as a rule when '
             'it was a dated measurement**, which `(R84)` withdraws as an instruction and keeps as a '
             'discipline.', '',
             '**The seat’s, as its acts entered them.** b468r: a toolchain read from the wrong '
             'drive, a comparison cut at a page break, an axiom scan that counted prose, and an '
             'incomplete account of a halted build, corrected by an appended paragraph. b469: a '
             '`utf-8-sig` read with a `utf-8` write that dropped a BOM, and a pointer computed onto a '
             'blank line. b470: a driver’s own timeout recorded as a module failure. b471: an '
             'elapsed time four hours wrong from a timezone conversion, an arm resting on file mtimes a '
             'branch switch had rewritten, and **a masked push failure — b433’s species, a '
             'discarded return code, in its third recurrence**. b472: a push predicate satisfied by the '
             'refused issue’s own commit. b473: a lock gate correctly refusing a banking error, an '
             'arm pointed at the refused run, an arm whose control could not reach what it read, and '
             '**the commit normalising the evidence’s line endings under `eol=lf`**. '
             '**Every one was found by this record’s own controls before its act closed.**', '',
             '### Filed with this fold, not done by it', '',
             '**The desk carries twenty-nine standing items into b475**, among them: a completed axiom '
             'run, whose price is now a measured memory bound rather than a guess; `W-ORD-GW-IMPORT`, '
             'priced and undischarged, with `(R82)` void and `(R83)` untriggered; the navigator’s '
             'ledger entries, which `(R81)` places at this fold; `(R66)`; and the twelve face-only '
             'arms. **The four lists are open.**', '',
             '*Filed by b474 (relay `data/b474_fold.json`, `data/b474_the_fold_at_ten.txt`). Nothing '
             'above this section was edited; no grade is conferred by a seat; nothing is minted; '
             'nothing is claimed about `h2`.*']
    st_f = append(FINDINGS, 'FINDINGS.md', MARK_F, body, rec)
    fnd = read(FINDINGS)
    m = re.search(re.escape(HEADING) + r'.*?### The arc in one statement\s*\n\s*\n(.+?)\n', fnd, re.S)
    quoted = m.group(1).strip() if m else None
    rec('  the arc`s one statement located in the section just written : %s' % bool(quoted))
    dbody = [MARK_D, '',
             '**Orientation refresh — filed b474, 2026-09-22 *(additive)*.** Under `(R31)` a fold '
             'refreshes this digest. The arc folded at b474 — **THE EXTERNAL-READING ARC, '
             'b464–b473** — carries this one statement, quoted from its fold:', '',
             quoted or '*NOT LOCATED in its fold section; nothing is summarised in its place.*', '',
             '**The governing claim at the head of this document is unchanged by the arc**, whose '
             'object column is empty: ten acts read a deposit’s concordance, two results by other '
             'hands, a third party’s Lean library and this record’s own rulings, and none '
             'made a statement about the object. `h2` stands where the deposit left it.']
    st_d = append(DIGEST, 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md', MARK_D, dbody, rec) if quoted else 'NOT WRITTEN'

    lbody = [MARK_L, '',
             '### `(R84)` — the compression register entered as a research lane — filed '
             '2026-09-22 (b474)', '',
             '**RULING `(R84)`, THE AUTHOR’S, RATIFIED AND STRIKEABLE: THE `h2` LANE IS OPEN AS '
             'ACTIVE RESEARCH.** *b360’s sentence is a dated measurement and not a rule; the '
             'navigator’s handoff line forbidding routes at the wall is WITHDRAWN as an '
             'instruction and kept as a discipline: a proposal at the clause is registered with its '
             'falsifiers and its control before any number is computed, and a resemblance is named as '
             'one. The compression register — Weil’s form on finite families of the '
             'corpus’s own windows, its signature, with the Epstein function as control — is '
             'entered as a research lane with its own trail entry.*', '',
             '**THE LANE IS OPENED HERE AND NOTHING IS COMPUTED IN IT.** This entry exists so that a '
             'later act’s first number has something to be measured against. What the lane is:',
             '',
             '- **The register.** Weil’s form evaluated on **finite families of the corpus’s '
             'own windows** — the test functions the arc already built and banked — and the '
             '**signature** of the resulting form.',
             '- **The control, named before any run:** the **Epstein function** of row `F7`, the '
             'corpus’s second object, for which the analogue of RH is **false**. A signature '
             'behaviour that does not separate the control from ξ is not evidence about ξ.',
             '- **The discipline `(R84)` keeps:** a proposal is **registered with its falsifiers and '
             'its control before any number is computed**, and **a resemblance is named as one** rather '
             'than allowed to function as an argument.', '',
             '**What this entry does not do.** It states no proposal, computes no form, builds no '
             'family, evaluates no signature, and claims nothing about `h2`, which stands exactly where '
             'the deposit left it. **It confers no grade and enters no site of row `U1`.** The four '
             'lists are open.', '',
             '*Entered by b474 with the fold at ten (relay `data/b474_lane.txt`). `(R61)`’s and '
             '`(R76)`’s trigger is untouched by this lane; no bridge is typed from it to any site '
             'or register.*']
    st_l = append(OT, 'OPEN_TRAILS.md', MARK_L, lbody, rec)
    rec('  ### FINDINGS %s ; DIGEST %s ; LANE %s' % (st_f, st_d, st_l))
    io.open(os.path.join(D, 'b474_lane.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(lbody) + NL)
    sp2, out2 = span(474)
    rec('')
    rec('  ### ### **THE SPAN READ BACK AFTER THE WRITE, PRINTED AND NOT ASSUMED:**')
    for l in out2.splitlines():
        if re.search(r'the last fold covers|FILED BY|next span STARTS AT|THE CURRENT SPAN', l):
            rec('      ' + l.strip())
    io.open(os.path.join(D, 'b474_span_notes2.txt'), 'w', encoding='utf-8', newline=NL).write(out2)
    io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0 if all(x in ('WRITTEN', 'DUPLICATE') for x in (st_f, st_d, st_l)) else 1


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'verify'
    sys.exit(dict(verify=verify, write=write)[mode]())
