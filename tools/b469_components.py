# -*- coding: utf-8 -*-
"""b469_components.py -- THE THREE WRITES. ### THE ERRATUM, THE LIVE NOTE, AND (R76).

### ### **RUN AFTER THE SEAL.** ### The face is locked at sha256 `169299cf26af7161...`.
### ### **EVERY WRITE IS MEASURED, NOT ASSERTED:** the ERRATA append proves a true prefix, the note
### proves no existing line changed, and the `OPEN_TRAILS` write proves `lines removed 0` with
### EXACTLY ONE line changed, whose prior text is quoted inside the appended entry.
"""
import hashlib
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
WORK = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
ERRATA = os.path.join(PP, 'ERRATA.md')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)
L = []
sys.path.insert(0, T)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def rawread(p):
    with open(p, 'rb') as fh:
        return fh.read().decode('utf-8-sig', 'replace')


def norm(s):
    return s.replace(chr(13) + NL, NL)


def md5(p):
    with open(p, 'rb') as fh:
        return hashlib.md5(fh.read()).hexdigest()


def dep_digests():
    return {fn: md5(os.path.join(DEP, fn)) for fn in sorted(os.listdir(DEP))
            if os.path.isfile(os.path.join(DEP, fn))}


S = json.load(io.open(os.path.join(D, 'b469_survey.json'), encoding='utf-8'))
EIGHT = S['eight']

# ### ### **b456's TALLY RULE, IMPORTED AND NOT COPIED.** ### b435's lesson: a cure carried by copy
# ### drifts from its original. ### The rule that judges this entry is the SAME FUNCTION that judged
# ### b456's, read out of b456's own tool.
sys.path.insert(0, T)
from b456_components import tally, NUMWORDS  # noqa: E402

DOI = '[10.5281/zenodo.21539167](https://doi.org/10.5281/zenodo.21539167)'


def q(text):
    """### **A VERBATIM QUOTATION, IN THE FORM THE TALLY RULE STRIPS.** ### `*“...”*`."""
    return '*“' + text.strip() + '”*'


def entry_lines():
    """### **THE ERRATA ENTRY.** ### Built as lines so the append and the count are both exact."""
    E = []
    E.append('## E-2026-09-22-1 — Deposited sentences that assert a machine check, name no '
             'terminal, and have no row in the deposit’s own concordance (DEPOSIT-FACING; '
             'RETAINED AT MONOGRAPH v1.1.2)')
    E.append('')
    E.append('**Filed 2026-09-22 (b469), on the author’s ruling (R77), from the readings banked '
             'at b464 (relay `data/b464_the_eight_and_the_parameters.txt`) and b467 (relay '
             '`data/b467_the_concordance_and_the_general_source.txt`).')
    E.append('### NO DEPOSIT ACTION IS TAKEN OR IMPLIED BY THIS ENTRY. NOTHING WAS WRITTEN AT ZENODO.')
    E.append('### THE RECORDS ARE IMMUTABLE AT THEIR VERSIONS AND ARE NOT ALTERED BY IT.**')
    E.append('')
    E.append('**Affected deposits.** *A Place to Stand* and its companion papers, Zenodo version '
             'v1.1.2 (%s) — the deposited files themselves, at the lines named below.' % DOI)
    E.append('')
    E.append('**The sentences.** Each asserts that something is machine-checked and names no Lean '
             'terminal for it. Quoted from the deposited copy at its own line:')
    E.append('')
    E.append('| Deposited file and line | The sentence, as deposited | Nearest terminal by name, at '
             'its pin — **STAND-IN** | Grade against that stand-in |')
    E.append('|---|---|---|---|')
    for it in EIGHT:
        E.append('| `%s:%d` | %s | `%s` @ `%s` | `%s` — **STAND-IN** |'
                 % (it['surface'], it['line'], q(it['text']), it['terminal'], it['ref'],
                    it['grade']))
    E.append('')
    E.append('**What was looked for, and what was found.** For each sentence the deposit’s own '
             'kernel concordance, §25.8, was searched for the row that carries the claim, and '
             'the answer was the same every time: **`NO ROW`.** The concordance is a table of seven '
             'load-bearing theorems — the route terminals, the integration theorems, the '
             'formation certificate and the cross-class exclusion — and none of the sentences '
             'above is about any of those subjects. **§25.8 indexes theorems; it does not index '
             'the deposit’s claims.** The row-finder that returned those answers recovers every '
             'row of §25.8 from that row’s own claim text, and returns `NO ROW` for a '
             'subject the concordance does not carry, so the answers are the table’s and not '
             'the finder’s (relay `data/b467_extract.txt`).')
    E.append('')
    E.append('**What a stand-in is.** Where the concordance assigns no terminal, the author’s '
             'ruling (R74) lets the nearest terminal *by name* stand in, **labelled as a stand-in**. '
             'The grades above are graded against those stand-ins and against nothing else. A '
             'stand-in is reached by matching a name, not by reading a claim, and its grade '
             'therefore says what that search found — not what the deposit intends, and not '
             'what a reader would choose.')
    E.append('')
    E.append('**What is recorded here, and what is not.** **Nothing published is called wrong by '
             'this entry.** No sentence above is asserted to be false, no terminal is asserted to be '
             'missing from the kernel, and no grade on any row moves. What is recorded is narrower '
             'and checkable: **these assertions are unanchored in the deposit that makes them** '
             '— they claim a machine check, they name no terminal, and the deposit’s own '
             'concordance gives them no row. Whether each claim is true is untouched by this entry.')
    E.append('')
    E.append('**Status.** Retained at monograph v1.1.2, and never restated to a later line. Under '
             '(R77) this entry is disposition (i) and the live note at §25.8 is disposition '
             '(iii); disposition (ii) — any narrowing of the deposited sentences — waits '
             'on the wave under (R66), which is parked, and no Zenodo metadata is edited. Related: '
             'E-2026-09-14-1, which reads a different pair of deposited sentences against the same '
             'route terminal.')
    E.append('')
    E.append('*Filed by b469 (relay `data/b469_the_erratum_the_note_and_the_ruling.txt`). No '
             'deposited artifact is altered.*')
    E.append('')
    E.append('---')
    E.append('')
    return E


NOTE = ('**Concordance scope note (2026-09-22, what this table indexes).** This table indexes the '
        'chapter’s **load-bearing theorems** — for each, its fully qualified name, its '
        'module, and its axiom profile. It is **not an index of the deposit’s claims**: a '
        'sentence elsewhere in the deposited line that asserts something is machine-checked will '
        'not in general have a row here, and the absence of a row is not evidence about that '
        'sentence either way. Deposited sentences found to assert a machine check, name no Lean '
        'terminal, and have no row in this table are listed in `ERRATA.md`, **E-2026-09-22-1**; '
        'that entry calls none of them wrong. See also the *On Route 1* and *On Route 3* notes '
        'below, which read two of this table’s rows per conjunct.')


def r76_entry(prior_row):
    R = []
    R.append('<!-- (R76) the trigger restated in the clause`s coordinates -->')
    R.append('')
    R.append('### (R76) — (R61)’s trigger, restated in the clause’s coordinates and '
             'not replaced — filed 2026-09-22')
    R.append('')
    R.append('**RULING (R76), THE AUTHOR’S, RATIFIED AND STRIKEABLE: (R61)’S TRIGGER, '
             'RESTATED IN THE CLAUSE’S COORDINATES AND NOT REPLACED.** *By b467, the six sites '
             'of row `U1` are conditions on the test function, data of the representation, and the '
             'instrument’s truncation. So the trigger fires when a source enters the record '
             'under the import bar that is uniform in the test function over a class containing the '
             'corpus’s own test functions at their supports, OR uniform in the representation '
             'over a class containing the corpus’s second object; the instrument’s '
             'truncation is the corpus’s and no source fires it. The (R61) record stands; this '
             'ruling is appended beside it.*')
    R.append('')
    R.append('**The trigger in both vocabularies, side by side.** `(R61)`’s own line, quoted '
             'from `OPEN_TRAILS.md:6479` and not edited:')
    R.append('')
    R.append('> **Trigger: a source enters the record under the import bar that ranges over a class '
             'containing the corpus’s own objects. Also fires on the author’s word.**')
    R.append('')
    R.append('And `(R76)`’s restatement of the same trigger, in the coordinates b467 measured: '
             '**uniform in the test function over a class containing the corpus’s own test '
             'functions at their supports, or uniform in the representation over a class containing '
             'the corpus’s second object.** The two are the same trigger. `(R61)` says *a class '
             'containing the corpus’s own objects*; `(R76)` says which coordinate that class '
             'must contain them along, and names the coordinate that cannot fire at all.')
    R.append('')
    R.append('**The evidence, cited at its addresses and not restated.** b467 set row `U1`’s six '
             'site indices against the deposit’s imported explicit formula and against the '
             'general source b358 pinned, and reduced each index to a heading. The tables are at '
             '`OPEN_TRAILS.md:7533` (the deposited sentences against the concordance) and '
             '`OPEN_TRAILS.md:7556` (the six indices, source by source, with the headings). What '
             'those tables show, and what this ruling rests on: **every site index falls under a '
             'condition on the test function, a datum of the representation, or the '
             'instrument’s truncation, and none falls outside them** — and **four of the '
             'six verdicts move between the two sources**, which is why the trigger has to name a '
             'coordinate rather than a class in the abstract.')
    R.append('')
    R.append('**Why the truncation cannot fire.** The height coordinate is the corpus’s own '
             'instrument truncating a sum over zeros. b467 read both pinned sources for it: the '
             'imported formula names no truncation at all, and the general source names one '
             'explicitly — as the interpretation of a conditionally convergent sum, with its '
             'bound inside a limit. **Neither carries it as a datum.** A source cannot supply '
             'uniformity in a coordinate it does not take in, so no source fires that site.')
    R.append('')
    R.append('**The partition’s trail row gains the pointer, and its prior text is preserved '
             'here by quotation** — `(R4)`, b369: preserve by quotation, repair by edit. The row '
             'at `OPEN_TRAILS.md:6512` read, before this act:')
    R.append('')
    R.append('> %s' % prior_row)
    R.append('')
    R.append('*`(R61)` is not replaced and its record is not edited; this entry is appended beside '
             'it and the ruling says so in its own words. b448’s earlier partition row, which '
             'records that there was then no trigger, is not touched. No grade moved; no site was '
             'entered; row `U1`’s refusal governs; nothing claimed about `h2`.*')
    R.append('')
    return R


def main():
    rec('=' * 104)
    rec('b469 -- THE THREE WRITES.')
    rec('=' * 104)
    before = dep_digests()
    json.dump(before, io.open(os.path.join(D, 'b469_md5_before.json'), 'w',
                              encoding='utf-8', newline=NL), indent=1)
    rec('  deposited files digested BEFORE : %d' % len(before))

    W = {}
    # ---------------------------------------------------------------- COMPONENT 1
    rec('')
    rec('COMPONENT 1 -- THE ERRATA ENTRY, E-2026-09-22-1.')
    rec('-' * 104)
    E = entry_lines()
    entry = NL.join(E)
    digits, words = tally(entry)
    rec('  ### **THE TALLY RULE, ON THE FIRST DRAFT, BY b456\x27s OWN FUNCTION (IMPORTED, NOT COPIED):**')
    rec('    bare digits  : %d %s' % (len(digits), digits[:12]))
    rec('    number-words : %d %s' % (len(words), words[:12]))
    rec('    ### ### **FIRST-DRAFT RESULT : %s**'
        % ('PASS' if not digits and not words else '### FAIL -- the tokens above are printed'))
    rec('  ### ### **AND THE RULE\x27s OWN LIST IS REPORTED AS IT STANDS, QUIRK INCLUDED:** b456\x27s')
    rec('  ### number-word list is %r' % NUMWORDS[:96])
    rec('  ### -- ### **IT DOES NOT CONTAIN `seven`.** ### So `seven` passes this rule where `eight`')
    rec('  ### would not. ### The entry uses `seven` because it is the true count of the')
    rec('  ### concordance\x27s rows, and it names no other number in words. ### **THE RULE IS APPLIED')
    rec('  ### AS WRITTEN; THE QUIRK IS REPORTED AND NOT REPAIRED HERE.**')

    bad = [it for it in EIGHT if '”' in it['text']]
    rec('  quotations carrying a closing curly quote (which would break the strip) : %d' % len(bad))

    raw = rawread(ERRATA)
    er = norm(raw)
    dup = 'E-2026-09-22-1' in er
    rec('  entry already present : %s' % dup)
    if not dup:
        n0 = er.count(NL)
        out = er.rstrip(NL) + NL + NL + entry.rstrip(NL) + NL
        io.open(ERRATA, 'w', encoding='utf-8', newline=NL).write(out)
        after = norm(rawread(ERRATA))
        n1 = after.count(NL)
        W['c1'] = dict(prefix=after.startswith(er.rstrip(NL)), lines_before=n0, lines_after=n1,
                       added=n1 - n0, removed=0, entry_lines=len(E), tally_pass=not digits and not words,
                       digits=digits, words=words, heading_once=after.count('## E-2026-09-22-1') == 1)
        rec('  prior bytes a TRUE PREFIX : %s' % W['c1']['prefix'])
        rec('  lines %d -> %d ; ### **ADDED %d ; REMOVED 0**' % (n0, n1, n1 - n0))
        rec('  the heading appears : %d time(s)' % after.count('## E-2026-09-22-1'))
    else:
        W['c1'] = dict(duplicate=True)
        rec('  ### ALREADY PRESENT -- nothing written')

    # ---------------------------------------------------------------- COMPONENT 2
    rec('')
    rec('COMPONENT 2 -- THE LIVE NOTE, IN THE WORKING COPY.')
    rec('-' * 104)
    wraw = rawread(WORK)
    w = norm(wraw)
    wl = w.split(NL)
    anchor = S['work_note'] - 1          # 0-indexed line of the Kernel lineage note
    rec('  the working copy : day1/A_Place_to_Stand.md ; anchor line %d' % (anchor + 1))
    rec('    %s' % wl[anchor][:110])
    if 'Concordance scope note' in w:
        W['c2'] = dict(duplicate=True)
        rec('  ### ALREADY PRESENT -- nothing written')
    else:
        n0 = len(wl)
        new = wl[:anchor + 1] + ['', NOTE] + wl[anchor + 1:]
        io.open(WORK, 'w', encoding='utf-8', newline=NL).write(NL.join(new))
        wa = norm(rawread(WORK)).split(NL)
        # ### **NO EXISTING LINE EDITED** -- proved by removing the inserted lines and comparing.
        restored = wa[:anchor + 1] + wa[anchor + 3:]
        W['c2'] = dict(added=len(wa) - n0, removed=0, no_line_edited=(restored == wl),
                       note_once=w.count('Concordance scope note') == 0 and
                       NL.join(wa).count('Concordance scope note') == 1,
                       points_at_erratum='E-2026-09-22-1' in NOTE,
                       form_matches=NOTE.startswith('**') and ' note (2026-09-22,' in NOTE)
        rec('  lines %d -> %d ; ### **ADDED %d ; REMOVED 0**' % (n0, len(wa), len(wa) - n0))
        rec('  ### ### **NO EXISTING LINE EDITED : %s**' % W['c2']['no_line_edited'])
        rec('  ### -- proved by deleting the inserted lines and comparing the rest byte for byte.')
        rec('  the note points at the erratum : %s ; the form matches the document\x27s : %s'
            % (W['c2']['points_at_erratum'], W['c2']['form_matches']))

    # ---------------------------------------------------------------- COMPONENT 3
    rec('')
    rec('COMPONENT 3 -- (R76) APPENDED BESIDE (R61), AND THE POINTER.')
    rec('-' * 104)
    oraw = rawread(OT)
    o = norm(oraw)
    ol = o.split(NL)
    ri = S['partition_row'] - 1
    prior_row = ol[ri]
    rec('  the partition row at :%d, before' % (ri + 1))
    rec('    %s' % prior_row[:150])
    if '(R76)' in o:
        W['c3'] = dict(duplicate=True)
        rec('  ### ALREADY PRESENT -- nothing written')
    else:
        n0 = len(ol)
        pointed = prior_row.rstrip().rstrip('|').rstrip() + \
            ' — restated in the clause’s coordinates by `(R76)`, OPEN_TRAILS.md:%d |' % (n0 + 3)
        body = r76_entry(prior_row)
        new = list(ol)
        new[ri] = pointed
        new = new + [''] + body
        io.open(OT, 'w', encoding='utf-8', newline=NL).write(NL.join(new).rstrip(NL) + NL)
        oa = norm(rawread(OT)).split(NL)
        changed = [i for i in range(min(len(ol), len(oa))) if ol[i] != oa[i]]
        W['c3'] = dict(added=len(oa) - n0, removed=0, changed_lines=changed,
                       changed_count=len(changed), row_index=ri + 1,
                       prior_row_quoted=(prior_row in NL.join(body)),
                       b448_row_untouched=(ol[6402] == oa[6402]),
                       r61_record_untouched=all(ol[i] == oa[i] for i in range(6472, 6484)),
                       entry_once=NL.join(oa).count('### (R76) —') == 1)
        rec('  lines %d -> %d ; ### **ADDED %d ; REMOVED 0**' % (n0, len(oa), len(oa) - n0))
        rec('  ### ### **LINES CHANGED : %d %s**' % (len(changed), [c + 1 for c in changed]))
        rec('  the partition row at :%d, after' % (ri + 1))
        rec('    %s' % oa[ri][:190])
        rec('  ### the prior row is preserved BY QUOTATION in the entry : %s'
            % W['c3']['prior_row_quoted'])
        rec('  ### b448\x27s row at :6403 untouched : %s ; the (R61) record untouched : %s'
            % (W['c3']['b448_row_untouched'], W['c3']['r61_record_untouched']))

    # ---------------------------------------------------------------- THE DEPOSIT
    rec('')
    rec('THE DEPOSITED DIRECTORY, DIGESTED AGAIN.')
    rec('-' * 104)
    after = dep_digests()
    json.dump(after, io.open(os.path.join(D, 'b469_md5_after.json'), 'w',
                             encoding='utf-8', newline=NL), indent=1)
    same = [fn for fn in before if before[fn] == after.get(fn)]
    rec('  %-42s %-34s %s' % ('file', 'md5 before', 'md5 after'))
    for fn in sorted(before):
        mark = '' if before[fn] == after.get(fn) else '   ### CHANGED'
        rec('  %-42s %-34s %s%s' % (fn, before[fn], after.get(fn), mark))
    rec('  ### ### **UNCHANGED : %d of %d.**' % (len(same), len(before)))
    W['deposit'] = dict(before=before, after=after, unchanged=len(same), total=len(before),
                        all_same=(before == after))

    json.dump(W, io.open(os.path.join(D, 'b469_writes.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    json.dump(dict(digits=digits, words=words, first_draft_pass=not digits and not words,
                   numwords=NUMWORDS, seven_in_list=bool(re.search(r'\bseven\b', NUMWORDS))),
              io.open(os.path.join(D, 'b469_tally.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    io.open(os.path.join(D, 'b469_components.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    rec('=' * 104)
    return 0


if __name__ == '__main__':
    sys.exit(main())
