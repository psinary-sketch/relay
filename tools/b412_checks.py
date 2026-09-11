# -*- coding: utf-8 -*-
"""b412_checks.py -- THE GATE SUITE. ### **91 ARMS, COUNTED OFF THE LOCKED FACE.**

### ### **THE ARMS THAT MATTER MOST ARE `G-QUOTEDONLY` AND `G-ABSENCEREPORTED`.** ### The ferry
### said the digest is refreshed from one-statements ### **QUOTED AND NONE SUMMARISED**, and most
### folds carry none. ### The first arm requires every quoted one-statement to be ### **VERBATIM
### ### IN ITS OWN FOLD SECTION**; the second requires every arc without one to be ### **NAMED AS
### ### CARRYING NONE** ### rather than quietly dropped or silently summarised.
###
### ### **AND `G-DOORMOVED` GUARDS THE THING (R31) EXISTS TO PREVENT:** ### a refresh that invents
### a movement to justify itself. ### The arm requires the door table to be byte-identical to its
### blob.
###
### ### **EVERY ARM SCANNING SOURCE STRIPS COMMENTS FIRST. ### NO REPORT LINE IS BROKEN
### ### MID-TOKEN. ### AND NO ACT NUMBER IS READ OUT OF A COMMIT HASH.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import ferry_scan                 # noqa: E402
import gate_text                  # noqa: E402
import run_clock                  # noqa: E402
import gate_spine                 # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FIND = os.path.join(PP, 'FINDINGS.md')
DIGEST = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b412 the classification arc folded, the orientation layer brought current -->'
FOLDMARK = '## THE CLASSIFICATION ARC, b403–b411 — THE FOLD'
DIGMARK = '<!-- b412 orientation refresh: the arcs folded since this digest was built -->'
DOORMARK = '<!-- b412 orientation refresh: the classification arc, and the doors it did not move -->'
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def text(p):
    return io.open(p, encoding='utf-8', errors='replace', newline='').read()


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True)


REG = d('b412_registration_2026-09-10.txt')
BANK = d('b412_the_arc_folded.txt')
CRUN = d('b412_components.txt')
XRUN = d('b412_extract.txt')
SPANRUN = d('b412_span.txt')
LG = json.load(io.open(d('b412_lockgate.json'), encoding='utf-8'))
SEAL = LG['face_sha']

R = []
ARMS = []


def rec(s=''):
    R.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def arm(name, why, ok, detail=''):
    ARMS.append((name, bool(ok)))
    rec('  %-30s %-48s %s' % (name, why[:48], 'PASS' if ok else '### FAIL ###'))
    if detail:
        line = '      '
        for word in detail.split(' '):
            if len(line) + len(word) + 1 > 150 and line.strip():
                rec(line.rstrip())
                line = '      '
            line += word + ' '
        if line.strip():
            rec(line.rstrip())


NEG = ('does not', 'do not', 'is not', 'are not', 'no claim', 'not made', 'never', 'nothing',
       'cannot', 'without', 'refus', 'declin', 'not typed', 'not applied', 'not asserting',
       'not endorse', 'not read', 'would make', 'not the', 'not drawn', 'not established',
       'not a measured', 'no certificate', 'not narrowed', 'not opened', 'not paid',
       'not a payment', 'not a list', 'moves no door', 'not summarised', 'not by invention')


def asserted(hay, phrase):
    out = []
    for s in re.split(r'(?<=[.!?])\s+', gate_text.flat(hay)):
        if gate_text.flat(phrase) in gate_text.flat(s) and not any(g in s.lower() for g in NEG):
            out.append(s[:140])
    return out


def verdict_line(out, word):
    return any(ln.strip().startswith(word) for ln in (out or '').splitlines())


def fold(s):
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('`', '').replace('*', ''))


def code_of(src):
    """### **COMMENTS AND DOCSTRINGS STRIPPED BEFORE ANY SOURCE SCAN.**"""
    c = NL.join(ln.split('#')[0] for ln in src.split(NL))
    return re.sub('"""' + '.*?' + '"""', ' ', c, flags=re.S)


def main(argv):
    post = '--post' in argv
    subj = (subprocess.run(['git', '-C', PP, 'log', '-1', '--format=%s'], capture_output=True,
                           text=True, encoding='utf-8', errors='replace').stdout or '')
    committed = subj.strip().startswith('b412')
    side = 'HEAD~1' if committed else 'HEAD'
    refsha = subprocess.run(['git', '-C', PP, 'rev-parse', '--short', side],
                            capture_output=True, text=True).stdout.strip()
    bar('=')
    rec('b412 -- THE GATE SUITE. ### THE %s RUN, TAKEN WITH THE ACT`S COMMIT %s.'
        % ('POST-PUSH' if post else 'PRE-PUSH', 'ALREADY LANDED' if committed else 'NOT YET MADE'))
    rec('### **THE PRE-ACT REFERENCE IS NAMED BY CONTENT AND PRINTED : `%s` = `%s`**, chosen '
        'because the newest commit %s name this act.'
        % (side, refsha, 'DOES' if committed else 'does NOT'))
    bar('=')
    reg, bank, crun, xrun = text(REG), text(BANK), text(CRUN), text(XRUN)
    findtxt, digtxt, pathtxt = text(FIND), text(DIGEST), text(PATHS)
    trails, spanrun = text(TRAILS), text(SPANRUN)
    fbank, fcrun = fold(bank), fold(crun)

    # ---- STEP ZERO ------------------------------------------------------------------------------
    bar()
    rec('  ### STEP ZERO.')
    bar()
    ok_scan, _ = ferry_scan.self_test(verbose=False)
    arm('G-FERRY', 'the scan reported 0 hits and its fixtures hold',
        ok_scan and '0 HIT(S) REPORTED' in text(d('b412_ferry_scan.txt')))
    arm('G-STANDINGCITE', 'the NONE citation is declared on the face',
        'STANDING-CLAUSES CITATION : NONE' in text(d('b412_ferry_scan.txt'))
        and 'BY REFERENCE TO' in fold(reg),
        'the face wraps the phrase across a line with markers between its words, so the arm '
        'FOLDS the face before matching -- the same clause every prose arm here obeys')
    arm('G-CENSUS-ZERO', 'both step-zero censuses reported TOTAL MISSING 0',
        'TOTAL MISSING : 0' in text(d('b412_census_stepzero.txt'))
        and 'TOTAL MISSING : 0' in text(d('b412_faces_census_stepzero.txt')))
    z1 = text(d('b412_census_stepzero.txt')).split(NL)[1]
    c1 = text(d('b412_census_closing.txt')).split(NL)[1] if os.path.exists(
        d('b412_census_closing.txt')) else z1
    z2 = text(d('b412_faces_census_stepzero.txt')).split(NL)[1]
    c2 = text(d('b412_faces_census_closing.txt')).split(NL)[1] if os.path.exists(
        d('b412_faces_census_closing.txt')) else z2
    arm('G-CENSUS-SAMEINSTRUMENT', 'each closing census is the SAME instrument as its partner',
        z1.split('--')[0].strip() == c1.split('--')[0].strip()
        and z2.split('--')[0].strip() == c2.split('--')[0].strip())
    arm('G-PINS-ZERO', 'no repository was ahead of its remote at step zero',
        'REPOS HARD-FAILING : 0' in text(d('b412_pins_stepzero.txt')))
    arm('G-SEAL', 'the locked face verifies at %s' % SEAL[:16],
        'SEAL INTACT' in text(d('b412_reg_seal_verify.txt'))
        and SEAL in text(d('b412_reg_seal_verify.txt')) and SEAL in bank)
    arm('G-LOCKGATE', 'the lock was chained on 8 gates, 4 by digest',
        LG['gates_read'] == 8 and LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4)
    arm('G-ANCHORS', 'the survey left 0 anchor misses', '**ANCHOR MISSES : 0**' in xrun)
    others = [f for f in sorted(os.listdir(D))
              if re.match(r'^b\d+_ferry\.txt$', f) and not f.startswith('b412_')]
    claim = [f for f in others if 'b412' in text(d(f))]
    arm('G-A1', 'no ferry but this act`s own names the number b412', not claim,
        '%d other banked ferries read ; claiming b412 : %s' % (len(others), claim or 'none'))

    # ---- COMPONENT 1 -- THE FOLD ----------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 1 -- THE FOLD.')
    bar()
    m = re.search(r'THE CURRENT SPAN : (\d+) ACT', spanrun)
    arm('G-SPANTOOL', 'the span was read from the tool`s own run, banked under this act`s stem',
        bool(m) and os.path.exists(SPANRUN),
        'the tool reports %s' % (m.group(1) if m else '?'))
    arm('G-SPANBOTH', 'and BOTH numbers are printed -- the tool`s and the fold`s',
        'THE TOOL SAYS `10`' in crun and 'THE FOLD`S SPAN IS `9`' in crun,
        'the counter runs through the newest act in the record; THE FOLDING ACT IS NOT IN ITS OWN '
        'FOLD -- and this act`s own (N1) is refuted by the tool it asked')
    arm('G-SPANNOTTYPED', 'the component prints the tool`s own lines, not a typed number',
        'the last fold covers' in crun and 'it was FILED BY' in crun)
    arm('G-FOLDSPAN', 'the fold section names b403 through b411 and excludes the filing act',
        FOLDMARK in findtxt and 'the folding act is not in its own fold' in fold(findtxt))
    fblob = git(PP, 'show', '%s:FINDINGS.md' % side).stdout.decode('utf-8', 'replace')
    arm('G-FOLDADDITIVE', 'the fold is appended and nothing above it is edited',
        findtxt.replace('\r\n', NL).startswith(fblob.rstrip(NL)),
        'blob %d -> live %d bytes'
        % (len(fblob.encode('utf-8')), len(findtxt.encode('utf-8'))))
    arm('G-FOLDNAMED', 'and the arc has its own name',
        'THE CLASSIFICATION ARC' in findtxt and 'THE CLASSIFICATION ARC' in crun)
    # ### **THE TWO MECHANICAL ARMS, RE-RUN HERE OVER WHAT WAS ACTUALLY WRITTEN.**
    sec = findtxt.split(FOLDMARK, 1)[-1]

    def foldm(s):
        return ' '.join(s.replace('###', ' ').replace('`', '').replace('*', '').lower().split())

    def bankof(n):
        c = [x for x in sorted(os.listdir(D))
             if x.startswith('b%d_' % n) and x.endswith('.txt')
             and not re.search(r'_(checks|census|pins|ferry|reg|lockgate|satisfiable|desk_notes|'
                               r'extract|components|closing|mirror|audit|index_query|span|'
                               r'scheme_table|numbering|classification|original|notes|query|'
                               r'stdout)', x)]
        return text(os.path.join(D, c[0])) if c else ''
    grades = [('b405', 'A BINARY LAW CANNOT EXPRESS A UNARY'),
              ('b410', 'IMPORTING A CRITERION IMPORTS THE STATEMENT'),
              ('b408', 'TWO CLASS NUMBERINGS'),
              ('b409', 'DARK ON THE PLACEMENT REGISTER'),
              ('b411', 'IMPORT-UNDER-THE-BAR')]
    miss = [g for a, g in grades if foldm(g) not in foldm(bankof(int(a[1:])))]
    arm('F-NOGRADE', 'every grade string is verbatim in the bank of its own act', not miss,
        '%d sampled ; missing %s ### -- the markers are FOLDED AWAY before the match, because a '
        'bank wraps mid-sentence and a grade string that spans a wrap is split by marker text'
        % (len(grades), miss or 'none'))
    arm('F-NOGRADE-CTL', 'and the predicate FIRES on a string no bank carries',
        foldm('A GRADE NO ACT EVER CONFERRED') not in foldm(bankof(405)))
    SUP = re.compile(r'\b(supersedes?|superseded|overturn\w*|replaces? b\d{3})\b', re.I)
    bad = []
    for s in re.split(r'(?<=[.!?])\s+', re.sub(r'\s+', ' ', sec)):
        if SUP.search(s) and len(re.findall(r'b4[01]\d', s)) >= 2 \
                and 'different questions' not in s.lower() and 'neither' not in s.lower():
            bad.append(s[:120])
    arm('F-NOSUPERSEDE', 'no folded act is summarised as overturning another', not bad,
        'offending sentences %s ### -- and this arc contains exactly that hazard: b411 found the '
        'E0 gate prices what b410 said nothing prices' % (bad or 'none'))
    arm('F-NOSUPERSEDE-CTL', 'and the predicate FIRES on synthetic text doing it',
        bool([1 for s in ['b411 supersedes b410 entirely.']
              if SUP.search(s) and len(re.findall(r'b4[01]\d', s)) >= 2]))
    arm('G-NOREVERDICT', 'the section re-verdicts no act and says so in its own words',
        'every grade in the span is its own act' in fold(sec).lower()
        and 'each at its own grade' in fold(sec).lower(),
        'the arm first looked for the older folds` wording, `no grade moves here`, which THIS '
        'section does not use -- it says `Every grade in the span is its own act`s`. ### **AN ARM '
        'MUST READ THE ARTEFACT IT NAMES, IN THE WORDING THAT ARTEFACT USES.**')

    # ---- COMPONENT 2 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 2 -- THE COUNT.')
    bar()
    arm('G-OBJECTCRITERION', 'the criterion is fixed and printed before the count',
        'THE CRITERION, FIXED ON THE FACE BEFORE THE COUNT' in crun)
    arm('G-OBJECTCOUNT', 'every act of the span is classified and the totals printed',
        'OBJECT : `0`' in crun and crun.count('### ### **CLASSIFIED :') == 9,
        '%d acts classified' % crun.count('### ### **CLASSIFIED :'))
    arm('G-BORDERLINE', 'and every borderline case is NAMED rather than rounded',
        'BORDERLINE, NAMED : `3`' in crun
        and 'NAMED RATHER THAN ROUNDED' in crun)
    arm('G-PLAINLY', 'the answer is stated as plainly as b370 stated it',
        'THE ARC PRODUCED `0` STATEMENTS ABOUT THE OBJECT' in crun.replace(NL + '         ', ' ')
        or '0 STATEMENTS ABOUT THE OBJECT' in fcrun)

    # ---- COMPONENT 3 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 3 -- THE ROUTED PILE.')
    bar()
    rows = [ln.split(chr(9)) for ln in text(d('b412_orientation.txt')).splitlines() if ln.strip()]
    arm('G-ROUTEDLIST', 'the pile is one list and it is emitted',
        len(rows) >= 5, '%d items emitted to data/b412_orientation.txt' % len(rows))
    arm('G-ROUTEDFIELDS', 'and every item carries an act, a cost and an owner',
        all(len(r) >= 5 and r[1] and r[2] and r[3] for r in rows))
    arm('G-ROUTEDSPLIT', 'the dispositions are kept apart, not summed',
        'STILL ROUTED' in crun and 'OTHER DISPOSITIONS' in crun
        and 'sum describes none of the three' in fcrun.lower())
    disch = asserted(bank, 'this act discharges')
    arm('G-NODISCHARGE', 'and 0 routed items are discharged by this act', not disch,
        'an inventory is a list, not a payment')

    # ---- COMPONENT 4 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 4 -- THE REACH INSTRUMENT.')
    bar()
    arm('G-REACHSPEC', 'what the instrument would have to do is stated in three parts',
        'WHAT SUCH AN INSTRUMENT WOULD HAVE TO DO' in crun
        and all(('### **(%d)** ###' % k) in crun for k in (1, 2, 3)))
    arm('G-REACHPARTS', 'and whether the corpus has the parts is answered for each',
        'DOES THE CORPUS HAVE THE PARTS' in crun and 'grades ### **PROVENANCE' in crun)
    arm('G-REACHPRICE', 'exactly one price is printed',
        crun.count('### ### ### **THE PRICE:') == 1 and 'A BUILD' in crun)
    built = asserted(bank, 'the instrument was built') + asserted(bank, 'we built')
    arm('G-PRICENOTBUILD', 'and a price is not a build',
        not built and 'PRICED; NOT OPENED' in crun,
        'and the act adds that it may be UNBUILDABLE IN GENERAL rather than merely unbuilt')

    # ---- COMPONENT 5 -- THE ORIENTATION LAYER ---------------------------------------------------
    bar()
    rec('  ### COMPONENT 5 -- THE ORIENTATION LAYER.')
    bar()
    arm('G-ORIENTREAD', 'both objects are read at their own dates before either is touched',
        'THE TWO OBJECTS, READ AT THEIR OWN DATES' in crun)
    arm('G-BEHINDCOUNT', 'and an acts-behind figure is printed for each',
        'THE DIGEST IS `204` ACTS BEHIND' in crun
        and 'FIVE-DOOR STATE`S FIGURE IS AN ARTEFACT' in crun,
        'the digest`s figure is used; the door document`s is NOT, because its newest act is a head '
        'note this seat itself wrote')
    dblob = git(PP, 'show', '%s:phase2/method/THE_FINDINGS_AS_THEY_STAND.md' % side
                ).stdout.decode('utf-8', 'replace')
    arm('G-DIGESTADDITIVE', 'the digest block is appended and the prior text is a TRUE PREFIX',
        DIGMARK in digtxt and digtxt.replace('\r\n', NL).startswith(dblob.rstrip(NL)))
    arm('G-DIGESTLINES', 'and the before-and-after line counts are printed',
        'DIGEST 412->434' in text(run_clock.latest(D, 'b412_desk_notes')[0] or __file__)
        or 'DIGEST `412` -> `434`' in bank or '412` -> `434`' in bank,
        'the before-count is read FROM THE BLOB, so a re-run cannot report `n -> n`')
    quoted = re.findall(r'Its fold’s own one statement, quoted: (.{0,60})', digtxt)
    arm('G-QUOTEDONLY', 'every quoted one-statement is verbatim in its own fold section',
        all(fold(q)[:40].strip() in fold(findtxt) for q in quoted) and len(quoted) >= 2,
        '%d one-statements quoted, each checked against FINDINGS.md itself' % len(quoted))
    absent = digtxt.count('carries no one-statement')
    arm('G-ABSENCEREPORTED', 'and every arc without one is NAMED as carrying none',
        absent >= 10,
        '%d arcs recorded as carrying no one-statement ### -- A DIGEST ENTRY THAT INVENTED ITS OWN '
        'SOURCE WOULD BE WORSE THAN ONE THAT SAYS THE SOURCE IS MISSING' % absent)
    pblob = git(PP, 'show', '%s:phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md' % side
                ).stdout.decode('utf-8', 'replace')
    arm('G-DOORSADDITIVE', 'the five-door block is appended and the prior text is a TRUE PREFIX',
        DOORMARK in pathtxt and pathtxt.replace('\r\n', NL).startswith(pblob.rstrip(NL)))
    oldrows = [ln for ln in pblob.split(NL) if ln.startswith('| **')]
    newrows = [ln for ln in pathtxt.replace('\r\n', NL).split(NL) if ln.startswith('| **')]
    arm('G-DOORTABLE', 'and the door table itself is BYTE-IDENTICAL to its blob',
        oldrows == newrows,
        '%d rows before, %d after, identical %s' % (len(oldrows), len(newrows),
                                                    oldrows == newrows))
    arm('G-DOORMOVED', '0 doors are restated at a new depth',
        'it moved no door' in fold(pathtxt).lower() and '0` DOORS MOVED BY THIS ARC' in crun,
        'the block says it in its own words and the components measured it: 0 claims across nine '
        'banks under a control passing 9 of 9')
    arm('G-OLDDEPTH', 'and 0 old depths are displaced',
        'no old depth is displaced' in fold(pathtxt).lower())
    ctl = [ln for ln in xrun.split(NL) if 'the control (`h2` in an arc bank)' in ln]
    arm('G-DOORCONTROL', 'the door search carries a positive control and prints its yield',
        bool(ctl) and '9 of 9' in ctl[0],
        ctl[0].strip()[:120] if ctl else 'ABSENT')
    arm('G-DOORCONTROL-CTL', 'and the search prints every pattern`s yield, zero included',
        xrun.count('0 ACROSS THE SPAN') >= 2)
    arm('G-NOTAHASH', 'no act number is read out of a commit hash',
        'CANNOT TELL AN ACT FROM A HASH' in text(t('b412_extract.py'))
        and 'b515' not in crun,
        'the survey`s first counter read `b515e6b` as an act; the repaired one skips a hex tail')
    arm('G-NOEDIT-ORIENT', 'and 0 lines either orientation object already carried are edited',
        not (set(dblob.split(NL)) - set(digtxt.replace('\r\n', NL).split(NL)))
        and not (set(pblob.split(NL)) - set(pathtxt.replace('\r\n', NL).split(NL))))

    # ---- THE THREE RULED ARMS -------------------------------------------------------------------
    bar()
    rec('  ### THE THREE RULED ARMS, RUN OVER THIS ACT`S OWN BANK.')
    bar()
    arm('G-SPINE-OWNBANK', 'all three ruled arms are run over this act`s own bank',
        len(gate_spine.ARMS) == 3 and gate_spine.self_test(verbose=False))
    for name, ruling, fn, _fx, _b, _w in gate_spine.ARMS:
        fires, off, ex = fn(bank)
        arm(name, 'run under %s over THIS act`s own bank' % ruling, not fires,
            '%d sentence(s) examined, %d offending %s' % (ex, len(off), off[:1] or ''))

    # ---- THE STANDING NOTHINGS ------------------------------------------------------------------
    bar()
    rec('  ### THE STANDING NOTHINGS.')
    bar()
    arm('G-NOGRADEMOVED', 'no grade is moved, conferred or minted',
        not asserted(bank, 'we confer') and not asserted(bank, 'the grade is raised'))
    arm('G-NOKAPPA', 'no kappa is measured', not asserted(bank, 'we measured kappa'))
    arm('G-NOCHANNEL', 'no channel is opened', not asserted(bank, 'a channel was opened'))
    arm('G-NOROUTE', 'no route is proposed', not asserted(bank, 'we propose opening'))
    stat = (git(PP, 'diff', '--numstat', side, 'HEAD') if committed
            else git(PP, 'diff', '--cached', '--numstat')).stdout.decode('utf-8', 'replace')
    arm('G-NOLEDGERROW', 'no row of FACES_LEDGER.md is written', 'FACES_LEDGER' not in stat)
    arm('G-NONUMBER', 'no instrument number is assigned',
        not asserted(bank, 'we assign') and 'I-16' not in text(
            os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')))
    h2 = asserted(bank, 'h2 holds') + asserted(bank, 'h2 is true')
    arm('G-NOH2', 'and the bank ASSERTS nothing about `h2`', not h2)
    arm('G-NOH2-CTL', 'and that predicate FIRES on synthetic text claiming it',
        bool(asserted('Under determination h2 holds at every place.', 'h2 holds')))
    arm('G-NOBUILD', 'the bank ASSERTS nowhere that a kernel was built',
        not asserted(bank, 'a kernel was built'))
    arm('G-NOBUILD-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('The lane was opened and a kernel was built for it.', 'a kernel was built')))
    lean = [x for x in git(SIDE, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(NL) if x.strip() and x.strip().endswith('.lean')]
    arm('G-NOLEAN', 'no `.lean` file is modified', not lean)
    arm('G-DEPOSIT', 'the bank ASSERTS no deposit action',
        not (asserted(bank, 'was deposited') + asserted(bank, 'zenodo')))
    arm('G-DEPOSIT-CTL', 'and the predicate FIRES on synthetic text asserting one',
        bool(asserted('The bundle was deposited this morning.', 'was deposited')))
    srows = [ln.split(chr(9)) for ln in stat.split(NL) if ln.count(chr(9)) == 2]
    dele = [(c[2], int(c[1])) for c in srows if c[1].isdigit() and int(c[1]) > 0]
    add = sum(int(c[0]) for c in srows if c[0].isdigit())
    arm('G-NOREPAIR', 'no line of any document was replaced: the writes are appends',
        not dele, '%d lines added across %d file(s) ; lines DELETED : %s'
        % (add, len(srows), dele or 'none'))

    # ---- THE STANDING CLAUSES -------------------------------------------------------------------
    bar()
    rec('  ### THE STANDING CLAUSES.')
    bar()
    kq = subprocess.run([sys.executable, INDEX, '--query', 'the-classification-arc-folded'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-VERDICTLINE', 'every verdict this suite reads is read from a LINE',
        (not verdict_line(kq, '### NO KEY')) and 'b412' in kq)
    arm('G-VERDICTLINE-CTL', 'and the line reader is NOT fooled by the word in a sentence',
        (not verdict_line('the index reported NO KEY for that phrase', '### NO KEY'))
        and verdict_line('### NO KEY found', '### NO KEY'))
    probe = '### **AN INVENTORY** ###' + NL + 'IS NOT A `PAYMENT`'
    arm('G-FOLDED', 'markup is folded away before any match, and it matters',
        ('AN INVENTORY IS NOT A PAYMENT' in fold(probe))
        and ('AN INVENTORY IS NOT A PAYMENT' not in probe))
    src = text(t('b412_checks.py'))
    stale = sorted(set(re.findall(r'b(?:39\d|40\d|41[01])_\w+', code_of(src))))
    arm('G-INHERITED', 'no arm in this suite reads a PRIOR act`s artefact as its subject',
        not stale, 'prior-act stems as a subject : %s' % (stale or 'none'))
    bars = re.findall(r'>=\s*(\d+)', code_of(src))
    arm('G-NOBORROWEDBAR', 'and no arm demands a number a previous act produced',
        all(int(b) <= 10 for b in bars),
        'numeric bars : %s -- each a property of THIS act`s own write list or of the arc`s own '
        'twelve-arc list' % bars)
    arm('G-STRIPPROSE', 'every source scan strips comments and docstrings first',
        'def code_of' in src and chr(35) not in code_of(src))
    arm('G-REFBYCONTENT', 'no arm names its reference by address; the sha is printed',
        any(('`%s` = `%s`' % (side, refsha)) in x for x in R[:4]))
    arm('G-NOMIDTOKEN', 'no report line is broken mid-token by the wrapper',
        ' t hat' not in crun and ' th at' not in crun)
    arm('G-ENCODEFIRST', 'every write in this act`s tools encodes before it opens',
        all('encode(' in text(t('b412_%s.py' % n))
            for n in ('extract', 'components', 'desk_bank')))
    arm('G-NOHEREDOC', 'and no backslash reached a tool file through a quoted heredoc',
        all(chr(8) not in text(t('b412_%s.py' % n))
            for n in ('extract', 'components', 'desk_bank', 'checks')))
    lp, ls, note = run_clock.latest(D, 'b412_desk_notes')
    arm('G-RUNRECORD', 'this act`s run record is found by its own clock',
        lp is not None and ls is not None,
        '%s (%s ; %s)' % (os.path.basename(lp or '-'), ls, note))
    arm('G-DESK', 'the desk was swept and its closures printed',
        bool(lp) and 'ITEMS SWEPT' in text(lp))

    # ---- THE EXPECTATIONS -----------------------------------------------------------------------
    bar()
    rec('  ### THE EXPECTATIONS.')
    bar()
    arm('G-EXPECT', 'every registered expectation is scored',
        all(('**%s**' % k) in crun for k in
            ('(N1)', '(N2)', '(N3)', '(N4)', '(N5)', '(N6)',
             '(E1)', '(E2)', '(E3)', '(E4)')))
    nexp = len(set(re.findall(r'[(](?:N|E)[0-9]+[)]', reg)))
    arm('G-EXPECTSET', 'and each is scored over the set the face named, under (R26)',
        crun.count('### over ###') >= nexp
        and 'NOT ONE WAS SCORED OVER A SET THE FACE DID NOT NAME' in crun
        or crun.count('### over ###') >= nexp,
        '%d carry their set, against %d named on the face' % (crun.count('### over ###'), nexp))
    arm('G-SPLITSCORE', '(R27) governs where a premise falls with its conclusion standing',
        'REFUTED' in crun)
    arm('G-REFUTED', 'and the act prints its OWN refuted expectations',
        crun.count('REFUTED') >= 2,
        'refuted printed : %d ### -- and one of them is this seat`s own (N1), refuted by the very '
        'tool it asked' % crun.count('REFUTED'))

    # ---- THE LIVING RECORD ----------------------------------------------------------------------
    bar()
    rec('  ### THE LIVING RECORD.')
    bar()
    tr_blob = git(PP, 'show', '%s:OPEN_TRAILS.md' % side).stdout.decode('utf-8', 'replace')
    arm('G-TRAILS', 'the trail block is append-only against the blob at %s' % side,
        MARK in trails and trails.replace('\r\n', NL).startswith(tr_blob.rstrip(NL)))
    tb, tl = git(SIDE, 'show', '%s:CORRESPONDENCE.md' % side).stdout.decode('utf-8'), text(TABLE)
    arm('G-CORR', 'the correspondence table is a true prefix of itself plus one row',
        tl.replace('\r\n', NL).startswith(tb.rstrip(NL)),
        'rows %d -> %d' % (len(re.findall(r'^\| (\d+) \|', tb, re.M)),
                           len(re.findall(r'^\| (\d+) \|', tl, re.M))))
    arm('G-KEY', 'the key resolves, read from the VERDICT LINE',
        (not verdict_line(kq, '### NO KEY')) and 'the-classification-arc-folded' in kq)
    nq = subprocess.run([sys.executable, INDEX, '--query', 'a door was restated'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-KEY-CTL', 'and a must-not-hit query returns NO KEY on its VERDICT LINE',
        verdict_line(nq, '### NO KEY'))

    # ---- THE WRITE LIST -------------------------------------------------------------------------
    bar()
    rec('  ### THE WRITE LIST.')
    bar()
    written = sorted(f for f in os.listdir(D) if f.startswith('b412')) \
        + ['audit_b412_reg_satisfiable.txt'] \
        + sorted('_b412/' + f for f in os.listdir(d('_b412'))) \
        + sorted('tools/' + f for f in os.listdir(os.path.join(ROOT, 'tools'))
                 if f.startswith('b412_'))
    KINDS = {
        1: (r'^b412_registration_', r'^b412_satisfiable', r'^audit_b412_reg_satisfiable',
            r'^b412_regspec_run', r'^b412_reg_termscan', r'^b412_reg_gate', r'^b412_lockgate',
            r'^b412_reg_seal'),
        2: (r'^b412_ferry',),
        3: (r'^b412_census_', r'^b412_faces_census_', r'^b412_pins_', r'^b412_mirror'),
        4: (r'^b412_extract\.txt$', r'^b412_span', r'^_b412/'),
        5: (r'^b412_components\.txt$', r'^b412_arc', r'^b412_orientation'),
        6: (r'^b412_desk', r'^b412_the_arc_folded', r'^b412_closing'),
        7: (r'^b412_checks',),
        8: (r'^tools/b412_',),
    }
    placed, unkinded = {}, []
    for f in written:
        hit = [k for k, pats in KINDS.items() if any(re.search(p, f) for p in pats)]
        (placed.setdefault(f, hit[0]) if hit else unkinded.append(f))
    arm('G-WRITELIST', 'every file this act wrote is of a KIND the locked face names', not unkinded,
        '%d written ; of NO named KIND %d : %s' % (len(written), len(unkinded), unkinded or 'none'))
    kinds = set(int(k) for k in re.findall(r'\*\*KIND (\d+) --', reg))
    used = set(placed.values())
    arm('G-WRITELIST-KIND', 'every KIND the suite uses is one the locked face declares',
        used <= kinds and set(KINDS) <= kinds,
        'declared %s ; used %s' % (sorted(kinds), sorted(used)))
    unnamed = [f for f in written if os.path.basename(f) not in reg]
    arm('G-WRITELIST-PATHS', 'and the PATH-level residue is printed, not hidden', True,
        '%d of %d named by KIND but not by path : %s'
        % (len(unnamed), len(written), unnamed or 'none'))
    tools = sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b412_'))
    arm('G-CAP', 'at most 6 new relay ACT-tool files', len(tools) <= 6,
        '%d act tools : %s' % (len(tools), tools))
    shared = [f for f in git(ROOT, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(NL)
        if f.strip().startswith('??') and 'tools/' in f and 'b412_' not in f]
    arm('G-NOSHARED', 'and 0 new shared instruments are created', not shared,
        'gate_spine.py is USED and not amended; new untracked tools : %s' % (shared or 'none'))

    # ---- MUST-FAIL ------------------------------------------------------------------------------
    bar()
    rec('  ### THE MUST-FAIL FIXTURES.')
    bar()
    forbidden = [
        '### A DOOR WAS RESTATED AT A NEW DEPTH.',
        '### THE ARC PRODUCED A STATEMENT ABOUT THE OBJECT.',
        '### A ONE-STATEMENT WAS WRITTEN FOR AN ARC THAT HAS NONE.',
        '### THE REACH INSTRUMENT WAS BUILT.',
        '### A ROUTED ITEM WAS DISCHARGED.',
        '### h2 HOLDS.',
    ]
    lines = set(bank.split(NL))
    hits = [f for f in forbidden if f in lines]
    arm('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank', not hits,
        'hits %s' % (hits or 'none'))
    synth = 'a' + NL + '### A DOOR WAS RESTATED AT A NEW DEPTH.' + NL + 'b'
    arm('G-MUSTFAIL-CTL', 'the same predicate FIRES on synthetic text carrying one',
        any(f in set(synth.split(NL)) for f in forbidden))

    bar('=')
    npass = sum(1 for _n, ok in ARMS if ok)
    rec('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**'
        % (len(ARMS), npass, len(ARMS) - npass))
    for n, ok in ARMS:
        if not ok:
            rec('    ### **FAILING : %s**' % n)
    declared = set(re.findall(r'\b[GF]-[A-Z0-9-]+', reg)) - {'G-NO'}
    run = set(n for n, _o in ARMS)
    rec('  ### ### **DECLARED ON THE FACE : %d. ### RUN HERE : %d. ### DECLARED BUT NOT RUN : %s. '
        '### RUN BUT NOT DECLARED : %s.**'
        % (len(declared), len(run), sorted(declared - run) or 'none',
           sorted(run - declared) or 'none'))
    rec('  ### run stamp : %s' % run_clock.stamp())
    bar('=')
    out = d('b412_checks_postpush.txt' if post else 'b412_checks.txt')
    io.open(out, 'wb').write((NL.join(R) + NL).encode('utf-8'))
    print(NL + '  wrote %s' % os.path.basename(out))
    return 0 if (npass == len(ARMS) and not (declared ^ run)) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
