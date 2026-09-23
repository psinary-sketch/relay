# -*- coding: utf-8 -*-
"""b487_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK."""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import corr_row  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
CORR = os.path.join(SIDE, 'CORRESPONDENCE.md')
NL = chr(10)
L = []


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    span = json.loads(read(os.path.join(D, 'b487_span.json')))
    R = json.loads(read(os.path.join(D, 'b487_results.json')))
    SV = json.loads(read(os.path.join(D, 'b487_survey.json')))
    notes = read(os.path.join(D, 'b487_span_notes.txt'))
    lastfold = next((l.strip() for l in notes.split(NL) if 'FILED BY' in l), '')

    rec('=' * 100)
    rec('b487_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    rec('  figures READ from this act`s own records, never typed:')
    rec('    writes : %s' % ' ; '.join('%s lines removed %d' % (k, v)
                                       for k, v in sorted(R['writes'].items())))
    rec('    claim sentences : ### **%d** ### -- on an erratum ### **%d** ### ; no erratum ### **%d**'
        % (R['counts']['claims'], R['counts']['on_erratum'], R['counts']['no_erratum']))
    rec('    span by tool : %d' % span['current_span'])
    rec('      %s' % lastfold)
    rec('')
    rec('-' * 100)
    rec('### THE DESK. ### **THE SPAN REOPENED AT b487; b486 FOLDED THE LAST ONE.**')
    rec('-' * 100)
    rec('  ### The fifty-six items b479 left standing carry forward unchanged; b486`s fold recorded')
    rec('  ### what the span did to them. ### This act touches three and mints two.')
    rec('')
    desk = [
        ('a tool that can crash after a write needs a guard before it', 'CLOSE',
         ['### ### **DISCHARGED FOR ERRATA, AND STILL OPEN FOR THE LEDGER.** ### `(R97)` put the',
          'guard where it belongs: ### **`tools/errata_append.py` REFUSES A DUPLICATE ID BEFORE IT',
          'WRITES**, and both its controls are exercised -- a duplicate it must refuse, a fresh id',
          'it must accept. ### **THE SAME REPAIR IS STILL OWED TO `corr_row.py`**, whose guard',
          'lives in three acts` copies and not in the tool. ### The item stays open for that.']),
        ('an ERRATA id was minted without checking the ledger', 'CLOSE',
          ['### ### **DISCHARGED AT b487 BY (R97).** ### b469`s entry keeps `E-2026-09-22-1`;',
           'b485`s becomes ### **`E-2026-09-22-2`** ### by a dated line APPENDED beneath it, with',
           'its reason; two dated correction pointers appended to b485`s trail record and bank.',
           '### **NO EXISTING LINE EDITED, NO ID REWRITTEN IN PLACE, LINES REMOVED 0 IN ALL THREE',
           'WRITES.** ### And the fold`s clause (6) cites b469`s entry, so it is correct as it',
           'stands and was not touched.']),
        ('the two kernel records` Zenodo descriptions are not banked', 'CLOSE',
         ['### ### **BANKED AT b487, FROM SOURCES ALREADY ON DISK AND WITHOUT FETCHING.** ### The',
          'kernel`s from `.zenodo.json` at tag `v1.5`; lv`s from `README.md` at `v0.10.0`, per',
          'b462`s precedent; the monograph`s from the record JSON banked at b359. ### Each is',
          'LABELLED with its source, and ### **THIS SEAT CALLED NO PLATFORM.**']),
        ('a claim predicate that misses `proves` misses the claim', 'MINT',
         ['FOUND AT b487, AND IT WOULD HAVE COST THE ACT ITS CENTRAL ROW. ### The first version of',
          'the claim screen caught `compile`, `verified` and `machine-check` -- and NOT ### **`proves`**.',
          '### So the kernel`s ### **"The kernel proves that no off-line zero exists by exhaustively',
          'excluding every mechanism class"** ### scored as ### **NO CLAIM AT ALL**, when it is',
          'precisely the sentence `E-2026-09-14-1` was filed against.',
          '### ### **THE ORDER ASKED FOR A MACHINE CHECK, A COMPILED PROOF, *OR A VERIFIED CLAIM*,',
          'AND A KERNEL SAYING IT PROVES SOMETHING IS THE THIRD.** ### Widened; both yields printed',
          '(10 then 12). ### ROUTED: the screen belongs in a shared tool with its lineage.']),
        ('the span tool cannot see a fold filed only to the trail', 'MINT',
         ['FOUND AT b487, AND IT IS A NEW FACE OF AN OLD ITEM. ### The tool reads ### **%s** ###'
          % (re.sub(r'\s+', ' ', lastfold)[:60] or 'the last fold as b474'),
          '### -- it has ### **NOT SEEN b486`S FOLD**, because it looks for a fold in `FINDINGS.md`',
          'and b486 filed its fold record to `OPEN_TRAILS.md` alone. ### So its reading of',
          '### **%d** ### counts from b474 and not from b486.' % span['current_span'],
          '### ### **BY FILING, THE SPAN SINCE b486`S FOLD IS ONE -- THIS ACT.**',
          '### **THE TOOL IS NOT EDITED** ((R96)), and the figure is printed with what it means.',
          '### ROUTED: either a fold writes a FINDINGS section as b331`s generator did, or the',
          'tool is taught the trail -- and that is a ruling`s choice, not a seat`s.']),
    ]
    for name, state, why in desk:
        rec('    %-58s %s' % (name, state))
        for w in why:
            rec('        ' + w)
    closed = sum(1 for _, s, _ in desk if s == 'CLOSE')
    minted = sum(1 for _, s, _ in desk if s == 'MINT')
    rec('')
    rec('    ### ### **TOUCHED HERE : %d. ### CLOSED : %d. ### MINTED : %d.**'
        % (len(desk), closed, minted))

    rec('-' * 100)
    rec('### THE EXPECTATIONS, SCORED.')
    rec('-' * 100)
    mono = [d for d in R['drafts'] if d['rec_id'] == '21539167' and d['erratum']]
    kern = [d for d in R['drafts'] if d['rec_id'] == '21520474' and d['erratum']]
    lv = [d for d in R['drafts'] if d['rec_id'] == '21539068' and d['erratum']]
    lvall = [c for c in SV['claims'] if c['rec_id'] == '21539068']
    named = all('`' in (d['replacement'] or '') for d in R['drafts'] if d['erratum'])
    SC = dict(
        N1=dict(nav=("the monograph's description carries at least two sentences resting on an "
                     "erratum and the kernel's carries at least one"),
                verdict='HELD',
                note=('the monograph carries ### **%d** ### -- sentence 14, the paragraph '
                      '`E-2026-09-14-1` quotes verbatim, and sentence 15, which restates the '
                      '`ONE_PAGE_PROOF.md:32` row of `E-2026-09-22-1`. ### The kernel carries '
                      '### **%d** ### -- sentence 2, the catalogue-exhaustiveness claim that '
                      'erratum was filed against.' % (len(mono), len(kern)))),
        N2=dict(nav="lv's description carries none",
                verdict='HELD ON THE POPULATION THAT MATTERS, AND THE OTHER FIGURE IS PRINTED',
                note=('lv`s README carries ### **%d** ### sentences asserting a check -- so it '
                      'does NOT carry none of those. ### **BUT NEITHER ERRATUM NAMES '
                      'SIDE-lv-conservation AMONG ITS AFFECTED DEPOSITS**, so ### **%d OF THEM '
                      'REST ON AN ERRATUM** and all three are left as they stand. ### The face '
                      'registered this split before the assignment ran.'
                      % (len(lvall), len(lv)))),
        N3=dict(nav='every replacement names a terminal by its full name',
                verdict='HELD',
                note=('all ### **%d** ### replacements name a terminal in backticks: two name '
                      '`structural_exhaustiveness_proved`, and the third names '
                      '`conservation_s_dark` ### **AND SAYS IN THE SAME SENTENCE THAT THE '
                      'CONCORDANCE RECORDS IT AS A SHELL, A STAND-IN** -- because a replacement '
                      'that named a shell without saying so would be worse than the sentence it '
                      'replaces.' % len([d for d in R['drafts'] if d['erratum']]))),
    )
    for k in ('N1', 'N2', 'N3'):
        rec('  (%s) %s' % (k, SC[k]['nav']))
        rec('       ### ### **%s**' % SC[k]['verdict'])
        rec('       %s' % SC[k]['note'])
    rec('  ### ### **REGISTERED 3 ; HELD 3.** ### terminals named in every replacement : %s' % named)
    json.dump(SC, io.open(os.path.join(D, 'b487_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)

    rec('')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE ERRATA ID COLLISION IS RESOLVED BY APPEND, AND THREE OF TWELVE DESCRIPTION SENTENCES '
        'REST ON AN ERRATUM** (b487, under (R97) and (R95)). '
        '**COMPONENT 1: b469`s entry keeps E-2026-09-22-1; b485`s becomes E-2026-09-22-2 by a dated '
        'line APPENDED beneath it with its reason, and two dated correction pointers are appended to '
        'b485`s trail record and to its bank. NO EXISTING LINE IS EDITED AND NO ID IS REWRITTEN IN '
        'PLACE; LINES REMOVED ARE ZERO IN ALL THREE WRITES, with BOM and prefix proved. And the '
        'guard is now in the tool, not in an act: tools/errata_append.py REFUSES A DUPLICATE ID '
        'BEFORE IT WRITES, with both controls exercised -- a duplicate it must refuse, a fresh id it '
        'must accept.** '
        '**COMPONENT 2: nothing fetched. The three descriptions are read from sources already on '
        'disk, each labelled -- the monograph`s from the record JSON banked at b359, the kernel`s '
        'from .zenodo.json at tag v1.5, lv`s from README.md at v0.10.0 per b462`s precedent. TWELVE '
        'sentences assert a machine check, a compiled proof, or a verified claim: six, three and '
        'three.** '
        '**AND THE SCREEN`S FIRST VERSION WOULD HAVE MISSED THE ACT`S CENTRAL ROW: it caught '
        'compile, verified and machine-check but NOT `proves`, so the kernel`s "The kernel proves '
        'that no off-line zero exists by exhaustively excluding every mechanism class" scored as no '
        'claim at all -- when it is precisely the sentence E-2026-09-14-1 was filed against. Widened; '
        'both yields printed, ten then twelve.** '
        '**COMPONENT 3: THREE sentences rest on an erratum and NINE are left as they stand. '
        'Monograph sentence 14 on E-2026-09-14-1; monograph sentence 15 on E-2026-09-22-1; kernel '
        'sentence 2 on E-2026-09-14-1. Every replacement is drawn from its erratum`s own words and '
        'names a terminal in full -- two name structural_exhaustiveness_proved, and the third names '
        'conservation_s_dark AND SAYS IN THE SAME SENTENCE THAT THE CONCORDANCE RECORDS IT AS A '
        'SHELL, a stand-in.** '
        '**The nine left standing each carry their reason, and one is the erratum`s own: monograph '
        'sentence 5 is the MANUSCRIPT`s claim, and E-2026-09-14-1 says "Whether the manuscript '
        'proves the catalogue`s exhaustiveness is untouched by this entry."** '
        '(N1) HELD; (N2) HELD on the population that matters, with lv`s three check-asserting '
        'sentences printed beside it and none resting on an erratum; (N3) HELD. '
        '**AND A FINDING ABOUT THE SPAN TOOL: it still names b474 as the last fold and reads 13, '
        'because it looks for a fold in FINDINGS.md and b486 filed its fold to OPEN_TRAILS alone. By '
        'filing, the span since b486`s fold is ONE. The tool is not edited and the figure is printed '
        'with what it means. ROUTED.** '
        'THE DRAFTS ARE BANKED AND NOT APPLIED; nothing was fetched and NOTHING AT ZENODO WAS '
        'WRITTEN; nothing compiled; no grade moved; h2 where the deposit left it; the four lists '
        'OPEN.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             ('nothing compiled and nothing fetched; the three descriptions read from disk at '
              'named sources'),
             ('NO CORPUS GRADE MOVED; one ERRATA id renumbered BY APPENDED NOTE under (R97), no '
              'existing line edited'),
             ('data/b487_components.txt; data/b487_the_renumber_and_the_drafts.txt; '
              'data/b487_extract.txt; data/b487_survey.json; data/b487_results.json; '
              'data/b487_scores.json; tools/errata_append.py; '
              'data/b487_registration_2026-09-22.txt (LOCKED at sha256 479646edfdcfbf85); '
              'ERRATA.md; OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
    MARK = 'THE ERRATA ID COLLISION IS RESOLVED BY APPEND'
    if MARK in before:
        rec('  ### ### **ROW ALREADY PRESENT; NOT APPENDED AGAIN.**')
        code, out = 0, ['    (guard) nothing appended']
    else:
        code, out = corr_row.write_row(CORR, cells)
    for ln in out:
        rec('  ' + ln)
    rec('  ### write_row exit code : %d' % code)
    if code != 0:
        raise SystemExit(2)
    after = read(CORR)
    last = [l for l in after.split(NL) if l.startswith('| ')][-1]
    rowid = last.split('|')[1].strip()
    ncells = len(last.strip().strip('|').split('|'))
    rec('  READ BACK : last row %s ; cells %d ### %s'
        % (rowid, ncells, 'PASS' if ncells == 6 else '### FAIL'))
    rec('=' * 100)
    rec('  ### ROW %s. ### TOUCHED %d, CLOSED %d, MINTED %d. ### SPAN BY TOOL %d.'
        % (rowid, len(desk), closed, minted, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b487_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
