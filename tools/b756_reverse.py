# -*- coding: utf-8 -*-
"""tools/b756_reverse.py -- b756 COMPONENT 2, (R366)(4)(ii) AND (iii): THE REVERSE READ OF SIX STATEMENTS, AND WHAT THE TWO TOOLS FIND
BEYOND (3).

Written at b756 by the Write tool and committed before its run ((R366)(4)(ii): "tools/b756_reverse.py, committed before its run, banked as
data/b756_reverse_read.txt"; the ferry's N2: "each tool of (4) commits before it runs and prints its controls before its figures").

THE READ. For each statement of (R366)(4)(ii)'s list, each line that carries it, by path and line, beside the record line it is read
against, over THE SCOPE: the roster's current editions (`tools/standing/roster.py json`, the builder's roster), of which FINDINGS.md and
OPEN_TRAILS.md are the two cuts' ledgers (tools/standing/cuts.py; each hit there marked by where the b756 cut puts its line), and every
file under tools/standing/fold/. PLACE-papers is read in its working tree at HEAD (its status printed), the fold in the relay's.
THE MATCHERS. Each statement has two shapes, printed with their yields (A the tight one, B the widened one), and the earlier versions the
seat tried before them (`lineage`), each with its yield over the same scope; a line is matched alone, or across a line break with the next
(a hard-wrapped template), the hit then named at its first line.
CARRYING. A line carries a statement when it states something of the statement's subject, in either form: the form (R366) reads against its
record, or the record's own (statement (1): that no zero of Z_Q0 is located in Lean, or that one is). A line shape A hits carries unless the
seat's hand-read reads it otherwise; a line shape B alone hits carries only where the hand-read reads it so. THE HAND-READ (HAND) names its
lines one by one, A and B alike; THE READ OF THE REST (REST) gives the reading of every other line shape B alone hits, each printed by a dry
run and read by the seat before the entry; a line neither reaches prints NOT YET READ and is not counted. Statement (6) carries only in a
front door, a repository's README in the scope (its `door`); a hit elsewhere prints where it stands and does not carry, and the
descriptions (R366)(6) names stand outside the scope.
THE PLACE-papers LINES. A hit in a ledger (FINDINGS, REGISTRY, OPEN_TRAILS, SPIRAL_MAP, VERIFICATION_LOOM, ERRATA, INSTRUMENTS, the
census, README, the archive) or in a paper is printed by path, line and the sha256 of the line, never by its words: the relay is public, and
data/b754_rules.txt (7) cites an edition not deposited by path, line and digest outside a sitting's CURRENT or DRAFTED ((8): [Q]'s lines
the same); the readings below are the seat's words and quote no paper. A template's line, the relay's own, prints in its words.
THE CLASSES. A carrying line is ADDRESSED BY (3) (the writes of (R366)(3), the line each cites), REPAIRED BY (1)(ii) (v1.34.7), THE RECORD
(the line the statement is read against, or that record's own entry, where it stands in the scope), or BEYOND (3).
THE FORMS. A carrying line is OVERTAKEN (it states the form (R366) reads against the record), AS THE RECORD READS, or A DATED RECORD (a
ledger's entry or a tool's version note, true of its own act; rule (2)(c) of data/b756_rules.txt moves no such line). The hand-read sets a
line's form where it names one; else an addressed line is OVERTAKEN, a repaired line or the record AS THE RECORD READS, a ledger's line A
DATED RECORD, and a paper's or a template's line OVERTAKEN where the statement's `old` shape hits it and AS THE RECORD READS where it does not.
THE COUNT of (4)(iii) and the root prompt: the lines BEYOND (3) in the form OVERTAKEN; the other forms printed beside it.
THE CONTROLS, printed before the figures: (i) each statement found at every line (R366) cites for it, by either shape, over the files as
read (statement (6) has no line cited in the scope, printed so); (ii) each shape fires on the text of its statement as a constructed line;
(iii) a planted needle in no file reads as no hit over the whole scope; (iv) statement (6)'s front doors stand in the scope and are read,
PLACE-papers' README.md among them.
`beyond` writes data/b756_beyond_three.txt from this bank and the constellation summary (data/b756_constellation_summary.json): what the
two find beyond (3), with its counts, written nowhere else at this act ((R366)(4)(iii)).

  python -X utf8 -u tools/b756_reverse.py dry       the controls and every hit printed, nothing written
  python -X utf8 -u tools/b756_reverse.py run       the same, banked as data/b756_reverse_read.txt and .json
  python -X utf8 -u tools/b756_reverse.py beyond    data/b756_beyond_three.txt and .json
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(ROOT, 'tools')
D = os.path.join(ROOT, 'data')
FOLD = os.path.join(T, 'standing', 'fold')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
ACT = 'b756'
if T not in sys.path:
    sys.path.insert(0, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SIMP = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md'
WSC = 'day1/Which_Structure_Confines_v2_4_0.md'
FAS7 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md'
MONO = 'day1/A_Place_to_Stand.md'
RTPL = 'tools/standing/fold/record.tpl'
CTPL = 'tools/standing/fold/closing.tpl'
EPS = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
INV = 'phase1.5/method/INVARIANCE_BARRIERS.md'
EUL = 'phase2/method/THE_EULER_SPECIFICATION.md'
TWO3 = 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM_v0_2.md'
TID = 'day1/Third_Identity_Element.md'
OTA = 'archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-2-historical-landings-and-programs.md'
VLA = 'archive/2026-08-24-ledger-split/VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md'
I_ = re.I
OVER, ASREC, DATED = 'OVERTAKEN', 'AS THE RECORD READS', 'A DATED RECORD'

# ### (R366)(4)(ii)'s list, in its order: the statement, the record line it is read against, the two shapes, the lines (R366) cites for it
STATEMENTS = [
    dict(id='1', what='a zero located in Lean, or none',
         against='zq_offline_zero, SIDE-explicit-formula v0.38, as THE_EPSTEIN_CONTROL_OBJECT §5 cites it ((R366)(3)(iv), (4)(ii))',
         A=r'\bzeros?\b[^.;]{0,60}\blocated\b[^.;]{0,40}\bin\s+Lean\b',
         B=r'\b[Ll]ocated\b[^.;]{0,80}(?<![./\w])Lean\b|(?<![./\w])Lean\b[^.;]{0,80}\b[Ll]ocated\b', Bflags=0,
         old=r'\bno\s+(?:\w+\s+){0,5}?zeros?\b|\bno sentence says a zero',
         lineage=[('v1 B', r'\blocated\b.{0,80}\bLean\b|\bLean\b.{0,80}\blocated\b', I_)],
         cited=[(FAS7, 45)]),
    dict(id='2', what='the Ramanujan bound at Epstein functions',
         against='relay data/b752_attribution_plan.txt :21 (the record`s mechanism table: the size bound kept, the Euler product dropped)',
         A=r'Ramanujan.{0,200}Epstein|Epstein.{0,200}Ramanujan',
         B=r'\bRamanujan\s+bound\b',
         old=r'(?:lack|violat|remov|without)\w*[^.;|]{0,60}\bRamanujan|\bRamanujan bound\s*\|\s*yes\s*\|\s*\**no\b',
         lineage=[('v1 B', r'\bRamanujan\b', I_)],
         cited=[(SIMP, 296), (SIMP, 317), (WSC, 133)]),
    dict(id='3', what='zeros inside the strip credited to Davenport and Heilbronn',
         against='THE_EPSTEIN_CONTROL_OBJECT §5, the paragraph on the classical theorem (their theorem concerns Re s > 1; inside the strip, Voronin`s)',
         A=r'^(?=.*Davenport[-\u2013\u2014 ]+(?:and\s+)?Heilbronn)(?=.*\b(?:inside|interior|within)\b[^.;]{0,30}\bstrip\b)',
         B=r'^(?=.*Davenport.{0,12}Heilbronn)(?=.*\bzeros?\b)',
         old=r'\b(?:inside|interior|within)\b[^.;]{0,30}\bstrip\b',
         lineage=[('v1 A', r'^(?=.*Davenport[-–— ]+(?:and\s+)?Heilbronn)(?=.*\b(?:strip|off-line|critical|interior)\b)', I_),
                  ('v2 A', r'^(?=.*Davenport[-–— ]+(?:and\s+)?Heilbronn)(?=.*\b(?:inside|interior|within)\b[^.;]{0,30}\bstrip\b|.*\boff-line zeros?\b'
                           r'|.*\bzeros?\b[^.;]{0,40}\boff the (?:critical )?line\b)', I_),
                  ('v1 B', r'Davenport.{0,12}Heilbronn', I_)],
         cited=[(SIMP, 306), (SIMP, 317)]),
    dict(id='4', what='the primes of valence 7 as \u00b11 mod 24',
         against='ERRATA :841, E-2026-10-04-1 (1 mod 24)',
         A=r'(?:\u00b1|\\pm|\+/-)\s*1\s*(?:\(\s*)?(?:mod|\\pmod|\\bmod)\s*\{?\s*24\b',
         B=r'\bvalence\b.{0,120}\b24\b|\b24\b.{0,120}\bvalence\b',
         old=r'(?:±|\\pm|\+/-)\s*1\s*(?:\(\s*)?(?:mod|\\pmod|\\bmod)\s*\{?\s*24\b',
         note='the two files E-2026-10-04-1 names beside the monograph (TRIVIUM_FINDINGS :171, CONSTANCE :2216) stand outside the roster`s '
              'current editions, and so outside this read`s scope',
         cited=[(MONO, 2098)]),
    dict(id='5', what='the events bank for what is found after the seal',
         against='(R366)(1)(ii) (the bank dropped by (R365)(2)(ii) and dropped again; the N4 wording corrected at v1.34.7)',
         A=r'events\s+bank\s+for\s+what\s+is\s+found\s+after\s+the\s+seal',
         B=r'events_postseal|post-?seal\s+events|events\s+bank\s+after\s+the\s+seal',
         old=r'events_postseal|post-?seal\s+events|events\s+bank\s+for\s+what\s+is\s+found\s+after\s+the\s+seal',
         cited=[(RTPL, 2533)]),
    dict(id='6', what='the words "verified surround" in a description or front door',
         against='the author`s word of 2026-11-14 that a newcomer cannot check a phrase they cannot parse ((R366)(4)(ii), (6))',
         A=r'verified\s+surround',
         B=r'\bverified\b.{0,40}\bsurround|\bsurround\b.{0,40}\bverified\b',
         old=r'verified\s+surround',
         door=r'(?:^|/)README\.md$',
         note='a front door is a repository`s README (data/b754_author_answers.txt :8, :71: the door`s head, body and description); the scope`s '
              'front doors are read whole (control (iv)), and CARRYING above counts the lines of them that hold the phrase; the two descriptions (R366)(6) '
              'names stand outside this scope (a repository`s description is read by gh over the network, which this read does not make), and '
              '(6)`s README route reads them',
         cited=[]),
]
# ### the lines the writes of (R366)(3) address (each note cites its line), and the line (1)(ii)'s standing change repaired
ADDRESSED = {(FAS7, 45, '1'): '(3)(iv)', (SIMP, 296, '2'): '(3)(ii)', (SIMP, 317, '2'): '(3)(ii)', (WSC, 133, '2'): '(3)(iii)',
             (SIMP, 306, '3'): '(3)(ii)', (SIMP, 317, '3'): '(3)(ii)', (MONO, 2098, '4'): '(3)(v) [L20]'}
REPAIRED = {(RTPL, 2533, '5'): '(1)(ii), tools/standing/ v1.34.7 (relay dc8319ea)', (RTPL, 2503, '5'): '(1)(ii), tools/standing/ v1.34.7 (relay dc8319ea)'}
# ### the record each statement is read against, where it stands in the scope: the line itself, or its own entry
RECORD = {(EPS, 41, '3'): 'the record`s §1 (the carrier widened past the strip, Davenport-Heilbronn`s zeros in Re s > 1)',
          (EPS, 89, '3'): 'the record`s §5 (Davenport and Heilbronn`s theorem, zeros with Re s > 1)',
          (EPS, 212, '3'): 'the record`s §5, the paragraph on the classical theorem, the line read against',
          ('ERRATA.md', 841, '4'): 'the record line, E-2026-10-04-1`s head', ('ERRATA.md', 845, '4'): 'E-2026-10-04-1`s own entry',
          ('ERRATA.md', 847, '4'): 'E-2026-10-04-1`s own entry', ('ERRATA.md', 849, '4'): 'E-2026-10-04-1`s own entry',
          ('FINDINGS.md', 15364, '5'): 'this act`s entry of (1)(ii), written by the c1 route (PLACE-papers d1133807)'}
# ### THE SEAT'S HAND-READ (path, line, statement): (carries, form or None, reading), entered after the dry runs printed every line; it
# ### reads a line shape A hits as well as one shape B alone hits. The form None takes the rule of read() (the class, the ledger, `old`).
_SIGMA = 'Davenport and Heilbronn`s zeros placed in Re s > 1 or beyond the strip, or the located zero read as Voronin`s, as §5 reads them'
HAND = {
    ('FINDINGS.md', 14029, '1'): (False, None, 'a zero of zeta on the line located in Lean (the zeta box, an instrument control on a known case), '
                                               'not a zero of Z_Q0: another object'),
    (SIMP, 296, '2'): (True, None, 'the mechanism table`s row, the Ramanujan bound yes at zeta and no at the Epstein function, as (R366)(3)(ii) cites it'),
    ('OPEN_TRAILS.md', 16589, '2'): (False, None, 'the order W-ORD-MECHANISM-TABLE as entered: Ramanujan size named among the table`s columns and '
                                                  'the Epstein zetas among its rows, neither read at the other'),
    (VLA, 2279, '2'): (False, None, 'Ramanujan Delta, the modular form, in the row beside the Epstein row: another object'),
    (WSC, 139, '2'): (False, None, 'the Ramanujan bound listed among the axioms of the Selberg class; of the Epstein functions the line says only '
                                   'that they lack the Euler product'),
    (EUL, 20, '2'): (False, None, 'Ramanujan Delta, the witness of S4, beside the Epstein one-switch, the witness of S1: another object'),
    (SIMP, 317, '3'): (True, OVER, 'read with :306 above it, as (R366) cites both: the line credits Davenport-Heilbronn with the off-line zeros '
                                   'of the strip`s unprotected interior that :306 names'),
    (SIMP, 369, '3'): (True, OVER, 'the line credits the Davenport-Heilbronn construction with explicit off-line zeros of specific Epstein '
                                   'functions, the credit of :306 again; (3)(ii)`s note cites :306 and :317 and not this line'),
    (INV, 425, '3'): (True, OVER, 'the line reduces the known off-line zeros of the disc -23 function, the located ones inside the strip, to '
                                  'Davenport-Heilbronn`s result: the located zero made an instance of their theorem, which §5 reads as Voronin`s'),
    ('FINDINGS.md', 8883, '3'): (True, None, _SIGMA), ('FINDINGS.md', 8889, '3'): (True, None, _SIGMA),
    ('FINDINGS.md', 8911, '3'): (True, None, _SIGMA), ('FINDINGS.md', 10002, '3'): (True, None, _SIGMA),
    ('FINDINGS.md', 14749, '3'): (True, None, _SIGMA), ('OPEN_TRAILS.md', 10370, '3'): (True, None, _SIGMA),
    ('OPEN_TRAILS.md', 15504, '3'): (True, None, _SIGMA), ('OPEN_TRAILS.md', 18176, '3'): (True, None, _SIGMA),
    ('OPEN_TRAILS.md', 18178, '3'): (True, None, _SIGMA), (OTA, 1980, '3'): (True, None, _SIGMA),
    (EPS, 41, '3'): (True, None, _SIGMA), (EPS, 89, '3'): (True, None, _SIGMA), (EPS, 212, '3'): (True, None, _SIGMA),
    (TWO3, 48, '4'): (True, ASREC, 'reports TF :171`s +-1 mod 24 against the argument`s 1 mod 24, as the erratum reads'),
    ('ERRATA.md', 847, '4'): (True, None, 'the erratum`s derivation of 1 mod 24 alone'),
    (TID, 184, '4'): (True, ASREC, 'p = 1 (mod 24) the case of valence 7, as the erratum reads'),
    (CTPL, 275, '5'): (True, OVER, 'the docstring of the closing`s events section: the post-seal events bank read beneath the events bank, '
                                   '"the bank the close writes by design"'),
    (CTPL, 277, '5'): (False, None, 'code: the loop over the two banks` names, each read optional'),
    (CTPL, 281, '5'): (True, OVER, 'the heading the closing prints names data/<act>_events_postseal.txt beside the events bank as read for the '
                                   'next corrigendum'),
    (RTPL, 2312, '5'): (True, DATED, 'a version note of v1.34.0 ((R364)(3)(v)): the post-seal bank read beside the events bank, both optional; '
                                     'the tool`s history'),
    (RTPL, 2314, '5'): (False, None, 'code: the counter`s read of the three banks, the two events banks optional'),
    (RTPL, 2503, '5'): (True, ASREC, 'v1.34.7`s line and its comment: the post-seal bank, "which the act does not keep"'),
    (RTPL, 2533, '5'): (True, ASREC, 'v1.34.7`s N4 words: "no events bank for what is found after the seal"'),
}
# ### THE SEAT'S READ OF THE REST: the lines shape B alone hits that HAND does not name, each printed by a dry run and read; (path pattern
# ### or None, carries, reading), the first that matches the path applying
REST = {
    '2': [(None, False, 'the Ramanujan bound named in general (among the structures that govern zero locations, or in the conjunction that '
                        'separates zeta from zeta_Q without saying which member zeta_Q lacks), or the bound of regular graphs (the spectral '
                        'margin, Alon-Boppana, Deligne): none reads the bound at the Epstein functions')],
    '3': [(None, False, 'Davenport and Heilbronn named beside zeros without placing the zeros credited to them inside the strip: zeros off the '
                        'critical line with the place unnamed (true of their zeros in Re s > 1), Voronin credited beside them, the corpus`s '
                        'located zeros named beside them as its own, the Davenport-Heilbronn function, discriminator or witness named as an '
                        'object, or a reference entry')],
    '4': [(None, False, 'the valence dichotomy or the modulus 24 named without the congruence of the valence-7 primes, or the erratum named '
                        'by its subject')],
    '5': [(r'^(?:FINDINGS|OPEN_TRAILS)\.md$', True, 'a ledger`s dated record naming the post-seal events bank of b753 or b754 (its rows, its '
                                                    'source, its reading at v1.34.0), or its absence at b755 and after')],
}
PLANTED = 'zz-b756-planted-needle-in-no-file'
LEDGER_STEMS = ('FINDINGS', 'REGISTRY', 'OPEN_TRAILS', 'SPIRAL_MAP', 'VERIFICATION_LOOM', 'ERRATA', 'INSTRUMENTS', 'THE_KEYSTONE_CENSUS', 'README')


def is_ledger(path):
    b = os.path.basename(path)
    return path.startswith('archive/') or any(b.startswith(s) for s in LEDGER_STEMS)


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def roster_files():
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'standing', 'roster.py'), 'json'], capture_output=True)
    if r.returncode != 0:
        sys.exit('### roster.py json exit %d' % r.returncode)
    return [p.replace('\\', '/') for p in json.loads(r.stdout.decode('utf-8'))['files']]


def scope():
    """[(label, path for the bank, lines)]: the roster's files at PLACE-papers' working tree, then every file under tools/standing/fold/."""
    out = []
    for p in roster_files():
        fp = os.path.join(PP, *p.split('/'))
        if os.path.isfile(fp):
            out.append(('pp', p, io.open(fp, encoding='utf-8', errors='replace').read().replace(chr(13), '').split(NL)))
    for dp, dn, fn in os.walk(FOLD):
        dn.sort()
        for f in sorted(fn):
            fp = os.path.join(dp, f)
            rel = os.path.relpath(fp, ROOT).replace('\\', '/')
            out.append(('relay', rel, io.open(fp, encoding='utf-8', errors='replace').read().replace(chr(13), '').split(NL)))
    return out


def hits_of(rx, lines):
    """[(line, how)]: the line alone, or the line joined to the next across a break (named at its first line, the next not hit alone)."""
    out = []
    alone = [bool(rx.search(l)) for l in lines]
    for i, l in enumerate(lines):
        if alone[i]:
            out.append((i + 1, 'line'))
        elif i + 1 < len(lines) and not alone[i + 1] and lines[i + 1].strip():
            if rx.search(l.rstrip() + ' ' + lines[i + 1].strip().lstrip('#').strip().strip("'\"")):
                out.append((i + 1, 'wrapped :%d-:%d' % (i + 1, i + 2)))
    return out


def digest(l):
    return hashlib.sha256(l.encode('utf-8')).hexdigest()[:16]


def rx(st, w):
    """### a statement's shape compiled: A ignoring case, B with its own flags (statement (1)'s B keeps case: `Lean` the language)."""
    return re.compile(st[w], st.get('Bflags', I_) if w == 'B' else I_)


def cut_place():
    """### where the b756 cuts put each line of the two ledgers: a function (path, line, text) -> words, or a refusal's words."""
    try:
        from standing import cuts as CU
        _c, _f, x = CU.build('HEAD', ACT)
    except Exception as e:   # noqa: BLE001 -- the cut's refusal is printed, not raised
        return lambda p, k, t: '', 'THE b756 CUTS NOT READ: %s' % str(e)[:200]

    def where(p, k, t):
        if p == 'FINDINGS.md':
            if k <= x['fend'] or k >= x['fs']:
                return 'in the b756 cut whole'
            return 'in the b756 cut by its heading line' if t.startswith('## ') else 'outside the b756 cut'
        if p == 'OPEN_TRAILS.md':
            s0, s1 = x['st']
            if k < x['ofirst'] or s0 <= k <= s1 or k >= x['t0']:
                return 'in the b756 cut whole'
            return 'in the b756 cut by its heading line' if t.startswith('### ') else 'outside the b756 cut'
        return ''
    return where, 'THE b756 CUTS at PLACE-papers %s: FINDINGS whole :1-:%d and from :%d; OPEN_TRAILS whole :1-:%d, :%d-:%d and from :%d' % (
        x['commit'], x['fend'], x['fs'], x['ofirst'] - 1, x['st'][0], x['st'][1], x['t0'])


def read(write=False):
    t0 = time.time()
    S = scope()
    by = dict((p, ls) for _r, p, ls in S)
    where, cut_line = cut_place()
    pp_head = g(PP, 'rev-parse', '--short=8', 'HEAD')[1].strip()
    pp_status = [l for l in g(PP, 'status', '--porcelain', '--untracked-files=no')[1].split(NL) if l.strip()]
    C = []
    # (i) each statement at every line (R366) cites for it, by either shape
    for st in STATEMENTS:
        ra, rb = rx(st, 'A'), rx(st, 'B')
        if not st['cited']:
            C.append(('(i) statement (%s)' % st['id'], 'no line of the scope cited by (R366) for this statement: the control NOT AVAILABLE, printed so', None))
        for p, k in st['cited']:
            ls = by.get(p) or []
            got = [h for h in hits_of(ra, ls) + hits_of(rb, ls) if h[0] == k]
            C.append(('(i) statement (%s)' % st['id'], 'found at %s :%d, cited by (R366)' % (p, k), bool(got)))
    # (ii) each shape fires on its statement written as a constructed line
    for st in STATEMENTS:
        line = {'1': 'the control, no zero located in Lean', '2': 'Epstein functions lack the Ramanujan bound',
                '3': 'off-line zeros inside the strip, Davenport-Heilbronn', '4': 'p \u2261 \u00b11 mod 24, valence 7',
                '5': 'the events bank for what is found after the seal present, events_postseal', '6': 'the verified surround'}[st['id']]
        C.append(('(ii) statement (%s)' % st['id'], 'shapes A and B fire on the constructed line "%s"' % line,
                  bool(rx(st, 'A').search(line)) and bool(rx(st, 'B').search(line))))
    # (iii) the planted needle over the whole scope
    rp = re.compile(re.escape(PLANTED), I_)
    nplant = sum(len(hits_of(rp, ls)) for _r, _p, ls in S)
    C.append(('(iii) the planted needle', '"%s", in no file, reads no hit over %d files' % (PLANTED, len(S)), nplant == 0))
    # (iv) statement (6)'s front doors stand in the scope and are read: PLACE-papers' README.md among them
    doors = [p for p in by if re.search(STATEMENTS[5]['door'], p)]
    C.append(('(iv) statement (6)', 'the front doors of the scope read whole, PLACE-papers` README.md among them: %s' % ', '.join(doors),
              'README.md' in doors))
    L = ['%s -- COMPONENT 2: THE REVERSE READ OF SIX STATEMENTS, (R366)(4)(ii) (%s)' % (ACT, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### the scope: the roster`s current editions (tools/standing/roster.py json) at PLACE-papers HEAD %s, tracked changes %d; every file under '
         'tools/standing/fold/; %d files in all' % (pp_head, len(pp_status), len(S)),
         '### %s' % cut_line,
         '### a PLACE-papers line, a ledger`s or a paper`s, printed by path, line and the sha256 of its text (16 hex), never by its words (the relay '
         'is public; data/b754_rules.txt (7), (8)); a template`s line, the relay`s own, in its words', '',
         '## THE CONTROLS, BEFORE THE FIGURES']
    for tag, what, ok in C:
        L.append('  %s %s: %s' % ('NOT AVAILABLE' if ok is None else ('AS WANTED' if ok else 'NOT AS WANTED'), tag, what))
    nc = sum(1 for c in C if c[2] is not None)
    nok = sum(1 for c in C if c[2])
    L += ['  ### THE CONTROLS: %d OF %d AS WANTED ; NOT AVAILABLE %d' % (nok, nc, sum(1 for c in C if c[2] is None)), '']
    J = dict(controls=dict(wanted=nc, as_wanted=nok), statements=[])
    tot = dict(carrying=0, addressed=0, repaired=0, record=0, beyond=0, beyond_overtaken=0, beyond_asrec=0, beyond_dated=0, not_carrying=0, unread=0)
    for st in STATEMENTS:
        sid = st['id']
        ra, rb, ro = rx(st, 'A'), rx(st, 'B'), re.compile(st['old'], I_)
        lin = [(nm, pt, sum(len(hits_of(re.compile(pt, fl), ls)) for _r, _p, ls in S)) for nm, pt, fl in st.get('lineage', [])]
        rows, ya, yb = [], 0, 0
        for _r, p, ls in S:
            ha = dict(hits_of(ra, ls))
            hb = dict(hits_of(rb, ls))
            ya += len(ha)
            yb += len(hb)
            for k in sorted(set(ha) | set(hb)):
                text = ls[k - 1]
                key = (p, k, sid)
                how = ha.get(k) or hb[k]
                shape = ('shape A (%s)' % how) if k in ha else ('shape B alone (%s)' % how)
                kind = 'ledger' if is_ledger(p) else ('template' if _r == 'relay' else 'paper')
                h, form = HAND.get(key), None
                if st.get('door') and not re.search(st['door'], p):
                    carries, why = False, '%s, outside a front door: %s' % (shape, {'ledger': 'a ledger`s record', 'template': 'a template',
                                                                                     'paper': 'a document`s body'}[kind])
                elif h is not None:
                    carries, form, why = h[0], h[1], '%s, hand-read: %s' % (shape, h[2])
                elif k in ha:
                    carries, why = True, shape
                else:
                    rest = next((x for x in REST.get(sid, []) if x[0] is None or re.search(x[0], p)), None)
                    if rest is None:
                        carries, why = None, '%s: NOT YET READ' % shape
                    else:
                        carries, why = rest[1], '%s, the seat`s read of the rest: %s' % (shape, rest[2])
                if key in ADDRESSED:
                    cls = 'ADDRESSED BY ' + ADDRESSED[key]
                elif key in REPAIRED:
                    cls = 'REPAIRED BY ' + REPAIRED[key]
                elif key in RECORD:
                    cls = 'THE RECORD: ' + RECORD[key]
                else:
                    cls = 'BEYOND (3)'
                if carries and form is None:
                    full = text + ((' ' + ls[k].strip()) if how.startswith('wrapped') else '')
                    form = (OVER if cls.startswith('ADDRESSED') else ASREC if cls.startswith(('REPAIRED', 'THE RECORD')) else
                            DATED if kind == 'ledger' else OVER if ro.search(full) else ASREC)
                rows.append(dict(path=p, line=k, carries=carries, why=why, cls=cls if carries else '--', form=form if carries else '--', kind=kind,
                                 where=where(p, k, text), text=('sha256 %s' % digest(text)) if kind != 'template' else text.strip()[:240]))
        car = [r for r in rows if r['carries']]
        bey = [r for r in car if r['cls'] == 'BEYOND (3)']
        c = dict(carrying=len(car), addressed=sum(1 for r in car if r['cls'].startswith('ADDRESSED')),
                 repaired=sum(1 for r in car if r['cls'].startswith('REPAIRED')), record=sum(1 for r in car if r['cls'].startswith('THE RECORD')),
                 beyond=len(bey), beyond_overtaken=sum(1 for r in bey if r['form'] == OVER), beyond_asrec=sum(1 for r in bey if r['form'] == ASREC),
                 beyond_dated=sum(1 for r in bey if r['form'] == DATED), not_carrying=sum(1 for r in rows if r['carries'] is False),
                 unread=sum(1 for r in rows if r['carries'] is None))
        for k_ in tot:
            tot[k_] += c[k_]
        L += ['## (%s) %s' % (sid, st['what'].upper()),
              '### read against: %s' % st['against'],
              '### the matcher lineage, each earlier version`s yield over the scope: %s' % (' ; '.join('%s /%s/ %d' % x for x in lin) or 'none before the shapes below'),
              '### the shapes read: A /%s/ %d hit(s) ; B /%s/ %d hit(s)%s' % (st['A'], ya, st['B'], yb, ' (case kept)' if st.get('Bflags', I_) == 0 else ''),
              '### lines %d ; CARRYING %d: addressed by (3) %d, repaired by (1)(ii) %d, the record %d, BEYOND (3) %d (%s %d, %s %d, %s %d) ; '
              'not carrying %d ; NOT YET READ %d' % (len(rows), c['carrying'], c['addressed'], c['repaired'], c['record'], c['beyond'], OVER,
                                                     c['beyond_overtaken'], ASREC, c['beyond_asrec'], DATED, c['beyond_dated'], c['not_carrying'], c['unread'])]
        if st.get('note'):
            L.append('### %s' % st['note'])
        for r in rows:
            L.append('  %s :%d -- %s -- %s%s%s -- %s' % (r['path'], r['line'], 'CARRIES' if r['carries'] else ('NOT YET READ' if r['carries'] is None else 'does not carry'),
                                                      r['cls'], (' ; ' + r['form']) if r['carries'] else '', (' ; ' + r['where']) if r['where'] else '', r['why']))
            L.append('      %s' % r['text'])
        L.append('')
        J['statements'].append(dict(id=sid, what=st['what'], against=st['against'], A=ya, B=yb, lineage=[(x[0], x[2]) for x in lin], counts=c,
                                    rows=[dict((k, v) for k, v in r.items() if k != 'text') for r in rows]))
    J['totals'] = tot
    J['seconds'] = round(time.time() - t0, 1)
    L.append('### ### **THE REVERSE READ: CONTROLS %d OF %d AS WANTED ; LINES CARRYING THE SIX STATEMENTS %d: ADDRESSED BY (3) %d ; REPAIRED BY (1)(ii) %d ; '
             'THE RECORD %d ; BEYOND (3) %d, OF THEM %s %d, %s %d, %s %d ; NOT CARRYING %d ; NOT YET READ %d ; %.1f s.**' % (
                 nok, nc, tot['carrying'], tot['addressed'], tot['repaired'], tot['record'], tot['beyond'], OVER, tot['beyond_overtaken'], ASREC,
                 tot['beyond_asrec'], DATED, tot['beyond_dated'], tot['not_carrying'], tot['unread'], J['seconds']))
    L.append('### ### **THE COUNT FOR (4)(iii) AND THE ROOT PROMPT: %d LINE(S) BEYOND (3) CARRYING A STATEMENT IN THE FORM (R366) READS AGAINST ITS '
             'RECORD, IN A PAPER OR A TEMPLATE.**' % tot['beyond_overtaken'])
    if write:
        put('%s_reverse_read.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
        put('%s_reverse_read.json' % ACT, (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    print(NL.join(L))
    return nok == nc


def put(name, b):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as f:
        f.write(b)
    os.replace(p + '.tmp', p)
    print('  written: data/%s (%d bytes)' % (name, len(b)))


def beyond():
    """### (R366)(4)(iii): what the two find beyond (3), with the two counts the root prompt carries; written nowhere else at this act."""
    rr = json.load(io.open(os.path.join(D, '%s_reverse_read.json' % ACT), encoding='utf-8'))
    cs = json.load(io.open(os.path.join(D, '%s_constellation_summary.json' % ACT), encoding='utf-8'))
    t = rr['totals']
    L = ['%s -- (R366)(4)(iii): WHAT THE TWO FIND BEYOND (3), BANKED WITH ITS COUNT AND WRITTEN NOWHERE AT THIS ACT (%s)' % (
        ACT, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### "it goes to the prose pass and the re-cuts, and the root prompt carries the two counts" ((R366)(4)(iii))', '',
         '## THE CONSTELLATION RERUN (relay data/%s_constellation_summary.txt): tables read %d of %d; rows moved or gone by the tool %d %s; '
         'after the seat`s hand-read %d counted, %d not, %d unread. None of them is a line the writes of (3) address.' % (
             ACT, cs['tables'], cs['population'], cs['moved'], cs['kinds'], cs.get('hand_counted', 0), cs.get('hand_not', 0), cs.get('hand_unread', 0)),
         '## THE REVERSE READ (relay data/%s_reverse_read.txt): lines carrying the six statements %d; addressed by (3) %d; repaired by (1)(ii) %d; '
         'the record itself %d; BEYOND (3) %d, of them %s %d (in a paper or a template), %s %d, %s %d; not yet read %d.' % (
             ACT, t['carrying'], t['addressed'], t['repaired'], t['record'], t['beyond'], OVER, t['beyond_overtaken'], ASREC, t['beyond_asrec'],
             DATED, t['beyond_dated'], t['unread']), '']
    for s in rr['statements']:
        bey = [r for r in s['rows'] if r['carries'] and r['cls'] == 'BEYOND (3)']
        L.append('  (%s) %s: %d beyond (3), %s %d' % (s['id'], s['what'], len(bey), OVER, sum(1 for r in bey if r['form'] == OVER)))
        for r in sorted(bey, key=lambda r: (r['form'] != OVER, r['path'], r['line'])):
            L.append('      %s :%d -- %s%s' % (r['path'], r['line'], r['form'], (' ; %s' % r['where']) if r['where'] else ''))
    n1, n2 = cs.get('hand_counted', cs['moved']), t['beyond_overtaken']
    L += ['', '### ### **THE TWO COUNTS FOR THE ROOT PROMPT: THE CONSTELLATION RERUN %d ROWS MOVED OR GONE (%d BY THE TOOL) ; THE REVERSE READ %d LINE(S) '
              'BEYOND (3) IN THE FORM (R366) READS AGAINST ITS RECORD (%d BEYOND (3) IN ALL).**' % (n1, cs['moved'], n2, t['beyond'])]
    put('%s_beyond_three.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    put('%s_beyond_three.json' % ACT, (json.dumps(dict(constellation_counted=n1, constellation_tool=cs['moved'], reverse_beyond_overtaken=n2,
                                                       reverse_beyond_all=t['beyond'], reverse_unread=t['unread']), indent=1) + NL).encode('utf-8'))
    print(NL.join(L[-3:]))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'dry':
        sys.exit(0 if read(False) else 1)
    elif cmd == 'run':
        sys.exit(0 if read(True) else 1)
    elif cmd == 'beyond':
        beyond()
    else:
        print('usage: b756_reverse.py dry | run | beyond')
        sys.exit(2)
