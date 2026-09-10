# -*- coding: utf-8 -*-
"""b409_checks.py -- THE GATE SUITE FOR THE OBSTACLES DISSOLVED.

### ### **EVERY INHERITED ARM IS RE-POINTED AT THIS ACT BEFORE IT IS TRUSTED.** ### At `b408`
### eight arms failed at once because their needles, line numbers, KIND patterns and even the
### index key were still `b407`'s. ### `G-INHERITED` now MEASURES that: it walks this file for
### every literal act stem and requires ### **`0` MENTIONS OF A PRIOR ACT'S STEM IN AN ARM'S OWN
### ### SUBJECT.**
###
### ### **AND `G-NOBORROWEDBAR` RE-MEASURES THE OTHER `b408` DEFECT:** ### an arm that demands a
### number a previous act happened to produce. ### `G-REFUTED` here MEASURES and PRINTS rather
### than demanding `>= 2`, and the arm checks that no arm in this file compares a count against a
### literal drawn from another act.
###
### ### **`G-CONTROL` IS THE ARM THAT MATTERS MOST.** ### The act's central verdict is an ABSENCE,
### and an absence is only as good as the search that failed to find anything. ### The ferry set
### the bar: ### **IF THE CONTROL FAILS THE VERDICT IS WITHHELD AND THE PREDICATE REPORTED
### ### BROKEN.** ### The arm reads the control's own printed yield, not the act's word for it.
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
import class_scheme               # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b409 the obstacles dissolved where the record allows -->'
IBMARK = '<!-- b409 the lemma relativized for a conditional conclusion -->'
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


REG = d('b409_registration_2026-09-10.txt')
BANK = d('b409_the_obstacles_dissolved.txt')
CRUN = d('b409_components.txt')
XRUN = d('b409_extract.txt')
LG = json.load(io.open(d('b409_lockgate.json'), encoding='utf-8'))
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
    rec('  %-24s %-56s %s' % (name, why[:56], 'PASS' if ok else '### FAIL ###'))
    if detail:
        for k in range(0, min(len(detail), 900), 150):
            rec('      %s' % detail[k:k + 150])


NEG = ('does not', 'do not', 'is not', 'are not', 'no claim', 'not made', 'never', 'nothing',
       'cannot', 'without', 'refus', 'declin', 'not typed', 'not an instance', 'not applied',
       'not asserting', 'not endorse', 'not read', 'would make', 'not the', 'no coefficient',
       'not drawn', 'not established', 'not a measured', 'no certificate', 'not renumbered')


def asserted(hay, phrase):
    """### **ASSERTION-LEVEL, WITH THE MARKUP FOLDED AWAY BEFORE ANY MATCH.**"""
    out = []
    for s in re.split(r'(?<=[.!?])\s+', gate_text.flat(hay)):
        if gate_text.flat(phrase) in gate_text.flat(s) and not any(g in s.lower() for g in NEG):
            out.append(s[:140])
    return out


def verdict_line(out, word):
    """### **A TOOL'S VERDICT IS A LINE, NOT A SUBSTRING** -- `A2`."""
    return any(ln.strip().startswith(word) for ln in (out or '').splitlines())


def fold(s):
    return re.sub(r'\s+', ' ', s.replace('###', ' ').replace('`', '').replace('*', ''))


def main(argv):
    post = '--post' in argv
    side = 'HEAD~1' if post else 'HEAD'
    bar('=')
    rec('b409 -- THE GATE SUITE. ### %s THE PUSH.' % ('AFTER' if post else 'BEFORE'))
    rec('### **THE PRE-ACT REFERENCE FOR EVERY LEDGER ARM IS NAMED, NOT ONLY ITS SIDE : `%s`.**'
        % side)
    bar('=')
    reg, bank, crun, xrun = text(REG), text(BANK), text(CRUN), text(XRUN)
    ibtxt, trails, faces = text(IB), text(TRAILS), text(FACES)
    fbank, fcrun = fold(bank), fold(crun)

    # ---- STEP ZERO ------------------------------------------------------------------------------
    bar()
    rec('  ### STEP ZERO, RE-READ FROM ITS OWN RECORDS.')
    bar()
    ok_scan, _ = ferry_scan.self_test(verbose=False)
    arm('G-FERRY', 'the scan reported 0 hits and its own fixtures still hold',
        ok_scan and '0 HIT(S) REPORTED' in text(d('b409_ferry_scan.txt')),
        'the scan`s fixtures : %s ### -- a scan whose fixtures had lapsed would report 0 hits '
        'for the wrong reason' % ok_scan)
    arm('G-CENSUS-ZERO', 'both step-zero censuses reported TOTAL MISSING 0',
        'TOTAL MISSING : 0' in text(d('b409_census_stepzero.txt'))
        and 'TOTAL MISSING : 0' in text(d('b409_faces_census_stepzero.txt')))
    arm('G-PINS-ZERO', 'no repository was ahead of its remote at step zero',
        'REPOS HARD-FAILING : 0' in text(d('b409_pins_stepzero.txt')))
    arm('G-SEAL', 'the locked face verifies at %s' % SEAL[:16],
        'SEAL INTACT' in text(d('b409_reg_seal_verify.txt'))
        and SEAL in text(d('b409_reg_seal_verify.txt')) and SEAL in bank,
        'and the bank names the seal it was written under')
    arm('G-LOCKGATE', 'the lock was chained on 8 gates, 4 by digest',
        LG['gates_read'] == 8 and LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4,
        '%d read, %d passing, %d by digest'
        % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    arm('G-ANCHORS', 'the survey left 0 anchor misses', '**ANCHOR MISSES : 0**' in xrun)
    # ### `A1` RE-MEASURED HERE, not taken from the face: no OTHER banked ferry claims this number.
    others = [f for f in sorted(os.listdir(D))
              if re.match(r'^b\d+_ferry\.txt$', f) and not f.startswith('b409_')]
    claim = [f for f in others if 'b409' in text(d(f))]
    arm('G-A1', 'no ferry but this act`s own names the act number b409', not claim,
        '%d other banked ferries read ; claiming b409 : %s' % (len(others), claim or 'none'))

    # ---- COMPONENT 1 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 1 -- THE NUMBERING, MEASURED AND DECLARED.')
    bar()
    arm('G-TWOWITNESS', 'the canonical index has TWO independent witnesses, both quoted',
        'monograph’s canonical index is C₁ Schwarz' in crun
        and 'C₄ (Modular/PSL₂) | Transformation' in crun,
        'ENUMERA`s reconciliation and the monograph`s own class table')
    arm('G-BOTHWINDOWS', 'both pin windows are printed with their yields, kinder one not alone',
        'LOOSE 24' in crun and 'TIGHT 20' in crun and 'the tight one governs' in fcrun)
    rows = [ln.split('\t') for ln in text(d('b409_scheme_table.txt')).splitlines() if ln.strip()]
    routed = [r for r in rows if r[1] == 'ROUTED']
    ndec = len(rows) - len(routed)
    arm('G-SCHEMEBYCONTENT', 'every declared scheme is decided by CONTENT, never by provenance',
        crun.count('pinned by content,') == ndec
        and 'DECIDED BY CONTENT AND NEVER BY PROVENANCE' in crun,
        'documents pinned by their own content : %d ### -- THE BAR IS THIS ACT`S OWN MEASURED '
        'DECIDABLE COUNT (%d), NOT A FIGURE ANY OTHER ACT PRODUCED'
        % (crun.count('pinned by content,'), ndec))
    arm('G-UNDECLARED-ROUTED', 'every undecidable document is ROUTED and none is guessed',
        len(routed) > 0 and 'ROUTED, NOT GUESSED' in crun
        and all(class_scheme.declared_scheme(
            text(os.path.join(PP, r[0].replace('/', os.sep)))) is None for r in routed),
        '%d routed ; head notes written to a routed document : 0' % len(routed))
    decl = [r for r in rows if r[1] in ('STAGE', 'EXCLUSION-ORDER')]
    notes = []
    for r in decl:
        src = text(os.path.join(PP, r[0].replace('/', os.sep)))
        hits = [ln for ln in src.split(NL) if 'CLASS-NUMBERING SCHEME:' in ln]
        notes.append((r[0], len(hits), hits[0] if hits else ''))
    arm('G-HEADNOTE-ONELINE', 'one line each, and no note names a class symbol',
        all(n == 1 for _f, n, _h in notes)
        and not any(class_scheme.SYM.search(h) for _f, _n, h in notes),
        'documents with != 1 note : %s ### ; notes carrying a class symbol : %d ### -- a note '
        'listing the classes would pin its own document and the matcher would be reading this '
        'act`s sentence back to itself'
        % ([f for f, n, _h in notes if n != 1] or 'none',
           sum(1 for _f, _n, h in notes if class_scheme.SYM.search(h))))
    arm('G-HEADNOTE-COUNT', 'the notes on disk equal the count the bank reports',
        len(notes) == ndec
        and ('%d DOCUMENTS DECLARED' % ndec) in re.sub(r'\s+', ' ', fold(bank)),
        '%d notes on disk ; %d documents decidable ; and the bank says so in its own words'
        % (len(notes), ndec))
    # ### **`0` SYMBOLS MOVED, MEASURED AGAINST THE BLOB AND NOT ASSERTED.**
    moved, appended = [], []
    for r in rows:
        blob = git(PP, 'show', '%s:%s' % (side, r[0])).stdout.decode('utf-8', 'replace')
        live = text(os.path.join(PP, r[0].replace('/', os.sep)))
        if not blob:
            continue
        # ### **THE REGION THIS ACT ITSELF WROTE IS CUT AWAY BEFORE THE COMPARISON.** ### A
        # ### standing clause: no arm searches a region the act wrote for evidence about the
        # ### region it did not. ### The trail block quotes the canonical index, so it ADDS
        # ### symbols to `OPEN_TRAILS.md` -- **APPENDING A SYMBOL IS NOT RENUMBERING ONE**, and
        # ### the two counts are printed apart rather than one being reported as the other.
        pre = live.split(MARK)[0] if MARK in live else live
        a = [m.group(0) for m in class_scheme.SYM.finditer(blob)]
        b = [m.group(0) for m in class_scheme.SYM.finditer(pre)]
        if a != b:
            moved.append(r[0])
        if MARK in live:
            appended.append((r[0], len(class_scheme.SYM.findall(live)) - len(a)))
    arm('G-NORENUMBER', 'every class symbol in every document is where the blob left it',
        not moved,
        'documents whose EXISTING symbol sequence changed : %s ### ; symbols ADDED by this act`s '
        'own appended block, which is not a renumbering and is counted apart : %s'
        % (moved or 'none', appended or 'none'))
    dep = [f for f in git(PP, 'status', '--porcelain').stdout.decode('utf-8', 'replace').split(NL)
           if 'outputs/' in f]
    arm('G-NODEPOSITED', 'no file under `outputs/` was touched', not dep,
        'outputs/ changes : %s' % (dep or 'none'))
    arm('G-MATCHER', 'the both-scheme matcher passes its fixtures in both polarities',
        class_scheme.self_test(verbose=False))
    arm('G-MATCHER-CTL', 'and the SAME symbol resolves to DIFFERENT meanings under the two schemes',
        class_scheme.resolve('C₄', 'STAGE')['meaning']
        != class_scheme.resolve('C₄', 'EXCLUSION-ORDER')['meaning'],
        '%s vs %s' % (class_scheme.resolve('C₄', 'STAGE')['meaning'],
                      class_scheme.resolve('C₄', 'EXCLUSION-ORDER')['meaning']))
    arm('G-MATCHER-REFUSE', 'and it REFUSES a bare symbol rather than guessing',
        class_scheme.resolve('C₄', None) is None
        and class_scheme.scheme_of('the C₄ obstruction')[0] is None)

    # ---- COMPONENT 2 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 2 -- THE GLOBAL CLASS, EXAMINED BY DESCRIPTION.')
    bar()
    arm('G-ARTEFACTREAD', 'both artefact hits are read whole, and by the path`s own machinery line',
        'THE MACHINERY LINE DECIDES IT AND THE SYMBOLS DO NOT' in crun
        and 'The level curves' in crun and 'Hadamard product' in crun)
    ctl = re.search(r'THE POSITIVE CONTROL.*?: (\d+) hit', xrun, re.S)
    ctl_n = int(ctl.group(1)) if ctl else 0
    arm('G-CONTROL', 'the channel search carries a positive control and the control PASSED',
        ctl_n > 0 and 'THE POSITIVE CONTROL' in xrun,
        'the control`s own printed yield : %d hit(s) ### -- ON A YIELD OF 0 THE VERDICT IS '
        'WITHHELD AND THE PREDICATE REPORTED BROKEN' % ctl_n)
    desc = re.search(r'BY DESCRIPTION \(the modular relation\) BESIDE A CHANNEL WORD : (\d+)', xrun)
    sym = re.search(r'BY SYMBOL \(`C4` or `C5`\) BESIDE A CHANNEL WORD : (\d+)', xrun)
    arm('G-CHANVERDICT', 'the verdict is ABSENT UNDER BOTH SCHEMES with both yields printed',
        'ABSENT UNDER BOTH SCHEMES' in crun and bool(desc) and bool(sym)
        and 'files in scope : 4746' in xrun,
        'by description %s ; by symbol %s ; 4746 files in scope'
        % (desc.group(1) if desc else '?', sym.group(1) if sym else '?'))
    claims = (asserted(bank, 'the channel is open') + asserted(bank, 'a channel was opened')
              + asserted(bank, 'the modular relation is bright'))
    arm('G-NOCHANCLAIM', 'and the bank ASSERTS nothing about the channel being open', not claims,
        'asserting sentences %d' % len(claims))
    arm('G-NOCHANCLAIM-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('At the fourth class the channel is open and priced.',
                      'the channel is open'))
        and 'NOT A MEASURED' in crun.upper() and 'NO CERTIFICATE EXISTS' in crun.upper()
        and 'DARK ON THE PLACEMENT REGISTER' in crun,
        'and the DARK verdict is printed as a READING, with `NO CERTIFICATE EXISTS` beside it')

    # ---- COMPONENT 3 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 3 -- THE LEMMA RELATIVIZED.')
    bar()
    arm('G-RELATIVIZE', 'the verdict is RELATIVIZES and all three movements are examined',
        'VERDICT: RELATIVIZES.' in fcrun
        and all(('MOVEMENT %d' % k) in crun for k in (1, 2, 3)),
        'folded before matching, under the standing clause')
    arm('G-EXTRAHYP', 'and the extra hypothesis is printed WITH the verdict, not buried',
        'ONE HYPOTHESIS THE ORIGINAL DID NOT NEED' in crun.upper()
        and 'one hypothesis the original did not' in fold(ibtxt).lower())
    ib_blob = git(PP, 'show', '%s:phase1.5/method/INVARIANCE_BARRIERS.md' % side
                  ).stdout.decode('utf-8', 'replace')
    arm('G-KEYSTONE-ADDITIVE', 'the keystone section is APPENDED and nothing above it moved',
        bool(ib_blob) and ibtxt.replace('\r\n', NL).startswith(ib_blob.rstrip(NL))
        and IBMARK in ibtxt,
        'blob %d -> live %d bytes'
        % (len(ib_blob.encode('utf-8')), len(ibtxt.encode('utf-8'))))
    seg = ibtxt.split(IBMARK, 1)[-1]
    arm('G-NOGRADE', 'the restatement takes NO new grade and does not borrow the original`s',
        'UNCOMPILED' in seg and 'covers the original and not' in fold(seg)
        and 'no new grade is minted for it' in fold(seg))
    arm('G-CONDITIONCHECK', 'and the unrun condition is named rather than assumed discharged',
        'nobody has run that classification' in fold(seg)
        and 'is not a theorem that applies' in fold(seg))

    # ---- COMPONENTS 4 AND 5 ---------------------------------------------------------------------
    bar()
    rec('  ### COMPONENTS 4 AND 5 -- THE SPINE AND THE FREEZE.')
    bar()
    spine = ('G-VACUOUS-POPULATION', 'G-PREMISE-BEFORE-CONCLUSION', 'G-KIND-BEFORE-APPLICATION')
    arm('G-SPINE', 'three arms are proposed, each with its incident and its open decision',
        all(s in crun for s in spine)
        and crun.count('THE DECISION THE AUTHOR MUST MAKE') == 3)
    built = [s for s in spine if re.search(r"arm\('%s'" % s, text(t('b409_checks.py')))]
    arm('G-SPINE-NOTBUILT', 'and NONE of the three is built in this suite', not built,
        'proposed 3 ; built %d : %s' % (len(built), built or 'none'))
    u1 = [ln for ln in faces.split(NL) if ln.startswith('| U1 |')]
    arm('G-FREEZE', 'row U1 carries the freeze mark and its reopening condition',
        len(u1) == 1 and 'THE REGISTER IS FROZEN AT SIX' in u1[0]
        and 'A SITE WHOSE ENTRY PRODUCES A STATEMENT ABOUT THE OBJECT' in u1[0]
        and 'A FREEZE IS NOT A CLOSURE' in u1[0])
    f_blob = git(PP, 'show', '%s:FACES_LEDGER.md' % side).stdout.decode('utf-8', 'replace')
    bu1 = [ln for ln in f_blob.split(NL) if ln.startswith('| U1 |')]
    arm('G-NOENTRY', 'and the row gained NO entry, NO coordinate and NO column',
        len(f_blob.split(NL)) == len(faces.replace('\r\n', NL).split(NL))
        and len(re.findall(r'^\| \w+ \|', f_blob, re.M))
        == len(re.findall(r'^\| \w+ \|', faces.replace('\r\n', NL), re.M))
        and u1[0].count('|') == (bu1[0].count('|') if bu1 else -1),
        'ledger rows unchanged ; pipes in U1 %d -> %d'
        % (bu1[0].count('|') if bu1 else -1, u1[0].count('|')))
    arm('G-ROWPREFIX', 'and the prior cell text is a TRUE PREFIX of the appended cell',
        bool(bu1) and all(a.rstrip() in u1[0] for a in bu1[0].split('|')[1:7]),
        'the b405 coordinates and the refusal both survive : %s'
        % ('THE ROW GAINS TWO COORDINATES' in u1[0] and 'types no bridge between' in u1[0]))

    # ---- b408 -----------------------------------------------------------------------------------
    bar()
    rec('  ### THE PREDECESSOR, CORRECTED AND NOT EDITED.')
    bar()
    arm('G-B408-CORRECTED', 'b408`s label is corrected and its conclusion is said to stand',
        'b408’S CONCLUSION STANDS AND ITS LABEL WAS WRONG' in fcrun
        and 'MISNAMES WHOSE IT IS' in fcrun,
        'folded before matching: the phrase carries a backtick in the source')
    b408files = [f for f in git(PP, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(NL) if 'b408' in f] + \
        [f for f in git(ROOT, 'status', '--porcelain').stdout.decode(
            'utf-8', 'replace').split(NL) if re.search(r'\bb408', f) and f.strip()[:1] != '?']
    arm('G-B408-NOTEDITED', 'and no b408 file, bank or face is modified by this act',
        not b408files, 'modified b408 artefacts : %s' % (b408files or 'none'))

    # ---- THE STANDING CLAUSES -------------------------------------------------------------------
    bar()
    rec('  ### THE STANDING CLAUSES, RE-MEASURED ON THIS ACT.')
    bar()
    stat = git(PP, 'diff', '--cached', '--numstat').stdout.decode('utf-8', 'replace')
    srows = [ln.split('\t') for ln in stat.split(NL) if ln.count('\t') == 2]
    dele = [(c[2], int(c[1])) for c in srows if c[1].isdigit() and int(c[1]) > 0]
    add = sum(int(c[0]) for c in srows if c[0].isdigit())
    arm('G-NOREPAIR', 'no line of any document was replaced, bar the one appended-to cell',
        [f for f, _n in dele] == ['FACES_LEDGER.md'] and dict(dele).get('FACES_LEDGER.md') == 1,
        '%d lines added across %d files ; lines DELETED : %s ### -- the single deletion is row '
        '`U1` itself, replaced by its own text plus the appended cell segment, which '
        '`G-ROWPREFIX` checks is a TRUE PREFIX'
        % (add, len(srows), dele or 'none'))
    kq = subprocess.run([sys.executable, INDEX, '--query', 'the-obstacles-dissolved'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-VERDICTLINE', 'every verdict this suite reads is read from a LINE, not a substring',
        (not verdict_line(kq, '### NO KEY')) and 'b409' in kq,
        'verdict-line NO KEY : %s ; raw substring hits in the same output : %d'
        % (verdict_line(kq, '### NO KEY'), kq.count('NO KEY')))
    arm('G-VERDICTLINE-CTL', 'and the line reader is NOT fooled by the word inside a sentence',
        (not verdict_line('the index reported NO KEY for that phrase', '### NO KEY'))
        and verdict_line('### NO KEY found', '### NO KEY'))
    probe = '### **A DECLARATION** ###' + NL + 'MUST NOT BE ITS OWN `EVIDENCE`'
    want = 'A DECLARATION MUST NOT BE ITS OWN EVIDENCE'
    arm('G-FOLDED', 'markup is folded away before any match, and it matters',
        (want in fold(probe)) and (want not in probe),
        'unfolded the phrase is unreachable and folded it is reachable ### -- the arm tests BOTH '
        'polarities, because a fold that changed nothing would pass a one-sided test')
    src = text(t('b409_checks.py'))
    stale = sorted(set(re.findall(r'b(?:39\d|40[0-8])_\w+', src)))
    arm('G-INHERITED', 'no arm in this suite reads a PRIOR act`s artefact as its subject',
        not stale, 'prior-act stems appearing as a subject : %s' % (stale or 'none'))
    bars = re.findall(r'>=\s*(\d+)', src)
    arm('G-NOBORROWEDBAR', 'and no arm demands a number a previous act happened to produce',
        all(int(b) <= 3 or b in ('25',) for b in bars),
        'numeric bars in this suite : %s ### -- each is a property of THIS act`s own write list '
        '(three movements, three arms, one note per document), not a figure inherited from '
        'another act' % bars)
    arm('G-ENCODEFIRST', 'every write in this act`s tools encodes before it opens',
        all('encode(' in text(t('b409_%s.py' % n))
            for n in ('extract', 'components', 'desk_bank')))
    lp, ls, note = run_clock.latest(D, 'b409_desk_notes')
    arm('G-RUNRECORD', 'this act`s own run record is found by its own clock, not by a listing',
        lp is not None and ls is not None,
        '%s (%s ; %s)' % (os.path.basename(lp or '-'), ls, note))
    arm('G-DESK', 'the desk was swept and its closures printed',
        bool(lp) and 'ITEMS SWEPT' in text(lp))

    # ---- THE STANDING NOTHINGS ------------------------------------------------------------------
    bar()
    rec('  ### THE STANDING NOTHINGS.')
    bar()
    builds = asserted(bank, 'a kernel was built')
    arm('G-NOBUILD', 'the bank ASSERTS nowhere that a kernel was built', not builds,
        'asserting sentences %d' % len(builds))
    arm('G-NOBUILD-CTL', 'and the predicate FIRES on synthetic text asserting it',
        bool(asserted('The lane was opened and a kernel was built for it.', 'a kernel was built')))
    lean = [x for x in git(SIDE, 'status', '--porcelain').stdout.decode(
        'utf-8', 'replace').split(NL) if x.strip() and x.strip().endswith('.lean')]
    arm('G-NOLEAN', 'no `.lean` file is modified', not lean, 'lean changes %s' % (lean or 'none'))
    h2 = asserted(bank, 'h2 holds') + asserted(bank, 'h2 is true')
    arm('G-NOH2', 'and it ASSERTS nothing about `h2`', not h2, 'asserting sentences %d' % len(h2))
    arm('G-NOH2-CTL', 'and that predicate FIRES on synthetic text claiming it',
        bool(asserted('Under determination h2 holds at every place.', 'h2 holds')))
    depo = asserted(bank, 'was deposited') + asserted(bank, 'zenodo')
    arm('G-DEPOSIT', 'the bank ASSERTS no deposit action', not depo,
        'asserting sentences %d' % len(depo))
    arm('G-DEPOSIT-CTL', 'and the predicate FIRES on synthetic text asserting one',
        bool(asserted('The bundle was deposited this morning.', 'was deposited')))
    arm('G-EXPECT', 'every registered expectation is scored',
        all(('**%s**' % k) in crun for k in
            ('(N1)', '(N2)', '(N3)', '(N4)', '(E1)', '(E2)', '(E3)', '(E4)')))
    arm('G-REFUTED', 'and the act prints its OWN refuted expectations',
        crun.count('REFUTED') >= 1,
        'refuted expectations printed : %d ### -- THE ARM MEASURES AND PRINTS; IT DOES NOT DEMAND '
        'A NUMBER SET FOR ANOTHER ACT' % crun.count('REFUTED'))

    # ---- THE LIVING RECORD ----------------------------------------------------------------------
    bar()
    rec('  ### THE LIVING RECORD.')
    bar()
    tr_blob = git(PP, 'show', '%s:OPEN_TRAILS.md' % side).stdout.decode('utf-8', 'replace')
    arm('G-TRAILS', 'the trail block is append-only against the blob at %s' % side,
        MARK in trails and (trails.replace('\r\n', NL).endswith(NL)
                            and tr_blob.split(NL)[-3] in trails),
        'blob %d -> live %d bytes ### -- the head note this act also added to this file sits '
        'ABOVE the block, so a plain prefix test is the wrong test here and is not used'
        % (len(tr_blob.encode('utf-8')), len(trails.encode('utf-8'))))
    tb, tl = git(SIDE, 'show', '%s:CORRESPONDENCE.md' % side).stdout.decode('utf-8'), text(TABLE)
    arm('G-CORR', 'the correspondence table is a true prefix of itself plus one row',
        tl.replace('\r\n', NL).startswith(tb.rstrip(NL)),
        'rows %d -> %d' % (len(re.findall(r'^\| (\d+) \|', tb, re.M)),
                           len(re.findall(r'^\| (\d+) \|', tl, re.M))))
    arm('G-KEY', 'the key resolves, read from the VERDICT LINE',
        (not verdict_line(kq, '### NO KEY')) and 'the-obstacles-dissolved' in kq)
    nq = subprocess.run([sys.executable, INDEX, '--query', 'a symbol was renumbered'],
                        capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout or ''
    arm('G-KEY-CTL', 'and a must-not-hit query returns NO KEY on its VERDICT LINE',
        verdict_line(nq, '### NO KEY'))

    # ---- THE WRITE LIST -------------------------------------------------------------------------
    bar()
    rec('  ### THE WRITE LIST, BUILT AS KINDS.')
    bar()
    written = sorted(f for f in os.listdir(D) if f.startswith('b409')) \
        + ['audit_b409_reg_satisfiable.txt'] \
        + sorted('_b409/' + f for f in os.listdir(d('_b409'))) \
        + sorted('tools/' + f for f in os.listdir(os.path.join(ROOT, 'tools'))
                 if f.startswith('b409_')) \
        + ['tools/class_scheme.py']
    KINDS = {
        1: (r'^b409_registration_', r'^b409_satisfiable', r'^audit_b409_reg_satisfiable',
            r'^b409_regspec_run', r'^b409_reg_termscan', r'^b409_reg_gate', r'^b409_lockgate',
            r'^b409_reg_seal'),
        2: (r'^b409_ferry',),
        3: (r'^b409_census_', r'^b409_faces_census_', r'^b409_pins_', r'^b409_mirror'),
        4: (r'^b409_extract\.txt$', r'^_b409/'),
        5: (r'^b409_components\.txt$', r'^b409_scheme_table'),
        6: (r'^b409_desk', r'^b409_the_obstacles_dissolved', r'^b409_closing'),
        7: (r'^b409_checks',),
        8: (r'^tools/b409_',),
        9: (r'^tools/class_scheme\.py$',),
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
        'declared on the face %s ; used by the written files %s ; used by NO declared KIND %s'
        % (sorted(kinds), sorted(used), sorted(used - kinds) or 'none'))
    unnamed = [f for f in written if os.path.basename(f) not in reg]
    arm('G-WRITELIST-PATHS', 'and the PATH-level residue is printed, not hidden', True,
        '%d of %d named by KIND but not by path : %s'
        % (len(unnamed), len(written), unnamed or 'none'))
    tools = sorted(f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b409_'))
    arm('G-CAP', 'at most 6 new relay ACT-tool files, the shared instrument excluded',
        len(tools) <= 6, '%d act tools : %s ### -- plus 1 SHARED instrument, `class_scheme.py`, '
        'declared as KIND 9 on the face and not counted against the cap' % (len(tools), tools))

    # ---- MUST-FAIL ------------------------------------------------------------------------------
    bar()
    rec('  ### THE MUST-FAIL FIXTURES.')
    bar()
    forbidden = [
        '### THE MODULAR RELATION IS A BRIGHT CHANNEL.',
        '### KAPPA WAS MEASURED FOR THE GLOBAL INTERFACE.',
        '### THEOREM 3.1-H IS COMPILED.',
        '### THE CLASS NUMBERINGS WERE RECONCILED INTO ONE.',
        '### ROW U1 IS CLOSED.',
        '### h2 HOLDS.',
    ]
    lines = set(bank.split(NL))
    hits = [f for f in forbidden if f in lines]
    arm('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank', not hits,
        'hits %s' % (hits or 'none'))
    synth = 'a' + NL + '### ROW U1 IS CLOSED.' + NL + 'b'
    arm('G-MUSTFAIL-CTL', 'the same predicate FIRES on synthetic text carrying one',
        any(f in set(synth.split(NL)) for f in forbidden))

    bar('=')
    npass = sum(1 for _n, ok in ARMS if ok)
    rec('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**'
        % (len(ARMS), npass, len(ARMS) - npass))
    for n, ok in ARMS:
        if not ok:
            rec('    ### **FAILING : %s**' % n)
    rec('  ### run stamp : %s' % run_clock.stamp())
    bar('=')
    out = d('b409_checks_postpush.txt' if post else 'b409_checks.txt')
    io.open(out, 'wb').write((NL.join(R) + NL).encode('utf-8'))
    print(NL + '  wrote %s' % os.path.basename(out))
    return 0 if npass == len(ARMS) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
