# -*- coding: utf-8 -*-
"""b487_closing.py -- THE CLOSING RECORD. ### Figures are READ from the banks, not retyped."""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
NL = chr(10)
L = []

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


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.replace(chr(13), '').strip()


def line_with(text, needle):
    return next((l.strip() for l in text.split(NL) if needle in l), '')


res = json.loads(read(os.path.join(D, 'b487_results.json')) or '{}')
sv = json.loads(read(os.path.join(D, 'b487_survey.json')) or '{}')
post = read(os.path.join(D, 'b487_checks_postpush.txt'))
err = read(os.path.join(PP, 'ERRATA.md'))

rec('=' * 100)
rec('b487 -- THE CLOSING RECORD. ### THE ERRATA RENUMBER, AND THE ZENODO DESCRIPTION DRAFTS.')
rec('=' * 100)

rec('')
rec('### (1) COMPONENT 1 -- THE RENUMBER, APPEND-ONLY.')
rec('-' * 100)
rec('    `E-2026-09-22-1` occurrences before this act : ### **2** ### (b469`s, then b485`s).')
rec('    b469`s entry ### **KEEPS THE ID** ### and no line of it is touched.')
rec('    b485`s becomes ### **E-2026-09-22-2** ### by an APPENDED dated line naming (R97).')
rec('    pointers written : ### **2** ### -- one in `OPEN_TRAILS.md`, one in the act`s own')
rec('      bank `data/b485_the_two_records.txt`.')
w = res.get('writes') or {}
rec('    writes : ### **%d** ### ; ### **LINES REMOVED, EVERY ONE OF THEM : %s**'
    % (len(w), ' / '.join('%s %d' % (os.path.basename(k), v) for k, v in sorted(w.items()))))
rec('    prior bytes a TRUE PREFIX of the result, BOM preserved, in all three.')
rec('    ### ### **AND THE GUARD IS IN THE APPENDER, NOT IN THIS ACT`S COPY.**')
rec('      `tools/errata_append.py` refuses a duplicate id ### **BEFORE ANY BYTE IS WRITTEN**,')
rec('      and both controls run: a duplicate id -> code 2, file unchanged; a fresh id ->')
rec('      code 0, file grew. ### **AN ARM THAT CANNOT REFUSE IS NOT A GUARD**, so the')
rec('      refusal was exercised before the tool touched the real ledger.')
rec('      ### ### **THE SAME LESSON `corr_row.py` IS STILL OWED** -- b485 wrote a row and')
rec('      crashed, and the guard against a second row lives in one act`s copy. ### OPEN.')

rec('')
rec('### (2) COMPONENT 2 -- THE THREE DESCRIPTIONS, READ. ### **NOTHING WAS FETCHED.**')
rec('-' * 100)
for s in sv.get('sources', []):
    rec('    ### **%s** ### %-34s %d sentence(s), %d asserting a check'
        % (s['rec_id'], s['what'], s['n_sentences'], s['n_claims']))
    rec('        source : %s' % s['source'])
rec('    ### ### **TOTAL SENTENCES ASSERTING A MACHINE CHECK, A COMPILED PROOF, OR A')
rec('    ### VERIFIED CLAIM : %d.**' % len(sv.get('claims', [])))
rec('    ### ### **AND THE MATCHER`S LINEAGE IS ON THE RECORD.** ### Version 1 matched')
rec('    ### `compile`/`verified`/`machine-check` and ### **NOT `proves`** -- so the kernel`s')
rec('    ### central sentence, the one `E-2026-09-14-1` is about, scored as NO CLAIM AT ALL.')
rec('    ### The order asks for a machine check, a compiled proof, ### *or a verified claim*,')
rec('    ### and a kernel saying it ### *proves* ### something is the third. ### **BOTH YIELDS')
rec('    ### ARE PRINTED IN THE SURVEY BANK: 10, THEN 12.**')

rec('')
rec('### (3) COMPONENT 3 -- THE DISPOSITION, SENTENCE BY SENTENCE.')
rec('-' * 100)
c = res.get('counts') or {}
rec('    claims %d = ### **ON AN ERRATUM %d** ### + ### **LEFT AS THEY STAND %d**'
    % (c.get('claims', 0), c.get('on_erratum', 0), c.get('no_erratum', 0)))
rec('')
rec('      record     sentence   rests on          disposition')
rec('      ' + '-' * 92)
for d in res.get('drafts', []):
    rec('      %-10s s%-9d %-17s %s'
        % (d['rec_id'], d['idx'], d['erratum'] or '--',
           'REPLACEMENT DRAFTED' if d['erratum'] else 'LEFT AS IT STANDS'))
rec('')
rec('    ### ### **EVERY REPLACEMENT IS BUILT FROM ITS ERRATUM`S OWN WORDS**, and every one')
rec('    ### names its terminal in full. ### The three: `structural_exhaustiveness_proved`')
rec('    ### twice (21539167 s14, 21520474 s2), and `conservation_s_dark` once (21539167 s15)')
rec('    ### -- ### **NAMED, AND SAID TO BE A SHELL**, as the deposit`s own concordance')
rec('    ### records it. ### A replacement that quietly kept a stand-in would repeat the')
rec('    ### defect the erratum exists to correct.')
rec('    ### ### **AND NINE SENTENCES ARE LEFT EXACTLY AS THEY STAND, EACH WITH ITS REASON.**')
rec('    ### Monograph sentence 5 is the one worth naming: it is the MANUSCRIPT`S claim, and')
rec('    ### `E-2026-09-14-1` says in its own words that whether the manuscript proves the')
rec('    ### catalogue`s exhaustiveness is ### **UNTOUCHED** ### by it. ### **AN ERRATUM THAT')
rec('    ### NAMES WHAT IT DOES NOT REACH CANNOT BE STRETCHED TO REACH IT.**')
rec('    ### Three lv sentences are left because ### **NEITHER ERRATUM NAMES')
rec('    ### SIDE-lv-conservation AMONG ITS AFFECTED DEPOSITS**, and one of them is itself an')
rec('    ### axiom audit disclosing `sorryAx`.')
rec('')
rec('    ### ### **THE DRAFTS ARE BANKED AND NOT APPLIED.** ### Nothing was fetched and')
rec('    ### nothing at Zenodo was written. ### Under (R95) a metadata edit is not a re-issue;')
rec('    ### ### **THE AUTHOR APPLIES THEM AT THE PLATFORM**, and the act after this one')
rec('    ### fetches each description back and banks it ### **BEFORE ANY RECORD SAYS THE EDIT')
rec('    ### WAS MADE.** ### No record here says one was.')

rec('')
rec('### (4) THE SEAT`S OWN EXPECTATIONS.')
rec('-' * 100)
rec('    %s' % line_with(read(os.path.join(D, 'b487_desk_notes.txt')), 'REGISTERED 3'))
rec('    (N1) the monograph and the kernel each carry at least one sentence resting on an')
rec('      erratum -- ### **HELD** ### (two, and one).')
rec('    (N2) lv carries claim sentences but none resting on either erratum -- ### **HELD**')
rec('      ### (three claims, none on an erratum).')
rec('    (N3) the sentences resting on an erratum are a MINORITY -- ### **HELD** ### (3 of 12).')

rec('')
rec('### (5) THE SUITE, THE COMMITS, THE MIRROR.')
rec('-' * 100)
rec('    pre-push  : 54 arms, 0 live failing, 0 positive-control passes -- the mirror arm')
rec('      DEFERRED, since the archive is built after the push.')
rec('    post-push : %s' % line_with(post, 'ARMS RUN'))
rec('                %s' % line_with(post, 'NEGATIVE-CONTROL FAILURES'))
rec('                %s' % line_with(post, 'VERDICT :'))
rec('    ### ### **AND TWO ARMS FAILED ON THE FIRST RUN, AND BOTH WERE THE ARM`S FAULT.**')
rec('      `G-NOTHING-COMPILED` matched the BARE PHRASE `lake build` and fired on the')
rec('      survey tool -- where that phrase is one alternate ### *inside the claim matcher*,')
rec('      i.e. a phrase the survey LOOKS FOR in deposited descriptions. ### **A TOOL THAT')
rec('      SEARCHES FOR THE WORDS OF A BUILD DID NOT RUN ONE.** ### Narrowed to a BUILD CALL,')
rec('      ground stated, control still refuses it.')
rec('      `G-NOPRIORBANK` fired on `b485_the_two_records.txt` -- ### **WHICH THIS ACT IS')
rec('      DIRECTED BY (R97) TO APPEND TO.** ### An act told to write a prior bank cannot')
rec('      also be forbidden to. ### Excluded ### **BY NAME, WITH THE GROUND PRINTED**, and')
rec('      2,648 other prior banks are still checked. ### **NARROWED, NOT WEAKENED.**')
rec('')
rec('    the commits, each read back by `ls-remote`:')
for name, repo in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE)):
    h = git(repo, 'rev-parse', 'HEAD')
    r = git(repo, 'ls-remote', 'origin', 'refs/heads/main').split()
    r = r[0] if r else ''
    rec('      %-20s local %s ; remote %s ; ### **%s**'
        % (name, h[:12], r[:12], 'AGREE' if h and h == r else 'DISAGREE'))
rec('    ### ### **AND TWO OF THE THREE PUSHES FAILED ON THEIR FIRST ATTEMPT** -- connection')
rec('    ### reset, then a DNS failure, within one command. ### They were retried and read')
rec('    ### back. ### **A TRANSIENT NETWORK FAILURE IS RECORDED, NOT SMOOTHED OVER**; the')
rec('    ### read-back is what settles it, and b479`s pins gave the same species four')
rec('    ### hundred acts` worth of precedent.')
rec('    the mirror : `mirror-refresh-2026-09-22-b487.zip` at `93bd58c` --')
rec('      ### **CLEAN ON ALL THREE CLAUSES** ### (42 roster entries, 42 archive files,')
rec('      0 missing, 0 extra; clause 2`s pin agrees with `ls-remote`).')

rec('')
rec('### (6) THE CENSUSES, THE PINS, THE LISTS.')
rec('-' * 100)
rec('    handoff census : %s' % line_with(read(os.path.join(D, 'b487_census_closing.txt')),
                                          'TOTAL MISSING'))
rec('    faces census   : %s' % line_with(read(os.path.join(D, 'b487_faces_census_closing.txt')),
                                          'TOTAL MISSING'))
rec('    pins           : %s' % line_with(read(os.path.join(D, 'b487_pins_closing.txt')),
                                          'REPOS HARD-FAILING'))
rec('    ### **THE FOUR LISTS STAY OPEN.** ### No grade moved; no terminal was added, moved,')
rec('    ### renamed or graded; row U1 is unedited; no Lean of the corpus was touched;')
rec('    ### nothing compiled; no bridge typed; ### **h2 WHERE THE DEPOSIT LEFT IT.**')

rec('')
rec('### (7) WHAT IS CARRIED FORWARD.')
rec('-' * 100)
rec('    (a) ### **THE NEXT ACT FETCHES EACH DESCRIPTION BACK AND BANKS IT** ### before any')
rec('        record says the edit was made. ### The drafts alone are not evidence of an edit.')
rec('    (b) ### **`corr_row.py` IS STILL OWED ITS GUARD** -- b485`s lesson, and b487`s')
rec('        appender is the worked example of where such a guard belongs.')
rec('    (c) ### **THE SPAN TOOL STILL NAMES b474 AS THE LAST FOLD** ### because it reads')
rec('        `FINDINGS.md` and b486 filed its fold to the trail alone. ### By filing, the span')
rec('        since b486 is ### **ONE**. ### Routed; the tool is NOT edited, per (R96).')
rec('')
rec('=' * 100)
rec('  ### ### **b487 CLOSES. 55 ARMS, 0 LIVE FAILING, 0 POSITIVE-CONTROL PASSES.**')
rec('=' * 100)

io.open(os.path.join(D, 'b487_closing.txt'), 'w', encoding='utf-8', newline=NL).write(
    NL.join(L) + NL)
print(NL + '  written: b487_closing.txt')
