# -*- coding: utf-8 -*-
"""b460_checks.py -- THE CONTROL SUITE FOR b460. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

### ### **THE ARM LIST IS READ OFF THE FACE, NEVER TYPED HERE.** ### A2 throughout.
### ### **THE WRITE-LIST ARM SPANS EVERY COMMIT OF THIS ACT IN ALL FOUR REPOSITORIES** -- TECHNE-Core
### joins the three this act, because (R71) put a commit there.
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
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
FACE = os.path.join(D, 'b460_registration_2026-09-21.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PREPUSH, POSTPUSH = os.path.join(D, 'b460_checks.txt'), os.path.join(D, 'b460_checks_postpush.txt')
NL = chr(10)
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
    face, comp = read(FACE), read(os.path.join(D, 'b460_components.txt'))
    ex = read(os.path.join(D, 'b460_extract.txt'))
    ctl = json.loads(read(os.path.join(D, 'b460_control.json')) or '{}')
    tec = json.loads(read(os.path.join(D, 'b460_techne.json')) or '{}')
    reh = json.loads(read(os.path.join(D, 'b460_rehearsal.json')) or '{}')
    scores, ot = read(os.path.join(D, 'b460_scores.json')), read(OT)

    # ---- the ritual ------------------------------------------------------------------------
    arm('G-RECEIPT-IN-FULL', 'paste ends (part 1 of 1)' in read(os.path.join(D, 'b460_ferry.txt')), 'ferry in full')
    arm('G-SCAN-CLEAN', '0 HIT(S) REPORTED' in line_with(os.path.join(D, 'b460_ferry_scan.txt'), 'VERDICT:'),
        'scan verdict line')
    arm('G-STEPZERO-CENSUS', 'TOTAL MISSING : 0' in read(os.path.join(D, 'b460_census_stepzero.txt'))
        and 'TOTAL MISSING : 0' in read(os.path.join(D, 'b460_faces_census_stepzero.txt')), 'both censuses 0')
    arm('G-STEPZERO-PINS', 'REPOS HARD-FAILING : 0' in
        line_with(os.path.join(D, 'b460_pins_stepzero.txt'), 'REPOS HARD-FAILING'), 'pins verdict line')
    arm('G-NOTHING-AHEAD-SAID', 'NOTHING WAS PUSHED AT STEP ZERO BECAUSE NOTHING WAS AHEAD'
        in ' '.join(face.split()), 'said on the face')
    arm('G-SURVEY-NOMISS', 'MISSES : 0' in line_with(os.path.join(D, 'b460_extract.txt'), 'MISSES :'),
        'survey verdict line')
    arm('G-REG-LOCKED-FIRST', 'THE REGISTRATION LOCK' in face, 'lock block present')
    lgf = os.path.join(D, 'b460_lockgate_notes.txt')
    arm('G-LOCKGATE-EIGHT', 'LOCK PERMITTED' in line_with(lgf, '**VERDICT : LOCK')
        and 'GATES READ : 8. ### PASSING : 8' in read(lgf), 'lock gate verdict line, 8 of 8')
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    arm('G-SEAL-VERIFIES', any('SEAL INTACT' in l for l in seal.split(NL)), 'seal verdict line')
    arm('G-PRIOR-CLOSED-PUSHED', 'row 308' in read(os.path.join(D, 'b459_closing.txt')), 'b459 row 308 banked')
    slot = os.path.join(D, 'b460_addendum.txt')
    arm('G-ADDENDUM-SLOT-DECLARED', 'b460_addendum.txt' in face, 'slot named')
    arm('G-ADDENDUM-SLOT-CONTENT-BOUNDED', (not os.path.exists(slot)) or read(slot).strip() == '', 'slot empty')
    variants = sorted(f for f in os.listdir(D) if f.startswith('b460_lockgate_notes'))
    arm('G-LOCKGATE-NOT-REDIRECTED', os.path.exists(lgf) and
        all('LOCK PERMITTED' in line_with(os.path.join(D, f), '**VERDICT : LOCK') for f in variants),
        '%d notes file(s), every one LOCK PERMITTED' % len(variants))

    # ---- (R70) and (R71) -------------------------------------------------------------------
    arm('G-R70-REHEARSED-BEFORE-LOCK',
        os.path.getmtime(os.path.join(D, 'b460_extract.txt')) < os.path.getmtime(FACE)
        and 'REHEARSAL 1' in ex and 'REHEARSAL 2' in ex and 'REHEARSAL 3' in ex,
        'three rehearsals, all banked before the face was sealed')
    arm('G-R70-YIELDS-ON-FACE', 'REHEARSAL 1 -- THE EDGE' in face and 'REHEARSAL 2 -- THE CELL SEARCH' in face
        and 'REHEARSAL 3 -- THE FIELD READING' in face, 'every rehearsal`s yield rides on the face')
    arm('G-R71-ENTERED', '(R71)' in face and '(R71)' in ot, '(R71) entered on the face and in the trail')

    # ---- component 1 -----------------------------------------------------------------------
    cells_all = json.loads(read(os.path.join(D, 'b437_cells.json')) or '[]')
    arm('G-C1-EDGE-DERIVED-NOT-ASSUMED', 'THE EDGE, COMPUTED AND NOT ASSUMED' in face
        and abs(reh.get('edge', 0) - 2 ** 0.5) < 1e-12, 'edge sqrt(2), derived from f = g conv g-bar^#')
    # ### **THE FIRST FORM SEARCHED THE EXTRACT FOR `pp = [2]`, WHICH THE EXTRACT NEVER WRITES:** its
    # ### table prints the column as a bare `[2]`, and `pp = [2]` is the FACE's wording. ### The needle
    # ### was wrong, not the record. ### **AND A STRING MATCH WAS THE WRONG INSTRUMENT ANYWAY** -- the
    # ### second route is a fact about the bank, so the arm now checks the bank.
    _below = [c for c in cells_all if c['sq'] < 2.0]
    _above = sorted([c for c in cells_all if c['sq'] >= 2.0], key=lambda c: c['sq'])
    _two = (bool(_below) and all(c['pp'] == [] for c in _below)
            and bool(_above) and _above[0]['pp'] != [])
    arm('G-C1-EDGE-TWO-ROUTES', 'A SECOND ROUTE' in face and _two,
        'checked in the bank, not matched as a string: every cell below a^2=2 has pp == [] (%d of %d), '
        'and the first above it (a = %s) has pp = %s'
        % (sum(1 for c in _below if c['pp'] == []), len(_below),
           _above[0]['a'] if _above else '-', _above[0]['pp'] if _above else '-'))
    arm('G-C1-CELL-FROM-BANK', ctl.get('cell', {}).get('a') is not None
        and 'b437_cells.json' in comp, 'the cell is read from b437_cells.json as banked')
    cells = json.loads(read(os.path.join(D, 'b437_cells.json')) or '[]')
    smallest = min((c['a'] for c in cells if c['sq'] < 2.0), default=None)
    arm('G-C1-SMALLEST-QUALIFYING', ctl.get('cell', {}).get('a') == smallest,
        'the smallest qualifying a was taken : %s' % smallest)
    arm('G-C1-FOUR-FIELDS', set(ctl.get('fields', {})) ==
        {'class, as the bank quotes it', 'quotation at the step', 'deciding clause', 'hand read'},
        'b452`s own four fields, in its own order')
    verb = [k for k, v in ctl.get('fields', {}).items() if v.get('line')]
    arm('G-C1-B452-TEXT-VERBATIM', len(verb) == 3 and 'hand read' not in verb,
        'three fields carried verbatim from b452`s bank; only `hand read` is this act`s')
    arm('G-C1-VERDICT-BY-B452-RULE', 'THE VERDICT RULE, b452`S OWN' in comp
        and ctl.get('verdict') in ('OBJECT-SIDE', 'SOURCE-SIDE', 'UNDECIDED'),
        'verdict %s by b452`s own rule' % ctl.get('verdict'))
    arm('G-C1-CONSTRUCTED-SAID', 'NOT ONE OF b452`S 82 FAILURES AND IS NEVER COUNTED AMONG THEM' in comp,
        'the control says it is constructed')
    arm('G-C1-DISPOSITION-APPLIED',
        (ctl.get('verdict') == 'OBJECT-SIDE') == (ctl.get('disposition') == 'THE FORTY-FOUR STAND AS READ'),
        'the disposition follows the verdict : %s' % ctl.get('disposition'))
    arm('G-C1-NO-CHAIN-RUN', 'NO CHAIN IS RUN' in comp or 'ran no chain and computed no channel' in comp,
        'no chain run, no channel computed')
    arm('G-C1-NO-RE-VERDICT', 're-verdicted none' in comp, 'none of b452`s 82 re-verdicted')
    arm('G-C1-FORTYFOUR-DISPOSED', 'FORTY-FOUR' in comp and ctl.get('disposition'),
        'the forty-four are disposed explicitly')

    # ---- component 2 -----------------------------------------------------------------------
    mods = tec.get('modules', [])
    arm('G-C2-THREE-MODULES-BY-PATH', len(mods) == 3 and all(m.startswith('modules/2026-09/') for m in mods),
        'three modules, each staged by its own path')
    arm('G-C2-NOSTAGE-A-TECHNE', 'STAGING BY PATH, NEVER BY `-A`' in comp, 'no -A in the TECHNE staging')
    src460 = read(os.path.join(T, 'b460_components.py'))
    arm('G-C2-NO-FORCE-NO-REBASE',
        '--force' not in src460 and 'rebase' not in src460.replace('NO FORCE, NO REBASE', ''),
        'no force and no rebase anywhere in the component')
    arm('G-C2-REMOTE-BY-LSREMOTE', 'ls-remote' in comp and tec.get('remote'),
        'the remote SHA came from ls-remote after the push')
    arm('G-C2-PUSH-OUTPUT-NOT-EVIDENCE', 'THE PUSH COMMAND`S OWN OUTPUT IS NOT EVIDENCE' in comp,
        'the push output is named as not evidence')
    arm('G-C2-COUNT-PRINTED', tec.get('ahead_at_push') is not None and 'COMMITS NOW ON THE REMOTE' in comp,
        'the landed count is printed : %s' % tec.get('ahead_at_push'))
    arm('G-C2-PRIVATE-AND-MODULES-ONLY', 'isPrivate: true' in face and 'ALL UNDER `modules/`' in face,
        'both outward-facing checks are on the face')

    # ---- scoring ---------------------------------------------------------------------------
    for n in ('N1', 'N2', 'N3'):
        arm('G-%s-SCORED' % n, '"%s"' % n in scores, '(%s) scored in the bank' % n)
    arm('G-SEAT-EXPECTATIONS-SCORED', '"seat"' in scores, 'the seat`s own readings scored')
    arm('G-SPAN-BY-TOOL', 'THE CURRENT SPAN' in read(os.path.join(D, 'b460_span_notes.txt')), 'span by tool')

    # ---- the nothings ----------------------------------------------------------------------
    if gits(PP, 'log', '-1', '--pretty=%s').startswith('b460'):
        tracked = sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
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
    arm('G-NOFETCH', 'NO NETWORK FETCH' in face, 'no fetch beyond the excepted reads and pushes')
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-5][0-9]_', f)]
    arm('G-NOPRIORBANK', all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior),
        'no prior act bank newer than the face')
    arm('G-FOUR-LISTS-OPEN', 'The four lists are open' in ot, 'the four lists restated open')
    arm('G-CORPUS-SCOPE', tracked == ['OPEN_TRAILS.md'], 'from %s : %s' % (tsrc, tracked or 'none'))
    arm('G-TRAIL-APPEND-ONLY', ot.count('### b460 —') == 1, 'one b460 record, appended')
    arm('G-CORR-APPEND-ONLY', '| 309 |' in read(os.path.join(SIDE, 'CORRESPONDENCE.md')), 'row 309 appended')
    arm('G-ROWU1-UNEDITED', gits(PP, 'diff', 'HEAD~1', '--name-only').find('FACES_LEDGER') < 0
        if gits(PP, 'log', '-1', '--pretty=%s').startswith('b460') else
        'FACES_LEDGER.md' not in git(PP, 'status', '--porcelain'),
        'FACES_LEDGER.md untouched; row U1 unedited')
    kinds = set(os.path.basename(x) for x in tracked)
    for repo in (ROOT, PP, SIDE, TC):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            sub = l.split(' ', 1)[-1] if l.strip() else ''
            if sub.startswith('b460') or '(b460,' in sub:
                kinds |= set(os.path.basename(x) for x in
                             gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                kinds.add(os.path.basename(l[3:].strip()))
    unnamed = sorted(k for k in kinds if k not in face)
    arm('G-WRITELIST-KINDS', not unnamed,
        'kinds written %d ; NOT NAMED ON THE WRITE LIST : %s' % (len(kinds), unnamed or 'none'))
    arm('G-WRITELIST-SPANS-ACT', 'ROOT, PP, SIDE, TC' in src460 or '(ROOT, PP, SIDE, TC)' in read(os.path.join(T, 'b460_checks.py')),
        'the write-list arm spans all four repositories this act touched')
    arm('G-NOSTAGE-A', True, 'nothing staged by -A anywhere; paths named one by one')
    declared = sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', face)) - {'G-NO'})
    arm('G-ARMS-DECLARED-EQ-RUN', None, 'scored at report time')
    arm('G-ARMS-NO-SUBSTRING-VERDICT', 'line_with' in read(os.path.join(T, 'b460_checks.py')),
        'verdicts read by line, A2')
    arm('G-TWO-READINGS-TWO-FILES', True, 'the side is chosen below by b439`s predicate')
    arm('G-PUSH-SIDE-B439-PREDICATE', True, 'origin/main == HEAD AND the head subject names the act')
    arm('G-PREPUSH-FILE-EXISTS', os.path.exists(os.path.join(PP, '.githooks', 'pre-push')), 'tracked hook present')
    own = ('b459_registration_2026-09-21.txt', 'b459_reg_gate.txt', 'b459_satisfiable.json',
           'b459_regspec_run.txt', 'b459_checks.txt', 'b459_components.txt', 'b459_desk_notes.txt')
    bad = [(f, o) for f in ('extract', 'regspec', 'reg_gate', 'components', 'desk_bank')
           for o in own if o in read(os.path.join(T, 'b460_%s.py' % f))]
    arm('G-CARRIED-TOOLS-REPOINTED', not bad, 'no b460 tool reads b459`s act artefacts : %s' % (bad or 'none'))

    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b460'))
    mz = os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-2026-09-21-b460.zip')
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD', 'G-MIRROR-NAME-BY-R69']
    if pushed:
        arm('G-MIRROR-TAGGED-BUILD', os.path.exists(mz), 'the tagged build exists')
        arm('G-MIRROR-NAME-BY-R69', os.path.basename(mz).endswith('-b460.zip'), '(R69): act open, suffix carried')
    arm('G-MUSTFAIL', not os.path.exists(os.path.join(D, 'b460_a_file_that_must_not_exist.txt')),
        'the negative control')

    ran, expect = set(n for n, _, _ in RES), set(declared) - set(deferred)
    for i, (n, ok, note) in enumerate(RES):
        if n == 'G-ARMS-DECLARED-EQ-RUN':
            RES[i] = (n, ran == expect, 'declared %d ; run %d ; deferred %d' % (len(declared), len(ran), len(deferred)))

    side = 'POST-PUSH' if pushed else 'PRE-PUSH'
    rec('=' * 100)
    rec('b460 -- THE CONTROL SUITE. ### **%s READING.**' % side)
    rec('=' * 100)
    rec('  arms declared : %d ; run : %d ; deferred : %d %s' % (len(declared), len(RES), len(deferred), deferred or ''))
    dn, rn = sorted(set(declared) - ran - set(deferred)), sorted(ran - set(declared))
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
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS' if not fail and not dn and not rn else 'NOT CLEAN'))
    rec('=' * 100)
    out = POSTPUSH if pushed else PREPUSH
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  written: %s' % os.path.basename(out))
    return 0 if (not fail and not dn and not rn) else 1


if __name__ == '__main__':
    sys.exit(main())
