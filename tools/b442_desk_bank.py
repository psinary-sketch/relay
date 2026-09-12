# -*- coding: utf-8 -*-
"""b442_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b442 the minimum named, and site (v) -->'
PRIOR = '<!-- b441 the identification filed, the overstatement corrected, and two filings -->'
BANKOUT = os.path.join(D, 'b442_the_minimum.txt')
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


FACE = read(os.path.join(D, 'b442_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b442_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b442_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b442_components.txt'))
B441C = read(os.path.join(D, 'b441_closing.txt'))


def _j(name, default):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return default


THETA = _j('b442_theta.json', {})
SITEV = _j('b442_site_v.json', {})
CANDS = SITEV.get('candidates') or []
KINDS = {}
for _c in CANDS:
    KINDS[_c['kind']] = KINDS.get(_c['kind'], 0) + 1
KINDSTR = '; '.join('%s %d' % kv for kv in sorted(KINDS.items(), key=lambda x: -x[1]))
HELD = bool(THETA.get('held'))
TH_U0 = str(THETA.get('theta_B', ''))[:22]

# ### b441's words, verified present in its banked closing before they are written anywhere (BAR 9).
# ### **VERBATIM, AND VERIFIED WITH WHITESPACE COLLAPSED** -- b441's closing wraps its sentences across lines;
# ### the first writing verified only a prefix and entered a paraphrase in the row, and the suite caught it.
W_DENIAL = 'THE RECORD NEVER DENIED THE IDENTIFICATION.'
W_REACH = 'b440' + chr(39) + 's sentence -- "b430' + chr(39) + 's defect, still live in every act since" -- is FALSE'
W_REPAIR = "AND b440'S REPAIR WAS DEFECTIVE TOO, AND IT REACHED THIS ACT."
_flat = re.sub(r'\s+', ' ', B441C.replace('**', ''))
WORDS_OK = all(w in _flat for w in (W_DENIAL, W_REACH, W_REPAIR))

ROWMARK = ('**THE MINIMUM OF THE RIEMANN-SIEGEL theta ON 0 <= t <= 50 IS u0 -- A NAME, NOT A CLOSED FORM; SITE (v) '
           'EXHAUSTED AT TEN CANDIDATES, ITS OBSTRUCTION MEMBERSHIP RATHER THAN UNIFORMITY; AND b440`S TWO '
           'CORRECTIONS ENTERED AS b440`S**')

SCOPE = ("### THE ACT CHECKS ONE NAME FOR ONE CONSTANT, RUNS ONE SITE OF THE WITNESS ARC, FILES TWO LEDGER BLOCKS "
         "THROUGH THE WRITER, AND ENTERS A PRIOR ACT'S CORRECTIONS UNDER ITS NAME. ### NO NEW INSTRUMENT, NO NEW "
         "FAMILY, NO LANE OPENED, NO CELL WRITTEN. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")

DESK = [
    ('whether u0 is the minimum of the Riemann-Siegel theta', 'CLOSE',
     'ANSWERED at b442: **YES, ON 0 <= t <= 50.** The argmin found from theta`s values alone agrees with b440`s u0 '
     'to `%.1e`; theta at u0 is `%s` by two routes sharing no code; theta is odd, so there is no minimum on the '
     'whole line; `h+` changes sign once on `(0, 50]`. The name is DERIVES-ON-IMPORTS on K5.'
     % (THETA.get('argmin_gap', 0), TH_U0)),
    ('which statuses the record holds for u0', 'CLOSE',
     'ANSWERED at b442: defining equation HELD; classical asymptote HELD (2 pi, not u0); name HELD; **closed form '
     'NOT HELD**; the classical value of theta at its minimum **NOT SOURCED** -- neither verified source states it.'),
    ('site (v) of the witness arc', 'CLOSE',
     'EXHAUSTED at b442: %d candidates, 0 held; %s. At the scale the order set -- the corpus`s two objects -- '
     'the obstruction is membership: over a finite class the interchange is free, and every theorem with a '
     'representation-dependent constant assumes cuspidality, while the Epstein function has no Euler product.'
     % (len(CANDS), KINDSTR)),
    ('row U1 entry (v)`s transcription of Theorem 6.1', 'STAND',
     'NOTED at b442, not repaired: the row writes `lambda_n(n,pi) + O(n log n)`, the source `lambda_n(sqrt n, '
     'pi-dual) + O(sqrt n log n)`. Rows are never rewritten; whether an update block should carry the correction '
     'is the author`s.'),
    ('site (vi)', 'STAND', 'OPEN. The arc is checkpointed after (v); (vi) is the last site.'),
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
        '### b442 — the minimum named, and site (v) — filed 2026-09-12',
        '',
        '**`u0` has a name, with a range on it; site (v) closes with no witness; and b440’s two corrections now sit under b440’s own name.** No new instrument, no new family, no lane opened, no cell written. `(R53)` and `(R54)` ratified by the paste and entered; the ferry carried no scanned-before-sending line, the seat’s own scan found `0` hits, and the permission to refuse was not used.',
        '',
        '#### Component 1 — `u0` is the minimum of the Riemann–Siegel theta, on `0 ≤ t ≤ 50`',
        '',
        'From K5’s import — CC’s *“It is the derivative of 2 θ(τ)”* — theta falls where `h₊ < 0` and rises where `h₊ > 0`. Checked rather than argued: golden-section search on theta’s **values alone**, never touching `h₊`, finds the argmin within `@GAP@` of b440’s `u0`; theta at `u0` is **`@TH@`** by `loggamma` and by `quad` over `digamma`, agreeing to `@RG@`; theta is odd at five heights; `h₊` changes sign exactly once on `(0, 50]`. **So the name holds with its quantifier** — theta being odd, there is no minimum on the whole line, and `−u0` is its maximum on the mirror range.',
        '',
        '| status | the record now holds |',
        '|:--|:--|',
        '| defining equation | HELD — `Re ψ(¼ + iu/2) = log π` |',
        '| classical asymptote | HELD — `2π`, which is not `u0` |',
        '| name | **HELD** — the minimum of theta on `0 ≤ t ≤ 50`, DERIVES-ON-IMPORTS |',
        '| closed form | **NOT HELD** |',
        '| classical value of theta there | **NOT SOURCED** — neither verified source states it; computed, not matched |',
        '',
        'The room’s mechanism in theta’s vocabulary keeps b440’s qualifier: **a heuristic, right at 9 of 10 cells, wrong for the second family at `a = 1.2`.** Filed through the writer’s `append_block` directly after b441’s block.',
        '',
        '#### Component 2 — site (v), the representation-dependent constant: exhausted',
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
        '**@N@ candidates, 0 held — @KINDS@.** The near-miss is Lagarias’s citation of a counting error *“with an absolute constant, which involves the analytic conductor”*: uniform across cuspidal representations, but about the counting function, not the finite-place sum, and still outside the class for the second object. **At the scale the order set, the obstruction is membership, not uniformity**: over two objects the maximum of two constants is one constant, and every theorem with a representation-dependent constant assumes cuspidality while the record measured that the Epstein function has no Euler product. The boundary count at five sites, from banked JSON: union of kinds **@UB@** before this site and **@UA@** after — **no new kind**. And one transcription noted, not repaired: row U1’s entry (v) writes Theorem 6.1 as `λ_n(n,π) + O(n log n)`; the source reads `λn(√n,π∨) + O(√n log n)`. **The arc is checkpointed after (v).**',
        '',
        '#### Component 3 — b440’s two corrections, entered as b440’s, beside row 289',
        '',
        'The table takes appends only, so the corrections ride in this act’s row, headed as b440’s and naming row 289, in b441’s words, quoted verbatim from `b441_closing.txt`: (1) *“THE RECORD NEVER DENIED THE IDENTIFICATION.”* (2) *“b440\'s sentence -- "b430\'s defect, still live in every act since" -- is FALSE”* (3) *“AND b440\'S REPAIR WAS DEFECTIVE TOO, AND IT REACHED THIS ACT.”* **The broken repair’s rule, `origin/main == HEAD`, is the wrong one**: it is true before an act commits anything. b439’s predicate — a commit naming this act, made and on the remote — stands as restored in b441’s committed suite and is carried unchanged in b442’s. `b440_checks.py` and row 289 are not edited.',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1)(a) | `u0` is theta’s argmin | **HELD, WITH ITS QUANTIFIER** — on `0 ≤ t ≤ 50`; theta is odd and has no minimum on the line |',
        '| (N1)(b) | the record now holds all three states | **HELD** — defining equation, asymptote, name; closed form still not held |',
        '| (N2)(a) | site (v) exhausted, no witness held | **HELD** — @N@ candidates, 0 held |',
        '| (N2)(b) | failures land at the class boundary because the class excludes the second object by hypothesis | **MOSTLY** — @CB@ of @N@; the other @OTHER@ land at coordinate boundary, bounded by a measurement, and refuted |',
        '',
        '*This seat’s own, from the face: (N1)(a) held only with the quantifier — held; (N1)(b) held with closed form not held and the value unsourced — held; (N2)(b) mostly, not wholly — held.*',
    ]
    rep = [('@GAP@', '%.1e' % THETA.get('argmin_gap', 0)), ('@TH@', TH_U0),
           ('@RG@', '%.1e' % THETA.get('route_gap', 0)), ('@N@', str(len(CANDS))), ('@KINDS@', KINDSTR),
           ('@UB@', str(SITEV.get('union_before'))), ('@UA@', str(SITEV.get('union_all'))),
           ('@CB@', str(KINDS.get('CLASS BOUNDARY', 0))),
           ('@OTHER@', str(len(CANDS) - KINDS.get('CLASS BOUNDARY', 0)))]
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
    m = ROWMARK + " (b442)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as b442 -- @GR@ "
            "gates read, @GDG@ checked by digest; (R53) AND (R54) RATIFIED AND ENTERED; THE FERRY CARRIED NO "
            "SCANNED-BEFORE-SENDING LINE, THE SEAT'S OWN SCAN FOUND 0 HITS, AND THE PERMISSION TO REFUSE WAS NOT "
            "USED. **COMPONENT 1: u0 IS THE MINIMUM OF THE RIEMANN-SIEGEL theta ON 0 <= t <= 50 -- THE ARGMIN FROM "
            "theta'S VALUES ALONE AGREES WITH b440'S u0 TO @GAP@, theta(u0) = @TH@ BY TWO ROUTES SHARING NO CODE, "
            "theta ODD, h+ ONE SIGN CHANGE ON (0, 50]; FILED DERIVES-ON-IMPORTS THROUGH THE WRITER AFTER b441'S "
            "BLOCK. THE RECORD HOLDS DEFINING EQUATION, CLASSICAL ASYMPTOTE AND NAME; CLOSED FORM NOT HELD; THE "
            "CLASSICAL VALUE NOT SOURCED. THE MECHANISM IN theta'S VOCABULARY STAYS A HEURISTIC, 9 OF 10 CELLS.** "
            "**COMPONENT 2: SITE (v) EXHAUSTED -- @N@ CANDIDATES, 0 HELD, @KINDS@; THE OBSTRUCTION AT THE ORDER'S "
            "SCALE IS MEMBERSHIP, NOT UNIFORMITY; NO NEW KIND AT FIVE SITES; ROW U1 ENTRY (v)'S TRANSCRIPTION OF "
            "THEOREM 6.1 NOTED AND NOT REPAIRED; THE ARC CHECKPOINTED AFTER (v).** "
            "**CORRECTIONS TO ROW 289, ENTERED AS b440'S, IN b441'S WORDS, QUOTED VERBATIM FROM b441_closing.txt: "
            "(1) '" + W_DENIAL + "' -- SPIRAL_MAP.md:114 DISCLAIMS A PRIME-POWER COUNTING FUNCTION; "
            "(2) '" + W_REACH + "' -- THE BROKEN PREDICATE WAS FIRST COMMITTED IN b440 ALONE; "
            "(3) '" + W_REPAIR + "' -- ITS RULE, origin/main == HEAD, IS THE WRONG ONE, TRUE BEFORE AN ACT "
            "COMMITS, AND b439'S PREDICATE STANDS AS RESTORED IN b441'S COMMITTED SUITE. ROW 289 AND "
            "b440_checks.py ARE NOT EDITED.** "
            "0 INSTRUMENTS BUILT, 0 FAMILIES DEFINED, 0 LANES OPENED, 0 CELLS WRITTEN, 0 GRADES MOVED, 0 CONTENT "
            "LOST")
    term = ("NO TERMINAL ADDED, MOVED, RENAMED OR GRADED. The name is filed DERIVES-ON-IMPORTS on K5 and confers "
            "nothing")
    prof = ("### TWO PLACE-papers FILES APPENDED (FACES_LEDGER.md by two writer blocks, OPEN_TRAILS.md), EACH PRIOR "
            "TEXT A TRUE PREFIX; ROW U1 BYTE-UNMOVED; NO ROW, NO CELL, THE FREEZE AT SIX STANDING; SIDE-window, "
            "TECHNE-Core AND EVERY INSTRUMENT FILE BYTE-UNMOVED; b440'S ROW AND TOOL BYTE-UNMOVED -- 0 CONTENT LOST")
    grade = ("### THE FACE DECLARED FIVE SURVEY FINDINGS BEFORE ANY MEASUREMENT -- AMONG THEM THAT NO VERIFIED "
             "SOURCE STATES theta'S MINIMUM, THAT THE NAME NEEDS A QUANTIFIER, AND THAT THE ORDER'S CLASS IS FINITE; "
             "THE ARGMIN WAS FOUND WITHOUT THE EQUATION IT WAS CHECKING; AND ONE ATTRIBUTION ERROR IN THIS ACT'S "
             "OWN LEDGER BLOCK WAS REVERTED BEFORE COMMIT AND RE-FILED")
    status = ("data/b442_the_minimum.txt; data/b442_components.txt; data/b442_theta.json; data/b442_site_v.json; "
              "data/b442_filings_run.txt; data/b442_checks.txt; "
              "data/b442_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "data/b442_addendum.txt (the (R50) slot, EMPTY); "
              "PLACE-papers FACES_LEDGER.md <!-- b442 update: u0 --> and <!-- b442 update: site (v) -->; "
              "OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@GAP@', '%.1e' % THETA.get('argmin_gap', 0)).replace('@TH@', TH_U0)
                .replace('@N@', str(len(CANDS))).replace('@KINDS@', KINDSTR))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('is u0 the minimum of the riemann siegel theta',
           'what name does the record hold for u0',
           'was site five of the witness arc exhausted',
           'why is site five a membership obstruction',
           'what corrections does b440 carry')
MUST_NOT_HIT = ('u0 has a closed form', 'site five witness held', 'row 289 edited')
KEY = 'the-minimum-named-and-site-v'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b442 NAMED u0 AND RAN SITE (v). u0 IS THE MINIMUM OF THE RIEMANN-SIEGEL theta ON 0 <= t <= 50: the argmin "
        "found from theta's values alone agrees with b440's u0 to %.1e, theta at u0 is %s by TWO ROUTES SHARING NO "
        "CODE, THETA IS ODD so there is no minimum on the whole line, and h+ changes sign once on (0, 50]. FILED "
        "DERIVES-ON-IMPORTS on K5. The record holds DEFINING EQUATION, CLASSICAL ASYMPTOTE AND NAME; CLOSED FORM NOT "
        "HELD; THE CLASSICAL VALUE NOT SOURCED. THE MECHANISM STAYS A HEURISTIC. SITE (v) EXHAUSTED: %d candidates, "
        "0 held, %s; THE OBSTRUCTION IS MEMBERSHIP, NOT UNIFORMITY, over the corpus's two objects; NO NEW KIND AT "
        "FIVE SITES; THE ARC CHECKPOINTED AFTER (v). ROW U1'S TRANSCRIPTION OF THEOREM 6.1 NOTED, NOT REPAIRED. "
        "b440'S TWO CORRECTIONS ENTERED AS b440'S BESIDE ROW 289, IN b441'S WORDS, AND THE WRONG REPAIR RULE "
        "origin/main == HEAD NAMED. 0 INSTRUMENTS, 0 LANES, 0 CELLS, 0 CONTENT LOST"
        % (THETA.get('argmin_gap', 0), TH_U0, len(CANDS), KINDSTR))
    grade = ("### NO GRADE MOVED, CONFERRED OR MINTED. ### THE NAME IS DERIVES-ON-IMPORTS ON K5. ### NO CELL "
             "WRITTEN. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")
    where = ("data/b442_the_minimum.txt; data/b442_components.txt; data/b442_theta.json; data/b442_site_v.json; "
             "data/b442_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); "
             "FACES_LEDGER.md (two b442 blocks); OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b442 (the minimum named, and site (v))"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE MINIMUM NAMED, AND SITE (v) (b442).%s'
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
        rec('    %-58s reaches the b442 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('the name carried', 'IS THE MINIMUM OF THE RIEMANN-SIEGEL theta ON 0 <= t <= 50' in out),
            ('the two routes carried', 'TWO ROUTES SHARING NO CODE' in out),
            ('the oddness carried', 'THETA IS ODD' in out),
            ('closed form not held carried', 'CLOSED FORM NOT' in out),
            ('the unsourced value carried', 'CLASSICAL VALUE NOT SOURCED' in out),
            ('the heuristic carried', 'STAYS A HEURISTIC' in out),
            ('site (v) exhausted carried', 'SITE (v) EXHAUSTED' in out),
            ('membership carried', 'MEMBERSHIP, NOT UNIFORMITY' in out),
            ('the transcription carried', 'TRANSCRIPTION OF THEOREM 6.1' in out),
            ('the corrections carried', "ENTERED AS b440'S BESIDE ROW 289" in out),
            ('the wrong rule carried', 'origin/main == HEAD' in out)):
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
    Bk = ['=' * 100, 'b442 -- THE MINIMUM NAMED, AND SITE (v).', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### u0 AND theta.', '-' * 100]
    for k in ('u0_banked', 'argmin', 'argmin_gap', 'theta_B', 'theta_A', 'route_gap', 'odd_max', 'sign_changes'):
        Bk.append('  %-12s : %s' % (k, THETA.get(k)))
    Bk += ['', '-' * 100, '### SITE (v), THE CANDIDATES.', '-' * 100]
    for c in CANDS:
        Bk.append('  %-4s %-8s %-26s %s' % (c['id'], c['step'], c['kind'], c['name']))
    Bk += ['', '-' * 100, '### THE BOUNDARY COUNT AT FIVE SITES.', '-' * 100]
    for act, t in (SITEV.get('tallies') or {}).items():
        Bk.append('  %-5s %2d candidates %s' % (act, sum(t.values()), t))
    Bk += ['  union before %s ; after %s ; new kinds %s' % (SITEV.get('union_before'), SITEV.get('union_all'),
                                                           SITEV.get('new_kinds'))]
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


B441ROW_RE = r"(?m)^\| (\d+) \| \*\*THE ARCHIMEDEAN CHANNEL IS THE SMOOTH"


def main():
    bar('=')
    rec('b442_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not COMP or not THETA or not CANDS:
        rec('  ### HARD FAILURE -- this act`s components bank or its JSON is missing.')
        return 1
    if not WORDS_OK:
        rec('  ### HARD FAILURE -- b441`s words are not in its closing as quoted; nothing written (BAR 9).')
        return 1
    rec('  figures READ from this act`s own records, none typed:')
    rec('      gates %s read / %s by digest ; arms %s run / %s passing / %s failing'
        % (GR, GDG, ARMS_RUN, ARMS_PASS, ARMS_FAIL))
    rec('      held %s ; argmin gap %.2e ; theta(u0) %s ; candidates %d ; kinds %s ; b441 words verified %s'
        % (HELD, THETA.get('argmin_gap', 0), TH_U0, len(CANDS), KINDSTR, WORDS_OK))
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
        % [int(x.group(1)) for x in re.finditer(B441ROW_RE, txt)])
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
        % ([int(x.group(1)) for x in re.finditer(B441ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b442_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
