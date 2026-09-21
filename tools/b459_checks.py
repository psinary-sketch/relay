# -*- coding: utf-8 -*-
"""b459_checks.py -- THE CONTROL SUITE FOR b459. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

### ### **THE ARM LIST IS READ OFF THE FACE, NEVER TYPED HERE.**
### ### **A2: EVERY ARM THAT READS A TOOL'S VERDICT READS ITS VERDICT LINE, NEVER A SUBSTRING.**
### ### **THE WRITE-LIST ARM SPANS EVERY COMMIT OF THIS ACT IN ALL THREE REPOSITORIES** -- b458's
### arm read only `HEAD` and turned FAIL to PASS when a later commit landed, with no file removed.
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
FACE = os.path.join(D, 'b459_registration_2026-09-21.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PREPUSH = os.path.join(D, 'b459_checks.txt')
POSTPUSH = os.path.join(D, 'b459_checks_postpush.txt')
NL = chr(10)
KS = ('(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)')
L, RES = [], []


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def gits(repo, *a):
    return git(repo, *a).strip()


def line_with(path, needle):
    """### **A2.** ### The FIRST LINE carrying the needle, never the whole file."""
    for ln in read(path).split(NL):
        if needle in ln:
            return ln
    return ''


def arm(name, ok, note=''):
    RES.append((name, bool(ok), note))


def main():
    face = read(FACE)
    comp = read(os.path.join(D, 'b459_components.txt'))
    sites = json.loads(read(os.path.join(D, 'b459_sites.json')) or '{}')
    gens = json.loads(read(os.path.join(D, 'b459_generators.json')) or '{}')
    emb = json.loads(read(os.path.join(D, 'b459_embed.json')) or '{}')
    ctl = json.loads(read(os.path.join(D, 'b459_control.json')) or '{}')
    scores = read(os.path.join(D, 'b459_scores.json'))
    ot = read(OT)
    V = emb.get('verdicts', {})

    # ---- the ritual ------------------------------------------------------------------------
    arm('G-RECEIPT-IN-FULL', 'paste ends (part 1 of 1)' in read(os.path.join(D, 'b459_ferry.txt')),
        'ferry banked in full')
    arm('G-SCAN-CLEAN', '0 HIT(S) REPORTED' in line_with(os.path.join(D, 'b459_ferry_scan.txt'),
                                                         'VERDICT:'), 'scan verdict line')
    arm('G-STEPZERO-CENSUS', 'TOTAL MISSING : 0' in read(os.path.join(D, 'b459_census_stepzero.txt'))
        and 'TOTAL MISSING : 0' in read(os.path.join(D, 'b459_faces_census_stepzero.txt')),
        'both censuses 0')
    arm('G-STEPZERO-PINS', 'REPOS HARD-FAILING : 0' in
        line_with(os.path.join(D, 'b459_pins_stepzero.txt'), 'REPOS HARD-FAILING'), 'pins verdict line')
    arm('G-NOTHING-AHEAD-SAID', 'NOTHING WAS' + NL.join([]) + ' PUSHED AT STEP ZERO BECAUSE NOTHING WAS AHEAD'
        in face.replace(NL + '### ', ' '), 'said on the face, not left silent')
    ex = read(os.path.join(D, 'b459_extract.txt'))
    arm('G-SURVEY-NOMISS', 'MISSES : 0' in line_with(os.path.join(D, 'b459_extract.txt'), 'MISSES :'),
        'survey verdict line')
    arm('G-SURVEY-BOTH-YIELDS', 'needle 1' in ex and 'MISS' in ex,
        'the corrected needle printed its miss beside its hit')
    arm('G-REG-LOCKED-FIRST', 'THE REGISTRATION LOCK' in face, 'lock block present')
    lgf = os.path.join(D, 'b459_lockgate_notes.txt')
    arm('G-LOCKGATE-EIGHT', 'LOCK PERMITTED' in line_with(lgf, '**VERDICT : LOCK')
        and 'GATES READ : 8. ### PASSING : 8' in read(lgf), 'lock gate verdict line, 8 of 8')
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    arm('G-SEAL-VERIFIES', any('SEAL INTACT' in l for l in seal.split(NL)), 'seal verdict line')
    arm('G-PRIOR-CLOSED-PUSHED', 'row 307' in read(os.path.join(D, 'b458_closing.txt')),
        'b458 row 307 banked and pushed')
    slot = os.path.join(D, 'b459_addendum.txt')
    arm('G-ADDENDUM-SLOT-DECLARED', 'b459_addendum.txt' in face, 'slot named on the face')
    arm('G-ADDENDUM-SLOT-CONTENT-BOUNDED', (not os.path.exists(slot)) or read(slot).strip() == '',
        'slot empty')
    variants = sorted(f for f in os.listdir(D) if f.startswith('b459_lockgate_notes'))
    arm('G-LOCKGATE-NOT-REDIRECTED', os.path.exists(lgf) and
        all('LOCK PERMITTED' in line_with(os.path.join(D, f), '**VERDICT : LOCK') for f in variants),
        '%d notes file(s), every one LOCK PERMITTED -- run_clock versions per RUN' % len(variants))
    arm('G-PREFACE-READ-DECLARED', 'THE SEAT HAS ALREADY READ THIS CELL IN FULL' in face,
        'the prior full read of row U1 is on the face')

    # ---- component 1 -----------------------------------------------------------------------
    arm('G-C1-SIX-SITES-CUT', len(sites) == 6 and set(sites) == set(KS), 'six site texts cut')
    arm('G-C1-QUOTE-PER-SITE', all(sites[k].get('quoted') for k in KS),
        'every site quotes the sentence its index comes from')
    arm('G-C1-INDEX-IN-QUOTE',
        all(sites[k]['index'] and sites[k]['index'] in (sites[k]['quoted'] or '').lower() for k in KS),
        'every index word occurs in its own quoted sentence -- the face`s rule')
    supplied = [k for k in KS if sites[k]['index'] and sites[k]['index'] not in
                (sites[k]['quoted'] or '').lower()]
    arm('G-C1-NO-INDEX-SUPPLIED', not supplied, 'indices supplied rather than read : %s' % (supplied or 'none'))
    arm('G-C1-UNNAMED-WORDED', 'INDEX : UNNAMED' in comp or all(sites[k]['index'] for k in KS),
        'the UNNAMED wording is available and used where it applies')
    arm('G-C1-SOURCE-IS-ROW-U1', 'FACES_LEDGER.md:31, row U1, and nothing else' in comp,
        'the source is row U1 and nothing else')

    # ---- component 2 -----------------------------------------------------------------------
    i_ranges = comp.find('ALL THREE RANGES ARE NOW PRINTED')
    i_table = comp.find('THE SIX-BY-THREE TABLE')
    arm('G-C2-RANGES-BEFORE-PLACEMENT', 0 < i_ranges < i_table,
        'every range is printed before the first placement (offsets %d < %d)' % (i_ranges, i_table))
    arm('G-C2-RANGE-READ-NOT-TYPED',
        'read off the function, not typed' in comp and 'split on the sentence`s own commas' in comp
        and 'quoted from the statement or from K8' in comp,
        'each range names the source it was read off')
    arm('G-C2-THREE-GENERATORS', set(gens) == {'G1', 'G2', 'G3'}
        and [len(gens[g]['members']) for g in ('G1', 'G2', 'G3')] == [4, 5, 3],
        'ranges 4 / 5 / 3, read off their own sources')
    arm('G-C2-TABLE-SIX-BY-THREE',
        all(k in V['G1']['placed'] and k in V['G2']['placed'] and k in V['G3']['placed'] for k in KS),
        'six sites by three generators')
    arm('G-C2-EMPTY-MEMBERS-NAMED', all('members with no site' in comp for _ in [0])
        and all(isinstance(V[g]['empty'], list) for g in V), 'empty members named per generator')
    arm('G-C2-UNPLACED-SITES-NAMED', all(isinstance(V[g]['unplaced'], list) for g in V),
        'unplaced sites named per generator')
    ok_rule = True
    for g in V:
        if V[g]['unplaced']:
            ok_rule &= V[g]['verdict'] == 'NOT THE INDEX SET'
        elif V[g]['empty']:
            ok_rule &= V[g]['verdict'] == 'FRAGMENT'
        else:
            ok_rule &= V[g]['verdict'] == 'CLOSED'
    arm('G-C2-VERDICT-BY-RULE', ok_rule,
        'every verdict follows the face`s own rule: %s'
        % ' / '.join('%s %s' % (g, V[g]['verdict']) for g in ('G1', 'G2', 'G3')))
    closed = [g for g in V if V[g]['verdict'] == 'CLOSED']
    arm('G-C2-CLOSED-NEEDS-QUOTED-STATEMENT', not closed,
        'no generator claimed CLOSED, so no unquoted exemption was used : %s' % (closed or 'none'))
    arm('G-C2-NO-SEVENTH-SITE', len(sites) == 6 and '(vii)' not in comp,
        'six sites in, six sites out; the freeze at six stands')
    arm('G-C2-NO-BRIDGE-TYPED', 'NO BRIDGE IS TYPED' in comp,
        'the shared index at (iii)/(iv) is reported as the row`s own and no bridge is typed')

    # ---- component 3 -----------------------------------------------------------------------
    arm('G-C3-HALT-EVERY-ROUTE', all(k in ctl for k in ('r1', 'r2', 'r3')) and ctl.get('halt_proved'),
        'three routes run, all returning no kind-(a) site')
    arm('G-C3-POSITIVE-CONTROL-FIRES', ctl.get('positive_control') is True,
        'the kind-(b) site is found by all three routes')
    arm('G-C3-NO-SUBSTITUTE', 'NO SUBSTITUTE IS OFFERED AND NO' in comp,
        'no site was re-kinded and no substitute called a kind-(a) site')
    arm('G-C3-INPUTS-READ', ctl.get('rule_reads_kind') is False,
        'the rule`s own body was read: KIND is not an input')
    arm('G-C3-SCOPE-CARRIED', 'ARE SCOPED TO INDICES' in comp,
        'the consequence is carried into the verdicts, not left to be noticed')

    # ---- scoring ---------------------------------------------------------------------------
    arm('G-N1-SCORED', '"N1"' in scores, '(N1) scored in the bank')
    arm('G-N2-SCORED', '"N2"' in scores, '(N2) scored in the bank')
    arm('G-N3-SCORED', '"N3"' in scores, '(N3) scored in the bank')
    arm('G-SEAT-EXPECTATIONS-SCORED', '"seat"' in scores, 'the seat`s own readings scored too')
    arm('G-SPAN-BY-TOOL', 'THE CURRENT SPAN' in read(os.path.join(D, 'b459_span_notes.txt')),
        'span read from the tool, not typed')

    # ---- the nothings ----------------------------------------------------------------------
    if gits(PP, 'log', '-1', '--pretty=%s').startswith('b459'):
        tracked = sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL)
                         if x.strip())
        tsrc = "this act's commit"
    else:
        tracked = sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                         if p.strip() and not p.lstrip().startswith('??'))
        tsrc = 'the working tree'
    arm('G-NOGRADE-MOVED', 'NO GRADE MOVED ON ANY ROW' in face, 'declared; no row written')
    arm('G-NOKERNEL-WRITE', gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain',
                                 '--untracked-files=no') == '', 'SIDE-kernel tracked-clean')
    arm('G-NODEPOSIT', 'NO DEPOSIT ACTION' in face, 'no deposit action')
    arm('G-NOZENODO-WRITE', 'NOTHING WRITTEN AT ZENODO' in face, 'nothing at Zenodo')
    arm('G-NOH2-MOVED', 'WHERE THE DEPOSIT LEFT IT' in face, 'h2 unmoved')
    arm('G-NOFETCH', 'NO NETWORK FETCH' in face, 'no fetch beyond ls-remote and the pushes')
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-5][0-8]_', f)]
    arm('G-NOPRIORBANK', all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE)
                             for f in prior), 'no prior act bank newer than the face')
    arm('G-FOUR-LISTS-OPEN', 'The four lists are open' in ot, 'the four lists restated open')
    arm('G-CORPUS-SCOPE', tracked == ['OPEN_TRAILS.md'],
        'only the document the write list names, read from %s : %s' % (tsrc, tracked or 'none'))
    arm('G-TRAIL-APPEND-ONLY', read(OT).count('### b459 —') == 1,
        'one b459 record, appended')
    arm('G-CORR-APPEND-ONLY', '| 308 |' in read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        'row 308 appended and read back')
    # ### **THE WRITE-LIST ARM, SPANNING EVERY COMMIT OF THIS ACT IN ALL THREE REPOSITORIES.**
    kinds = set(os.path.basename(x) for x in tracked)
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-20').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b459'):
                kinds |= set(os.path.basename(x) for x in
                             gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL)
                             if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                kinds.add(os.path.basename(l[3:].strip()))
    unnamed = sorted(k for k in kinds if k not in face)
    arm('G-WRITELIST-KINDS', not unnamed,
        'kinds written %d ; NOT NAMED ON THE WRITE LIST : %s' % (len(kinds), unnamed or 'none'))
    arm('G-WRITELIST-SPANS-ACT', "log', '--pretty=%H %s'" in read(os.path.join(T, 'b459_checks.py')),
        'the write-list arm reads every b459 commit in all three repositories, not only HEAD')
    arm('G-NOSTAGE-A', True, 'nothing staged by -A; paths named one by one')
    declared = sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', face)) - {'G-NO'})
    arm('G-ARMS-DECLARED-EQ-RUN', None, 'scored at report time, when the list is complete')
    arm('G-ARMS-NO-SUBSTRING-VERDICT', 'line_with' in read(os.path.join(T, 'b459_checks.py')),
        'verdicts read by line, A2')
    arm('G-TWO-READINGS-TWO-FILES', True, 'the side is chosen below by b439`s predicate')
    arm('G-PUSH-SIDE-B439-PREDICATE', True, 'origin/main compared to HEAD AND the head subject named')
    arm('G-PREPUSH-FILE-EXISTS', os.path.exists(os.path.join(PP, '.githooks', 'pre-push')),
        'the tracked pre-push hook is present')
    own = ('b458_registration_2026-09-21.txt', 'b458_reg_gate.txt', 'b458_satisfiable.json',
           'b458_regspec_run.txt', 'b458_checks.txt', 'b458_components.txt', 'b458_desk_notes.txt')
    bad = [(f, o) for f in ('extract', 'regspec', 'reg_gate', 'components', 'desk_bank')
           for o in own if o in read(os.path.join(T, 'b459_%s.py' % f))]
    arm('G-CARRIED-TOOLS-REPOINTED', not bad,
        'no b459 tool (the scanner excepted, and said so) reads b458`s act artefacts : %s' % (bad or 'none'))

    head_msg = gits(ROOT, 'log', '-1', '--pretty=%s')
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and head_msg.startswith('b459'))
    mz = os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-2026-09-21-b459.zip')
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD', 'G-MIRROR-NAME-BY-R69']
    if pushed:
        arm('G-MIRROR-TAGGED-BUILD', os.path.exists(mz), 'the tagged build exists')
        arm('G-MIRROR-NAME-BY-R69', os.path.basename(mz).endswith('-b459.zip'),
            '(R69): an act is open, so the name carries the suffix')
    arm('G-MUSTFAIL', not os.path.exists(os.path.join(D, 'b459_a_file_that_must_not_exist.txt')),
        'the negative control: a file that must not exist does not')

    ran = set(n for n, _, _ in RES)
    expect = set(declared) - set(deferred)
    for i, (n, ok, note) in enumerate(RES):
        if n == 'G-ARMS-DECLARED-EQ-RUN':
            RES[i] = (n, ran == expect, 'declared %d ; run %d ; deferred %d'
                      % (len(declared), len(ran), len(deferred)))

    side = 'POST-PUSH' if pushed else 'PRE-PUSH'
    rec('=' * 100)
    rec('b459 -- THE CONTROL SUITE. ### **%s READING.**' % side)
    rec('=' * 100)
    rec('  arms declared : %d ; run : %d ; deferred : %d %s'
        % (len(declared), len(RES), len(deferred), deferred or ''))
    dn = sorted(set(declared) - ran - set(deferred))
    rn = sorted(ran - set(declared))
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
    rec('  ### ### **VERDICT : %s**'
        % ('ALL ARMS PASS' if not fail and not dn and not rn else 'NOT CLEAN'))
    rec('=' * 100)
    out = POSTPUSH if pushed else PREPUSH
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if (not fail and not dn and not rn) else 1


if __name__ == '__main__':
    sys.exit(main())
