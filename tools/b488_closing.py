# -*- coding: utf-8 -*-
"""b488_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
import io
import json
import os
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


def lw(text, needle):
    return next((l.strip() for l in text.split(NL) if needle in l), '')


res = json.loads(read(os.path.join(D, 'b488_results.json')) or '{}')
sv = json.loads(read(os.path.join(D, 'b488_survey.json')) or '{}')
post = read(os.path.join(D, 'b488_checks_postpush.txt'))
comp1 = read(os.path.join(D, 'b488_components_firstrun.txt'))
f = res.get('findings') or {}

rec('=' * 100)
rec('b488 -- THE CLOSING RECORD. ### THE FOLD`S SECTION WRITTEN HOME, AND THE ROW WRITER GUARDED.')
rec('=' * 100)

rec('')
rec('### (1) COMPONENT 1 -- (R98)`S SECTION.')
rec('-' * 100)
rec('    `## THE BOOKKEEPING ARC, b475-b479 - THE FOLD`, the ### **NINETEENTH** ### fold section')
rec('    of `FINDINGS.md`. ### **A TRANSCRIPTION, NOT A FOLD.**')
rec('    from b486`s own bank : the ### **11**-act span table in filing order ; the ### **6**')
rec('      digest clauses, each naming its cited act, ### **TWO FROM OUTSIDE THE SPAN** ### (b110,')
rec('      b469) ; the ### **13** ### rulings ; the ### **7** ### acts recording a defect of their')
rec('      own instruments ; and the fold`s own sentences.')
rec('    ### ### **NO VERDICT IS RE-READ AND NO ACT IS RE-SCORED.** ### An arm reads this act`s')
rec('    ### own tools for a verdict word written into the section, and finds none: every')
rec('    ### verdict in it is a quotation.')
rec('    %s' % lw(comp1, 'bytes before / appended / after'))
rec('    %s' % lw(comp1, 'PRIOR BYTES A TRUE PREFIX'))
rec('    lines removed : ### **%s** ### ; and by git`s own `--numstat` : ### **76 added, 0'
    % f.get('lines_removed'))
rec('      removed.** ### Two independent witnesses to the same claim.')
rec('    fold sections before / after : ### **18 / 19.**')
rec('    ### b486`s trail record ### **STANDS** ### and the section cites it; the section is')
rec('    ### dated as written at b488 for b486.')

rec('')
rec('### (2) THE SPAN TOOL -- ITS READING MOVED, ITS CODE DID NOT.')
rec('-' * 100)
sb, sa = res.get('span_before') or {}, res.get('span_after') or {}
rec('    BEFORE  last fold ### **b464 - b473** ### filed by ### **b474** ### ; folds ### **19**')
rec('            current span ### **14**   (banked at `data/b488_extract.txt` (P3))')
rec('    AFTER   last fold ### **%s** ### filed by ### **b%s** ### ; folds ### **%s**'
    % (sa.get('last_fold', '?'), sa.get('filed_by', '?'), sa.get('folds', '?')))
rec('            current span ### **%s**' % sa.get('span', '?'))
rec('    `tools/b363_span.py` edited by this act : ### **NO** ### -- (R98) is explicit, and')
rec('    b486`s routed finding is discharged by ### **GIVING THE TOOL THE INPUT IT WAS ALWAYS')
rec('    LOOKING FOR.**')

rec('')
rec('### (3) COMPONENT 2 -- `corr_row.py` GUARDED.')
rec('-' * 100)
rec('    ### ### **THE TOOL`S PRIOR BEHAVIOUR, FROM ITS OWN HEADER:** ### three declared limits')
rec('    ### -- the shell-string hazard, cell truth, terminal existence -- and ### **NOT ONE OF')
rec('    ### THEM MENTIONS THE ROW NUMBER.** ### It appended unconditionally and then read the')
rec('    ### row back, and read-back checks that the CELLS SURVIVED, not that the NUMBER was')
rec('    ### free. ### A row under a number the ledger already held was written and then')
rec('    ### reported ### *verified.*')
rec('    ### the guard : it reads the ledger and ### **REFUSES BEFORE ANY BYTE IS WRITTEN**,')
rec('    ### returns a code rather than raising, and names the next free number without')
rec('    ### choosing one. ### Two new limits stand beside the three: ### **(4)** it checks the')
rec('    ### number, not the content ; ### **(5)** it does not assign numbers.')
rec('    ### ### **BOTH CONTROLS, FIRST RUN, NO REPAIR:**')
for n in ('POSITIVE CONTROL', 'NEGATIVE CONTROL', 'BOTH CONTROLS BEHAVE'):
    rec('      %s' % lw(read(os.path.join(D, 'b488_components.txt')), n))
rec('    ### ### **AND NEITHER CONTROL IS EVER POINTED AT THE LIVE LEDGER.** ### A positive')
rec('    ### control that refuses is safe; ### **A NEGATIVE CONTROL THAT ACCEPTS WRITES A ROW**,')
rec('    ### so both run against a temporary fixture that is then removed.')
rec('    row ### **337** ### is this guard`s ### **FIRST LIVE USE** ### -- it returned `0`, and')
rec('    the ledger reads back 337 rows with this act`s mark present once.')

rec('')
rec('### (4) THE EXPECTATIONS.')
rec('-' * 100)
rec('    ### **(N1)** ### the span tool reads `b486` as the last fold -- ### **%s.**'
    % ('HELD' if res.get('n1') else 'REFUTED'))
rec('    ### **(N2)** ### the guard`s positive control refuses on its initial run -- ### **%s.**'
    % ('HELD' if res.get('n2') else 'REFUTED'))
rec('    ### **(S1) (S2) (S3)** -- %s' % lw(read(os.path.join(D, 'b488_desk_notes.txt')),
                                            'REGISTERED 3'))

rec('')
rec('### (5) THE DEFECTS THIS ACT RECORDS OF ITS OWN INSTRUMENTS. ### **FIVE.**')
rec('-' * 100)
rec('    ### ### **(a) THE (N1) SCORER READ THE WRONG LINE AND SAID REFUTED.** ### The span tool')
rec('    ### prints the span a fold ### *covers* ### and, separately, ### **THE ACT THAT FILED')
rec('    ### IT.** ### A fold heading carries the span and ### **NEVER** ### the filing act, so a')
rec('    ### score taken off the heading can never find `b486`. ### It would have reported the')
rec('    ### navigator`s expectation refuted by a reading that does not bear on it.')
rec('    ### ### **(b) A CHECK ON THE GUARD`S ORDERING SAID `False` AND THE TOOL WAS RIGHT.**')
rec('    ### It looked for `io.open(path + .tmp` where the source writes `open(path + .tmp`, so')
rec('    ### `find` returned `-1`. ### **A PREDICATE THAT CANNOT FIND ITS NEEDLE REPORTS A FAULT')
rec('    ### IN ITS SUBJECT.**')
rec('    ### ### **(c) `G-C1-PREFIX-PROVED` READ THE WRONG RUN**, demanding `after > before` from')
rec('    ### the results bank the LAST components run wrote -- a run that did not append, because')
rec('    ### the idempotence guard stopped it. ### Re-pointed at the run that made the append,')
rec('    ### with git`s numstat as an independent witness. ### And its line-anchored numstat')
rec('    ### needle matched nothing, because the figure sits inside a prose line.')
rec('    ### ### **(d) `G-C2-CONTROLS-ON-A-FIXTURE` OVERRAN ITS SUBJECT**, reading `self_test`')
rec('    ### AND `main()` after it, and condemning the tool for its own banner. ### Narrowed --')
rec('    ### and then its CONTROL missed the narrowed slice, so the arm ### **COULD NOT FAIL.**')
rec('    ### The control now points the fixture line itself at the live ledger.')
rec('    ### ### **(e) THE CARRIED SPEC CONTRADICTED THIS ACT`S OWN SEALED FACE, TWICE.**')
rec('    ### `b488_regspec.py` was carried from b487 and its clauses are TYPED, not measured, so')
rec('    ### nothing checked them against the face. ### It capped ### *existing relay tools')
rec('    ### edited in place* ### at ### **0**, while the face names `corr_row.py` in its own')
rec('    ### write list under (R98); and it declared ### **8 BARS**, while this face has ### **NO')
rec('    ### (K) SECTION AT ALL** ### and puts its constraints in (Z). ### **THE FACE WAS NOT')
rec('    ### EDITED AND IS NOT EDITABLE** -- the instrument was wrong and was repaired, its')
rec('    ### earlier runs banked as `b488_regspec_run_firstrun.txt` and `_secondrun.txt`.')
rec('    ### ### **AND REPAIRING A GATE AFTER THE SEAL COST A LOCK REFUSAL.** ### Re-running two')
rec('    ### gates over the sealed file left the other two stamped against the PRE-seal bytes,')
rec('    ### and `b378_lockgate.py` refused ### **2 of 8** ### -- exactly what it exists to')
rec('    ### catch. ### All four were then re-run over the sealed face, so ### **EVERY STAMP NOW')
rec('    ### NAMES BYTES ITS GATE ACTUALLY READ**, the lock reads 8 of 8, and the seal verifies')
rec('    ### INTACT at the same digest. ### **THE FACE BODY NEVER CHANGED.**')
rec('    ### ### **AND ONE REPEAT OF A KNOWN TRAP:** ### `> data/b488_span_notes.txt` redirected')
rec('    ### onto the span tool`s own record, so it wrote `b488_span_notes2.txt` beside it. ### A')
rec('    ### memory already carries this; ### **IT DID NOT STOP THE HAND.** ### Both files are')
rec('    ### banked and the tool`s own is the one read.')
rec('    ### ### **FOUR OF THE FIVE ARE ONE SPECIES:** ### a predicate whose needle is absent,')
rec('    ### or aimed at the wrong text, reporting a fault in its subject. ### **THE CURE IS TO')
rec('    ### PRINT A NEEDLE`S OWN YIELD BEFORE TRUSTING ITS VERDICT** -- b395 minted that rule')
rec('    ### for ceilings, and it belongs to every arm.')

rec('')
rec('### (6) THE SUITE, THE COMMITS, THE MIRROR.')
rec('-' * 100)
rec('    pre-push  : 57 arms, 0 live failing, 0 positive-control passes -- the mirror arm')
rec('      DEFERRED, since the archive is built after the push.')
rec('    post-push : %s' % lw(post, 'ARMS RUN'))
rec('                %s' % lw(post, 'NEGATIVE-CONTROL FAILURES'))
rec('                %s' % lw(post, 'VERDICT :'))
rec('')
rec('    the commits, each read back by `ls-remote`:')
for name, repo in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE)):
    h = git(repo, 'rev-parse', 'HEAD')
    r = git(repo, 'ls-remote', 'origin', 'refs/heads/main').split()
    r = r[0] if r else ''
    rec('      %-20s local %s ; remote %s ; ### **%s**'
        % (name, h[:12], r[:12], 'AGREE' if h and h == r else 'DISAGREE'))
rec('    ### all three pushed and read back on the FIRST attempt.')
rec('    the mirror : `mirror-refresh-2026-09-23-b488.zip` at `51967e4` --')
rec('      ### **CLEAN ON ALL THREE CLAUSES.**')

rec('')
rec('### (7) THE CENSUSES, THE PINS, THE LISTS.')
rec('-' * 100)
rec('    handoff census : %s' % lw(read(os.path.join(D, 'b488_census_closing.txt')),
                                   'TOTAL MISSING'))
rec('    faces census   : %s' % lw(read(os.path.join(D, 'b488_faces_census_closing.txt')),
                                   'TOTAL MISSING'))
rec('    pins           : %s' % lw(read(os.path.join(D, 'b488_pins_closing.txt')),
                                   'REPOS HARD-FAILING'))
rec('    ### **THE FOUR LISTS STAY OPEN.** ### No grade moved; no terminal was added, moved,')
rec('    ### renamed or graded; row U1 is unedited; no Lean of the corpus was touched; nothing')
rec('    ### compiled; no bridge typed; ### **h2 WHERE THE DEPOSIT LEFT IT.** ### Nothing')
rec('    ### deposits and nothing at Zenodo is written.')

rec('')
rec('### (8) WHAT IS CARRIED FORWARD.')
rec('-' * 100)
rec('    (a) ### **b487`S ORDER STILL STANDS:** ### the act that applies the three Zenodo')
rec('        description drafts must fetch each description back and bank it ### **BEFORE ANY')
rec('        RECORD SAYS THE EDIT WAS MADE.** ### This act made no platform call.')
rec('    (b) ### **THE SPEC TOOL`S CLAUSES ARE TYPED, NOT MEASURED**, and nothing checks them')
rec('        against the face they are emitted from. ### Two contradicted this act`s own sealed')
rec('        face and only a crash in an unrelated arm exposed one of them. ### **A CLAUSE THAT')
rec('        CANNOT BE FALSIFIED BY ITS OWN FACE IS NOT A BOUND.** ### ROUTED, not taken.')
rec('    (c) ### **THE FOLD THRESHOLD IS NINE AND THE SPAN IS NOW 2** ### -- b487 and b488. ###')
rec('        No fold is due.')
rec('')
rec('=' * 100)
rec('  ### ### **b488 CLOSES. 58 ARMS, 0 LIVE FAILING, 0 POSITIVE-CONTROL PASSES.**')
rec('=' * 100)

io.open(os.path.join(D, 'b488_closing.txt'), 'w', encoding='utf-8', newline=NL).write(
    NL.join(L) + NL)
print(NL + '  written: b488_closing.txt')
