# -*- coding: utf-8 -*-
"""tools/b759_fields.py -- (R369)(7): THE FIELDS OF THE TEXT BLOCK, FILLED FROM THE BANKS AND FROM NO RECALL; A FIELD THE ACT CANNOT FILL
STAYS IN ITS BRACKETS AND IS NAMED.

(7)'s fields, each from the bank named beside it:
  PIN       (7)'s two forms cut from the ferry bank :25; the landing read from data/b759_outcomes.json (tools/b759_outcomes.py)
  AX        each row of section 9.2's Lean table (the text block's rows carrying the AX bracket, and WEILROW's), each name's axioms line from the
            run that printed it at the pin (the run's axioms file, its built ref read equal to the pin); a row of several names one cell where
            their lines agree; units24_iso_signs from data/b757_outcomes.txt; a name no run printed "compiled, axioms not printed"
  WEILROW, WEILNAME, WEILERR, V041   BLOCK F's texts (and BLOCK E's WEILERR) where (5)'s theorem compiled, its LINE read at the pin's blob;
            empty where it did not; V041 entered where the four lines landed
  LAWSUM, LAWROW, the law span, the appendix   by (6)'s verdict line in data/b759_c3table.txt
  F1, F2    the FIELD lines of data/b759_costlaw.txt, with the sentence's form (STANDS or CUT)
  MD5       the md5 of each of the six generated modules at 14ca5725, from the kernel's blobs, read against data/b742_offlinezero.txt :68
  HISTORY   v0.1's nine dated notes, :3 to :19, from PLACE-papers' HEAD blob, the working copy read equal to it with CR removed
  DATE      the UTC date of the run
  N, DEPOSITS   BLOCK E's, by (9)'s count and REGISTRY's deposit pins: not filled by this route (Component 6), named unfilled

  control   the planted controls, printed
  print     the fields composed and printed, nothing written
  bank      the same, written to data/b759_fields.txt and data/b759_fields.json (the composer's input)
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b759_worklist as K       # noqa: E402  (PP, EF_RUNS_B758)
import b759_controls as C       # noqa: E402  (the artifacts' folder, the axioms reader, the kernels' folders)
import figbank as FB            # noqa: E402

NL = '\n'
ACT = 'b759'
TEXT = os.path.join(D, 'b759_text.txt')
FERRY = os.path.join(D, 'b759_ferry.txt')
OUTJ = os.path.join(D, 'b759_outcomes.json')
TABLE = os.path.join(D, 'b759_c3table.txt')
COST = os.path.join(D, 'b759_costlaw.txt')
B742, B742_LINE = os.path.join(D, 'b742_offlinezero.txt'), 68
B757 = os.path.join(D, 'b757_outcomes.txt')
BANK = os.path.join(D, 'b759_fields.txt')
BANKJ = os.path.join(D, 'b759_fields.json')
V01 = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
WEIL = 'zq_weil_positivity_fails'
WEIL_FILE = 'SIDEExplicitFormula/Schema/Wide/HalfScaleControl.lean'
V040_RUN = K.EF_RUNS_B758[1]      # ### v0.40's run (data/b758_outcomes.txt; the worklist's note at :627)
B758_ART = 'D:/b758-runs/ef-%d/build-module-%d' % (V040_RUN, V040_RUN)
EFP = C.KERNELS['ef']['path']
MARKS = ('LAWSUM THEOREM', 'LAWSUM OBSERVED', 'LAWROW THEOREM', 'LAWROW OBSERVED', 'WEILROW COMPILED', 'WEILNAME COMPILED', 'V041 LANDED',
         'WEILERR COMPILED')
LBR, RBR = '\u2039', '\u203a'


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _lines(p):
    return io.open(p, encoding='utf-8').read().replace('\r', '').split(NL)


def _git(repo, *a, raw=False):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout if raw else r.stdout.decode('utf-8', 'replace')


def marked(lines):
    """{mark: text} for MARKS, the lines after each marker to the next marker line, trailing blanks dropped, one line each (leading space kept);
    ALT8: the lines between ALT8 BEGIN and ALT8 END. A mark not found once, or a text not one line, is None."""
    out = {}
    for m in MARKS:
        ix = [i for i, l in enumerate(lines) if l == '@@ ' + m]
        if len(ix) != 1:
            out[m] = None
            continue
        body = []
        for l in lines[ix[0] + 1:]:
            if l.startswith('@@'):
                break
            body.append(l)
        while body and not body[-1].strip():
            body.pop()
        out[m] = body[0] if len(body) == 1 else None
    b = [i for i, l in enumerate(lines) if l == '@@ ALT8 BEGIN']
    e = [i for i, l in enumerate(lines) if l == '@@ ALT8 END']
    out['ALT8'] = NL.join(lines[b[0] + 1:e[0]]) if len(b) == 1 and len(e) == 1 and b[0] < e[0] else None
    return out


def pin_forms(ferry_lines):
    """(7)'s two PIN forms, cut from the ferry bank: (the landed form carrying <peel>, the form where (5) did not land)."""
    t = [l for l in ferry_lines if l.startswith('(7) ')]
    m = re.findall(r'PIN: "([^"]*<peel>[^"]*)" where \(5\) landed, else "([^"]+)"', t[0]) if len(t) == 1 else []
    return m[0] if len(m) == 1 else (None, None)


def resolve(short, names):
    c = [n for n in names if n == short or n.endswith('.' + short)]
    return (c[0] if len(c) == 1 else None), c


def ax_words(a):
    if a is None:
        return 'compiled, axioms not printed'
    if sorted(a) == sorted(C.STANDARD):
        return 'the standard three'
    if not a:
        return 'no axioms'
    order = list(C.STANDARD)
    return ', '.join(sorted(a, key=lambda x: (order.index(x) if x in order else 9, x)))


def ax_cell(shorts, ax, run):
    """one cell for a row's names: (the cell, [(short, full, axioms)], ambiguous [shorts])."""
    got, amb = [], []
    for s in shorts:
        full, c = resolve(s, list(ax))
        if len(c) > 1:
            amb.append(s)
        got.append((s, full, ax.get(full) if full else None))
    al = [g[2] for g in got]
    if all(a is None for a in al):
        return 'compiled, axioms not printed', got, amb
    if all(a is not None for a in al) and all(sorted(a) == sorted(al[0]) for a in al):
        return '%s, run %s' % (ax_words(al[0]), run), got, amb
    return '%s; run %s' % ('; '.join('`%s` %s' % (s, ax_words(a)) for s, _f, a in got), run), got, amb


def md5_read(line, blobs):
    """the six modules' md5s against the bank line: [(name, md5, printed, agree)]; a module not printed or not found agrees False."""
    pr = dict(re.findall(r'(FrontierData|NodesF|Nodes[0-3]) ([0-9a-f]{8,32})', line))
    return [(n, blobs.get(n), pr.get(n), bool(blobs.get(n)) and bool(pr.get(n)) and blobs[n].startswith(pr[n])) for n in
            ('FrontierData', 'NodesF', 'Nodes0', 'Nodes1', 'Nodes2', 'Nodes3')]


def law_of(lines):
    v = [l for l in lines if l.startswith('### ### **THE TABLE OF APPENDIX A: ')]
    if len(v) != 1:
        return None
    return 'THEOREM' if v[0].startswith('### ### **THE TABLE OF APPENDIX A: REPRODUCED ;') else 'OBSERVED'


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    names = ['A.Schema.detector', 'A.Schema.Wide.wide_detector', 'A.B.x', 'A.C.x', 'C2Walk.c2_least_negative']
    c('a short name resolved where one full name ends in it; two refused; none refused',
      (resolve('detector', names)[0], resolve('x', names)[0], len(resolve('x', names)[1]), resolve('y', names)[0]),
      resolve('detector', names)[0] == 'A.Schema.detector' and resolve('x', names)[0] is None and resolve('y', names)[0] is None)
    ax = {'A.a': ('propext', 'Classical.choice', 'Quot.sound'), 'A.b': ('Quot.sound', 'propext', 'Classical.choice'), 'A.c': ('propext',),
          'A.d': ()}
    cs = [ax_cell(['a', 'b'], ax, 7)[0], ax_cell(['c'], ax, 7)[0], ax_cell(['a', 'c'], ax, 7)[0], ax_cell(['e'], ax, 7)[0], ax_cell(['d'], ax, 7)[0]]
    c('the cells: two agreeing in the three, one in propext, two disagreeing, one unprinted, one with none', cs,
      cs == ['the standard three, run 7', 'propext, run 7', '`a` the standard three; `c` propext; run 7', 'compiled, axioms not printed',
             'no axioms, run 7'])
    pl = ['x', '@@ LAWSUM THEOREM', 'and proves.', '@@ WEILNAME COMPILED', ' (`n`)', '', '@@ V041 LANDED', 'one', 'two', '@@ ALT8 BEGIN', 'p',
          '', 'q', '@@ ALT8 END']
    m = marked(pl)
    c('the marked texts: one line taken, its leading space kept; two lines refused; the span between its two markers', (m['LAWSUM THEOREM'],
      m['WEILNAME COMPILED'], m['V041 LANDED'], m['ALT8']), m['LAWSUM THEOREM'] == 'and proves.' and m['WEILNAME COMPILED'] == ' (`n`)'
      and m['V041 LANDED'] is None and m['ALT8'] == 'p\n\nq' and m['LAWROW THEOREM'] is None)
    bl = {'FrontierData': 'aa' * 16, 'NodesF': 'bb' * 16, 'Nodes0': 'c' * 32, 'Nodes1': 'd' * 32, 'Nodes2': 'e' * 32, 'Nodes3': 'f' * 32}
    good = 'FrontierData %s, NodesF %s, Nodes0 cccccccc..., Nodes1 dddddddd..., Nodes2 eeeeeeee..., Nodes3 ffffffff...' % ('aa' * 16, 'bb' * 16)
    c('the md5s read whole and by their opening characters; one planted differing refused; one absent refused',
      ([x[3] for x in md5_read(good, bl)], [x[3] for x in md5_read(good.replace('eeeeeeee', 'eeeeeee0'), bl)].count(False),
       [x[3] for x in md5_read(good.replace('Nodes3 ffffffff...', ''), bl)].count(False)),
      all(x[3] for x in md5_read(good, bl)) and [x[3] for x in md5_read(good.replace('eeeeeeee', 'eeeeeee0'), bl)].count(False) == 1
      and [x[3] for x in md5_read(good.replace('Nodes3 ffffffff...', ''), bl)].count(False) == 1)
    pf = pin_forms(['(7) THE FIELDS. PIN: "the tag v9 (<peel>)" where (5) landed, else "the tag v8 (abc)". AX: ...'])
    c('the PIN forms cut from planted words', pf, pf == ('the tag v9 (<peel>)', 'the tag v8 (abc)'))
    lw = [law_of(['### ### **THE TABLE OF APPENDIX A: REPRODUCED ; x']), law_of(['### ### **THE TABLE OF APPENDIX A: NOT REPRODUCED AT (3,2) ; x']),
          law_of([])]
    c('the law read from the table`s verdict line: reproduced, not reproduced, absent', lw, lw == ['THEOREM', 'OBSERVED', None])
    return L, ok


def compose():
    out, F, src, refuse = [], {}, {}, []
    text = _lines(TEXT)
    ferry = _lines(FERRY)
    mk = marked(text)
    # ### the landing
    if not os.path.exists(OUTJ):
        return None, ['### data/b759_outcomes.json ABSENT -- nothing composed (bank the outcomes first)']
    rec = json.load(io.open(OUTJ, encoding='utf-8'))[0]
    oc = rec.get('outcome') or ''
    landed, compiled = oc.startswith('LANDED'), oc == 'LANDED, COMPILED'
    if oc.startswith('SHOWN') or oc in ('NOT READ', ''):
        return None, ['### THE OUTCOME OF (5) READS %r: THE LANDING NOT YET READ -- nothing composed' % oc]
    pl, pn = pin_forms(ferry)
    if not pl:
        return None, ['### (7)`S PIN FORMS NOT CUT ONCE -- nothing composed']
    if landed:
        peel = (rec.get('peel') or '')[:8]
        F['PIN'] = pl.replace('<peel>', peel)
        run, art, want = rec['run'], C._art('ef', rec['run']), rec.get('peel') or ''
    else:
        F['PIN'] = pn
        peel = None
        run, art, want = V040_RUN, B758_ART, re.findall(r'\(([0-9a-f]{7,40})\)', pn)[0]
    src['PIN'] = 'data/b759_outcomes.json: %s ; (7)`s form, ferry :25' % oc
    ref = C._f(art, 'ref.txt').strip().split()
    ref_ok = bool(ref) and bool(want) and (ref[0].startswith(want) or want.startswith(ref[0][:len(want)]))
    out.append('  THE PIN: %s ; the run that printed it %s, its built ref %s, %s' % (F['PIN'], run, (ref[0] if ref else 'NONE')[:12],
                                                                                      'EQUAL TO THE PIN' if ref_ok else 'NOT THE PIN'))
    if not ref_ok:
        refuse.append('the pin`s run built another ref')
    ax = C.axioms_of(C._f(art, 'axioms.txt'))
    out.append('  the axioms file %s: %d lines' % (os.path.join(art, 'axioms.txt').replace('\\', '/'), len(ax)))
    # ### AX: the rows of 9.2's Lean table carrying the bracket, keyed by the text block's line
    AXF = {}
    hdr = [i for i, l in enumerate(text) if l.startswith('| § | What it says | Lean statement |')]
    rows = []
    if len(hdr) == 1:
        for i in range(hdr[0] + 2, len(text)):
            if not text[i].startswith('|') and text[i] != LBR + 'WEILROW' + RBR:
                break
            if LBR + 'AX' + RBR in text[i]:
                rows.append((i + 1, text[i]))
    u = [l for l in _lines(B757) if re.search(r'SIDEDirichletMod24\.units24_iso_signs\s+\[', l)]
    us = re.findall(r'units24_iso_signs, SIDE-dirichlet-mod-24 v0\.2\.0 = [0-9a-f]+, run (\d+)', NL.join(_lines(B757)))
    for ln, row in rows:
        cells = [x.strip() for x in row.strip().strip('|').split('|')]
        shorts = re.findall(r'`([^`]+)`', cells[2])
        if 'SIDE-dirichlet-mod-24' in cells[3]:
            a = re.findall(r'\[([^\]]*)\]', u[0]) if len(u) == 1 else []
            cell = '%s, run %s' % (ax_words(tuple(x.strip() for x in a[0].split(',') if x.strip())), us[0]) if a and len(us) == 1 else None
            AXF[ln] = cell
            out.append('  AX :%d %s -> %s (data/b757_outcomes.txt)' % (ln, shorts, cell))
            continue
        cell, got, amb = ax_cell(shorts, ax, run)
        if amb:
            refuse.append('names resolved to more than one: %s' % amb)
        AXF[ln] = cell
        out.append('  AX :%d %s -> %s' % (ln, ', '.join('%s=%s' % (s, f or 'NONE') for s, f, _a in got), cell))
    F['AX'] = AXF
    src['AX'] = 'the axioms file of run %s; units24_iso_signs data/b757_outcomes.txt' % run
    # ### WEILROW, WEILNAME, WEILERR, V041
    if compiled:
        blob = _git(EFP, 'show', '%s:%s' % (rec['peel'], WEIL_FILE)).replace('\r', '').split(NL)
        wl = [i + 1 for i, l in enumerate(blob) if l.startswith('theorem %s ' % WEIL) or l == 'theorem %s :' % WEIL]
        wcell, _g, wamb = ax_cell([WEIL], ax, run)
        F['WEIL_LINE'] = wl[0] if len(wl) == 1 else None
        F['WEILROW'] = (mk['WEILROW COMPILED'] or '').replace(LBR + 'LINE' + RBR, str(F['WEIL_LINE'])).replace(LBR + 'AX' + RBR, wcell) if (
            F['WEIL_LINE'] and mk['WEILROW COMPILED']) else None
        F['WEILNAME'] = mk['WEILNAME COMPILED']
        F['WEILERR'] = mk['WEILERR COMPILED']
        what = '`%s` and four print lines' % WEIL
        out.append('  WEILROW: the theorem at %s :%s at the pin`s blob ; its axioms %s' % (WEIL_FILE, F['WEIL_LINE'], wcell))
    else:
        F['WEILROW'], F['WEILNAME'], F['WEILERR'], F['WEIL_LINE'] = '', '', '', None
        what = 'four print lines'
    if landed and mk['V041 LANDED']:
        F['V041'] = mk['V041 LANDED'].replace(LBR + 'PEEL' + RBR, peel).replace(LBR + 'WHAT LANDED' + RBR, what).replace(LBR + 'RUN' + RBR, str(run))
    else:
        F['V041'] = '' if not landed else None
    src['WEIL*'] = 'BLOCK F (and BLOCK E`s WEILERR) of data/b759_text.txt by (5)`s outcome'
    # ### the law
    law = law_of(_lines(TABLE))
    F['LAW'] = law
    F['APPENDIX'] = law == 'THEOREM'
    F['LAWSUM'] = mk['LAWSUM %s' % law] if law else None
    F['LAWROW'] = mk['LAWROW %s' % law] if law else None
    F['ALT8'] = mk['ALT8'] if law == 'OBSERVED' else ''
    src['LAW'] = 'data/b759_c3table.txt`s verdict line'
    out.append('  THE LAW: %s (data/b759_c3table.txt) ; the appendix %s' % (law, 'ENTERED' if F['APPENDIX'] else 'NOT ENTERED'))
    # ### F1, F2
    cl = dict(re.findall(r'^FIELD (\w+) = (.+)$', NL.join(_lines(COST)), re.M))
    F['F1'], F['F2'], F['F1_SENTENCE'], F['F1_QUOTIENT'] = cl.get('F1'), cl.get('F2'), cl.get('F1_SENTENCE'), cl.get('F1_QUOTIENT')
    src['F1, F2'] = 'data/b759_costlaw.txt`s FIELD lines'
    out.append('  F1 %s (the sentence %s, the quotient %s) ; F2 %s (data/b759_costlaw.txt)' % (F['F1'], F['F1_SENTENCE'], F['F1_QUOTIENT'], F['F2']))
    # ### MD5
    at = re.findall(r'MD5: the md5 of each of the six generated modules at ([0-9a-f]{8})', [l for l in ferry if l.startswith('(7) ')][0])
    tree = _git(EFP, 'ls-tree', '-r', '--name-only', at[0]).split(NL) if at else []
    blobs = {}
    for n in ('FrontierData', 'NodesF', 'Nodes0', 'Nodes1', 'Nodes2', 'Nodes3'):
        p = [x for x in tree if x.endswith('/%s.lean' % n)]
        if len(p) == 1:
            blobs[n] = hashlib.md5(_git(EFP, 'cat-file', 'blob', '%s:%s' % (at[0], p[0]), raw=True)).hexdigest()
    mr = md5_read(_lines(B742)[B742_LINE - 1], blobs)
    for n, m5, pr, ag in mr:
        out.append('  MD5 %-12s at %s %s ; data/b742_offlinezero.txt :68 prints %s -> %s' % (n, at[0] if at else '?', m5, pr, 'AGREE' if ag else 'DIFFER'))
    F['MD5'] = ', '.join('%s `%s`' % (n, m5) for n, m5, _p, _a in mr) + ' (relay data/b742_offlinezero.txt :68)' if all(x[3] for x in mr) else None
    src['MD5'] = 'the kernel`s blobs at %s, against data/b742_offlinezero.txt :68' % (at[0] if at else '?')
    # ### HISTORY
    hb = _git(K.PP, 'show', 'HEAD:%s' % V01, raw=True)
    wb = io.open(os.path.join(K.PP, V01), 'rb').read()
    hl = hb.decode('utf-8').split(NL)
    notes = hl[2:19]
    equal_wc = wb.replace(b'\r\n', b'\n') == hb
    nine = [x for x in notes if x.strip()]
    hist_ok = equal_wc and len(nine) == 9 and all(x.startswith('*') and x.endswith('*') for x in nine) and all(not x.strip() for x in notes[1::2])
    F['HISTORY'] = notes if hist_ok else None
    out.append('  HISTORY: v0.1 :3-:19 from PLACE-papers HEAD`s blob (sha256 %s), the working copy (sha256 %s) equal to it with CR removed: %s ; '
               'dated notes %d, each opening and closing with an asterisk, blank lines between: %s' % (
                   hashlib.sha256(hb).hexdigest()[:16], hashlib.sha256(wb).hexdigest()[:16], equal_wc, len(nine), hist_ok))
    src['HISTORY'] = 'PLACE-papers HEAD:%s :3-:19' % V01
    # ### DATE; N and DEPOSITS left to Component 6
    F['DATE'] = time.strftime('%Y-%m-%d', time.gmtime())
    F['N'], F['DEPOSITS'] = None, None
    src['DATE'] = 'the UTC date of this run'
    src['N, DEPOSITS'] = 'not filled by this route: (9)`s count and REGISTRY`s deposit pins at Component 6'
    F['_landed'], F['_compiled'], F['_run'], F['_outcome'] = landed, compiled, run, oc
    F['_refused'] = refuse
    return F, out + ['  SOURCES: ' + ' ; '.join('%s <- %s' % kv for kv in src.items())]


def unfilled(F):
    names = ['PIN', 'LAWSUM', 'LAWROW', 'WEILROW', 'WEILNAME', 'WEILERR', 'V041', 'F1', 'F2', 'MD5', 'HISTORY', 'DATE', 'N', 'DEPOSITS']
    left = [n for n in names if F.get(n) is None]
    left += ['AX :%d' % ln for ln, v in sorted(F['AX'].items()) if v is None]
    return left


def run(write):
    L, ok = controls()
    head = ['%s -- (R369)(7): THE FIELDS OF THE TEXT BLOCK, FROM THE BANKS (%s, tools/b759_fields.py %s)' % (ACT, _now(), 'bank' if write else 'print'),
            '', '## THE CONTROLS'] + L + ['  controls %d of %d as wanted' % (sum(ok), len(ok)), '']
    if not all(ok):
        print(NL.join(head))
        sys.exit('### THE CONTROLS NOT AS WANTED -- nothing composed')
    F, out = compose()
    if F is None:
        print(NL.join(head + out))
        sys.exit('### NOTHING COMPOSED')
    left = unfilled(F)
    body = head + ['## THE READS'] + out + ['', '## THE FIELDS']
    for k in ('DATE', 'PIN', 'LAWSUM', 'LAWROW', 'WEILNAME', 'WEILROW', 'WEILERR', 'V041', 'F1', 'F1_SENTENCE', 'F2', 'MD5', 'N', 'DEPOSITS'):
        body.append('FIELD %s = %s' % (k, '(left in its brackets)' if F.get(k) is None else F[k] if F[k] != '' else '(empty: the row or text enters nothing)'))
    for ln, v in sorted(F['AX'].items()):
        body.append('FIELD AX :%d = %s' % (ln, v if v is not None else '(left in its brackets)'))
    body.append('FIELD HISTORY = %s' % ('v0.1 :3-:19, %d lines' % len(F['HISTORY']) if F['HISTORY'] else '(left in its brackets)'))
    body.append('FIELD LAW = %s ; APPENDIX %s ; ALT8 %s' % (F['LAW'], 'ENTERED' if F['APPENDIX'] else 'NOT ENTERED', 'IN PLACE OF THE LAW SPAN' if F['ALT8'] else 'NOT USED'))
    body += ['', '### ### **FIELDS FILLED %d ; LEFT %d%s ; AX CELLS %d ; THE PIN %s ; THE LAW %s ; REFUSALS %d ; CONTROLS %d OF %d.**' % (
        14 - len([x for x in left if not x.startswith('AX')]) + len([v for v in F['AX'].values() if v is not None]),
        len(left), ' (%s)' % ', '.join(left) if left else '', len(F['AX']), F['PIN'], F['LAW'], len(F['_refused']), sum(ok), len(ok))]
    for r in F['_refused']:
        body.append('### REFUSED: %s' % r)
    print(NL.join(body))
    if not write:
        return
    if F['_refused']:
        sys.exit('### A REFUSAL STANDS -- nothing written')
    js = json.dumps(dict((k, v) for k, v in F.items()), indent=1, ensure_ascii=False, default=str)
    r = FB.write(BANK, NL.join(body))
    with open(BANKJ + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(js + NL)
    os.replace(BANKJ + '.tmp', BANKJ)
    print('written data/b759_fields.txt and data/b759_fields.json ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        L_, ok_ = controls()
        print(NL.join(L_))
        print('### CONTROLS %d OF %d AS WANTED' % (sum(ok_), len(ok_)))
    elif a[:1] == ['print']:
        run(False)
    elif a[:1] == ['bank']:
        run(True)
    else:
        sys.exit(__doc__)
