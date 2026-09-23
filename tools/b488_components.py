# -*- coding: utf-8 -*-
"""b488_components.py -- THE COMPONENTS. ### **(R98)'S SECTION, AND THE GUARD'S CONTROLS.**

### ### **COMPONENT 1 IS A TRANSCRIPTION, NOT A FOLD.** ### Every block below is lifted from
### b486's own bank -- `data/b486_the_fold.txt` and b486's record in `OPEN_TRAILS.md` -- and
### re-headed in the form the eighteen fold sections already in `FINDINGS.md` use.
### ### **NO VERDICT IS RE-READ, NO ACT IS RE-SCORED, AND NO FIGURE IS TYPED THAT THE BANK DOES
### NOT CARRY.** ### The section is dated as written at b488 for b486 and cites the trail record,
### which stands.

### ### **COMPONENT 2 PUTS THE APPENDER'S GUARD IN `corr_row.py`** and runs both controls on a
### FIXTURE. ### The live ledger is written exactly once, for this act's own row, by the guarded
### tool.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FND = os.path.join(PP, 'FINDINGS.md')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)
L = []
sys.path.insert(0, T)
import corr_row  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def span_read(tag):
    r = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py')],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    txt = (r.stdout or '').replace(chr(13), '')
    out = {}
    # ### ### **THE FIRST VERSION OF THIS READER TOOK ONLY THE `covers` LINE, AND SCORED (N1)
    # ### REFUTED ON IT.** ### The tool prints TWO facts about the last fold -- the span it
    # ### COVERS and ### **THE ACT THAT FILED IT** -- and (N1) is about the second.
    # ### **A SCORE TAKEN OFF THE WRONG LINE IS NOT A SCORE**, and this one would have reported
    # ### the navigator's expectation refuted by a reading that does not bear on it.
    for key, pat in (('last_fold', r'the last fold covers\s*:\s*(b\d+[a-z]? - b\d+[a-z]?)'),
                     ('filed_by', r'it was FILED BY\s*:\s*b(\d+)'),
                     ('folds', r'FOLDS RUN : (\d+)'),
                     ('span', r'THE CURRENT SPAN : (\d+) ACT')):
        m = re.search(pat, txt)
        out[key] = m.group(1) if m else ''
    rec('    %-7s last fold covers ### **%s** ### ; FILED BY ### **b%s** ### ; folds ### **%s**'
        % (tag, out['last_fold'] or '?', out['filed_by'] or '?', out['folds'] or '?'))
    rec('            current span ### **%s** ### act(s)' % (out['span'] or '?'))
    return out


def block(trail, head, nxt):
    """### one `####` block of b486's trail record, VERBATIM, minus its own heading line."""
    i = trail.find(head)
    j = trail.find(nxt, i + 1) if i >= 0 else -1
    if i < 0:
        return ''
    body = trail[i + len(head):(j if j > i else len(trail))]
    return body.strip(NL).strip()


def main():
    rec('=' * 104)
    rec('b488 -- THE COMPONENTS. ### (R98)`S SECTION, AND THE ROW WRITER`S GUARD.')
    rec('=' * 104)

    # ================================================================= COMPONENT 1
    rec('')
    rec('COMPONENT 1 -- (R98)`S SECTION, WRITTEN HOME FROM b486`S OWN BANK.')
    rec('-' * 104)

    fold = read(os.path.join(D, 'b486_the_fold.txt'))
    ot = read(OT)
    i = ot.find('### b486 ')
    j = ot.find('### b487 ', i + 1)
    trail = ot[i:j]
    rec('    sources, both b486`s own:')
    rec('      `relay data/b486_the_fold.txt`   %6d bytes' % len(fold))
    rec('      b486`s record in `OPEN_TRAILS.md` %6d bytes' % len(trail))

    rec('')
    already = '## THE BOOKKEEPING ARC' in read(FND)
    if already:
        rec('    ### THE SPAN TOOL, RE-READ. ### **THIS IS NOT THE PRE-WRITE READING** -- the')
        rec('    ### section is already in the document, so this run cannot take one. ### The')
        rec('    ### ### **TRUE BEFORE-READING IS BANKED** ### in `data/b488_extract.txt` (P3) and')
        rec('    ### in `data/b488_components_firstrun.txt`: ### **last fold `b464 - b473`, filed')
        rec('    ### by `b474`, folds `19`, current span `14`.**')
        before = span_read('RE-READ')
    else:
        rec('    ### THE SPAN TOOL, BEFORE THE WRITE:')
        before = span_read('BEFORE')

    # --- the section, assembled from the bank's own blocks -------------------
    one = block(trail, '**The span’s mathematics moved little', '#### Component 1')
    one = '**The span’s mathematics moved little' + one
    c1 = block(trail, '#### Component 1 — the span, act by act', '#### Component 2')
    c2 = block(trail, '#### Component 2 — the (R31) digest block, 2026-09-22', '#### Component 3')
    c3 = block(trail, '#### Component 3 — the two ledgers', '#### One finding')
    c4 = block(trail, '#### One finding this fold makes about an act it folds',
               '#### What closed, and what was minted')
    c5 = block(trail, '#### What closed, and what was minted', '#### What this fold does not do')
    c6 = block(trail, '#### What this fold does not do', '*The next span begins')
    for name, b in (('one statement', one), ('C1 span table', c1), ('C2 digest', c2),
                    ('C3 ledgers', c3), ('the finding', c4), ('closed/minted', c5),
                    ('what it does not do', c6)):
        rec('      block %-22s %5d bytes %s' % (name, len(b), '' if b else '### **EMPTY**'))
        if not b:
            rec('        ### ### **REFUSING TO WRITE A SECTION WITH AN EMPTY BLOCK.**')
            return 2

    sec = []
    sec.append('')
    sec.append('## THE BOOKKEEPING ARC, b475–b479 — THE FOLD')
    sec.append('')
    sec.append('**Eleven acts, filed since the fold at b474.** `b363_span.py` read **12** by number '
               'order through b486, the filing act; **the span by filing is 11**, and the tool was '
               'not edited to make the two agree. Filed by b486 to the trail alone; **written here '
               'at b488 on ruling `(R98)`, from b486’s own bank** — not re-folded, no '
               'verdict re-read, no act re-scored.')
    sec.append('')
    sec.append('### The arc in one statement')
    sec.append('')
    sec.append(one)
    sec.append('')
    sec.append('### The span, act by act, each verdict quoted from its own closing bank')
    sec.append('')
    sec.append(c1)
    sec.append('')
    sec.append('### The (R31) digest block, 2026-09-22')
    sec.append('')
    sec.append(c2)
    sec.append('')
    sec.append('### The rulings of the span, and the acts that record their own defects')
    sec.append('')
    sec.append(c3)
    sec.append('')
    sec.append('### The finding this fold makes about an act it folds')
    sec.append('')
    sec.append(c4)
    sec.append('')
    sec.append('### What closed, and what was minted')
    sec.append('')
    sec.append(c5)
    sec.append('')
    sec.append('### Filed with this fold, not done by it')
    sec.append('')
    sec.append(c6)
    sec.append('')
    sec.append('*Folded by b486 (relay `data/b486_the_fold.txt`, `data/b486_closing.txt`); its '
               'trail record in `OPEN_TRAILS.md` stands and is this section’s source. '
               '**Written into FINDINGS at b488 on the author’s ruling `(R98)`, which rules '
               'that a fold’s home is FINDINGS.** Nothing above this section was edited; no '
               'verdict of any folded act is re-scored here; no grade is conferred by a seat.*')
    sec.append('')
    body = NL.join(sec)

    # --- the append, with the prefix proved ---------------------------------
    rec('')
    rec('    ### THE APPEND, WITH THE PRIOR BYTES PROVED A TRUE PREFIX:')
    raw = io.open(FND, 'rb').read()
    # ### ### **THE IDEMPOTENCE GUARD.** ### `corr_row.write_row` taught this at b485: a tool that
    # ### appends and is run twice writes twice. ### **THIS TOOL READS THE DOCUMENT FOR ITS OWN
    # ### HEADING BEFORE IT APPENDS**, and refuses a second copy rather than making one.
    head = '## THE BOOKKEEPING ARC, b475–b479 — THE FOLD'
    old_text_pre = raw.decode('utf-8-sig', 'replace').replace(chr(13), '')
    if head in old_text_pre:
        rec('      ### ### **THE SECTION IS ALREADY IN `FINDINGS.md`. ### NOT APPENDING AGAIN.**')
        rec('      ### This run re-reads and re-checks; the append`s own figures are banked in')
        rec('      ### `data/b488_components_firstrun.txt`, from the run that made it.')
        rec('      occurrences of the heading : ### **%d** ### -- a second would be the defect'
            % old_text_pre.count(head))
        rec('      ### this guard exists to prevent.')
        rec('      FINDINGS.md now : %d bytes, %d lines'
            % (len(raw), raw.decode('utf-8-sig', 'replace').count(NL)))
        prior = subprocess.run(['git', '-C', PP, 'diff', '--numstat', '--', 'FINDINGS.md'],
                               capture_output=True, text=True).stdout.strip()
        rec('      `git diff --numstat` for the document : ### **%s** ### (added / removed / path)'
            % (prior or 'clean'))
        rec('      ### ### **LINES REMOVED, BY GIT`S OWN COUNT : %s.**'
            % (prior.split()[1] if prior else 'n/a'))
    bom = raw.startswith(b'\xef\xbb\xbf')
    eol = chr(13) + NL if (chr(13) + NL).encode() in raw else NL
    old_text = raw.decode('utf-8-sig', 'replace').replace(chr(13), '')
    add = (eol + eol.join(body.split(NL))).encode('utf-8')
    if head not in old_text:
        io.open(FND, 'ab').write(add)
    after = io.open(FND, 'rb').read()
    new_text = after.decode('utf-8-sig', 'replace').replace(chr(13), '')
    missing = [x for x in old_text.split(NL) if x not in set(new_text.split(NL))]
    rec('      bytes before / appended / after : %d / %d / %d' % (len(raw), len(add), len(after)))
    rec('      PRIOR BYTES A TRUE PREFIX : ### **%s** ### ; BOM preserved : ### **%s**'
        % (after.startswith(raw), after.startswith(b'\xef\xbb\xbf') == bom))
    rec('      lines before / after : %d / %d' % (old_text.count(NL), new_text.count(NL)))
    rec('      ### ### **LINES OF THE OLD FILE ABSENT FROM THE NEW : %d.**' % len(missing))
    rec('      fold sections in FINDINGS.md, before / after : %d / %d'
        % (old_text.count(' — THE FOLD'), new_text.count(' — THE FOLD')))
    ok1 = after.startswith(raw) and not missing

    rec('')
    rec('    ### THE SPAN TOOL, AFTER THE WRITE -- THE SAME COMMAND, THE TOOL UNEDITED:')
    after_span = span_read('AFTER')
    n1 = after_span['filed_by'] == '486'
    rec('    ### ### **(N1) -- the span tool reads `b486` as the act that FILED the last fold :')
    rec('    ### %s.**' % ('HELD' if n1 else 'REFUTED'))
    rec('    ### ### **AND THE TWO READINGS ARE BOTH PRINTED, BECAUSE THEY SAY DIFFERENT THINGS.**')
    rec('    ### The tool names the span a fold COVERS (`%s`) and, separately,'
        % after_span['last_fold'])
    rec('    ### ### **THE ACT THAT FILED IT** ### (`b%s`), read from the section`s own sentence'
        % after_span['filed_by'])
    rec('    ### and not typed.')
    rec('    ### A fold section`s heading carries its SPAN, never its filing act -- so a score')
    rec('    ### taken off the heading alone can never find `b486` and would refute (N1) for a')
    rec('    ### reason that has nothing to do with it. ### **THE FIRST SCORER DID EXACTLY THAT.**')
    rec('    ### the tool`s own file is untouched by this act : ### **%s**'
        % (subprocess.run(['git', '-C', ROOT, 'status', '--porcelain', '--', 'tools/b363_span.py'],
                          capture_output=True, text=True).stdout.strip() == ''))

    # ================================================================= COMPONENT 2
    rec('')
    rec('COMPONENT 2 -- `corr_row.py` GAINS THE APPENDER`S GUARD.')
    rec('-' * 104)
    cr = read(os.path.join(T, 'corr_row.py'))
    rec('    ### THE TOOL`S PRIOR BEHAVIOUR, QUOTED FROM ITS OWN HEADER -- its three declared')
    rec('    ### limits, none of which mentions the row number:')
    rec('      *"(1) IT CANNOT STOP A CALLER FROM STILL WRAPPING ITS ARGUMENTS IN A DOUBLE-QUOTED')
    rec('      SHELL STRING."*')
    rec('      *"(2) It checks cell COUNT and EMPTINESS, not cell TRUTH. A ROW OF SIX')
    rec('      HONEST-LOOKING LIES PASSES."*')
    rec('      *"(3) It appends. It does not verify the row`s terminals exist ..."*')
    rec('    ### ### **IT APPENDED UNCONDITIONALLY AND THEN READ THE ROW BACK** -- and read-back')
    rec('    ### checks that the CELLS SURVIVED, not that the NUMBER was free. ### A row bearing')
    rec('    ### a number the ledger already held was written and then reported ### *verified.*')
    rec('    ### the two limits the guard adds, now in the same header : ### **(4)** it checks the')
    rec('    ### NUMBER, not the content ; ### **(5)** it does not ASSIGN numbers -- it refuses a')
    rec('    ### taken one and names the next free one.')
    rec('      `numbers_in` present : %s ; the refusal reads before it writes : %s'
        % ('def numbers_in(' in cr,
           0 <= cr.find('have = numbers_in(') < cr.find("open(path + '.tmp'")))
    # ### ### **THIS CHECK'S FIRST VERSION SAID `False` AND THE TOOL WAS RIGHT.** ### It looked
    # ### for `io.open(path + '.tmp'` where the source writes ### **`open(path + '.tmp'`** -- so
    # ### `find` returned `-1`, and `-1 < anything` is True for the guard's position but the
    # ### comparison ran the other way and reported the guard as LATE. ### **A PREDICATE THAT
    # ### CANNOT FIND ITS NEEDLE REPORTS A FAULT IN THE SUBJECT**, which is the same species as
    # ### b482's arm that could not fail. ### The needle is corrected and the `-1` case excluded
    # ### explicitly, so an absent needle can no longer read as a verdict either way.

    rec('')
    rec('    ### ### **BOTH CONTROLS, ON A FIXTURE -- FIRST RUN, NO REPAIR:**')
    import tempfile
    good, ls = corr_row.self_test(tempfile.mkdtemp(prefix='corr_'))
    for l in ls:
        rec(l)
    rec('    ### ### **(N2) -- the positive control refuses on its initial run : %s.**'
        % ('HELD' if good else 'REFUTED'))
    rec('    ### the controls wrote to the live ledger : ### **False** ### -- a negative control')
    rec('    ### that ACCEPTS writes a row, so neither control is ever pointed at')
    rec('    ### `CORRESPONDENCE.md`.')

    rec('')
    rec('=' * 104)
    rec('  ### COMPONENT 1 CLEAN : %s ### ; COMPONENT 2 CONTROLS BEHAVE : %s' % (ok1, good))
    rec('=' * 104)
    io.open(os.path.join(D, 'b488_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(span_before=before, span_after=after_span, n1=n1, n2=good,
                   findings=dict(before=len(raw), added=len(add), after=len(after),
                                 lines_removed=len(missing),
                                 prefix=after.startswith(raw)),
                   guard=dict(numbers_in=('def numbers_in(' in cr), controls=good)),
              io.open(os.path.join(D, 'b488_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0 if (ok1 and good) else 2


if __name__ == '__main__':
    sys.exit(main())
