# -*- coding: utf-8 -*-
"""tools/b757_sweep.py -- b757 COMPONENT 6, (R367)(9) BY (R366)(2)(b): THE LINES OF THE ROSTER'S CURRENT EDITIONS AND OF THE STANDING
TEMPLATES THAT SAY ONE OF THE THREE STATEMENTS THIS ACT NAMES, EACH WITH WHAT IT TAKES.

Written at b757 by the Write tool and committed before its run (the ferry's N2), in the form of tools/b756_reverse.py.

THE RULING'S WORDS (data/b757_ferry.txt :27): "By (R366)(2)(b), run once on the statements this act names: the seat prints each line of the
roster's current editions and of the standing templates that says the control's explicit formula is unproved, that no arithmetic side stands
compiled at the control, or that the four branches are unmerged, and each takes the change or a dated note." (R366)(2)(b) and (c)
(data/b756_ferry.txt :11): "Where an act changes a statement's grade or wording, it prints each line ... that carries that statement, and those
lines take the change or a dated note. (c) A note is appended at a document's end or beside its dated notes, no cited line moving"; "(b) runs
once, on the statements the act names."
THE SCOPE: the roster's current editions (`tools/standing/roster.py json`) in PLACE-papers' working tree, and every file under
tools/standing/fold/. THE SHAPES: each statement has a tight shape A and a wide shape B, each requiring the statement's context in the line
it hits (the control named for (1) and (2); one of the four branches, or the four, for (3)); a template's line is also read joined to the
next across a hard wrap, the hit named at its first line. Each shape's yield is printed beside its yield with no context, and beside the
first shape the seat measured (`v1`). A LINE SAYS A STATEMENT when it says the statement as (R367)(9) words it; a line stating the record's
form (the formula compiled, the side compiled, the branches joined) does not say it. THE HAND-READ (HAND) reads every line that carries,
and every line shape A hits; THE READ OF THE REST (REST) gives the reading of every other line shape B hits, each printed by a dry run and
read by the seat before the bank; a line neither reaches prints NOT YET READ and is not counted. LINES READ BEYOND THE SHAPES (BEYOND) are
printed apart with their readings.
THE FORMS of a line that says a statement: OVERTAKEN (it says the statement in a current text the record no longer bears out), AS THE RECORD
READS (true at b757), A DATED RECORD (a ledger's entry, an order's line or a dated note, true of its own act; (R366)(2)(c) moves no such line).
WHAT EACH TAKES: an OVERTAKEN line in a document of (9)(a)-(d) takes that document's note; one elsewhere stands outside (R367)(10)'s (W)
list and is printed with the route it lacks; a line AS THE RECORD READS takes no change; A DATED RECORD is moved by no rule.
THE PLACE-papers LINES are printed by path, line and the sha256 of the line (16 hex), never by its words (the relay is public;
data/b754_rules.txt (7), (8)); a template's line, the relay's own, in its words.
THE CONTROLS, printed before the figures: (i) each shape fires on its statement written as a constructed line; (ii) a planted needle in no
file reads no hit over the scope; (iii) each statement found by its shapes at a line the seat read as carrying it; (iv) the four documents
of (9) stand in the scope; (v) the docstrings of EpsteinZQ.lean read at the tag v0.38's peel and at (R367)(4)(i)'s commit on push-b757-join.

  python -X utf8 -u tools/b757_sweep.py dry       the controls and every hit printed, nothing written
  python -X utf8 -u tools/b757_sweep.py run       the same, banked as data/b757_sweep.txt and .json
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
ACT = 'b757'
if T not in sys.path:
    sys.path.insert(0, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

I_ = re.I
OVER, ASREC, DATED = 'OVERTAKEN', 'AS THE RECORD READS', 'A DATED RECORD'
EPS = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
CEN = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'
NINE = {EPS: '(9)(a)', 'FACES_LEDGER.md': '(9)(b)', CEN: '(9)(c)', 'REGISTRY.md': '(9)(d)'}
V038, EDIT_I = '14ca5725', '6f2d7e26'   # ### the tag v0.38's peel; (R367)(4)(i)'s commit on push-b757-join (data/b757_steps.json)
EZQ = 'SIDEExplicitFormula/Schema/EpsteinZQ.lean'

CTX = r'(?:Epstein|Z_?Q0?\b|\bZQ|zq[-_]|\u221223|-23|x\^?2 \+ xy \+ 6y|x\u00b2 \+ xy \+ 6y|\bthe control\b|control function|control object)'
NEG = (r'(?:unproved|not (?:yet )?proved|stated,? (?:and |but )?not proved|not compiled|uncompiled|not (?:yet )?(?:a )?compiled|'
       r'(?:is|remains|stands|left) open|assumed|named premises?|as a premise|enters? as (?:a )?premises?|carried as (?:a |the )?premise)')
EF_ = r'(?<![-\w])explicit[- ]formula'
STATEMENTS = [
    dict(id='1', what='the control`s explicit formula is unproved',
         against='zq_premises and zq_explicit_formula_instance, SIDE-explicit-formula zq-b730 at b25fd82c, run 41483457057 (b735; REGISTRY 1.5c-21, '
                 '1.5c-22): the formula compiled premise-free; the docstrings at EpsteinZQ.lean :124-:126 and :133-:136, edited by (R367)(4)(i) on '
                 'push-b757-join at 6f2d7e26, the join broken and that branch unmerged',
         A=EF_ + r'[^.;]{0,140}?' + NEG + '|' + NEG + r'[^.;]{0,140}?' + EF_,
         B=r'^(?=.*' + EF_ + r')(?=.*(?:\bnot\b|\bno\b|\bun\w+|premise|\bopen\b|stated|HELD|held|lacks?|absent|without|does not close))',
         ctx=CTX,
         v1=r'explicit formula[^.]{0,120}?(?:unproved|not (?:yet )?proved|stated,? (?:and )?not proved|not compiled|uncompiled|(?:is|remains|stands|left) open|'
            r'not (?:yet )?(?:a )?compiled|assumed|premise)|(?:unproved|not (?:yet )?proved|stated,? (?:and )?not proved|not compiled|uncompiled|'
            r'(?:is|remains|stands|left) open|not (?:yet )?(?:a )?compiled|assumed|premise)[^.]{0,120}?explicit formula',
         constructed='the explicit formula of the Epstein zeta Z_Q is stated, not proved'),
    dict(id='2', what='no arithmetic side stands compiled at the control',
         against='zq_arith_side_re_neg, SIDE-explicit-formula push-b757-coeff at 596d1c9e, run 43841545568 (b757, (R367)(7)): a test function in classK '
                 'at which the arithmetic side of the control`s explicit formula has negative real part, on a branch, main and the tags unmoved by it',
         A=(r'(?:\bno\b|\bnot\b|\bun)[^.;]{0,60}arithmetic side|arithmetic side[^.;]{0,100}?' + NEG +
            r'|positivity (?:fails?|failure)[^.;]{0,140}?(?:not (?:a )?compiled|uncompiled|no declaration|not stated)'
            r'|(?:not (?:a )?compiled|uncompiled|no declaration)[^.;]{0,140}?positivity (?:fails?|failure)'),
         B=r'arithmetic side|positivity (?:fails?|failure)|Weil[- ]positiv\w*[^.;]{0,60}\bfails?\b',
         ctx=CTX,
         v1=r'arithmetic side[^.]{0,120}?(?:unproved|not (?:yet )?proved|stated,? (?:and )?not proved|not compiled|uncompiled|(?:is|remains|stands|left) open|'
            r'not (?:yet )?(?:a )?compiled|assumed|premise)|(?:unproved|not (?:yet )?proved|stated,? (?:and )?not proved|not compiled|uncompiled|'
            r'(?:is|remains|stands|left) open|not (?:yet )?(?:a )?compiled|assumed|premise)[^.]{0,120}?arithmetic side|no arithmetic side',
         constructed='no arithmetic side stands compiled at the Epstein control'),
    dict(id='3', what='the four branches are unmerged',
         against='the join of (R367)(4) broke (run 43818699881; data/b757_outcomes.txt): main stands at 8fbab45d, no tag was cut, and the four '
                 'branches stand as they stood -- the statement true at b757',
         A=(r'(?:four|held|the) (?:held )?branches[^.;]{0,140}?(?:unmerged|not merged|no merge|un-merged|stand apart|unjoined|not joined|apart)'
            r'|(?:unmerged|not merged|no merge)[^.;]{0,140}?(?:four|held) branches'),
         B=r'\b(?:unmerged|un-merged|not merged|no merge|held unmerged|stand(?:s)? apart)\b',
         ctx=r'zq-b730|keiper-b725|c2-b725|detect-b729|four (?:held )?branches',
         v1=r'(?:four|held) branches[^.]{0,120}?(?:unmerged|not merged|no merge|un-merged|stand apart|unjoined|not joined)|(?:unmerged|not merged|no merge)'
            r'[^.]{0,120}?(?:four|held) branches',
         constructed='the four branches zq-b730, keiper-b725, c2-b725 and detect-b729 stand unmerged'),
]
# ### THE SEAT'S HAND-READ (path, line, statement): (says it, form, reading), entered after the dry runs printed every line
_DQ = 'an act`s "what this act is not": no merge, every Lean file of the act on zq-b730 alone; true of its act and at b757'
HAND = {
    ('FINDINGS.md', 6746, '1'): (True, DATED, 'b590`s Epstein instance on Schema/Epstein.lean: Z_Q entering as named premises, the explicit formula among '
                                              'them cited T1-lit; true of its act'),
    ('FINDINGS.md', 8988, '1'): (True, DATED, 'a later entry`s reading list quoting :6746 whole; a dated record'),
    ('FINDINGS.md', 9810, '1'): (True, DATED, 'the Epstein count`s opening step (R311)(4): the explicit formula`s identity a stated premise; true of its act'),
    ('FINDINGS.md', 9890, '1'): (True, DATED, 'v0.37`s entry: the explicit formula`s three terms and the count each a named premise, none proved; true '
                                              'of v0.37'),
    ('README.md', 141, '1'): (True, DATED, 'a dated note of b704 under (R314)(5), the author`s supportable sentence of v0.37: the zero sum and the local '
                                           'count stated as named premises'),
    ('OPEN_TRAILS.md', 9779, '1'): (True, DATED, 'a trail line of its act: banks read under a kernel that did not then close the Epstein explicit formula'),
    ('OPEN_TRAILS.md', 13436, '1'): (True, DATED, 'the order on b590`s premise structure EpsteinPremises (Schema/Epstein.lean :41 at 8c51431), its ef '
                                                  'field cited T1-lit; an order`s line'),
    ('OPEN_TRAILS.md', 13533, '1'): (True, DATED, 'b642`s price of the five rungs read from the pin, none of them then built'),
    ('ERRATA.md', 1043, '2'): (True, DATED, 'the withdrawal at b736: no declaration then stated the control`s positivity failure, its side unnamed; a dated '
                                           'record'),
    ('FINDINGS.md', 12999, '2'): (True, DATED, 'b736`s discharge: the control`s positivity failure held numerically at b726`s two windows, stated by no '
                                               'declaration then; true of its act'),
    ('FINDINGS.md', 13005, '2'): (True, DATED, 'b736`s rule until a declaration compiles: no sentence that the positivity fails as a theorem, its side '
                                               'unnamed; true of its act'),
    ('OPEN_TRAILS.md', 17335, '2'): (True, DATED, 'b735`s trail, what did not compile: the positivity failure held numerically at b726`s two windows'),
    ('archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-2-historical-landings-and-programs.md', 2499, '2'): (
        False, None, 'a census experiment priced in the archive: Li-type coefficients computed numerically from the functional equation, not a '
                     'statement that no arithmetic side stands compiled'),
    ('REGISTRY.md', 177, '3'): (True, ASREC, '1.5c-21`s status at b735, zq-b730 a branch with no merge; unmerged at b757, the join broken; the tag v0.38 '
                                             'since given by the dated note at :1244'),
    ('REGISTRY.md', 1244, '3'): (True, DATED, 'b745`s dated note: the tag v0.38 on zq-b730, no merge'),
    ('README.md', 170, '3'): (True, DATED, 'b750`s appended note: v0.38 an annotated tag on the branch zq-b730, no merge'),
    ('FINDINGS.md', 13259, '3'): (True, DATED, _DQ), ('FINDINGS.md', 13471, '3'): (True, DATED, _DQ),
    ('FINDINGS.md', 13595, '3'): (True, DATED, _DQ), ('FINDINGS.md', 13707, '3'): (True, DATED, _DQ),
    ('FINDINGS.md', 13964, '3'): (True, DATED, 'b744 at its weight, quoting the author`s word "a tag on zq-b730 at 14ca5725, no merge"'),
    ('FINDINGS.md', 14027, '3'): (True, DATED, 'b745`s entry heading: the tag v0.38 on zq-b730, no merge'),
    ('FINDINGS.md', 14035, '3'): (True, DATED, 'b745`s entry: v0.38 on zq-b730, no merge, main unmoved at 8fbab45d'),
    ('FINDINGS.md', 14067, '3'): (True, DATED, 'b745 at its weight: the one tag v0.38, no merge'),
    ('OPEN_TRAILS.md', 17816, '3'): (True, DATED, 'the author`s word at b744`s root, verbatim: a tag on zq-b730, no merge'),
}
# ### THE SEAT'S READ OF THE REST: the lines shape B alone hits that HAND does not name, each printed by a dry run and read
REST = {
    '1': 'does not say it: the explicit formula of another object (zeta, chi, the literature`s, the bench`s numerical windows, the family order '
         'W-ORD-ZQ-FAMILY), b590`s premise structure read as a compiled conditional (FD-02, epstein_ef_at_window), the control`s formula in the '
         'record`s form (compiled premise-free at b735), or the words "explicit formula" beside a negation about something else',
    '2': 'does not say it: the control`s positivity failure measured or certified by the bench (b325-b326, b663), compiled for Li nonnegativity '
         '(zq_li_nonneg_fails, b742), an order`s object or condition (W-ORD-ZQ-OFFLINE-ZERO, W-ORD-LI-ARITH), a face`s row, or the arithmetic side '
         'of another object or of zeta`s faces',
    '3': 'does not say it: a branch outside the four, or a merge of something else',
}
# ### LINES READ BY HAND BEYOND THE SHAPES: (path, line, statement, says it, reading)
BEYOND = [
    (EPS, 69, '1', False, 'reports the docstring at the tag v0.38 calling each field of ZQPremises "stated, not proved" (EpsteinZQ.lean :133-:136) '
                          'and gives section 3 for what holds at Z_Q0; true of the tag; (R367)(4)(i)`s edit of that docstring stands at 6f2d7e26 on '
                          'push-b757-join, unmerged (control (v))'),
]
PLANTED = 'zz-b757-planted-needle-in-no-file'
LEDGER_STEMS = ('FINDINGS', 'REGISTRY', 'OPEN_TRAILS', 'SPIRAL_MAP', 'VERIFICATION_LOOM', 'ERRATA', 'INSTRUMENTS', 'THE_KEYSTONE_CENSUS', 'README')
CARRIER = {'1': ('FINDINGS.md', 6746), '2': ('FINDINGS.md', 13005), '3': ('REGISTRY.md', 177)}


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
    """[(where, path, lines)]: the roster's files at PLACE-papers' working tree, then every file under tools/standing/fold/."""
    out = []
    for p in roster_files():
        fp = os.path.join(PP, *p.split('/'))
        if os.path.isfile(fp):
            out.append(('pp', p, io.open(fp, encoding='utf-8', errors='replace').read().replace(chr(13), '').split(NL)))
    for dp, dn, fn in os.walk(FOLD):
        dn.sort()
        for f in sorted(fn):
            fp = os.path.join(dp, f)
            out.append(('relay', os.path.relpath(fp, ROOT).replace('\\', '/'),
                        io.open(fp, encoding='utf-8', errors='replace').read().replace(chr(13), '').split(NL)))
    return out


def hits_of(rx, cx, lines, wrap):
    """[(line, how)]: the shape and the context in the line alone, or (a template) in the line joined to the next across a break."""
    out = []
    for i, l in enumerate(lines):
        if rx.search(l) and (cx is None or cx.search(l)):
            out.append((i + 1, 'line'))
        elif wrap and i + 1 < len(lines) and lines[i + 1].strip():
            two = l.rstrip() + ' ' + lines[i + 1].strip().lstrip('#').strip().strip("'\"")
            if rx.search(two) and (cx is None or cx.search(two)) and not (rx.search(lines[i + 1]) and (cx is None or cx.search(lines[i + 1]))):
                out.append((i + 1, 'wrapped :%d-:%d' % (i + 1, i + 2)))
    return out


def digest(l):
    return hashlib.sha256(l.encode('utf-8')).hexdigest()[:16]


def docstrings():
    """(v): "stated, not proved" counted in EpsteinZQ.lean at the tag v0.38's peel and at (R367)(4)(i)'s commit, read from the kernel's objects."""
    try:
        from standing import commit as NEW
        ef = NEW.KERNELS['SIDE-explicit-formula']
    except Exception as e:   # noqa: BLE001 -- printed, not raised
        return None, 'the kernel`s folder not read: %s' % e
    out = {}
    for c in (V038, EDIT_I):
        rc, txt = g(ef, 'show', '%s:%s' % (c, EZQ))
        out[c] = txt.count('stated, not proved') if rc == 0 else None
    br = g(ef, 'branch', '--contains', EDIT_I, '--format=%(refname:short)')[1].split()
    on_main = g(ef, 'merge-base', '--is-ancestor', EDIT_I, '8fbab45d')[0] == 0
    return out, 'EpsteinZQ.lean "stated, not proved": at %s (v0.38`s peel) %s ; at %s ((4)(i) on push-b757-join) %s ; %s on the local branches %s ; an ancestor of main 8fbab45d %s' % (
        V038, out.get(V038), EDIT_I, out.get(EDIT_I), EDIT_I, br or 'NONE', on_main)


def takes(r):
    if not r['says']:
        return '--'
    if r['form'] == OVER:
        return ('THE NOTE OF %s' % NINE[r['path']]) if r['path'] in NINE else 'OUTSIDE (R367)(10)`S (W) LIST: no note written, the route it lacks an item passed by the author`s word'
    if r['form'] == ASREC:
        return 'NO CHANGE%s' % ((' ; the note of %s beside it' % NINE[r['path']]) if r['path'] in NINE else '')
    return 'MOVED BY NO RULE ((R366)(2)(c))%s' % ((' ; the note of %s at the document`s end' % NINE[r['path']]) if r['path'] in NINE else '')


def read(write=False):
    t0 = time.time()
    S = scope()
    by = dict((p, ls) for _w, p, ls in S)
    pp_head = g(PP, 'rev-parse', '--short=8', 'HEAD')[1].strip()
    pp_status = [l for l in g(PP, 'status', '--porcelain', '--untracked-files=no')[1].split(NL) if l.strip()]
    C = []
    for st in STATEMENTS:
        ra, rb, cx = re.compile(st['A'], I_), re.compile(st['B'], I_), re.compile(st['ctx'], I_)
        line = st['constructed']
        C.append(('(i) statement (%s)' % st['id'], 'shapes A and B, with the context, fire on "%s"' % line,
                  bool(ra.search(line) and rb.search(line) and cx.search(line))))
    rp = re.compile(re.escape(PLANTED), I_)
    nplant = sum(len(hits_of(rp, None, ls, w == 'relay')) for w, _p, ls in S)
    C.append(('(ii) the planted needle', '"%s", in no file, reads no hit over %d files' % (PLANTED, len(S)), nplant == 0))
    for st in STATEMENTS:
        p, k = CARRIER[st['id']]
        ls = by.get(p) or []
        cx = re.compile(st['ctx'], I_)
        got = [h for h in hits_of(re.compile(st['A'], I_), cx, ls, False) + hits_of(re.compile(st['B'], I_), cx, ls, False) if h[0] == k]
        C.append(('(iii) statement (%s)' % st['id'], 'found by its shapes at %s :%d, a line the hand-read reads as saying it' % (p, k),
                  bool(got) and bool(HAND.get((p, k, st['id']), (False,))[0])))
    C.append(('(iv) the documents of (9)', 'standing in the scope: %s' % ', '.join('%s %s' % (v, p) for p, v in NINE.items()), all(p in by for p in NINE)))
    dv, dline = docstrings()
    C.append(('(v) the docstrings', dline, bool(dv) and (dv.get(V038) or 0) > 0 and dv.get(EDIT_I) == 0))
    L = ['%s -- COMPONENT 6: (R367)(9)`S SWEEP BY (R366)(2)(b), THE THREE STATEMENTS THIS ACT NAMES (%s, tools/b757_sweep.py)' % (
             ACT, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### the scope: the roster`s current editions (tools/standing/roster.py json) at PLACE-papers HEAD %s, tracked changes %d; every file under '
         'tools/standing/fold/; %d files in all' % (pp_head, len(pp_status), len(S)),
         '### a PLACE-papers line printed by path, line and the sha256 of its text (16 hex), never by its words (data/b754_rules.txt (7), (8)); a '
         'template`s line in its words', '',
         '## THE CONTROLS, BEFORE THE FIGURES']
    for tag, what, ok in C:
        L.append('  %s %s: %s' % ('AS WANTED' if ok else 'NOT AS WANTED', tag, what))
    nok = sum(1 for c in C if c[2])
    L += ['  ### THE CONTROLS: %d OF %d AS WANTED' % (nok, len(C)), '']
    J = dict(controls=dict(wanted=len(C), as_wanted=nok), statements=[], beyond=[])
    tot = dict(says=0, overtaken=0, asrec=0, dated=0, not_saying=0, unread=0)
    for st in STATEMENTS:
        sid = st['id']
        ra, rb, cx, rv = re.compile(st['A'], I_), re.compile(st['B'], I_), re.compile(st['ctx'], I_), re.compile(st['v1'], I_)
        y = dict(v1=0, A_free=0, B_free=0, A=0, B=0)
        rows = []
        for w, p, ls in S:
            wrap = w == 'relay'
            y['v1'] += len(hits_of(rv, None, ls, wrap))
            y['A_free'] += len(hits_of(ra, None, ls, wrap))
            y['B_free'] += len(hits_of(rb, None, ls, wrap))
            ha, hb = dict(hits_of(ra, cx, ls, wrap)), dict(hits_of(rb, cx, ls, wrap))
            y['A'] += len(ha)
            y['B'] += len(hb)
            for k in sorted(set(ha) | set(hb)):
                text = ls[k - 1]
                how = ha.get(k) or hb[k]
                shape = ('shape A (%s)' % how) if k in ha else ('shape B alone (%s)' % how)
                kind = 'ledger' if is_ledger(p) else ('template' if w == 'relay' else 'paper')
                h = HAND.get((p, k, sid))
                if h is not None:
                    says, form, why = h[0], h[1], '%s, hand-read: %s' % (shape, h[2])
                elif k in ha:
                    says, form, why = None, None, '%s: NOT YET READ' % shape
                else:
                    says, form, why = False, None, '%s, the seat`s read of the rest: %s' % (shape, REST[sid])
                r = dict(path=p, line=k, says=says, form=form if says else '--', kind=kind, why=why,
                         text=('sha256 %s' % digest(text)) if kind != 'template' else text.strip()[:240])
                r['takes'] = takes(r)
                rows.append(r)
        sy = [r for r in rows if r['says']]
        c = dict(says=len(sy), overtaken=sum(1 for r in sy if r['form'] == OVER), asrec=sum(1 for r in sy if r['form'] == ASREC),
                 dated=sum(1 for r in sy if r['form'] == DATED), not_saying=sum(1 for r in rows if r['says'] is False),
                 unread=sum(1 for r in rows if r['says'] is None))
        for k_ in tot:
            tot[k_] += c[k_]
        L += ['## (%s) %s' % (sid, st['what'].upper()),
              '### read against: %s' % st['against'],
              '### the yields over the scope: v1 (the first shape measured, no context) %d ; A with no context %d ; B with no context %d ; A with the '
              'context %d ; B with the context %d' % (y['v1'], y['A_free'], y['B_free'], y['A'], y['B']),
              '### the shapes: A /%s/ ; B /%s/ ; the context /%s/' % (st['A'], st['B'], st['ctx']),
              '### lines %d ; SAYING IT %d: %s %d, %s %d, %s %d ; not saying it %d ; NOT YET READ %d' % (
                  len(rows), c['says'], OVER, c['overtaken'], ASREC, c['asrec'], DATED, c['dated'], c['not_saying'], c['unread'])]
        for r in rows:
            L.append('  %s :%d -- %s%s -- TAKES %s -- %s' % (r['path'], r['line'], 'SAYS IT' if r['says'] else ('NOT YET READ' if r['says'] is None else 'does not say it'),
                                                       (' ; ' + r['form']) if r['says'] else '', r['takes'], r['why']))
            L.append('      %s' % r['text'])
        L.append('')
        J['statements'].append(dict(id=sid, what=st['what'], against=st['against'], yields=y, counts=c,
                                    rows=[dict((k, v) for k, v in r.items() if k != 'text') for r in rows]))
    L.append('## LINES READ BY HAND BEYOND THE SHAPES')
    for p, k, sid, says, why in BEYOND:
        ls = by.get(p) or []
        t = ls[k - 1] if 0 < k <= len(ls) else ''
        L.append('  %s :%d -- statement (%s) -- %s -- %s' % (p, k, sid, 'SAYS IT' if says else 'does not say it', why))
        L.append('      sha256 %s' % digest(t))
        J['beyond'].append(dict(path=p, line=k, statement=sid, says=says, why=why))
    L.append('')
    J['totals'] = tot
    J['seconds'] = round(time.time() - t0, 1)
    L.append('### ### **THE SWEEP: CONTROLS %d OF %d AS WANTED ; LINES SAYING ONE OF THE THREE STATEMENTS %d: %s %d ; %s %d ; %s %d ; NOT SAYING IT %d ; '
             'NOT YET READ %d ; %.1f s.**' % (nok, len(C), tot['says'], OVER, tot['overtaken'], ASREC, tot['asrec'], DATED, tot['dated'],
                                              tot['not_saying'], tot['unread'], J['seconds']))
    text = NL.join(L) + NL
    print(text)
    if write:
        for nm, body in (('b757_sweep.txt', text), ('b757_sweep.json', json.dumps(J, indent=1, ensure_ascii=False) + NL)):
            p = os.path.join(D, nm)
            with io.open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
                f.write(body)
            os.replace(p + '.tmp', p)
            print('BANKED: data/%s' % nm)
    return 0 if nok == len(C) and tot['unread'] == 0 else 3


if __name__ == '__main__':
    if sys.argv[1:2] not in (['dry'], ['run']):
        sys.exit(__doc__)
    sys.exit(read(write=sys.argv[1] == 'run'))
