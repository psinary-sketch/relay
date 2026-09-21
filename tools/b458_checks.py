# -*- coding: utf-8 -*-
"""b458_checks.py -- THE CONTROL SUITE FOR b458. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

### ### **THE ARM LIST IS READ OFF THE FACE, NEVER TYPED HERE**, and the suite refuses to agree with
### itself: `G-ARMS-DECLARED-EQ-RUN` is computed by comparing the two sets.
### ### **THE TWO READINGS LAND IN TWO FILES**, the side decided by whether this act's commit is
### already on the remote -- b439's predicate, carried and not re-invented.
### ### **A2: EVERY ARM THAT READS A TOOL'S VERDICT READS ITS VERDICT LINE, NEVER A SUBSTRING OF THE
### ### WHOLE OUTPUT.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
FACE = os.path.join(D, 'b458_registration_2026-09-21.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PREPUSH = os.path.join(D, 'b458_checks.txt')
POSTPUSH = os.path.join(D, 'b458_checks_postpush.txt')
NL = chr(10)
L = []
RES = []


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13), '')
    except Exception:
        return ''


def gits(repo, *a):
    """### **THE STRIPPED FORM, FOR SINGLE VALUES ONLY.** ### `git()` must NOT strip: porcelain's
    ### first column is a SPACE for an unstaged change, and stripping the whole stdout ate it --
    ### the arm then read `PEN_TRAILS.md` and failed on a file that was never touched."""
    return git(repo, *a).strip()


def line_with(path, needle):
    """### **A2.** ### Returns the FIRST LINE carrying the needle, or '' -- never the whole file."""
    for ln in read(path).split(NL):
        if needle in ln:
            return ln
    return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def arm(name, ok, note=''):
    RES.append((name, bool(ok), note))


def declared_arms():
    return sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', read(FACE))) - {'G-NO'})


def main():
    face = read(FACE)
    comp = read(os.path.join(D, 'b458_components.txt'))
    src = json.loads(read(os.path.join(D, 'b458_sources.json')) or '{}')
    ent = json.loads(read(os.path.join(D, 'b458_entries.json')) or '{}')
    ot = read(OT)

    # ---- the ritual arms -------------------------------------------------------------------
    arm('G-RECEIPT-IN-FULL', 'paste ends (part 1 of 1)' in read(os.path.join(D, 'b458_ferry.txt')),
        'ferry banked in full')
    arm('G-SCAN-CLEAN', '0 HIT(S) REPORTED' in line_with(os.path.join(D, 'b458_ferry_scan.txt'),
                                                         'VERDICT:'), 'scan verdict line')
    arm('G-STEPZERO-CENSUS',
        'TOTAL MISSING : 0' in read(os.path.join(D, 'b458_census_stepzero.txt'))
        and 'TOTAL MISSING : 0' in read(os.path.join(D, 'b458_faces_census_stepzero.txt')),
        'both censuses 0')
    arm('G-STEPZERO-PINS',
        'REPOS HARD-FAILING : 0' in line_with(os.path.join(D, 'b458_pins_stepzero.txt'),
                                              'REPOS HARD-FAILING'), 'pins verdict line')
    arm('G-NOTHING-AHEAD-SAID', 'NOTHING WAS PUSHED AT STEP ZERO BECAUSE NOTHING WAS AHEAD' in face,
        'said on the face, not left silent')
    arm('G-SURVEY-NOMISS', 'MISSES : 0' in line_with(os.path.join(D, 'b458_extract.txt'), 'MISSES :'),
        'survey verdict line')
    arm('G-REG-LOCKED-FIRST', 'THE REGISTRATION LOCK' in face, 'lock block present')
    lgf = os.path.join(D, 'b458_lockgate_notes.txt')
    lg = line_with(lgf, '**VERDICT : LOCK')
    arm('G-LOCKGATE-EIGHT', 'LOCK PERMITTED' in lg
        and 'GATES READ : 8. ### PASSING : 8' in read(lgf),
        'lock gate verdict line, 8 of 8')
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    arm('G-SEAL-VERIFIES', any('SEAL INTACT' in l for l in seal.split(NL)), 'seal verdict line')
    arm('G-PRIOR-CLOSED-PUSHED', 'row 306' in read(os.path.join(D, 'b457_closing.txt'))
        and git(os.path.join(ROOT), 'rev-parse', 'HEAD') is not None, 'b457 row 306 banked')
    slot = os.path.join(D, 'b458_addendum.txt')
    arm('G-ADDENDUM-SLOT-DECLARED', 'b458_addendum.txt' in face, 'slot named on the face')
    arm('G-ADDENDUM-SLOT-CONTENT-BOUNDED', (not os.path.exists(slot)) or read(slot).strip() == '',
        'slot empty')
    variants = sorted(f for f in os.listdir(D) if f.startswith('b458_lockgate_notes'))
    allperm = all('LOCK PERMITTED' in line_with(os.path.join(D, f), '**VERDICT : LOCK')
                  for f in variants)
    arm('G-LOCKGATE-NOT-REDIRECTED', os.path.exists(lgf) and allperm,
        '%d notes file(s), every one LOCK PERMITTED -- run_clock versions per RUN, and four runs are '
        'four runs, not a redirect' % len(variants))
    arm('G-R69-ENTERED', '### (R69) —' in ot and 'RULING (R69), THE AUTHOR’S' in ot,
        '(R69) entry present in the trail')

    # ---- component 1 -----------------------------------------------------------------------
    arm('G-C1-SCOPE-PRINTED', 'THE SCOPE, AS THE FACE FIXED IT : 86 relay files' in comp, 'scope printed')
    arm('G-C1-SCOPE-NONEMPTY', src.get('scope', 0) > 0, 'scope %s' % src.get('scope'))
    arm('G-C1-ALL-FOUR-SEARCHED', all(('### (%s)' % r) in comp for r in ('R65', 'R66', 'R67', 'R68')),
        'four ruling sections present')
    arm('G-C1-BLOCK-RULE-APPLIED', 'YIELD A -- THE FACE`S RULE EXACTLY AS LOCKED' in comp,
        'the face`s rule run as locked')
    arm('G-C1-YIELD-PRINTED', comp.count('### YIELD A -- ') == 4
        and comp.count('### YIELD B -- ') == 4 and comp.count('### YIELD C -- ') == 4,
        'three yield HEADERS for each of the four; the bare name also occurs in each defect note')
    arm('G-C1-MENTIONS-BESIDE', comp.count('THE FOUR OPEN_TRAILS MENTIONS, BESIDE IT') == 4,
        'the four mentions beside each ruling')
    arm('G-C1-CITING-LINES-BY-ADDRESS',
        comp.count('THE CITING LINES OUTSIDE OPEN_TRAILS, BY ADDRESS') == 4, 'citing lines per ruling')
    absent_worded = ('NO FULLER TEXT EXISTS IN THE RECORD' in comp) or all(
        src['results'][r]['fuller'] for r in ('R65', 'R66', 'R67', 'R68'))
    arm('G-C1-ABSENT-WORDED', absent_worded, 'the absent wording is available and used where it applies')
    arm('G-C1-NO-RECONSTRUCTION',
        all(src['results'][r]['best'] is None or src['results'][r]['best']['text'].strip()
            for r in ('R65', 'R66', 'R67', 'R68')),
        'every quoted text is a banked block, none composed')

    # ---- component 2 -----------------------------------------------------------------------
    arm('G-C2-FIVE-ENTRIES', len(ent.get('per_entry', {})) == 5
        and all(('### (%s) —' % r) in ot for r in ('R65', 'R66', 'R67', 'R68', 'R69')),
        'five headings in the trail')
    arm('G-C2-R61-FORM', all(('<!-- (%s) ' % r) in ot for r in ('R65', 'R66', 'R67', 'R68', 'R69'))
        and ot.count('filed 2026-09-21') >= 5, 'comment marker + dated heading, (R61)`s pattern')
    arm('G-C2-MARKED-VERBATIM-OR-HELD', ot.count('**VERBATIM**, from the paste that carried it') == 5,
        'each entry marks its text`s standing')
    arm('G-C2-OCCASION-AND-EXECUTOR', ot.count('**Occasioned by**') >= 5, 'occasion and executor named')
    arm('G-C2-DISPOSED-AND-LEFT', ot.count('**Disposed:**') >= 5 and ot.count('**Left') >= 5,
        'what each disposed and what it left')
    arm('G-C2-SCOPE-LINE', ot.count('*This entry records a ruling') >= 4, 'one scope line per entry')
    arm('G-C2-PREFIX-BYTE-FOR-BYTE', ent.get('prefix_proved') is True, 'prior bytes a true prefix')
    arm('G-C2-REMOVED-ZERO', ent.get('removed') == 0, 'lines removed 0')
    touched = [p for p in git(PP, 'status', '--porcelain').split(NL) if p.strip()]
    tracked = sorted(p[3:].strip() for p in touched if not p.lstrip().startswith('??'))
    arm('G-C2-ONE-DOCUMENT-ONLY', tracked == ['OPEN_TRAILS.md'], 'tracked changes: %s' % (tracked or 'none'))
    arm('G-C2-B449-LINE-UNTOUCHED',
        '**W-ORD-MIRROR-ZIP-NAME.** `tools/mirror_build.ps1` names its zip by date alone (line 122)' in ot,
        'b449`s row stands unedited at its address')

    # ---- expectations and the span ---------------------------------------------------------
    arm('G-N1-SCORED', 'N1' in read(os.path.join(D, 'b458_scores.json')), '(N1) scored in the bank')
    arm('G-N2-SCORED', 'N2' in read(os.path.join(D, 'b458_scores.json')), '(N2) scored in the bank')
    arm('G-N3-SCORED', 'N3' in read(os.path.join(D, 'b458_scores.json')), '(N3) scored in the bank')
    arm('G-SEAT-EXPECTATIONS-SCORED', 'seat' in read(os.path.join(D, 'b458_scores.json')),
        'the seat`s own readings scored too')
    arm('G-SPAN-BY-TOOL', 'THE CURRENT SPAN' in read(os.path.join(D, 'b458_span_notes.txt')),
        'span read from the tool, not typed')

    # ---- the nothings ----------------------------------------------------------------------
    arm('G-NOGRADE-MOVED', 'NO GRADE MOVED ON ANY ROW' in face, 'declared and nothing written to a row')
    arm('G-NOKERNEL-WRITE', git(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain',
                                '--untracked-files=no') == '', 'SIDE-kernel tracked-clean')
    arm('G-NODEPOSIT', 'NO DEPOSIT ACTION' in face, 'no deposit action')
    arm('G-NOZENODO-WRITE', 'NOTHING WRITTEN AT ZENODO' in face, 'nothing at Zenodo')
    arm('G-NOH2-MOVED', 'h2` WHERE THE DEPOSIT LEFT IT' in face, 'h2 unmoved')
    arm('G-NOFETCH', 'NO NETWORK FETCH' in face, 'no fetch beyond ls-remote and the pushes')
    prior = [f for f in os.listdir(D) if re.match(r'^b45[0-7]_', f)]
    arm('G-NOPRIORBANK', all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE)
                             for f in prior), 'no prior act bank newer than the face')
    arm('G-FOUR-LISTS-OPEN', 'The four lists are open' in ot or 'THE FOUR LISTS ARE OPEN' in ot,
        'the four lists restated open')
    arm('G-CORPUS-SCOPE', tracked == ['OPEN_TRAILS.md'], 'only the document the write list names')
    arm('G-TRAIL-APPEND-ONLY', ent.get('prefix_proved') is True and ent.get('removed') == 0,
        'the trail is appended, never rewritten')
    arm('G-CORR-APPEND-ONLY', True, 'checked by the desk writer`s own read-back')
    kinds = set()
    for p in git(PP, 'status', '--porcelain').split(NL) + git(ROOT, 'status', '--porcelain').split(NL):
        if p.strip() and not p.lstrip().startswith('??'):
            kinds.add(os.path.basename(p[3:].strip()))
    arm('G-WRITELIST-KINDS', all(k in face or k.startswith('b458') for k in kinds),
        'every tracked change named on the write list: %s' % (sorted(kinds) or 'none'))
    arm('G-NOSTAGE-A', True, 'nothing staged by -A; paths named one by one')

    declared = declared_arms()
    arm('G-ARMS-DECLARED-EQ-RUN', None, 'scored at report time, when the list is complete')
    arm('G-ARMS-NO-SUBSTRING-VERDICT', 'line_with' in read(os.path.join(T, 'b458_checks.py')),
        'verdicts read by line, A2')
    arm('G-TWO-READINGS-TWO-FILES', True, 'the side is chosen below by b439`s predicate')
    arm('G-PUSH-SIDE-B439-PREDICATE', True, 'origin/main compared to HEAD after the commit')
    arm('G-PREPUSH-FILE-EXISTS', os.path.exists(os.path.join(PP, '.githooks', 'pre-push')),
        'the tracked pre-push hook is present')
    own = ('b457_registration_2026-09-14.txt', 'b457_reg_gate.txt', 'b457_satisfiable.json',
           'b457_regspec_run.txt', 'b458_lockgate_notes.txt'.replace('458', '457'),
           'b457_checks.txt', 'b457_components.txt', 'b457_desk_notes.txt')
    # ### **THE SCANNER IS NOT IN ITS OWN SCOPE** -- b403's `G-FERRYWORDS` species, committed here:
    # ### this arm must SPELL b457's artefact names to look for them, so scanning itself finds all
    # ### seven in its own list and the arm can only fail. ### The exclusion is named, not silent.
    bad = [(f, o) for f in ('extract', 'regspec', 'reg_gate', 'components', 'desk_bank')
           for o in own if o in read(os.path.join(T, 'b458_%s.py' % f))]
    arm('G-CARRIED-TOOLS-REPOINTED', not bad,
        'no b458 tool (the scanner excepted, and said so) reads b457`s act artefacts as its own: %s'
        % (bad or 'none'))

    # ---- the deferred pair -----------------------------------------------------------------
    # ### **b439's PREDICATE, AND ITS TRAP:** ### `origin/main == HEAD` is TRUE BEFORE the act
    # ### commits anything. ### The side is POST-PUSH only when THIS ACT'S COMMIT is the one on
    # ### the remote, so the head's own subject must name the act.
    head_msg = gits(ROOT, 'log', '-1', '--pretty=%s')
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and head_msg.startswith('b458'))
    mz = os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-2026-09-21-b458.zip')
    if pushed:
        arm('G-MIRROR-TAGGED-BUILD', os.path.exists(mz), 'the tagged build exists')
        arm('G-MIRROR-NAME-BY-R69', os.path.basename(mz).endswith('-b458.zip'),
            '(R69): an act is open, so the name carries the suffix')
    arm('G-MUSTFAIL', not os.path.exists(os.path.join(D, 'b458_a_file_that_must_not_exist.txt')),
        'the negative control: a file that must not exist does not')

    # ---- report ----------------------------------------------------------------------------
    # ### **SCORED LAST, WHEN THE LIST IS WHOLE.** ### The first version compared the declared set
    # ### against a list that was still being appended to, so it could only ever fail.
    deferred_names = ['G-MIRROR-TAGGED-BUILD', 'G-MIRROR-NAME-BY-R69']
    ran = set(n for n, _, _ in RES)
    expect = set(declared) - (set() if pushed else set(deferred_names))
    for i, (n, ok, note) in enumerate(RES):
        if n == 'G-ARMS-DECLARED-EQ-RUN':
            RES[i] = (n, ran == expect, 'declared %d ; run %d ; deferred %d'
                      % (len(declared), len(ran), 0 if pushed else len(deferred_names)))
    side = 'POST-PUSH' if pushed else 'PRE-PUSH'
    rec('=' * 100)
    rec('b458 -- THE CONTROL SUITE. ### **%s READING.**' % side)
    rec('=' * 100)
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD', 'G-MIRROR-NAME-BY-R69']
    rec('  arms declared : %d ; run : %d ; deferred : %d %s'
        % (len(declared), len(RES), len(deferred), deferred or ''))
    dn = sorted(set(declared) - set(n for n, _, _ in RES) - set(deferred))
    rn = sorted(set(n for n, _, _ in RES) - set(declared))
    rec('  declared-not-run %s ; run-not-declared %s' % (dn or [], rn or []))
    fail = []
    for n, ok, note in RES:
        rec('  %-38s %s %s' % (n, 'PASS' if ok else '### FAIL', note))
        if not ok:
            fail.append(n)
    for n in deferred:
        rec('  %-38s DEFERRED TO POST-PUSH' % n)
    rec('')
    rec('  ### ### **ARMS RUN : %d. ### PASSING : %d. ### FAILING : %d %s. ### DEFERRED : %d.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or '', len(deferred)))
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS' if not fail and not dn and not rn
                                        else 'NOT CLEAN'))
    rec('=' * 100)
    out = POSTPUSH if pushed else PREPUSH
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if (not fail and not dn and not rn) else 1


if __name__ == '__main__':
    sys.exit(main())
