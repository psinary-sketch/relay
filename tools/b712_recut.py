# -*- coding: utf-8 -*-
"""b712_recut.py -- (R322)(7): THE RE-CUT OF day1/Silence_of_Foundations.md IN KEYSTONE FORM, ITS COMPILE STEPS, QUOTE SEARCH, CUT AND DIFF.

### Written whole by the Write tool at b712. The keystone form, (R322)(7): "the compile steps done and banked before any prose; the body carrying
### the results as declarative sentences, each section doing one thing, each result pinned to its kernel or bank; Correspondence, Errata and
### Placement in the back matter; the throughstone footings available to its result lines. Written in PLACE-papers on a branch, its diff banked;
### nothing published." Routes, each `dry` to print and write nothing:
###   compile  data/b712_recut_compile.txt (.json): every pin the cut cites read at its tag by `git show <tag>:<path>` -- the tag peeled, the line
###            carrying its needle, the blob's sha256 -- BEFORE ANY PROSE (the bank's time against the branch's first commit is the order's record);
###   quote    data/b712_recut_quote.txt (.json): data/b690_rules.txt row (2), b708's form -- each line the cut changes read at PLACE-papers HEAD,
###            its two needles checked to stand in it, each searched with git grep -F across the tracked tree, before the cut's commit;
###   cut      data/b712_recut_cut.txt (.json) `cut <commit>`: the distance by the b670 method (b708's cutbank), the body read without the Errata
###            section (the retired sentences stand there as quotations, by the table's own RETIRE TO ERRATA action); the MATCHES rows the control;
###   diff     data/b712_recut_diff.txt `diff <commit>`: `git diff <commit>^ <commit> -- <document>`, captured by the tool, not by a redirect.
### No file is removed by this tool (G-DELETE-FREE).
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT = 'b712'
PP = 'D:/MY-DOwnloads/PLACE-papers'
CUT_DOC = 'day1/Silence_of_Foundations.md'
CUT_TABLE = 'b646_table_Silence_of_Foundations.txt'
KER, EF, FJ = 'D:/SIDE-kernel', 'D:/SIDE-explicit-formula', 'D:/SIDE-faces-join'

# ### (repo, tag, path, line, needle, what the cut states of it)
PINS = [
    (KER, 'v1.8', 'Kernel/SilenceTheorem.lean', 42, 'def Interface.is_universal', 'the premise: an interface is universal when its action is the same on every pair of configurations'),
    (KER, 'v1.8', 'Kernel/SilenceTheorem.lean', 74, 'theorem silence_universal', 'silence_universal: from I.is_universal, I.kappa_zero (the logical schema over an abstract domain)'),
    (KER, 'v1.8', 'Kernel/ProductFormula_Rat.lean', 71, 'theorem conservation_of_spectra', 'ProductFormula.conservation_of_spectra, the statement'),
    (KER, 'v1.8', 'Kernel/ProductFormula_Rat.lean', 72, '(1 : Rat) ^ s = 1', 'its content: (1 : Q)^s = 1 for every integer s'),
    (KER, 'v1.8', 'Kernel/StructuralCount.lean', 80, 'theorem formation_count : allClasses.length = 7', 'formation_count: the defined list of classes has length 7'),
    (KER, 'v1.8', 'Kernel/StructuralCount.lean', 83, 'theorem stage_sum', 'stage_sum: the arithmetic 2 + 3 + 2 + 0 = 7'),
    (KER, 'v1.8', 'Bridge/CardDerived.lean', 44, 'theorem mechanism_class_card_derived', 'Fintype.card MechanismClass = 7, a defined type counted'),
    (KER, 'v1.8', 'Kernel/Layer1.lean', 23, 'covers_all', 'covers_all: a field of ExhaustiveCatalogue, a hypothesis supplied, not a theorem'),
    (EF, 'v0.37', 'SIDEExplicitFormula/Seam.lean', 101, 'h2_sign_iff_rh', 'RH equivalent to the one open clause h2_sign'),
    (EF, 'v0.37', 'SIDEExplicitFormula/H2Bridge.lean', 71, 'ch_iff_rh', 'Route 3: RH from its own restatement, no route and no reduction'),
    (EF, 'v0.37', 'SIDEExplicitFormula/RegisterDepth.lean', 60, 'not_register1', 'register 1 false as stated'),
    (EF, 'v0.37', 'SIDEExplicitFormula/RegisterDepth.lean', 297, 'register5_output_holds', 'register 5: its output a theorem'),
    (EF, 'v0.37', 'SIDEExplicitFormula/PageConverses.lean', 32, 'register4_positivity_liCoeff_iff_rh', 'register 4 equivalent to RH'),
    (FJ, 'v0.1.0', 'FacesJoin.lean', 29, 'theorem faces_join', 'the faces joined by closure: h2_sign iff lv`s Register4_positivity, through RH'),
]
PRESENT = [(KER, 'v1.8', 'MetaKernel.lean')]   # ### the file the paper names for its nine instances, read present at the pin (its count not re-read)

# ### the lines the cut changes, each with a case-exact needle and a case-insensitive needle from the base wording
QUOTE_LINES = [
    (15, 'Two specific instances load-bearing for the proof of the Riemann Hypothesis', 'load-bearing for the proof of the riemann hypothesis'),
    (47, 'unchanged for 3.5 billion years', 'unchanged for 3.5 billion years'),
    (68, 'the Euler product fully determines zero confinement', 'euler product fully determines zero confinement'),
    (70, 'This inter-class conservation is the proof of RH', 'inter-class conservation is the proof of rh'),
    (124, 'But they *are* what constrains zero locations.', 'what constrains zero locations'),
    (193, 'This paper develops one component of a proof of Theorem (RH)', 'develops one component of a proof of theorem (rh)'),
    (206, 'one of the five registers of the open premise and is not discharged anywhere', 'five registers of the open premise'),
    (232, 'the register sentence (`h2` the single open premise) unchanged', 'the register sentence (`h2` the single open premise) unchanged'),
]
CUT_HELD = (210, 211)   # ### the Correspondence table's cells: no Correspondence cell by hand, b708's form (b704's at data/b704_cut.txt :32-:39)
TROW = re.compile(r'^  :(\d+) \| [^|]+\| [^|]+\| [^|]+\| [^|]+\| (MATCHES|OVERREACHES|UNLICENSED|UNDERSTATES) ; "(.*)" ; (.*)$')


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def g(repo, *a, raw=False):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout if raw else r.stdout.decode('utf-8', errors='replace')


def rd(p):
    with open(p, encoding='utf-8', errors='replace') as fh:
        return fh.read()


def norm(s):
    return ' '.join((s or '').split())


def put(name, text):
    import act_membrane as MEM
    import b712_record as REC
    p = os.path.join(D, name)
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)


def compile_(*a):
    rows, bad = [], []
    for repo, tag, path, ln, nd, what in PINS:
        peeled = g(repo, 'rev-parse', tag + '^{commit}').strip()
        blob = g(repo, 'show', '%s:%s' % (tag, path), raw=True)
        lines = blob.decode('utf-8', errors='replace').replace(chr(13), '').split(NL)
        line = lines[ln - 1] if 0 < ln <= len(lines) else ''
        ok = bool(blob) and nd in line
        if not ok:
            bad.append((os.path.basename(repo), tag, path, ln, nd))
        rows.append(dict(repo=os.path.basename(repo), tag=tag, peeled=peeled, path=path, line=ln, needle=nd, text=line.strip(), what=what,
                         sha256=hashlib.sha256(blob).hexdigest(), stands=ok))
    # ### the control: the same reader on a needle one line off its pin must read False, or the reader cannot fail and nothing is written
    cblob = g(KER, 'show', 'v1.8:Kernel/ProductFormula_Rat.lean', raw=True).decode('utf-8', errors='replace').replace(chr(13), '').split(NL)
    control = 'theorem conservation_of_spectra' in cblob[70 - 1]
    if control:
        sys.exit('### THE CONTROL READ TRUE ONE LINE OFF ITS PIN -- THE READER CANNOT FAIL -- NOTHING WRITTEN')
    # ### the old pin the paper names (SIDE-kernel v1.3 = 0bc21c0), where its axiom profile was read: the statement's two lines stand in its blob
    old = g(KER, 'show', '0bc21c0:Kernel/ProductFormula_Rat.lean', raw=True).decode('utf-8', errors='replace')
    oldpin = dict(commit=g(KER, 'rev-parse', '0bc21c0^{commit}').strip(), v13=g(KER, 'rev-parse', 'v1.3^{commit}').strip(),
                  statement='theorem conservation_of_spectra' in old, content='(1 : Rat) ^ s = 1' in old)
    pres = []
    for repo, tag, path in PRESENT:
        names = [x for x in g(repo, 'ls-tree', '--name-only', tag, '--', path).split(NL) if x.strip()]
        pres.append(dict(repo=os.path.basename(repo), tag=tag, path=path, present=path in names))
    L = ['%s -- COMPONENT 4, (R322)(7): THE RE-CUT`S COMPILE STEPS, BANKED BEFORE ANY PROSE OF %s (%s)' % (ACT, CUT_DOC, utc()), '',
         '### each pin the cut cites, read at its tag by `git show <tag>:<path>` (the working trees not read): the tag peeled to its commit, the line',
         '### carrying its needle, the blob`s sha256. The compile steps are the kernels` own builds at these tags, banked by their acts (SIDE-kernel v1.8,',
         '### SIDE-explicit-formula v0.37, SIDE-faces-join v0.1.0 at this act`s join run 40210894425); this bank reads that each cited statement stands',
         '### where the cut will pin it. No lean on this host. Rows: repo tag (peeled) | path :line | needle | stands | sha256 (16) | what the cut states:', '']
    for r in rows:
        L.append('  %s %s (%s) | %s :%d | %r | %s | %s | %s' % (r['repo'], r['tag'], r['peeled'][:8], r['path'], r['line'], r['needle'], r['stands'],
                                                          r['sha256'][:16], r['what']))
        L.append('      %s' % r['text'][:200])
    L += ['', '### THE CONTROL: the needle `theorem conservation_of_spectra` read at Kernel/ProductFormula_Rat.lean :70 (one line off its pin): %s' % control,
          '### THE OLD PIN: 0bc21c0 = %s ; v1.3 peeled %s ; equal %s ; `theorem conservation_of_spectra` stands %s ; `(1 : Rat) ^ s = 1` stands %s' % (
              oldpin['commit'][:12], oldpin['v13'][:12], oldpin['commit'] == oldpin['v13'], oldpin['statement'], oldpin['content']),
          '### PRESENT AT THE PIN: %s' % '; '.join('%s %s %s %s' % (p['repo'], p['tag'], p['path'], p['present']) for p in pres),
          '### ### **PINS %d ; STANDING %d ; NOT STANDING %s ; BANKED BEFORE ANY PROSE OF THE CUT.**' % (len(rows), sum(r['stands'] for r in rows), bad or 'NONE')]
    if bad:
        print(NL.join(L))
        sys.exit('### A PIN DOES NOT STAND -- NOTHING WRITTEN')
    if 'dry' not in a:
        put('%s_recut_compile.txt' % ACT, NL.join(L) + NL)
        put('%s_recut_compile.json' % ACT, json.dumps(dict(at=utc(), document=CUT_DOC, pins=rows, present=pres, control=control, oldpin=oldpin), indent=1, ensure_ascii=False) + NL)
    print(NL.join(L[7:]) if 'dry' in a else L[-1])


def quote(*a):
    doc = g(PP, 'show', 'HEAD:' + CUT_DOC).replace(chr(13), '').split(NL)
    rows, bad = [], []
    lines_cut = [q[0] for q in QUOTE_LINES]
    for ln, nd, wd in QUOTE_LINES:
        line = doc[ln - 1]
        if nd not in line or wd.lower() not in line.lower():
            bad.append((ln, nd in line, wd.lower() in line.lower()))
        h1 = [x for x in g(PP, 'grep', '-n', '-F', nd, 'HEAD', '--').split(NL) if x.strip()]
        h2 = [x for x in g(PP, 'grep', '-n', '-i', '-F', wd, 'HEAD', '--').split(NL) if x.strip()]
        own = lambda h: h.split(':', 2)[1] == CUT_DOC and int(h.split(':', 3)[2]) in lines_cut   # noqa: E731
        rows.append(dict(line_no=ln, line=line, needle=nd, wide=wd, hits=[h for h in h1 if not own(h)], hits_wide=[h for h in h2 if not own(h)],
                         own=[h for h in h2 if own(h)]))
    if bad:
        sys.exit('### A NEEDLE DOES NOT STAND IN ITS OWN LINE %s -- NOTHING WRITTEN' % bad)
    quoting = sorted(set((h.split(':', 3)[1], int(h.split(':', 3)[2])) for r in rows for h in r['hits'] + r['hits_wide']))
    head = g(PP, 'rev-parse', 'HEAD').strip()
    L = ['%s -- COMPONENT 4, (R322)(7): THE QUOTATION SEARCH BEFORE THE CUT`S COMMIT, data/b690_rules.txt row (2), OVER %s (%s)' % (ACT, CUT_DOC, utc()), '',
         '### the lines the cut changes, read at PLACE-papers HEAD %s; each with a case-exact needle and a case-insensitive needle, both checked to' % head[:7],
         '### stand in the line; each searched with git grep -n -F across the tracked tree at HEAD. The cut lines themselves are not counted (their own',
         '### hits printed). Rows are lines: :line | needle | hits | case-insensitive needle | hits, then every hit with its quoting line.', '']
    for r in rows:
        L.append('  :%-3d | %-62r %d hit(s) | %-50r %d hit(s) | own %d' % (r['line_no'], r['needle'], len(r['hits']), r['wide'], len(r['hits_wide']), len(r['own'])))
        L += ['      %s' % h[:220] for h in sorted(set(r['hits'] + r['hits_wide']))]
    L += ['', '### THE QUOTING LINES, DISTINCT (file :line), EACH A RESIDUE: %s' % ('; '.join('%s :%d' % q for q in quoting) or 'NONE'),
          '### ### **LINES CHANGED BY THE CUT %d ; NEEDLES %d IN TWO SHAPES ; QUOTING LINES %d -- EACH ENTERED AS A RESIDUE ; SEARCHED BEFORE THE CUT`S COMMIT.**' % (
              len(rows), 2 * len(rows), len(quoting))]
    if 'dry' not in a:
        put('%s_recut_quote.txt' % ACT, NL.join(L) + NL)
        put('%s_recut_quote.json' % ACT, json.dumps(dict(at=utc(), document=CUT_DOC, base=head, rows=rows, quoting=[list(q) for q in quoting]),
                                                     indent=1, ensure_ascii=False) + NL)
    print(NL.join(L[6:]) if 'dry' in a else NL.join([x for x in L if x.startswith('  :')] + L[-2:]))


def _split(text):
    """(the document without its Errata section, the Errata section) -- the section from its `## Errata` heading to the next `## ` heading."""
    out, err, skip = [], [], False
    for ln in text.replace(chr(13), '').split(NL):
        if ln.startswith('## '):
            skip = ln.startswith('## Errata')
        (err if skip else out).append(ln)
    return NL.join(out), NL.join(err)


def cut(*a):
    commit = next((x for x in a if re.match(r'^[0-9a-f]{7,40}$', x)), None)
    base_ref = (commit + '^') if commit else 'HEAD'
    base = norm(g(PP, 'show', '%s:%s' % (base_ref, CUT_DOC)))
    whole = g(PP, 'show', '%s:%s' % (commit, CUT_DOC)) if commit else rd(os.path.join(PP, CUT_DOC))
    now, errata = (norm(x) for x in _split(whole))
    table = rd(os.path.join(D, CUT_TABLE)).split(NL)
    rows = []
    for l in table:
        m = TROW.match(l)
        if not m or m.group(2) == 'MATCHES':
            continue
        ln, v, st, act = int(m.group(1)), m.group(2), m.group(3), m.group(4)
        rows.append(dict(line=ln, verdict=v, stated=st, action=act.split(' -- ')[0][:60], held=ln in CUT_HELD, base=norm(st) in base, now=norm(st) in now,
                         in_errata=act.startswith('RETIRE TO ERRATA') and norm(st) in errata))
    mt = [(int(m.group(1)), m.group(3)) for m in (TROW.match(l) for l in table) if m and m.group(2) == 'MATCHES']
    mt_lost = [(ln, st) for ln, st in mt if norm(st) in base and norm(st) not in now]
    try:
        q = json.load(open(os.path.join(D, '%s_recut_quote.json' % ACT), encoding='utf-8'))
    except (OSError, ValueError):
        q = {}
    res = [list(x) for x in (q.get('quoting') or [])]
    dist = [r for r in rows if r['verdict'] in ('OVERREACHES', 'UNLICENSED')]
    und = [r for r in rows if r['verdict'] == 'UNDERSTATES']
    before, after = sum(1 for r in dist if r['base']), sum(1 for r in dist if r['now'])
    L = ['%s -- COMPONENT 4, (R322)(7): THE RE-CUT OF %s, ITS DISTANCE, ITS RESIDUES (%s)' % (ACT, CUT_DOC, utc()), '',
         '### the document: %s (v2.3.1), the licensed table`s next document (relay data/b712_tie, (R322)(7)); its table relay data/%s,' % (CUT_DOC, CUT_TABLE),
         '### pinned at 96779e5, 232 lines, sha256 b7c7c61180766722 = the base`s. The cut: each non-MATCHES row`s ACTION applied by the Edit tool on the',
         '### rows alone, the paper`s title, opening label lines, version line and file name untouched (W-ORD-KEYSTONE-HEADS held); the Correspondence',
         '### cells :210 and :211 held (b708`s form); the three UNLICENSED rows retired to the back matter`s Errata, quoted there with their base lines.',
         '### the base %s ; now %s. "now" is read without the Errata section, where the retired sentences stand as quotations.' % (base_ref, commit or 'the working tree'), '',
         '### THE DISTANCE BY THE b670 METHOD: each non-MATCHES row`s STATED text searched whitespace-normalized in the document at the base and now,',
         '### the row met where it no longer stands. Rows: base line | verdict | applied or HELD | stands at the base | stands now | in Errata | STATED:']
    for r in rows:
        L.append('  :%-3d | %-11s | %-7s | base %-5s | now %-5s | errata %-5s | %s' % (r['line'], r['verdict'], 'HELD' if r['held'] else 'applied', r['base'], r['now'],
                                                                                r['in_errata'], r['stated'][:110]))
        if r['held']:
            L.append('        HELD: a cell of the paper`s Correspondence table (base :208-:212); no Correspondence cell by hand')
    unmet = [r for r in rows if not r['held'] and r['now']]
    ret = [r for r in rows if r['action'].startswith('RETIRE TO ERRATA')]
    L += ['', '### THE RESIDUES (data/b690_rules.txt row (2); relay data/b712_recut_quote.txt, two shapes, the search run before the cut`s commit): each',
          '### quoting line, file :line -- carried by its own table or frozen as deposited; none written:']
    L += ['  %s :%d' % (f, n_) for f, n_ in res] or ['  NONE']
    L += ['', '### THE ROWS APPLIED THAT STILL STAND: %s' % (['%d %s' % (r['line'], r['stated'][:60]) for r in unmet] or 'NONE'),
          '### RETIRED TO ERRATA: %d rows ; quoted in the Errata section %d' % (len(ret), sum(1 for r in ret if r['in_errata'])),
          '### UNDERSTATES (not in the distance): %d at the base, %d now' % (sum(1 for r in und if r['base']), sum(1 for r in und if r['now'])),
          '### THE CONTROL, THE MATCHES ROWS: %d at the base ; standing now %d ; no longer standing %s' % (
              sum(1 for _l, st in mt if norm(st) in base), sum(1 for _l, st in mt if norm(st) in now), ['%d %s' % (ln, st[:60]) for ln, st in mt_lost] or 'NONE'),
          '### ### **THE DISTANCE BY THE b670 METHOD: BEFORE %d, AFTER %d ; ROWS APPLIED %d ; HELD %d (CORRESPONDENCE CELLS) ; QUOTING LINES %d ENTERED AS RESIDUES.**' % (
              before, after, sum(1 for r in rows if not r['held']), sum(1 for r in rows if r['held']), len(res))]
    if 'dry' not in a:
        put('%s_recut_cut.txt' % ACT, NL.join(L) + NL)
        put('%s_recut_cut.json' % ACT, json.dumps(dict(at=utc(), document=CUT_DOC, base=base_ref if commit else '', before=before, after=after,
                                                       held=[r['line'] for r in rows if r['held']], residues=res, matches_lost=[list(x) for x in mt_lost],
                                                       rows=rows), indent=1, ensure_ascii=False) + NL)
    print(NL.join(L[-6:]))


def diff(*a):
    commit = next((x for x in a if re.match(r'^[0-9a-f]{7,40}$', x)), None)
    if not commit:
        sys.exit('usage: b712_recut.py diff <commit> [dry]')
    full = g(PP, 'rev-parse', commit).strip()
    branch = [x.strip(' *') for x in g(PP, 'branch', '--contains', full).split(NL) if x.strip()]
    stat = g(PP, 'diff', '--stat', full + '^', full, '--', CUT_DOC).strip()
    body = g(PP, 'diff', full + '^', full, '--', CUT_DOC).replace(chr(13), '')
    L = ['%s -- COMPONENT 4, (R322)(7): THE RE-CUT`S DIFF, %s^..%s -- %s (%s)' % (ACT, full[:8], full[:8], CUT_DOC, utc()), '',
         '### the cut`s commit %s on PLACE-papers branch(es) %s, not pushed (nothing published); captured by the tool from `git diff`.' % (full, branch),
         '### %s' % stat.replace(NL, ' ; '), '', body,
         '### ### **THE DIFF OF THE RE-CUT, %s^..%s, %d LINES ; ON THE BRANCH, NOT PUSHED.**' % (full[:8], full[:8], body.count(NL))]
    if 'dry' not in a:
        put('%s_recut_diff.txt' % ACT, NL.join(L) + NL)
    print(L[2])
    print(L[3])
    print(L[-1])


def standing_name(*a):
    """data/b712_cut.json: the cut bank under the paper-cut form's standing name (b703's G-RULE-RECUT-QUOTE reads data/b<act>_cut.json beside
    data/b<act>_quote.json), its bytes those of data/b712_recut_cut.json, copied through the membrane; nothing else written (defect (t))."""
    src = os.path.join(D, '%s_recut_cut.json' % ACT)
    b = open(src, 'rb').read()
    import act_membrane as MEM
    import b712_record as REC
    p = os.path.join(D, '%s_cut.json' % ACT)
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)
    if 'dry' not in a:
        with open(p + '.tmp', 'wb') as fh:
            fh.write(b)
        os.replace(p + '.tmp', p)
    import hashlib
    print('  data/%s_cut.json %s bytes %d sha256 %s (data/%s_recut_cut.json sha256 %s)' % (
        ACT, 'DRY' if 'dry' in a else 'written', len(b), hashlib.sha256(open(p, 'rb').read() if os.path.exists(p) else b'').hexdigest()[:16], ACT,
        hashlib.sha256(b).hexdigest()[:16]))


def quote_lf(*a):
    """data/b712_recut_quote.txt written LF (defect (l)): its CR bytes stripped, the result written only where it equals the bank's blob at relay
    HEAD byte for byte (git normalized the line ends at the add), so the working file and the committed bank agree; nothing else written."""
    p = os.path.join(D, '%s_recut_quote.txt' % ACT)
    now = open(p, 'rb').read()
    lf = now.replace(b'\r', b'')
    r = subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:data/%s_recut_quote.txt' % ACT], capture_output=True)
    head = r.stdout
    print('  the working file %d bytes, CR %d ; stripped %d bytes ; HEAD`s blob %d bytes ; equal %s' % (len(now), now.count(b'\r'), len(lf), len(head), lf == head))
    if lf != head:
        sys.exit('### THE STRIPPED FILE IS NOT HEAD`S BLOB -- NOTHING WRITTEN')
    import act_membrane as MEM
    import b712_record as REC
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)
    if 'dry' not in a:
        with open(p + '.tmp', 'wb') as fh:
            fh.write(lf)
        os.replace(p + '.tmp', p)
        print('  written LF')


ROUTES = dict(compile=compile_, quote=quote, cut=cut, diff=diff, standing_name=standing_name, quote_lf=quote_lf)

if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ROUTES:
        print('usage: b712_recut.py compile|quote|cut|diff|standing_name [<commit>] [dry]')
        sys.exit(2)
    ROUTES[r](*sys.argv[2:])
