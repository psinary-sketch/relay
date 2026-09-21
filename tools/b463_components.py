# -*- coding: utf-8 -*-
"""b463_components.py -- THE FOLD AT SPAN NINE, b454 THROUGH b462. ### **PURELY ADDITIVE. AFTER THE LOCK.**

### Usage: `verify` -- every row's verdict strings matched in its own closing, into data/b463_fold.json
###        and data/b463_components.txt; `write` -- the FINDINGS section and the (R31) digest block, each
###        appended with its HEAD blob proved a prefix, into data/b463_fold_run.txt.
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
FOLDJ, COMP, RUN = (os.path.join(D, 'b463_fold.json'), os.path.join(D, 'b463_components.txt'),
                    os.path.join(D, 'b463_fold_run.txt'))
MARK_F = '<!-- b463 the fold: b454-b462, the deposit-and-instrument arc -->'
MARK_D = '<!-- b463 orientation refresh: the deposit-and-instrument arc -->'
HEADING = '## THE DEPOSIT-AND-INSTRUMENT ARC, b454–b462 — THE FOLD'
NL = chr(10)

sys.path.insert(0, T)
from b463_extract import ROWS, norm      # noqa: E402  ### THE ROWS AND THE NORMALISER, IMPORTED

ONE = ('**An instrument that had reported every act passing was found never to have been asked to '
       'fail, by the rule it existed to apply — and the same reading, turned on the deposit, found '
       'eight sentences asserting a machine check that point at nothing.**')

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
    rec('b463 -- THE FOLD AT SPAN NINE, b454 THROUGH b462. ### VERIFY.')
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
    sp, _ = span(463)
    rec('')
    rec('  ### ### **ROWS %d ; STRINGS %d ; VERIFIED %d ; ROWS NOT CARRIED %d.**'
        % (len(rows), n_strings, n_ver, sum(1 for r in rows if not r['verified'])))
    rec('  ### columns : %s ; ### **OBJECT %d**' % (' ; '.join('%s %d' % (k, cols[k]) for k in sorted(cols)),
                                                    cols.get('OBJECT', 0)))
    rec('  ### span by the tool through this filing act : %s ; the fold`s own span, filing act excluded : 9'
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
    nz = lambda s: s.replace(chr(13) + NL, NL)
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
            '**Nine acts, b454 through b462 — the span at `(R1)`’s declared threshold exactly.** '
            '`b363_span.py` reads **%s** through this filing act; the fold’s own span, the filing act '
            'excluded as at b434, b444 and b453, is **9**.' % F['span_tool'], '',
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
             '**%d verdict strings across %d acts, every one matched in that act’s own closing bank, '
             'with both sides normalised for curly quotes, dashes, backticks and whitespace.** One string '
             'was corrected before the seal: the wording first chosen for b458 sits in its components bank '
             'and not in its closing, and **a fold may carry only what the act’s own closing says**.'
             % (F['strings'], len(F['rows'])), '',
             '### The three columns, kept apart', '',
             '**Statements about the object** — the zeros, ξ, the Euler balance: **%d**. **About '
             'the model** — kernel terminals, their axiom profiles, the instrument’s channels and '
             'cells: **%d**. **About the record** — its documents, deposits, rulings, tools and grades: '
             '**%d**. Three acts were borderline, each named in its row rather than rounded: b455, b459 and '
             'b460.' % (c.get('OBJECT', 0), c.get('MODEL', 0), c.get('RECORD', 0)), '',
             '**The object column is empty for the ninth consecutive span and is carried as a property of '
             'the span, not as an achievement.** Nine acts read the deposit, the kernel’s printed '
             'profiles, the record’s rulings and the suite’s own arms, and not one of them made a '
             'statement about ξ, about the Epstein object, or about any zero.', '',
             '### The carried arm failures, all real', '',
             '**b461’s two breaches.** `G-WRITELIST-KINDS` failed on `b461_components.py` and '
             '`b461_exercise.json` — a second tool and a json sibling its locked face did not name. '
             'Both files were kept as evidence and **the arm was not weakened**.', '',
             '**The version-naming mismatch, at b461 and again at b462, now closed by `(R73)`.** A face '
             'that wrote *“and its versions 2, 3, 4”* named no file the arm could read, and the '
             'arm reads full filenames. b460 spelled them out and passed; b461 compressed them and failed; '
             'b462 compressed them and failed on the mismatch **alone**, its write-list discipline otherwise '
             'clean. **`(R73)` moves the convention and leaves the arm where it is.**', '',
             '### Errors entered as their owners’', '',
             '**The navigator’s, five, in the order’s own words:** the twenty-eight annotation '
             'targets miscounted (b454); `(N2)` at b459 refuted at five of six; the `√17` observation '
             'answered by `√13` already in the record, which b447 had noted sits at a prime power **and '
             'converged**; the `45`/`494` figures attributed to b455 when they are b457’s, and measured '
             'over a wider population; and a population named at b462 that was not banked — the two '
             'kernel records’ Zenodo descriptions, which hold zero description characters.', '',
             '**The seat’s, as its acts entered them.** b458: a block rule that ranked file shape '
             'rather than ruling text, failing at three tiers, with every yield printed; a live banned stem; '
             'a discarded return code; and a write-list arm that turned FAIL to PASS when a later commit '
             'landed. b459: a cut rule that assumed one enumeration where row `U1` has two, and a matcher '
             'that assumed a vocabulary two sites do not use. b460: a face incomplete twice, caught by the '
             'registration gate and the bar-floor arm. b461: two gate refusals, a case-sensitive needle, and '
             'an arm defective on its own positive control. b462: a bad escape in a replacement template, '
             'caught by the rehearsal, and an arm that read the world instead of its supplied source. '
             '**Six acts of the nine found a defect in their own instrument before their own close.**', '',
             '### The rulings of the span, with their status', '',
             '| ruling | status |', '|:--|:--|',
             '| `(R63)` the twenty-nine and ENUMERA, disposed by the data | **executed at b454** under `(R64)` |',
             '| `(R64)` the four blockers on `(R63)` | **executed at b454**; `(R64)(4)` deferred |',
             '| `(R65)` dispositions (i) and (iii), not (ii) | **executed at b456**; (ii) waits on the wave |',
             '| `(R66)` the deposit is corrected, not re-issued | **STANDING** — a rule with no closing act; the wave stays parked |',
             '| `(R67)` the route terminals are profiled at the deposited tag | **executed at b457**, all three standard three |',
             '| `(R68)` THE_RESIDUE_OF_RH’s held cells take the merged-branch term | **executed at b457** |',
             '| `(R69)` the mirror zip is named by date, with the act suffix when an act is open | **executed at b459**; closed `W-ORD-MIRROR-ZIP-NAME` |',
             '| `(R70)` the counted rehearsal | **executed from b460 onward**, on every face since |',
             '| `(R71)` TECHNE-Core’s commits are pushed | **executed at b460**; twenty-four landed, verified at the remote |',
             '| `(R72)` the retirement rule is the applied one | **entered at b462**; its second limb triggers at the next act that touches the suite |',
             '| `(R73)` the write-list arm’s reading governs | **entered and obeyed at b463**, by this fold’s own face |',
             '',
             '*`(R66)` is the only ruling of the span that stands rather than closes, and it stands by its '
             'own nature: it opens a wave when substance moves, and no substance moved.*', '',
             '### Filed with this fold, not done by it', '',
             '**The desk carries eight standing items into b464**, among them the sentence gate priced at '
             'twelve acts and not built; `(R66)`; the twelve face-only arms awaiting `(R72)`’s second '
             'limb; the two kernel records’ unbanked Zenodo descriptions, which need a lane permitting '
             'a fetch; and b462’s census itself, whose three hundred `NAMES NOTHING` items **are not a '
             'defect count** — their strongest members are attributions to Ostrowski, Størmer, '
             'Artin–Whaples, Riemann, Hecke and Tate, which name no kernel terminal because they are '
             'not kernel claims. **The four lists are open.**', '',
             '*Filed by b463 (relay `data/b463_fold.json`, `data/b463_the_fold_at_span_nine.txt`). Nothing '
             'above this section was edited; no grade is conferred by a seat; nothing is minted; nothing is '
             'claimed about `h2`.*']
    st_f = append(FINDINGS, 'FINDINGS.md', MARK_F, body, rec)
    fnd = read(FINDINGS)
    m = re.search(re.escape(HEADING) + r'.*?### The arc in one statement\s*\n\s*\n(.+?)\n', fnd, re.S)
    quoted = m.group(1).strip() if m else None
    rec('  the arc`s one statement located in the section just written : %s' % bool(quoted))
    dbody = [MARK_D, '',
             '**Orientation refresh — filed b463, 2026-09-21 *(additive)*.** Under `(R31)` a fold '
             'refreshes this digest. The arc folded at b463 — **THE DEPOSIT-AND-INSTRUMENT ARC, '
             'b454–b462** — carries this one statement, quoted from its fold:', '',
             quoted or '*NOT LOCATED in its fold section; nothing is summarised in its place.*', '',
             '**The governing claim at the head of this document is unchanged by the arc**, whose object '
             'column is empty: nine acts read the deposit, the kernel’s printed profiles and the '
             'record’s own instruments, and none made a statement about the object. `h2` stands where '
             'the deposit left it.']
    st_d = append(DIGEST, 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md', MARK_D, dbody, rec) if quoted else 'NOT WRITTEN'
    rec('  ### FINDINGS %s ; DIGEST %s' % (st_f, st_d))
    sp2, out2 = span(463)
    rec('')
    rec('  ### ### **THE SPAN READ BACK AFTER THE WRITE, PRINTED AND NOT ASSUMED:**')
    for l in out2.splitlines():
        if re.search(r'the last fold covers|FILED BY|next span STARTS AT|THE CURRENT SPAN', l):
            rec('      ' + l.strip())
    io.open(os.path.join(D, 'b463_span_notes2.txt'), 'w', encoding='utf-8', newline=NL).write(out2)
    io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0 if st_f in ('WRITTEN', 'DUPLICATE') and st_d in ('WRITTEN', 'DUPLICATE') else 1


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'verify'
    sys.exit(dict(verify=verify, write=write)[mode]())
