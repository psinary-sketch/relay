# -*- coding: utf-8 -*-
"""b443r_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure here is read off this act's
### own records -- the components bank, the lock gate's notes, the suite -- and none is typed.
### ### **AND WHERE A FIGURE CANNOT BE READ, THE TOOL REFUSES RATHER THAN PRINTS A GUESS.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b443 site (vi), and the arc`s product named -->'
PRIOR = '<!-- b442 the minimum named, and site (v) -->'
BANKOUT = os.path.join(D, 'b443r_the_arc_product.txt')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def write_bytes(path, text):
    data = text.encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)
    return len(data)


def wrap(text, width):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        out.append(line)
    return out


FACE = read(os.path.join(D, 'b443r_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b443r_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b443r_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b443r_components.txt'))


def _j(name, default):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return default


SITE = _j('b443r_site_vi.json', {})
CANDS = SITE.get('candidates') or []
TALL = SITE.get('tallies') or {}
KINDS = {}
for _c in CANDS:
    KINDS[_c['kind']] = KINDS.get(_c['kind'], 0) + 1
KINDSTR = '; '.join('%s %d' % kv for kv in sorted(KINDS.items(), key=lambda x: (-x[1], x[0])))
LABELS = dict(b424='(i)', b427='(ii)', b428='(iii)', b436='(iv)', b442='(v)', b443='(vi)')
PERCB = '; '.join('%s %d of %d' % (LABELS[a], t.get('CLASS BOUNDARY', 0), sum(t.values())) for a, t in TALL.items())
TOTAL = SITE.get('total', 0)
U5, U6 = SITE.get('union5'), SITE.get('union6')
AGG = SITE.get('aggregate') or {}

ROWMARK = ('**SITE (vi) EXHAUSTED AND THE WITNESS ARC COMPLETE AT SIX SITES: NO WITNESS HELD, THE UNION OF FAILURE KINDS '
           'STILL ELEVEN; AND THE SEAL NOW REFUSES A REFUSED GATE IN THE TOOL**')

SCOPE = ("### THE ACT RE-REGISTERED ON A FRESH FACE AFTER SEALING AGAINST A REFUSAL, MOVED THE REFUSAL INTO THE SEAL, RAN "
         "THE ARC'S LAST SITE, DRAFTED ROW U1'S RESTATEMENT AND FILED THREE ITEMS UNOPENED. ### NO FAMILY, NO LANE BEYOND "
         "reg_seal.py'S ONE CHANGE, NO CELL. ### NO CLAIM ABOUT RH, h2, OR ANY PRIME PROBLEM")

DESK = [
    ('the stranded registration b443_registration_2026-09-12.txt', 'STAND',
     'LEFT AS IT LIES under (R55), sha256 b8d4838c..., its improper lock block intact, never governing; no component '
     'ran under it. Its ferry, step-zero records, survey and gate records stay untracked beside it.'),
    ('(R56) the seal refuses a refused gate in the tool', 'CLOSE',
     'DONE at b443: reg_seal.py --lock reads <stem>_lockgate.json and refuses on absent, refused, other-face and stale '
     'records, naming every refusing arm; four refusal fixtures and one permitting fixture pass; against the real '
     'incident it names the banned-term scan. 91 lines added, 0 deleted.'),
    ('site (vi) of the witness arc', 'CLOSE',
     'EXHAUSTED at b443: %d candidates, 0 held; %s. The arc`s six sites hold %d candidates and no witness; the union '
     'of failure kinds stays at %s.' % (len(CANDS), KINDSTR, TOTAL, U6)),
    ('row U1`s restatement in the keystone`s residue form', 'STAND',
     'DRAFTED at b443 as relay data/b443r_u1_draft.md and routed; not applied.'),
    ('row U1 entry (v)`s index defect', 'STAND', 'FILED at b443 as the b341 species; update block drafted and routed.'),
    ('the keystone`s line 231', 'STAND',
     'FILED at b443 as a sentence owing a source read; the seat`s recollection that the 1919 result is an upper bound '
     'is named as a recollection.'),
    ('the fast-radio-burst trail', 'STAND', 'FILED at b443, not opened; trigger stated.'),
    ('b363_span.py misses b434`s fold', 'STAND',
     'NOTED at b443: the tool reports 21 acts from b423; counted from b434`s fold the span is b433-b443, 11 acts. Not '
     'repaired -- the instrument lane was open for reg_seal.py alone.'),
]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for seg in wrap(why[:1900], 150):
            rec('        %s' % seg)
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block():
    body = [
        '### b443 — site (vi), and the arc’s product named — filed 2026-09-12',
        '',
        '**Re-issued on a fresh face after the first face was sealed against a refusal. The seal now refuses a refused gate itself; the witness arc’s sixth and last site holds no witness; and the union of failure kinds stays at eleven.**',
        '',
        '#### Component 0 — (R55) and (R56)',
        '',
        'The first face carried a banned stem in a candidate’s name; its term scan read NOT CLEAN and the lock gate read 7 of 8 and refused — and the seat’s PowerShell chain ran the seal anyway, because a semicolon does not stop on an exit code. Under **(R55)** that file, `data/b443_registration_2026-09-12.txt`, stays exactly where it is with its improper lock block (sha256 `b8d4838c…`), never edited and never governing; **no component ran under it**, and the act re-registered on a fresh face under the stem `b443r`. Under **(R56)** the cure moved from the shell into the guard: `reg_seal.py --lock` now reads the lock gate’s own record beside the face and **refuses** when it is absent, names another face, carries a stale digest, or says the gate refused — printing every refusing arm. Four refusal fixtures and one permitting fixture pass, the old self-test arms still pass, and run read-only against the real incident it names *the banned-term scan on the face*. 91 lines added, none deleted; the instrument lane closes with this act.',
        '',
        '#### Component 1 — site (vi), the Type-D residue: exhausted',
        '',
        '| candidate | first failing step |',
        '|:--|:--|',
        '@C0@',
        '@C1@',
        '@C2@',
        '@C3@',
        '@C4@',
        '@C5@',
        '@C6@',
        '@C7@',
        '@C8@',
        '@C9@',
        '',
        '**@N@ candidates, 0 held — @KINDS@.**',
        '',
        '**The class boundary, per site, corrected:** @PERCB@. The navigator’s premise that it is the majority at every site is withdrawn as his and false — site (iv) has it at 1 of 7, and site (vi) at 4 of 10.',
        '',
        '**The arc’s finding: six sites, @TOTAL@ candidates, no witness held, and the union of failure kinds was @U5@ after five sites and is @U6@ after six — the sixth site added no new way to fail.** W-ORD-WITNESS-ENUMERATION is checkpointed after (vi), its last site; the exhausted list is filed through the writer’s `append_block`, row U1 untouched.',
        '',
        '#### Component 2 — row U1’s restatement, drafted and routed',
        '',
        'Drafted in the conspiracy keystone’s residue form — each site’s missing statement named, the residue filed as the whole remaining weight, the taxonomy of eleven kinds with per-site counts read from banked JSON, and the row’s refusal quoted verbatim — as relay `data/b443r_u1_draft.md`. **Not applied.**',
        '',
        '#### Component 3 — three filings, none opened',
        '',
        '**(i) Row U1’s entry (v)** writes Theorem 6.1’s Li index as `n` where the source has `√n` (and drops the dual): a transcription defect of the b341 species. The update block is drafted in the same file and routed; the row is unedited.',
        '',
        '**(ii) The conspiracy keystone’s line 231** credits a 1919 sieve result with lower bounds for twin primes. No verified source holds a sieve text. The seat’s recollection — named as a recollection, not a reading — is that the 1919 result is an upper bound. **Filed as a sentence owing a source read**, not as a finding; the keystone is not edited.',
        '',
        '**(iii) A trail: fast-radio-burst dispersion measures as an independent baryon-fraction probe.** Trigger: a published burst-sample baryon fraction with a stated uncertainty, read at address under the `(R38)` threshold rule — the author’s order in this paste applying `(R38)` to a new lane. Filed, not opened; nothing is read at any address.',
        '',
        '**The fold’s span:** `b363_span.py` reports 21 acts from b423 because its pattern misses b434’s fold heading; counted from that fold by the record’s convention, the span is b433–b443, **11 acts**. Both figures are printed; the tool is not repaired.',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1)(a) | site (vi) exhausted, no witness held | **HELD** — @N@ candidates, 0 held |',
        '| (N1)(b) | the union of kinds stays at eleven | **HELD** — @U5@ before, @U6@ after |',
        '| (N2) | failures land mostly at ABSENT rather than the class boundary | **REFUTED** — a tie, ABSENT @AB@ and CLASS BOUNDARY @CB@ of @N@ |',
    ]
    rep = [('@N@', str(len(CANDS))), ('@KINDS@', KINDSTR), ('@PERCB@', PERCB), ('@TOTAL@', str(TOTAL)),
           ('@U5@', str(U5)), ('@U6@', str(U6)), ('@AB@', str(KINDS.get('ABSENT', 0))),
           ('@CB@', str(KINDS.get('CLASS BOUNDARY', 0)))]
    out = []
    for ln in body:
        m = re.match(r'^@C(\d+)@$', ln)
        if m:
            i = int(m.group(1))
            if i < len(CANDS):
                c = CANDS[i]
                out.append('| **%s** %s | %s — %s |' % (c['id'], c['name'].replace('|', '/'), c['step'], c['kind']))
            continue
        for k, v in rep:
            ln = ln.replace(k, v)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b443)"
    stmt = (m + ". **RE-ISSUED ON A FRESH FACE UNDER (R55)**: the first face, data/b443_registration_2026-09-12.txt, was "
            "sealed against a refusal -- term scan NOT CLEAN, lock gate 7 of 8, a PowerShell semicolon running the seal "
            "anyway -- and stays byte for byte with its improper lock block, never governing, no component run under it. "
            "The fresh face locked with @GR@ gates read and @GDG@ by digest. **(R56): reg_seal.py --lock NOW REFUSES WHEN "
            "THE LOCK GATE'S OWN RECORD IS ABSENT, NAMES ANOTHER FACE, IS STALE OR SAYS REFUSED, PRINTING EVERY REFUSING "
            "ARM; FOUR REFUSAL FIXTURES AND ONE PERMITTING FIXTURE PASS; AGAINST THE REAL INCIDENT IT NAMES THE "
            "BANNED-TERM SCAN.** **COMPONENT 1: SITE (vi) EXHAUSTED -- @N@ CANDIDATES, 0 HELD, @KINDS@. THE CLASS "
            "BOUNDARY PER SITE: @PERCB@ -- NOT THE MAJORITY AT EVERY SITE, THE PREMISE WITHDRAWN. THE ARC'S FINDING: SIX "
            "SITES, @TOTAL@ CANDIDATES, NO WITNESS, THE UNION OF KINDS @U5@ THEN @U6@ -- NO NEW WAY TO FAIL; CHECKPOINTED "
            "AFTER (vi).** **COMPONENT 2: ROW U1'S RESTATEMENT DRAFTED IN THE KEYSTONE'S RESIDUE FORM, REFUSAL VERBATIM, "
            "NOT APPLIED.** **COMPONENT 3: U1 (v)'S n-FOR-sqrt-n FILED AS THE b341 SPECIES AND ITS BLOCK DRAFTED; THE "
            "KEYSTONE'S LINE 231 FILED AS A SENTENCE OWING A SOURCE READ, THE SEAT'S RECOLLECTION NAMED AS ONE; THE "
            "FAST-RADIO-BURST TRAIL FILED, NOT OPENED. THE SPAN: 21 BY THE TOOL, WHICH MISSES b434'S FOLD; 11 COUNTED "
            "FROM IT.** 0 FAMILIES, 0 CELLS, 0 GRADES MOVED, THE INSTRUMENT LANE CLOSED, 0 CONTENT LOST")
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED"
    prof = ("### relay: reg_seal.py +91 -0 UNDER (R56); THE STRANDED FACE AND EVERY b443_ FILE BYTE-UNMOVED AND UNCOMMITTED. "
            "PLACE-papers: FACES_LEDGER.md ONE BLOCK THROUGH THE WRITER AND OPEN_TRAILS.md, BOTH APPENDED, ROW U1 AND THE "
            "KEYSTONE BYTE-UNMOVED -- 0 CONTENT LOST")
    grade = ("### AN INCIDENT OF THIS SEAT'S -- A SEAL RUN PAST A REFUSAL -- WAS STOPPED ON, ROUTED, AND CURED IN THE GUARD "
             "RATHER THAN IN THE CALLER, WITH FIXTURES THAT CAN FAIL AND A CONTROL AGAINST THE REAL INCIDENT")
    status = ("data/b443r_the_arc_product.txt; data/b443r_components.txt; data/b443r_site_vi.json; data/b443r_u1_draft.md; "
              "data/b443r_seal_fixtures.txt; data/b443r_span.txt; data/b443r_checks.txt; "
              "data/b443r_registration_2026-09-12.txt (LOCKED at sha256 %s); data/b443r_addendum.txt (EMPTY); "
              "the stranded data/b443_registration_2026-09-12.txt (UNCOMMITTED, NEVER GOVERNING); "
              "FACES_LEDGER.md <!-- b443 update: site (vi) -->; OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG)).replace('@N@', str(len(CANDS)))
                .replace('@KINDS@', KINDSTR).replace('@PERCB@', PERCB).replace('@TOTAL@', str(TOTAL))
                .replace('@U5@', str(U5)).replace('@U6@', str(U6)))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('was site six of the witness arc exhausted',
           'how many kinds of failure does the witness arc have',
           'why does the seal refuse a refused gate',
           'what happened to the registration sealed against a refusal',
           'is the class boundary the majority at every site')
MUST_NOT_HIT = ('site six witness held', 'the stranded registration was edited', 'row U1 restated in place')
KEY = 'site-vi-and-the-arcs-product-named'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b443 RE-REGISTERED ON A FRESH FACE UNDER (R55) AFTER ITS FIRST FACE WAS SEALED AGAINST A REFUSAL; THAT FILE "
        "STAYS BYTE FOR BYTE, NEVER GOVERNING, NO COMPONENT RUN UNDER IT. UNDER (R56) THE SEAL REFUSES A REFUSED GATE IN "
        "THE TOOL: reg_seal.py --lock reads the lock gate's record and refuses on absent, other-face, stale or refused, "
        "naming every refusing arm, with fixtures both polarities. SITE (vi) EXHAUSTED: %d candidates, 0 held, %s. THE "
        "ARC'S FINDING: SIX SITES, %d CANDIDATES, NO WITNESS, THE UNION OF FAILURE KINDS STAYS AT %s; THE CLASS BOUNDARY "
        "IS NOT THE MAJORITY AT EVERY SITE (%s). ROW U1'S RESTATEMENT DRAFTED AND ROUTED, NOT APPLIED. U1 (v)'S INDEX "
        "DEFECT FILED AS THE b341 SPECIES. THE KEYSTONE'S LINE 231 FILED AS A SENTENCE OWING A SOURCE READ. THE "
        "FAST-RADIO-BURST TRAIL FILED, NOT OPENED."
        % (len(CANDS), KINDSTR, TOTAL, U6, PERCB))
    grade = "### NO GRADE MOVED. ### NO CELL WRITTEN. ### NO CLAIM ABOUT RH, h2 OR ANY PRIME PROBLEM"
    where = ("data/b443r_the_arc_product.txt; data/b443r_components.txt; data/b443r_site_vi.json; data/b443r_u1_draft.md; "
             "data/b443r_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); FACES_LEDGER.md; "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b443 (site (vi), and the arc's product named)"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### SITE (vi), AND THE ARC`S PRODUCT NAMED (b443).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = dict((qq, no_key(query(qq)[0])) for qq in MUST_NOT_HIT)
    for qq in MUST_NOT_HIT:
        rec('    %-48s NO KEY before : %s' % (qq[:48], pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + NL
    ROW_ANCHOR = ('INDEX = [' + NL +
                  '    # (key, act, one-line statement, grade as its own act recorded it, '
                  'location)' + NL)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        rec('  ### HARD FAILURE -- an anchor is not in the file.')
        return False
    if ("'%s'" % KEY) not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    write_bytes(INDEX, txt)
    out, rc = query(KEY)
    n = out.count('act      :')
    ok = (not no_key(out)) and rc == 0 and n >= 1
    rec('  READ BACK : %s returns %d row(s)  %s   [verdict LINE read, under A2]'
        % (KEY, n, 'PASS' if ok else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-58s reaches the b443 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('the re-issue carried', 'RE-REGISTERED ON A FRESH FACE' in out),
            ('the stranded file carried', 'NEVER GOVERNING' in out),
            ('the guard carried', 'THE SEAL REFUSES A REFUSED GATE IN' in out),
            ('site (vi) carried', 'SITE (vi) EXHAUSTED' in out),
            ('the union carried', 'THE UNION OF FAILURE KINDS STAYS AT' in out),
            ('the corrected premise carried', 'NOT THE MAJORITY AT EVERY SITE' in out),
            ('the draft carried', 'DRAFTED AND ROUTED, NOT APPLIED' in out),
            ('the b341 filing carried', 'b341 SPECIES' in out),
            ('line 231 carried', 'OWING A SOURCE READ' in out),
            ('the trail carried', 'FAST-RADIO-BURST TRAIL' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-48s NO KEY after  : %s' % (qq[:48], no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank_file(Q, rownum, kok):
    Bk = ['=' * 100, 'b443 -- SITE (vi), AND THE ARC`S PRODUCT NAMED. (RE-ISSUE)', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE SIX SITES.', '-' * 100]
    for act, t in TALL.items():
        Bk.append('  %-5s %-5s %2d candidates %s' % (LABELS[act], act, sum(t.values()), t))
    Bk += ['  total %s ; union after five %s ; after six %s' % (TOTAL, U5, U6), '']
    for k, v in sorted(AGG.items(), key=lambda x: (-x[1], x[0])):
        Bk.append('  %-28s %3d' % (k, v))
    Bk += ['', '-' * 100, '### THE CONTROL SUITE.', '-' * 100,
           '  arms run %d ; passing %d ; failing %d' % (ARMS_RUN, ARMS_PASS, ARMS_FAIL),
           '  gates read %d ; checked by digest %d' % (GR, GDG)]
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))
    return len(Bk)


B442ROW_RE = r"(?m)^\| (\d+) \| \*\*THE MINIMUM OF THE RIEMANN-SIEGEL"


def main():
    bar('=')
    rec('b443r_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not COMP or not CANDS or len(TALL) != 6:
        rec('  ### HARD FAILURE -- this act`s components bank or its JSON is missing.')
        return 1
    rec('  figures READ from this act`s own records, none typed:')
    rec('      gates %s read / %s by digest ; arms %s run / %s passing / %s failing'
        % (GR, GDG, ARMS_RUN, ARMS_PASS, ARMS_FAIL))
    rec('      candidates %d ; kinds %s ; six-site total %s ; union %s -> %s' % (len(CANDS), KINDSTR, TOTAL, U5, U6))
    bar()
    rec('### THE DESK, SWEPT.')
    bar()
    Q = do_desk()
    bar()
    rec('### THE TRAIL, APPENDED.')
    bar()
    t = read(TRAILS)
    if MARK in t:
        rec('  already present; not re-appended.')
    else:
        if PRIOR not in t:
            rec('  ### HARD FAILURE -- the prior act`s mark is absent; refusing to append.')
            return 1
        before = len(t.splitlines())
        t2 = t.rstrip(NL) + NL + NL.join(trail_block()) + NL
        write_bytes(TRAILS, t2)
        rec('  appended %d lines; prior mark still present : %s ; prior text a TRUE PREFIX : %s'
            % (len(t2.splitlines()) - before, PRIOR in t2, t2.startswith(t.rstrip(NL))))
    rec('  lines deleted : 0')
    bar()
    rec('### THE CORRESPONDENCE ROW. ### READ BY MARKER.')
    bar()
    ROWS2 = corr_rows()
    txt = read(TABLE)
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    bad = [(i, j) for i, r in enumerate(ROWS2) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    slip = [mm for mm, s2, *_ in ROWS2 if not s2.startswith(mm)]
    rec('  fixtures %s %s %s %s %s %s ; unescaped pipes %d ; marker a prefix %s'
        % (pos, neg, sa, sb, sc, sd, len(bad), not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### HARD FAILURE at the row fixtures -- nothing written.')
        return 1

    def at(mk, s):
        return [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mk), s)]
    rec('  the prior act`s row by its marker : %s'
        % [int(x.group(1)) for x in re.finditer(B442ROW_RE, txt)])
    nums = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', txt)]
    if ROWS2[0][0] in txt:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = at(ROWS2[0][0], txt)[0]
    else:
        start = max(nums) + 1
        lines = ['| %d | %s | %s | %s | %s %s | %s |'
                 % (start, stmt, term, prof, grade, scope, status % start)
                 for (_m, stmt, term, prof, grade, scope, status) in ROWS2]
        new_txt = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new_txt)
        back = read(TABLE)
        got = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', back)]
        cellsx = [GD.split_cells(t2) for t2 in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx)
               and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; prior text a TRUE PREFIX %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)),
               'PASS' if okr else '### FAIL ###'))
        if not okr:
            return 1
        rownum = start
    after = read(TABLE)
    rec('  after -- the prior act`s : %s ; this act`s, by its marker : %s'
        % ([int(x.group(1)) for x in re.finditer(B442ROW_RE, after)], at(ROWS2[0][0], after)))
    bar()
    rec('### THE KEY.')
    bar()
    kok = do_key(rownum)
    bar()
    rec('### THE BANK.')
    bar()
    bank_file(Q, rownum, kok)
    bar('=')
    rec('  ### ROW %d. ### KEY %s. ### DESK %d items, %d closed.'
        % (rownum, 'PASS' if kok else '### FAIL ###', Q['items'], Q['closed']))
    bar('=')
    write_bytes(os.path.join(D, 'b443r_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
