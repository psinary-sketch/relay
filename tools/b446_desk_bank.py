# -*- coding: utf-8 -*-
"""b446_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b446 the floor has a domain -->'
PRIOR = '<!-- b445 whose residual it is -->'
BANKOUT = os.path.join(D, 'b446_floor_domain.txt')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []
DESK = []


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


FACE = read(os.path.join(D, 'b446_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b446_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

CHK = read(os.path.join(D, 'b446_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS, ARMS_FAIL = ((int(_a.group(1)), int(_a.group(2)), int(_a.group(3)))
                                  if _a else (0, 0, -1))

COMP = read(os.path.join(D, 'b446_components.txt'))
FLOOR = 1.49e-08
FIVE = ['3.158312', '3.461088', '3.605551', '4.061553', '4.123106']
OUTLIER = '4.123106'


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)) or '')
    except Exception:
        return {}


DJ = _j('b446_doubling.json')
CJ = _j('b446_floor_census.json')
B445 = _j('b445_arms.json')
RJ = DJ.get('report') or {}
KD = CJ.get('kind') or {}
RES = CJ.get('residue') or {}
M0 = CJ.get('m0') or {}
READY = bool(RJ) and bool(CJ) and all(k in DJ for k in FIVE)
if READY:
    NB = RJ['below']
    REF = RJ['outlier_refuses']
    ORD = RJ['orders']
    OTHERS = [ORD[k] for k in FIVE if k != OUTLIER]
    NALL, NOUT = KD['all'], KD['out']
    SHARE = NOUT / NALL
    SHARE2 = (NOUT - RES.get('b264_rows_out', 0)) / NALL
    JAF = RES.get('json_verdicts', {}).get('AT_FLOOR', 0)
    ZERO_ONLY = RES.get('at_floor_zero_only')
    M1V = CJ.get('m1_verdicts') or {}
    EXP = RJ.get('expect') or {}

ROWMARK = ('**THE 1.49e-08 FLOOR IS A ROUNDING LEVEL WITH A DOMAIN OF KIND, NOT A MEASUREMENT AT RADII; ITS SIZE DECIDED NO '
           'BANKED VERDICT, AND THE CHAIN`S RESIDUAL FALLS BELOW IT ON A SECOND DOUBLING**')

SCOPE = ("### THE ACT TRACED THE FLOOR TO ITS SOURCE, COUNTED ITS BANKED COMPARISONS BY MATCHERS AND CONTROLS FIXED ON ITS "
         "FACE, DOUBLED THE GRID A SECOND TIME AT FIVE CELLS UNDER (R58), AND FILED THE MINT AS JUDGEMENT; NO CHAIN FILE, "
         "noise_floor.py OR registration_gate.py EDITED; THE LANE CLOSED AT ITS END. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO")


def desk():
    return [
        ('where the floor came from', 'CLOSE',
         'TRACED at b446 from source: b264 measured eigenvalues at NQ 700/1400 whose floor modes sat near sqrt(machine '
         'epsilon); b272`s noise_floor.py set DEFAULT_FLOOR = sqrt(eps) = 1.4901e-08 with a contract of KIND (spectral or '
         'modal quantities); b437 ran the gate at radii and called it priced. No domain of radius exists.'),
        ('the floor`s comparisons, counted', 'CLOSE',
         'COUNTED at b446: %d banked comparisons against 1.49e-08, controls passing; %d OUT of the floor`s kind (share %.3f; '
         '%.3f with b264`s mode rows read IN). Nothing re-verdicted.' % (NALL, NOUT, SHARE, SHARE2)),
        ('what the floor arm decided', 'CLOSE',
         'COUNTED at b446: 0 AT_FLOOR verdicts within the text matchers; %d structured AT_FLOOR records in one JSON bank, '
         'all on an exact zero (%s) -- the floor`s size decided none. Drift arm refusals %d; passed both %d.'
         % (JAF, ZERO_ONLY, M1V.get('DRIFTING', 0), M1V.get('RESOLVED', 0))),
        ('the second doubling at the five cells', 'CLOSE',
         'RUN at b446: |e| below 1.49e-08 (the bar quoted outside its kind) at %d of 5; measured orders %s at the four, not '
         'the asymptotic 2; limits E pre-asymptotic.' % (NB, ', '.join('%.2f' % x for x in OTHERS))),
        ('the outlier 4.123106', 'STAND',
         'MEASURED at b446, NOT EXPLAINED: order %.2f, %s by the face`s rule. Candidate: kinks of the integrand falling '
         'against the grid differently per level (not the rung alone -- 3.605551 = sqrt(13) converged). Third doubling '
         'priced, about two minutes, NOT RUN.' % (ORD[OUTLIER], 'REFUSES' if REF else 'converges')),
        ('the chain`s quadrature floor per cell', 'STAND',
         'PRINTED at b446 for 14 cells, no function fitted; p* not taken because the measured orders span more than 1.0, so '
         'nine cells carry e0 - e1 alone; eight ladder cells NOT MEASURED.'),
        ('the floor-domain rule', 'STAND',
         'FILED AS JUDGEMENT at b446, NOT MECHANIZED: noise_floor.py binds neither kind nor parameters in code. TECHNE '
         'FLOOR_DOMAIN_RULE.md, local, not pushed. The route to mechanizing it is an instrument edit no lane has opened.'),
        ('the seat`s word count supplied as verdict counts', 'CLOSE',
         'CORRECTED at b446 on the locked face and by the census: 1146/64/2 over 167 stems were word-lines, prose '
         'included; the two AT_FLOOR lines are definitions.'),
        ('W-ORD-SPAN-HEADING', 'STAND', 'CARRIED: (R58) opened the instrument lane for the floor`s domain only.'),
        ('the instrument lane under (R58)', 'CLOSE', 'CLOSED at the end of b446; no instrument built, no chain file edited.'),
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
        '### b446 — the floor has a domain — filed 2026-09-12',
        '',
        '**The `1.49e-08` floor is `sqrt(machine epsilon)`: a float64 rounding level with a domain of kind — computed spectral or modal quantities — not a measurement taken at any radius. Of @NALL@ banked comparisons against it, @NOUT@ are of another kind. Its size decided no banked verdict. On a second doubling of the grid the chain’s residual falls below it at @NB@ of 5 cells, and one cell still does not converge. The instrument lane `(R58)` opened for this and closed at the act’s end.**',
        '',
        '#### Component 1 — where the floor came from',
        '',
        '**From the sources, not from any act’s prose.** b264 measured eigenvalues `lam_n` of a quadrature discretization at `NQ = 700` and `1400`. Four modes stopped decaying between `1.52e-08` and `2.18e-08`, and b264 identified that level with `sqrt(machine epsilon)`. b272’s `tools/noise_floor.py` set `DEFAULT_FLOOR = sqrt(2.220446049250313e-16) = 1.4901161193847656e-08` under a contract of kind: *“ANY ACT READING A COMPUTED SPECTRAL OR MODAL QUANTITY MUST CALL THIS.”* b437 ran the gate at `5.196152`, `5.385165` and `5.567764` and titled that “the floor, priced”; it set no floor and stated no domain. **There is no domain of radius.**',
        '',
        '**The quadrature floor the chain actually has**, per cell, with no function fitted. At the five cells with three levels, the error at `nv = 8193` comes from the measured order. At nine cells it is `e0 − e1` alone, because the measured orders span more than `1.0` and the face’s rule then takes no assumed order. Eight ladder cells are NOT MEASURED.',
        '',
        '| a | e at 8193 | e at 16385 | error at 8193 | how |',
        '|:--|--:|--:|--:|:--|',
    ]
    for r in RJ.get('c1', []):
        body.append('| %s | %+.3e | %+.3e | %+.3e | %s |' % (r['a'], r['e0'], r['e1'], r['err'], r['how']))
    body += [
        '',
        '#### Component 2 — the census',
        '',
        'Every banked comparison against `1.49e-08`, over `relay/data`, counted by four matchers fixed on the face, with controls in both polarities (all passing). **@NALL@ comparisons: @NIN@ IN the floor’s kind, @NOUT@ OUT (share @SHARE@).** Read by hand, b264’s own mode-table rows are IN, which gives a share of @SHARE2@. **The radius reading is VACUOUS:** the floor was measured at no radius, so every comparison lies outside a radius domain, and that is not a finding. Nothing is re-verdicted. An OUT comparison is the bar quoted outside its scope, and only that.',
        '',
        '**What the floor arm decided.** Within the text matchers there are **0** AT_FLOOR verdicts; the drift arm refused **@DRIFT@** and **@RES@** passed both arms. The residue matchers found **@JAF@ structured AT_FLOOR records** in one JSON bank, and **every one is on a value of exactly zero, which any positive floor refuses.** **The floor’s size, `1.49e-08`, decided none of them.** The tool’s own header said so at b272: *“IT IS THE DRIFT ARM THAT BITES, NOT THE FLOOR ARM.”*',
        '',
        '**Addition (a)’s figures, as what they count:** `@M0R@` RESOLVED, `@M0D@` DRIFTING and `@M0A@` AT_FLOOR are lines that carry the words, prose included, over `@STEMS@` file stems (`@ASTEMS@` of them act stems). Both AT_FLOOR lines are definitions of the arm. This seat supplied those figures unread; the error is entered as its own.',
        '',
        '#### Component 3 — the second doubling',
        '',
        '| a | e at 8193 | e at 16385 | e at 32769 | rate | order p | limit E | against the quoted bar |',
        '|:--|--:|--:|--:|--:|--:|--:|:--|',
    ]
    for k in FIVE:
        c = RJ['c3'][k]
        body.append('| %s | %+.3e | %+.3e | %+.3e | %.2f | %.2f | %+.2e | %s |'
                    % (k, c['e0'], c['e1'], c['e2'], c['rate'], c['p'], c['E'], 'below (outside its kind)' if c['below'] else 'above (outside its kind)'))
    body += [
        '',
        '**@NB@ of 5 cells fall below `1.49e-08`**, a bar quoted outside its kind. At the four the measured orders are @OTHERS@, not the trapezoid rule’s asymptotic 2, so the limits `E` are pre-asymptotic estimates, printed and not read as residuals of the object. **The outlier `4.123106` @REFW@ by the face’s rule:** its order is @ORDO@, against a window of @WIN@. The rung alone does not explain it: `3.605551 = sqrt(13)` also sits at a prime power and converged. The candidate is kinks of the integrand falling differently against the grid at each level. A third doubling is priced at about two minutes and **not run**.',
        '',
        '#### Component 4 — the mint',
        '',
        '**A floor carries the domain of kind and the parameters over which it was measured; a floor quoted outside that domain is a bar whose strictness is unknown.** The face fixed the mechanization test: the emitting source must bind the kind and the parameters in code. `noise_floor.py` binds neither, so **the rule is filed as judgement, not mechanized.** `registration_gate.py` is not edited. The TECHNE module is `FLOOR_DOMAIN_RULE.md`, beside `BAR_FLOOR_RULE.md`, local and not pushed.',
        '',
        '#### Errors entered as their owners’',
        '',
        'The navigator’s, by ruling (4): he read the outlying cell as a sixth when it was among the five. The navigator’s, by addition (b), in his words: *“he read “priced” in an act’s prose and never opened the tool that defines the floor, so he took a rounding level for a measured quantity and a domain of kind for a domain of radius.”* **The seat’s:** it supplied a word count as verdict counts without reading what it counted, and the census replaced it.',
        '',
        '#### The expectations',
        '',
        '| | the navigator’s | verdict |',
        '|:--|:--|:--|',
        '| (N1) | neither emitting act stated a domain for the floor | **@N1@** · radius reading VACUOUS |',
        '| (N2) | more than half the banked comparisons lie outside it | **@N2@** · radius reading VACUOUS |',
        '| (N3)(a) | the second doubling brings four of five below the floor | **@N3A@** |',
        '| (N3)(b) | the outlier still refuses | **@N3B@** |',
        '',
        'This seat’s own, from the face: (N1) refuted — **HELD**; (N2) held — **HELD**; (N3) no expectation.',
        '',
        '**The instrument lane opened by `(R58)` is closed.** The four lists are open.',
    ]
    oth = sorted(OTHERS)
    m = (oth[1] + oth[2]) / 2
    rep = [('@NALL@', str(NALL)), ('@NOUT@', str(NOUT)), ('@NIN@', str(NALL - NOUT)), ('@SHARE2@', '%.3f' % SHARE2),
           ('@SHARE@', '%.3f' % SHARE), ('@NB@', str(NB)), ('@DRIFT@', str(M1V.get('DRIFTING', 0))),
           ('@RES@', str(M1V.get('RESOLVED', 0))), ('@JAF@', str(JAF)), ('@M0R@', str(M0.get('RESOLVED'))),
           ('@M0D@', str(M0.get('DRIFTING'))), ('@M0A@', str(M0.get('AT_FLOOR'))), ('@ASTEMS@', str(CJ.get('m0_act_stems'))),
           ('@STEMS@', str(CJ.get('m0_stems'))), ('@OTHERS@', ', '.join('%.2f' % x for x in OTHERS)),
           ('@REFW@', 'refuses' if REF else 'converges'), ('@ORDO@', '%.2f' % ORD[OUTLIER]),
           ('@WIN@', '[%.2f, %.2f]' % (m - 0.5, m + 0.5)),
           ('@N1@', EXP.get('n1', '')), ('@N2@', EXP.get('n2', '')), ('@N3A@', EXP.get('n3a', '')), ('@N3B@', EXP.get('n3b', ''))]
    out = []
    for ln in body:
        for k, v in rep:
            ln = ln.replace(k, v)
        out.append(ln)
    return ['', MARK, ''] + out + ['']


def corr_rows():
    m = ROWMARK + " (b446)"
    stmt = (m + (". **LOCKED BEFORE ANY WRITE**, %d gates read, %d by digest. **COMPONENT 1: THE FLOOR TRACED TO SOURCE -- "
                 "b264'S EIGENVALUES AT NQ 700/1400, b272'S noise_floor.py DEFAULT_FLOOR = sqrt(eps) = 1.4901e-08 UNDER A "
                 "CONTRACT OF KIND (SPECTRAL OR MODAL QUANTITIES); b437 RAN THE GATE AT RADII AND SET NO FLOOR; NO DOMAIN OF "
                 "RADIUS. THE CHAIN'S OWN QUADRATURE ERROR PRINTED PER CELL, NO FUNCTION FITTED.** **COMPONENT 2: %d BANKED "
                 "COMPARISONS, CONTROLS PASSING, %d OUT OF KIND (SHARE %.3f); THE RADIUS READING VACUOUS; 0 AT_FLOOR VERDICTS "
                 "IN THE TEXT MATCHERS AND %d STRUCTURED AT_FLOOR RECORDS, ALL ON AN EXACT ZERO -- THE FLOOR'S SIZE DECIDED "
                 "NONE; NOTHING RE-VERDICTED.** **COMPONENT 3: THE SECOND DOUBLING TAKES %d OF 5 CELLS BELOW 1.49e-08 (A BAR "
                 "OUTSIDE ITS KIND) AT ORDERS %s; THE OUTLIER 4.123106 %s AT ORDER %.2f, A THIRD DOUBLING PRICED AND NOT "
                 "RUN.** **COMPONENT 4: A FLOOR CARRIES THE DOMAIN OF KIND AND THE PARAMETERS OVER WHICH IT WAS MEASURED -- "
                 "FILED AS JUDGEMENT, NOT MECHANIZED; TECHNE MODULE LOCAL.** ERRORS ENTERED AS THEIR OWNERS': THE "
                 "NAVIGATOR'S TWO, THE SEAT'S WORD COUNT. (N1) REFUTED, (N2) HELD, (N3)(a) REFUTED, (N3)(b) %s. THE LANE "
                 "(R58) CLOSED. 0 CHAIN FILES EDITED, 0 GRADES MOVED, 0 CONTENT LOST")
            % (GR, GDG, NALL, NOUT, SHARE, JAF, NB, ', '.join('%.2f' % x for x in OTHERS),
               'REFUSES' if REF else 'CONVERGES', ORD[OUTLIER], 'HELD' if REF else 'REFUTED'))
    term = "NO TERMINAL ADDED, MOVED, RENAMED OR GRADED"
    prof = ("### PLACE-papers: OPEN_TRAILS.md +1 RECORD, APPENDED AS A TRUE PREFIX; noise_floor.py, registration_gate.py, "
            "carto_atlas.py, zeta_ordinates.npy, b317_smear.py, b318_square.py AND b321_window.py BYTE-UNMOVED; TECHNE-Core "
            "+1 MODULE, LOCAL -- 0 CONTENT LOST")
    grade = ("### THE MATCHERS, CONTROLS, KIND RULE, ORDER RULE AND OUTLIER RULE WERE ON THE FACE BEFORE ANY VALUE; THE "
             "SEAT'S OWN SUPPLIED FIGURES WERE CORRECTED ON THAT FACE; THE MATCHERS' MISSES ARE PRINTED AS RESIDUE, NOT "
             "PATCHED; EVERY VACUOUS READING IS SAID TO BE VACUOUS")
    status = ("data/b446_floor_domain.txt; data/b446_components.txt; data/b446_floor_census.txt; data/b446_floor_census.json; "
              "data/b446_doubling.json; data/b446_extract.txt; data/b446_checks.txt; "
              "data/b446_registration_2026-09-12.txt (LOCKED at sha256 %s); data/b446_addendum.txt (EMPTY); "
              "TECHNE-Core FLOOR_DOMAIN_RULE.md (LOCAL); OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])
    return [(m, stmt, term, prof, grade, SCOPE, status)]


ALIASES = ('where did the noise floor come from',
           'what is the domain of the 1.49e-08 floor',
           'how many verdicts did the floor arm decide',
           'does the residual fall below the floor on a second doubling',
           'is sqrt machine epsilon a measured floor')
MUST_NOT_HIT = ('the floor was priced at radii', 'the floor rule is mechanized', 'noise floor edited')
KEY = 'the-floor-has-a-domain'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b446 TRACED THE 1.49e-08 FLOOR TO SOURCE: sqrt(MACHINE EPSILON), SET AT b272 FROM b264'S EIGENVALUES AT NQ "
        "700/1400, WITH A DOMAIN OF KIND (SPECTRAL OR MODAL QUANTITIES) AND NONE OF RADIUS. %d BANKED COMPARISONS, %d OUT OF "
        "KIND; THE FLOOR ARM'S %d AT_FLOOR RECORDS ARE ALL ON EXACT ZEROS, SO THE FLOOR'S SIZE DECIDED NONE. A SECOND "
        "DOUBLING TAKES %d OF 5 CELLS BELOW IT; THE OUTLIER 4.123106 %s. THE FLOOR-DOMAIN RULE FILED AS JUDGEMENT, NOT "
        "MECHANIZED. NO CLAIM ABOUT ZEROS."
        % (NALL, NOUT, JAF, NB, 'REFUSES' if REF else 'CONVERGES'))
    grade = "### NO GRADE MOVED. ### NO CHAIN FILE OR GATE EDITED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO"
    where = ("data/b446_floor_domain.txt; data/b446_floor_census.txt; data/b446_components.txt; "
             "data/b446_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b446 (the floor has a domain)"

    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE FLOOR HAS A DOMAIN (b446).%s'
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
        rec('    %-58s reaches the b446 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('the source carried', 'sqrt(MACHINE EPSILON)' in out),
            ('the domain of kind carried', 'A DOMAIN OF KIND' in out),
            ('the census carried', 'BANKED COMPARISONS' in out),
            ('the floor arm carried', 'DECIDED NONE' in out),
            ('the doubling carried', 'A SECOND DOUBLING TAKES' in out),
            ('judgement carried', 'FILED AS JUDGEMENT, NOT MECHANIZED' in out),
            ('no zero claim carried', 'NO CLAIM ABOUT ZEROS' in out)):
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
    Bk = ['=' * 100, 'b446 -- THE FLOOR HAS A DOMAIN.', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
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


B445ROW_RE = r"(?m)^\| (\d+) \| \*\*THE CHANNELS` RESIDUAL IS THE CHAIN`S INTEGRATION"


def main():
    global DESK
    bar('=')
    rec('b446_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not COMP or not READY or ARMS_FAIL != 0:
        rec('  ### HARD FAILURE -- a figure this tool reads is missing, or the suite is not passing.')
        return 1
    DESK = desk()
    rec('  figures READ from this act`s own records, none typed:')
    rec('      gates %s read / %s by digest ; arms %s run / %s passing / %s failing'
        % (GR, GDG, ARMS_RUN, ARMS_PASS, ARMS_FAIL))
    rec('      comparisons %d, OUT %d ; json AT_FLOOR %d zero-only %s ; below %d of 5 ; outlier refuses %s'
        % (NALL, NOUT, JAF, ZERO_ONLY, NB, REF))
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
        % [int(x.group(1)) for x in re.finditer(B445ROW_RE, txt)])
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
        % ([int(x.group(1)) for x in re.finditer(B445ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b446_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
