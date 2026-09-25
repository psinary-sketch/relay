# -*- coding: utf-8 -*-
"""b516_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b515's AND RE-POINTED ARM BY ARM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### The kernel arms read the kernel's own tree and git state, and Lean's own output in the run files.
"""
import io
import glob
import hashlib
import fnmatch
import json
import math
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
FACE = os.path.join(D, 'b516_registration_2026-09-24.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = '879834b6'      # ### b515's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '0a9391e'           # ### the kernel's tip, untouched by this act
PRIOR_PP = '4d3a6d6'           # ### b515's PLACE-papers commit
FIND = os.path.join(PP, 'FINDINGS.md')
DIG = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b516 —'
GRADE_RE = re.compile(r'\b(DERIVES|INTERFACES|SHELL|ENCODES-CONCLUSION|ENCODES)\b')


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


def line_with(text, needle):
    """### **A2.** ### The FIRST LINE of a TEXT carrying the needle -- never the whole text."""
    for ln in (text or '').split(NL):
        if needle in ln:
            return ln
    return ''


def cut(S, k, sub):
    M = dict(S)
    M[k] = (S.get(k) or '').replace(sub, '')
    return M


def put(S, k, v):
    M = dict(S)
    M[k] = v
    return M


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout


def flat(s):
    return (s or '').replace(NL + '### ', ' ').replace(NL, ' ')


def declared_arms(face):
    """### ### **THE ARMS THE FACE DECLARES, MINUS THE ONES IT EXPRESSLY RETIRES.**
    ### This face says in its own (G2) block that `G-NOB475LOG` ### *"IS NOT CARRIED FORWARD
    ### UNDER THAT NAME"* ### and names its replacement. ### **AN ARM A FACE RETIRES IN WORDS IS
    ### NOT AN ARM IT DECLARES**, and a counter that reads only the token disagrees with the
    ### sentence beside it. ### The face is sealed; the COUNTER is what was wrong."""
    names = set(re.findall(r'`(G-[A-Z0-9-]+)`', face))
    for m in re.finditer(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', face):
        names.discard(m.group(1))
    return names


def globs_of(face):
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS.

    ### ### **THE CORPUS WRITES A POSSESSIVE WITH A BACKTICK** -- `this act`s record`, `b496`s
    ### face`, `(R108)`s first line` -- a convention adopted so that ground strings survive being
    ### written into Python. ### ### **EVERY SUCH POSSESSIVE MAKES THE BACKTICK COUNT ODD**, and a
    ### naive `` `([^`]+)` `` pairing then DESYNCHRONISES: it pairs the closing backtick of one
    ### path with the possessive of the next sentence and returns a multi-line blob of prose as
    ### though it were a glob.
    ### ### **MEASURED ACROSS THE LAST FIVE FACES: b493 EVEN (0 malformed), b494 EVEN (0), b495
    ### ### ODD (5 malformed), b496 ODD (4), b497 ODD (6).** ### So `G-WRITELIST-KINDS` has been
    ### reading a partly-garbled glob list for three acts, and at b497 it reported a file
    ### UNDECLARED that the face declares by name in its own (W).
    ### ### **THE REPAIR IS TO PAIR WITHIN A LINE AND TO KEEP ONLY WHAT LOOKS LIKE A PATH.**
    ### A glob has no spaces and no newlines; a possessive's neighbourhood has both.
    ### ### **THIS WIDENS NOTHING.** ### It lets the tool read declarations that were already
    ### written; a file the face does not name is still uncovered.
    """
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    out = []
    for line in w.split(NL):
        for g in re.findall(BT + '([^' + BT + NL + ']+)' + BT, line):
            g = g.strip()
            if not g or ' ' in g or len(g) > 120:
                continue          # ### prose, not a path
            if not re.match(r'^[A-Za-z0-9_./*?\[\]{}-]+$', g):
                continue
            out.append(g.split('/')[-1])
    return out


def sc(S, k):
    return (S['sc'] or {})


def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=220):
    """### ### **THE TEXT AFTER A MARKER, OR EMPTY WHEN THE MARKER IS GONE.**
    ### A negative control removes the marker; a bare `split(...)[1]` then RAISES instead of
    ### failing, and ### **AN ARM THAT CRASHES UNDER ITS CONTROL HAS NOT BEEN EXERCISED.**"""
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=260):
    """### the text after a marker, or EMPTY when the control removes it."""
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def rows(S):
    return (S['cells'] or {}).get('rows') or []
def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=300):
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


PIN_SHA = '3635e74826a4c1fcece7d1cd2b6fa75e43a00510'
STMT_SHA = '0255fa699a72c941d7dcb70e0232a0184fb9e0c48c66659a6a237c4022000fe6'
NAMES3 = ('EF_lit_zetaZeroConfig', 'Zeta23.EF.EF_lit', 'EF_lit_zeta')

def top_level_assign(text):
    """### ### **IS THERE A `:=` AT BRACKET DEPTH 0?** ### `(C := C)` is a NAMED ARGUMENT and
    ### `let n := c.1` inside a `fun` is a binding; neither hands a declaration to its proof."""
    depth = 0
    i = 0
    while i < len(text) - 1:
        c = text[i]
        if c in '([{':
            depth += 1
        elif c in ')]}':
            depth -= 1
        elif c == ':' and text[i + 1] == '=' and depth <= 0:
            return True
        i += 1
    return False


def strip_prose(text):
    """### ### **A `G-NO*` ARM MUST NOT READ THE ACT'S OWN SENTENCE SAYING IT DID NOT DO IT.**

    ### The trail writer holds its record in a module-level string; scanning that string for the
    ### forbidden word finds the DENIAL. ### This removes triple-quoted blocks and comments, so
    ### what remains is CODE, which is the only place a call can be. ### b487 minted this rule and
    ### this act re-learned it by being caught twice on one run.
    """
    t = re.sub(r'"""[\s\S]*?"""', ' ', text or '')
    t = re.sub(r"'''[\s\S]*?'''", ' ', t)
    t = re.sub(r'^\s*#.*$', ' ', t, flags=re.M)
    return t


def live_limb_guard(suite):
    """### ### **THE GUARD AGAINST A CONTROL THAT LEAVES A LIVE LIMB, AND WHERE IT ACTUALLY IS.**

    ### b495's `G-PUSHED-PREDICATE-THREE-CLAUSED` passed its own positive control because its
    ### predicate was `A or B` and the mutation falsified only `B`. ### This act declared a new arm
    ### to catch that species BY READING THE SUITE'S TEXT, and ### **FOUR REVISIONS LATER THE
    ### ### TEXTUAL PROXY STILL COULD NOT DO IT**: it fired on `x or []` none-defaults, on the word
    ### `or` inside quoted strings, on its own source, and on `any(A or B for ...)` whose control
    ### DOES falsify both limbs.
    ### ### **THE REASON IS THAT THE PROPERTY IS NOT TEXTUAL.** ### Whether a control falsifies
    ### every limb is a fact about what the control DOES, and the only thing that can decide it is
    ### ### **RUNNING THE CONTROL** -- which this harness already does for every arm, and whose
    ### result is the `POS` column and the `POSITIVE-CONTROL PASSES` count. ### **b495 WAS CAUGHT
    ### ### BY THAT COLUMN AND BY NOTHING ELSE.**
    ### So this arm no longer proxies. ### It asserts that the guard IS RUN: that the harness
    ### exercises a positive control on every arm, counts the passes, and ### **FAILS THE WHOLE
    ### ### SUITE ON A SINGLE ONE.**
    """
    need = ['p = bool(pred(pos(S)))',
            'defective.append(name)',
            'not defective']
    return [n for n in need if n not in suite]


def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=300):
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def tb(S, k, d=None):
    return (S['tblj'] or {}).get(k, d)


def cnt(S, k, d=None):
    return ((S['tblj'] or {}).get('counts') or {}).get(k, d)


def trows(S):
    return (S['tblj'] or {}).get('rows') or []








def c2(S, k, d=None):
    return (S['c2'] or {}).get(k, d)


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def c2_closed(S):
    f = c2(S, 'found') or []
    return (c2(S, 'not_near') == 0 and all(c2(S, 'control') or [False]) and all(z.get('inside') for z in f)
            and all(z.get('rho') and z.get('route_a', 1) < 1e-10 for z in f) and abs(c2(S, 'whole', 0) - c2(S, 'total', -9)) < 0.05)


def least_nv(L):
    nv = 8193
    while 2 * math.pi * (nv - 1) / L <= 350.0:
        nv += 1
    return nv


def population(S):
    return [c for c in S['cells'] if c['tail_inside']]


def log_span(log):
    ts = re.findall(r'^\[(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)\]', log, re.M)
    if not ts:
        return None
    import datetime
    f = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
    return (f(ts[-1]) - f(ts[0])).total_seconds()


def edge_secs(log):
    m = re.findall(r'edges 1051 / 1051  (\d+) s', log)
    return int(m[-1]) if m else -1


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def fnorm(s):
    s = (s or '').replace('’', '').replace("'", '').replace('`', '').replace('*', '').replace('#', '')
    return re.sub(r'\s+', ' ', s).strip().lower()


def corr_row(S):
    return next((l for l in S['corr'].split(NL) if l.startswith('| 365 |')), '')


def sec(S):
    h = (S['fold'] or {}).get('heading', '')
    return S['ft'][S['ft'].index(h):] if h and h in S['ft'] else ''


def rows_of(S, repo):
    return [r['name'] for r in (S['tt'].get('rows') or []) if r['repo'] == repo]


def demo_iphi():
    """### READING (8)'s case recomputed HERE, independently: h = i phi on a grid; is h * h~ even and h non-real?"""
    import numpy as np
    u = np.linspace(-1.0, 1.0, 1001)
    phi = (1 - u * u) ** 3
    h = 1j * phi
    k = np.convolve(h, np.conj(h[::-1]))
    return float(np.max(np.abs(h.imag))) > 0.5 and float(np.max(np.abs(k - k[::-1]))) < 1e-12 * float(np.max(np.abs(k)))


WOS = ('W-ORD-TABLE-PROFILE-JSON', 'W-ORD-TABLE-SHORTNAME-DEDUP', 'W-ORD-WEIL-CONVERSE')
RULE2 = 'eps times the sum of the'

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R125) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b516' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'this act`s banked scan', lambda S: '(R81) FLAGS : 0' in S['scan'],
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 0', '(R81) FLAGS : 1'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS', 'a banked verdict LINE -- the pins tool RUN ALONE',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-REG-LOCKED-FIRST', 'the face lock block', lambda S: 'THE REGISTRATION LOCK' in S['face'],
     lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK') and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b515`s closing AND the ledger',
     lambda S: 'THE COMMITS, THE MIRROR, THE CENSUSES' in S['prior'] and S['corr'].count('| 364 |') == 1,
     lambda S: put(S, 'corr', S['corr'].replace('| 364 |', '| 3640 |'))),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b516' in S['ferry'] and 'ACT b516' in S['face'] and not glob.glob(os.path.join(D, 'b517_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b516')),
    ('G-PEEK-DECLARED', 'the face`s (C) block AND the component files` times against the lock',
     lambda S: 'NOTHING IS APPENDED BEFORE THE SEAL' in flat(S['face']) and S['after_lock'], lambda S: put(S, 'after_lock', False)),
    ('G-R125-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R125) END' in S['ferry'] and S['ot'].count('**(R125) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R125) ratified', '(R125) noted'))),
    ('G-SPAN-READ', 'the fold record against the span record -- b508 to b515, eight acts, the tool reading nine',
     lambda S: (S['fold'].get('span') or {}) == dict(lo=S['span']['span_starts_at'], hi=S['span']['this_act'] - 1,
                                                     acts=S['span']['this_act'] - S['span']['span_starts_at'],
                                                     tool_reads=S['span']['current_span'], filed_by=S['span']['filed_by'])
     and S['span']['span_starts_at'] == 508 and S['span']['this_act'] == 516,
     lambda S: put(S, 'fold', dict(S['fold'], span=dict((S['fold'].get('span') or {}), lo=507)))),
    ('G-QUOTES-MATCHED', 'every quoted verdict re-matched HERE in its own closing bank',
     lambda S: len(S['fold'].get('quotes') or []) >= 8 and all(fnorm(q['quote']) in fnorm(read(os.path.join(D, 'b%d_closing.txt' % q['act'])))
                                                                for q in S['fold']['quotes'])
     and sorted(set(q['act'] for q in S['fold']['quotes'])) == list(range(508, 516)),
     lambda S: put(S, 'fold', dict(S['fold'], quotes=S['fold']['quotes'] + [dict(act=508, quote='A VERDICT NO BANK PRINTS', found=True)]))),
    ('G-DEFECTS-MATCHED', 'every defect phrase re-matched HERE, and the total the section prints',
     lambda S: all(fnorm(d['phrase']) in fnorm(read(os.path.join(D, 'b%d_closing.txt' % d['act']))) for d in S['fold'].get('defects') or [])
     and len(S['fold'].get('defects') or []) == 8 and ('%d defects' % sum(d['n'] for d in S['fold']['defects'])) in sec(S),
     lambda S: put(S, 'fold', dict(S['fold'], defects=[dict(d, phrase='NO SUCH PHRASE') for d in S['fold']['defects']]))),
    ('G-RULINGS-MATCHED', 'each ruling`s BEGIN and END re-matched HERE in the ferry named',
     lambda S: [r['ruling'] for r in S['fold'].get('rulings') or []] == list(range(118, 126))
     and all(('RULING (R%d) BEGIN' % r['ruling']) in read(os.path.join(D, r['file'])) and ('RULING (R%d) END' % r['ruling']) in read(os.path.join(D, r['file']))
             for r in S['fold']['rulings']),
     lambda S: put(S, 'fold', dict(S['fold'], rulings=[dict(r, file='b999_ferry.txt') for r in S['fold']['rulings']]))),
    ('G-ERRORS-BLOCK', 'the section -- (R121)`s withdrawals and (R125)(1)`s reading, each quoted',
     lambda S: 'THE LADDER’S SHAPE FINDINGS ARE WITHDRAWN AS WINDOW ARTEFACTS.' in sec(S)
     and 'Neither b514’s window (second property alone) nor b515’s (the zero alone) is the witness' in sec(S),
     lambda S: put(S, 'ft', S['ft'].replace('WITHDRAWN AS WINDOW ARTEFACTS', 'kept'))),
    ('G-OBJECT-EMPTY', 'the fold record`s columns AND the section`s sentence',
     lambda S: (S['fold'].get('columns') or {}).get('OBJECT') == 0 and '**Statements about the object: 0.' in sec(S),
     lambda S: put(S, 'fold', dict(S['fold'], columns=dict(S['fold'].get('columns') or {}, OBJECT=1)))),
    ('G-FOLD-ADDITIVE', 'FINDINGS against its blob at b515`s commit -- a true prefix, one heading',
     lambda S: S['ft_prefix'] and S['ft'].count(S['fold'].get('heading', '#none#')) == 1,
     lambda S: put(S, 'ft_prefix', False)),
    ('G-DIGEST-ADDITIVE', 'the digest against its blob at b515`s commit -- a true prefix, one marker',
     lambda S: S['dg_prefix'] and S['dg'].count('<!-- b516 orientation refresh') == 1,
     lambda S: put(S, 'dg_prefix', False)),
    ('G-TABLE-FIXTURES', 'the instrument`s own fixtures RUN LIVE HERE, and its banked run line',
     lambda S: S['tt_fix'] is True and 'FIXTURES, BOTH POLARITIES : ### **ALL PASS** (12 cases)' in S['ttrun'],
     lambda S: put(S, 'tt_fix', False)),
    ('G-TABLE-DEDUP-READ', 'every dropped short row -- one qualified twin in its repo, and the short row gone',
     lambda S: len((S['tt'].get('workorders_b516') or {}).get('shortname_dedup') or []) >= 1
     and all(len([q for q in rows_of(S, repo) if q.endswith('.' + n)]) == 1 and n not in rows_of(S, repo)
             for repo, n in S['tt']['workorders_b516']['shortname_dedup']),
     lambda S: put(S, 'tt', dict(S['tt'], workorders_b516=dict(S['tt']['workorders_b516'], shortname_dedup=[['SIDE-explicit-formula', 'no_such_name']])))),
    ('G-TABLE-JSON-READ', 'every JSON-profiled row -- its committed bank carries the printed line, and no b456 source',
     lambda S: bool((S['tt'].get('workorders_b516') or {}).get('profile_json'))
     and all(("'%s' %s" % (n, next(r['profile'] for r in S['tt']['rows'] if r['repo'] == repo and r['name'] == n)))
             in gits(ROOT, 'show', 'HEAD:' + f) and 'b456' not in f for repo, n, f in S['tt']['workorders_b516']['profile_json']),
     lambda S: put(S, 'tt', dict(S['tt'], workorders_b516=dict(S['tt']['workorders_b516'],
                                                               profile_json=S['tt']['workorders_b516']['profile_json'] + [['SIDE-kernel', 'structural_exhaustiveness_proved', 'data/b456_profile.json']])))),
    ('G-WORKORDERS-CARRIED', 'the section`s work-order table -- three rows, each with its trigger',
     lambda S: all(('| `%s` |' % x) in sec(S) for x in WOS) and sec(S).count('| `W-ORD-') == 3 and 'the kernel lane after this fold' in sec(S),
     lambda S: put(S, 'ft', S['ft'].replace('| `W-ORD-WEIL-CONVERSE` |', '| gone |'))),
    ('G-LEMMAS-PRICED', 'the section`s lemma table -- (d) and (f1)-(f4), and weeks stated',
     lambda S: all(('| (%s) |' % k) in sec(S) for k in ('d', 'f1', 'f2', 'f3', 'f4')) and 'weeks, stated as weeks' in sec(S),
     lambda S: put(S, 'ft', S['ft'].replace('| (f3) |', '| (x) |'))),
    ('G-CLASSK-PRINTED', 'the banked definition against H2Sign.lean at the kernel`s HEAD, read HERE',
     lambda S: bool(S['ck'].get('definition')) and S['ck']['definition'] in S['h2sign'] and 'h : ℝ → ℂ' in S['ck']['definition'],
     lambda S: put(S, 'ck', dict(S['ck'], definition='def classK (k : ℝ → ℝ) : Prop := True'))),
    ('G-CLASSK-DEMO', 'the i-phi case recomputed HERE, and the banked cases agreeing',
     lambda S: S['demo'] is True and [c['admitted'] for c in S['ck'].get('cases') or []] == [True, False, True],
     lambda S: put(S, 'demo', False)),
    ('G-FIXTURE-RULE-FILED', 'the section AND the trail -- (R125)(2)`s rule in its own words',
     lambda S: RULE2 in flat(sec(S)) and RULE2 in trail(S), lambda S: put(S, 'ot', S['ot'].replace(RULE2, 'a floor'))),
    ('G-N1-SCORED', 'the desk against the recount', lambda S: 'n1' in S['sc'] and desk_word(S, 'N1') == word_of(S['sc']['n1'])
     and S['sc']['n1'] == all(fnorm(q['quote']) in fnorm(read(os.path.join(D, 'b%d_closing.txt' % q['act']))) for q in S['fold']['quotes']),
     lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the columns', lambda S: 'n2' in S['sc'] and desk_word(S, 'N2') == word_of(S['sc']['n2'])
     and S['sc']['n2'] == ((S['fold'].get('columns') or {}).get('OBJECT') == 0), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the section', lambda S: 'n3' in S['sc'] and desk_word(S, 'N3') == word_of(S['sc']['n3'])
     and S['sc']['n3'] == (all(('| `%s` |' % x) in sec(S) for x in WOS) and sec(S).count('| `W-ORD-') == 3),
     lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the definition and the demo', lambda S: 'n4' in S['sc'] and desk_word(S, 'N4') == word_of(S['sc']['n4'])
     and S['sc']['n4'] == (not ('h : ℝ → ℂ' in S['ck'].get('definition', '') and S['demo'])),
     lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk']
     and desk_word(S, 'S1') == word_of(len((S['tt'].get('workorders_b516') or {}).get('shortname_dedup') or []) >= 3)
     and desk_word(S, 'S3') == word_of(bool(S['demo'])),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NOGRADE-CONFERRED', 'this act`s trail record and row -- no grade word, the row`s grade cell NO GRADE',
     lambda S: not GRADE_RE.search(seg(S['ot'], TRAILH, 99999)) and '| NO GRADE |' in corr_row(S),
     lambda S: put(S, 'ot', S['ot'] + ' `x_y_z` DERIVES')),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b516 -'))),
    ('G-NOPRIORBANK', 'file times against the face', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-LANE-SHUT', 'the trail`s own record -- the instrument lane shut, said', lambda S: 'The instrument lane shuts at this act' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(NL, ' ').replace('The instrument lane shuts at this act', 'the lane stays open'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- FINDINGS, the digest, the trail; the kernel untouched',
     lambda S: sorted(S['tracked']) == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md'])
     and S['chain_clean'] is True and S['ker_clean'] is True, lambda S: put(S, 'ker_clean', False)),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text', lambda S: S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger -- row 365 once, six cells as it landed',
     lambda S: S['corr'].count('| 365 |') == 1 and S['corr'].count('(b516, under (R125))') == 1
     and len(corr_row(S).strip().strip('|').split('|')) == 6,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 365 | a duplicate row |')),
    ('G-INSTRUMENT-EDIT-SCOPED', 'relay`s tools against b515`s close -- terminal_table.py alone modified',
     lambda S: S['tools_edited'] == ['terminal_table.py'], lambda S: put(S, 'tools_edited', ['terminal_table.py', 'corr_row.py'])),
    ('G-WRITELIST-KINDS', 'every b516 commit in four repositories, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds'] if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite`s own text', lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the PLACE-papers file list -- no internal document, no `.lean`',
     lambda S: all(not x.startswith('internal/') and not x.endswith('.lean') for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite`s own text', lambda S: 'def line_with(text, needle)' in S['suite'],
     lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness itself -- the positive control is RUN on every arm',
     lambda S: not live_limb_guard(S['suite']), lambda S: put(S, 'suite', S['suite'].replace('defective.append(name)', 'pass'))),
    ('G-MIRROR-TAGGED-BUILD', 'the built zip presence, UNDATED', lambda S: S['mirror'], lambda S: put(S, 'mirror', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree -- (R58)', lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/formal-math/LICENSE')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: ("rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                and "log', '-1', '--pretty=%s').startswith('b516')" in S['suite']
                and "data/b516_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b516_components.txt' in gits(ROOT, 'show'")),
]


def sources():
    import importlib
    tt_mod = importlib.import_module('terminal_table')
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b516_ferry.txt')),
        scan=read(os.path.join(D, 'b516_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b516_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b516_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b516_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b516_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b515_closing.txt')),
        addendum=read(os.path.join(D, 'b516_addendum.txt')),
        comp=read(os.path.join(D, 'b516_components.txt')),
        desk=read(os.path.join(D, 'b516_desk_notes.txt')),
        fold=json.loads(read(os.path.join(D, 'b516_fold.json')) or '{}'),
        span=json.loads(read(os.path.join(D, 'b516_span.json')) or '{}'),
        ck=json.loads(read(os.path.join(D, 'b516_classk.json')) or '{}'),
        h2sign=gits(KER, 'show', 'HEAD:SIDEExplicitFormula/H2Sign.lean'),
        ft=read(FIND), dg=read(DIG),
        ft_prefix=open(FIND, 'rb').read().replace(bytes([13, 10]), bytes([10])).startswith(blob(PP, PRIOR_PP + ':FINDINGS.md')),
        dg_prefix=open(DIG, 'rb').read().replace(bytes([13, 10]), bytes([10])).startswith(blob(PP, PRIOR_PP + ':phase2/method/THE_FINDINGS_AS_THEY_STAND.md')),
        tt=json.loads(read(os.path.join(D, 'terminal_table.json')) or '{}'),
        ttrun=read(os.path.join(D, 'terminal_table_run.txt')),
        tt_fix=bool(tt_mod.workorder_fixtures()[0]),
        demo=demo_iphi(),
        sc=json.loads(read(os.path.join(D, 'b516_scores.json')) or '{}'),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b516_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-*-b516.zip'))),
        chain_clean=(gits(ROOT, 'status', '--porcelain', '--', 'tools/b321_window.py', 'tools/e16/carto_atlas.py',
                          'tools/b326_closure.py', 'tools/b325_epstein.py', 'tools/b511_families.py', 'tools/b514_window.py',
                          'tools/b515_window.py', 'tools/corr_row.py', 'tools/registration_gate.py') == ''),
        ker_clean=(gits(KER, 'rev-parse', '--short=7', 'HEAD') == KER_TIP and gits(KER, 'status', '--porcelain', '--untracked-files=no') == ''),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b516 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b516_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, 'b516_fold.json'), os.path.join(D, 'b516_classk.json'), os.path.join(T, 'terminal_table.py'))),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b516 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                rel = l[3:].strip()
                try:
                    if os.path.getmtime(os.path.join(repo, rel)) < os.path.getmtime(FACE):
                        continue
                except OSError:
                    pass
                k.add(os.path.basename(rel))
    S['kinds'] = k
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-5]_|^b334_', f)]
    S['prior_checked'] = len(prior)
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


def regenerate():
    """### ### **(R107): THE GENERATOR IS PART OF THE CLOSING SUITE.**

    ### *"the generator added to the closing suite so every later close regenerates it and diffs
    ### against the prior run"* -- the ruling's own words. ### The suite therefore RE-RUNS
    ### `tools/terminal_table.py` before it scores anything, and the diff it emits is a cell of
    ### this act's record. ### **A TABLE REGENERATED ONLY WHEN SOMEONE REMEMBERS IS A TABLE THAT
    ### ### DRIFTS**, and the whole point of an instrument output is that it cannot.
    """
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    d = os.path.join(D, 'terminal_table_diff.json')
    diff = json.loads(read(d) or '{}')
    return r.returncode, diff


def main():
    S = sources()
    rc_gen, gen_diff = regenerate()
    # ### ### **THE TABLE IS READ AFTER IT IS REGENERATED (b512's own defect, repaired post-push).** ### `sources()`
    # ### read `terminal_table.md` BEFORE `regenerate()` rewrote it, so `G-TABLE-ROW` scored the previous close's
    # ### table; the first post-push run is banked as `b512_checks_postpush_first.txt`.
    S['table'] = read(os.path.join(D, 'terminal_table.md'))
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (W) THE WRITE LIST.')]
    # ### ### **AN ARM THE FACE RETIRES IN WORDS IS NOT AN ARM IT DECLARES.** ### This face's
    # ### (G2) block says `G-NOB475LOG` *"IS NOT CARRIED FORWARD UNDER THAT NAME"* and names its
    # ### replacement. ### A counter that reads only the token disagreed with the sentence beside
    # ### it, and reported an arm declared-but-not-run. ### The face is sealed and correct; the
    # ### COUNTER was wrong, and it now honours the retirement it is reading.
    retired = set(re.findall(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', S['face']))
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'} - retired)
    if retired:
        rec('  ### arms the face RETIRES in its own words : %s' % sorted(retired))
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b516')
              and 'data/b516_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b516 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
        % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    rec('  arms in the (G2) block : %d ; run here : %d ; deferred : %d'
        % (len(declared), len(names), len(deferred)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  %-42s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 92)
    fail, defective, negfail = [], [], 0
    for name, reads, pred, pos in ARMS:
        if name in deferred:
            continue
        live = bool(pred(S))
        neg = bool(pred(dict(S)))
        p = bool(pred(pos(S)))
        if not neg:
            negfail += 1
        if p:
            defective.append(name)
        v = 'OK' if (neg and not p) else ('### DEFECTIVE' if p else '### NEG FAILS')
        rec('  %-42s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL',
                                           'PASS' if neg else '###FAIL', 'FAIL' if not p else '###PASS', v))
        RES.append(name)
        EX.append(dict(name=name, live=live, neg=neg, pos=p, reads=reads))
        if not live:
            fail.append(name)
    for n in deferred:
        rec('  %-42s DEFERRED TO POST-PUSH' % n)
    stray = sorted(k for k in S['kinds']
                   if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face'])))
    rec('')
    rec('  ### files written that NO (W) GLOB COVERS : %d %s' % (len(stray), stray or ''))
    rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
    if gen_diff.get('first_run'):
        rec('  ###   ### **NO PRIOR RUN TO DIFF AGAINST -- THIS CLOSE IS THE FIRST.** ### From')
        rec('  ###   ### the next close the diff is a cell; saying "no change" now would be a')
        rec('  ###   ### reassuring line about nothing.')
    else:
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d'
            % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
               len(gen_diff.get('changed') or [])))
    rec('  ### G-NOPRIORBANK checked %d prior banks, none excluded.'
        % S['prior_checked'])
    rec('  ### ### **THE b475 LOG EXCEPTION STAYS RETIRED.** ### b481-b489 excused')
    rec('  ###   `b475_zeta23_build.log` as still being appended to by a live process. ### b490')
    rec('  ### found pid 27508 ABSENT at two readings sixty seconds apart and the file cold, and')
    rec('  ### b491 read the log COMPLETE. ### **AN EXCEPTION IS A CLAIM ABOUT THE WORLD AND')
    rec('  ### DECAYS LIKE ONE.** ### b487`s second exclusion is not carried either: it was')
    rec('  ### b485`s bank, which (R97) directed b487 to append to. ### The arm runs at FULL WIDTH.')
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b516_checks_postpush.txt' if pushed else 'b516_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b516_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
