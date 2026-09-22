# -*- coding: utf-8 -*-
"""b469_extract.py -- THE SURVEY. ### THE ANCHORS, THE EIGHT QUOTATIONS, AND THE DEPOSITED DIGESTS.

### ### **THIS ACT WRITES TO LIVE SURFACES**, which no act in this arc has done since b456. ### So
### the survey's job is to fix, before the seal, exactly WHERE each write lands and exactly WHAT is
### there now -- the ERRATA entry form and its last entry, the working monograph's own annotation
### form beside section 25.8, the `(R61)` entry form and the partition's trail row -- and to take
### ### **THE DEPOSITED COPIES' DIGESTS BEFORE ANYTHING IS WRITTEN.**
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
L, MISSES = [], []

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


def md5(p):
    try:
        return hashlib.md5(open(p, 'rb').read()).hexdigest()
    except Exception:
        return None


def at(path, needle, label):
    for i, l in enumerate(read(path).split(NL)):
        if needle in l:
            return i + 1, l
    MISSES.append((os.path.basename(path), label, needle))
    rec('    ### MISS : %s -- %r' % (label, needle))
    return None, None


def main():
    rec('=' * 104)
    rec('b469 -- THE SURVEY. ### **THE ACT WRITES; THE SURVEY FIXES WHERE, AND WHAT IS THERE NOW.**')
    rec('=' * 104)

    rec('')
    rec('(P1) THE DEPOSITED COPIES, DIGESTED BEFORE ANYTHING IS WRITTEN.')
    rec('-' * 104)
    before = {}
    for fn in sorted(os.listdir(DEP)):
        p = os.path.join(DEP, fn)
        if os.path.isfile(p):
            before[fn] = md5(p)
    for fn in sorted(before):
        rec('    %-42s md5 %s' % (fn, before[fn]))
    rec('  ### ### **%d DEPOSITED FILES DIGESTED.** ### **NONE OF THEM IS A WRITE TARGET OF THIS ACT**'
        % len(before))
    rec('  ### -- the write targets are `ERRATA.md`, `day1/A_Place_to_Stand.md` and `OPEN_TRAILS.md`,')
    rec('  ### and the deposited directory is read here only so the closing can prove it unmoved.')

    rec('')
    rec('(P2) THE ERRATA ENTRY FORM, AND ITS LAST ENTRY.')
    rec('-' * 104)
    er = read(ERRATA)
    heads = [(i + 1, l) for i, l in enumerate(er.split(NL)) if l.startswith('## E-')]
    rec('    entries : %d ; ### **APPEND ORDER IS OLDEST-FIRST, NEWEST LAST**' % len(heads))
    rec('    first : %s:%d' % (os.path.basename(ERRATA), heads[0][0]))
    rec('      %s' % heads[0][1][:150])
    rec('    last  : %s:%d' % (os.path.basename(ERRATA), heads[-1][0]))
    rec('      %s' % heads[-1][1][:150])
    n, l = at(ERRATA, 'Filed by b456', 'b456 closing line of its entry')
    if n:
        rec('    the last entry closes at :%d' % n)
        rec('      %s' % l.strip()[:150])
    rec('    ### ### **E-2026-09-22-1 IS NOT PRESENT YET : %s**' % ('E-2026-09-22' not in er))
    rec('    ### the file ends with %r' % er[-40:])

    rec('')
    rec('(P3) THE WORKING MONOGRAPH, AND THE ANNOTATION FORM IT ALREADY USES.')
    rec('-' * 104)
    n258, _ = at(WORK, '## 25.8 Kernel Concordance', 'section 25.8 in the working copy')
    nlin, llin = at(WORK, '**Kernel lineage note (2026-07-24', 'the existing dated note')
    rec('    section 25.8 : day1/A_Place_to_Stand.md:%s' % n258)
    rec('    the note form already in use, at :%s' % nlin)
    rec('      %s' % (llin or '')[:150])
    rec('    ### ### **THE FORM IS `**<NAME> NOTE (<DATE>, <GLOSS>).** <TEXT>`**, sitting between the')
    rec('    ### section`s opening paragraph and its table. ### The new note goes BESIDE it, as a')
    rec('    ### sibling, and ### **NO EXISTING LINE IS EDITED.**')
    wl = read(WORK).split(NL)
    rec('    the line after it is a table head : %s' % (wl[nlin].strip()[:60] if nlin else '?'))

    rec('')
    rec('(P4) THE (R61) ENTRY FORM, AND THE PARTITION`S TRAIL ROW.')
    rec('-' * 104)
    n61, _ = at(OT, '<!-- (R61) the failure-mode partition', 'the (R61) comment anchor')
    nhead, lhead = at(OT, '### (R61) — the failure-mode partition', 'the (R61) heading')
    ntrig, ltrig = at(OT, '**Trigger: a source enters the record', 'the (R61) trigger line')
    # ### ### **THE FIRST NEEDLE WAS NOT UNIQUE AND IT MATCHED THE WRONG ROW.** ### `OPEN_TRAILS`
    # ### carries MORE THAN ONE partition row with the same prefix: b448's, whose trigger cell reads
    # ### *NO TRIGGER IN THE RECORD'S WORDS*, and the `(R61)`-ratified one that carries the trigger.
    # ### ### **b448's ROW IS A HISTORICAL RECORD OF WHAT b448 SAID AND MUST NOT BE EDITED**, and a
    # ### first-match needle would have edited exactly that. ### Every candidate is printed and the
    # ### row is selected by CONTENT -- the one whose trigger cell names `(R61)`.
    cands = [(i + 1, l) for i, l in enumerate(read(OT).split(NL))
             if l.startswith('| the failure-mode partition | FINDINGS.md:3375 |')]
    rec('    partition rows found : %d ### **EVERY ONE PRINTED; THE ROW IS CHOSEN BY CONTENT**'
        % len(cands))
    for i, l in cands:
        owns = '`(R61)`' in l
        rec('      :%-6d %s   %s' % (i, 'CARRIES (R61)' if owns else '### b448`s -- NOT EDITED',
                                     l.strip()[:120]))
    sel = [(i, l) for i, l in cands if '`(R61)`' in l]
    if len(sel) != 1:
        MISSES.append(('OPEN_TRAILS.md', 'exactly one (R61)-carrying partition row', len(sel)))
    nrow, lrow = (sel[0] if len(sel) == 1 else (None, None))
    rec('    the (R61) entry : OPEN_TRAILS.md:%s (comment) / :%s (heading)' % (n61, nhead))
    rec('    ### ### **THE (R61) RECORD`S OWN LINE, TO BE QUOTED BESIDE (R76)** -- :%s' % ntrig)
    rec('      %s' % (ltrig or '').strip()[:220])
    rec('    the partition`s trail row : OPEN_TRAILS.md:%s' % nrow)
    rec('      %s' % (lrow or '').strip()[:260])
    rec('    ### ### **THAT ROW IS AN EXISTING LINE AND THE ORDER SAYS IT GAINS A POINTER.** ### So')
    rec('    ### this act`s write to `OPEN_TRAILS.md` is ### **AN APPEND PLUS EXACTLY ONE LINE')
    rec('    ### CHANGED**, which is not a pure append and is measured as such: the prior text of')
    rec('    ### that row is preserved BY QUOTATION inside the appended entry -- `(R4)`, b369 --')
    rec('    ### and the closing proves `lines removed 0` and `lines changed 1`.')

    rec('')
    rec('(P5) b467`s TWO TABLES, CITED AT THEIR ADDRESSES AS (R76)`s EVIDENCE.')
    rec('-' * 104)
    n8, _ = at(OT, '| # | at | b464: nearest by name @pin |', 'b467 table one, the eight')
    n6, _ = at(OT, '| site | index | under CC (148), b464 |', 'b467 table two, the six sites')
    rec('    the eight, with NO ROW per sentence : OPEN_TRAILS.md:%s' % n8)
    rec('    the six sites against the general source : OPEN_TRAILS.md:%s' % n6)

    rec('')
    rec('(P6) THE EIGHT, FROM b464`s BANK, WITH THEIR VERBATIM SENTENCES.')
    rec('-' * 104)
    G = json.loads(read(os.path.join(D, 'b464_grades.json')))
    eight = []
    for it in G['items']:
        src = os.path.join(DEP, it['surface'])
        line = read(src).split(NL)[it['line'] - 1]
        found = it['text'][:60] in line
        if not found:
            MISSES.append((it['surface'], 'item %d quote at its line' % it['n'], it['text'][:40]))
        rec('    %d  %-30s quote found at its own line : %s'
            % (it['n'], '%s:%d' % (it['surface'], it['line']), found))
        eight.append(dict(n=it['n'], surface=it['surface'], line=it['line'], text=it['text'],
                          claim=it['claim'], terminal=it['terminal'], grade=it['grade'],
                          ref=it['ref'], kernel=it['kernel'], at_line=found))
    rec('  ### ### **ALL EIGHT QUOTATIONS VERIFIED AT THEIR OWN FILE AND LINE IN THE DEPOSITED COPY:')
    rec('  ### %s** -- so the erratum quotes the deposit, not a bank about it.'
        % all(e['at_line'] for e in eight))

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b469_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(deposited_md5_before=before, errata_entries=len(heads),
                   errata_last_line=heads[-1][0], work_258=n258, work_note=nlin,
                   r61_comment=n61, r61_heading=nhead, r61_trigger=ntrig,
                   r61_trigger_text=(ltrig or '').strip(), partition_row=nrow,
                   partition_row_text=(lrow or '').strip(),
                   b467_table_eight=n8, b467_table_sites=n6, eight=eight, misses=MISSES),
              io.open(os.path.join(D, 'b469_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
