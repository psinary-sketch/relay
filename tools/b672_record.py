# -*- coding: utf-8 -*-
"""b672_record.py -- THE ACT'S RECORD TOOL, b672 under (R282).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b672's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b671_record.py (the helpers, the guarded landing, the readers); new here: Component 1's record lines
### (b671's weight, the three rules read from the ferry bank verbatim, the ledger-split census item); the later routes are added at their
### components. No kernel byte is written by any route.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b672_record.py <route> [dry]`.
"""
import io
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
PP = 'D:/MY-DOwnloads/PLACE-papers'
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported
import b672_worklist as K          # noqa: E402

SP = K.SP
STANDIN = 'standin' in sys.argv[2:]          # ### the dry-run step's stand-ins, by argument (environment variables left as they are)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(path):
    return io.open(path, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(path) else ''


def rdn(name):
    return rd(os.path.join(D, name))


def put_json(name, obj):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b672's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b672_scanfile_%s.md' % tag)
    R3._write(p, allt.encode('utf-8'))
    sc = R3._scan(p)
    clean = R3._clean(sc)
    ticks = odd_lines(allt)
    unread = [x for x in ('### NOT', 'None', ' ? ', '`?`') if x in allt]
    outside = [n for n in R41.OAI_NEEDLES if n in allt]
    stems = [s for s in ('gap', 'blind') if re.search(r'\b' + s, allt, re.I)]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks by line: %s ; unread figures: %s ; outside names: %s ; '
          'stems: %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', outside or 'NONE',
                         stems or 'NONE'))
    if not clean:
        print(sc[-1500:])
    fired = bool(any(nd.values()) or not clean or ticks or unread or outside or stems)
    return [tuple(c) for c in cells], fired


def land(items, bank, tag, entry=None, check=(), expect_cells=(), dry=True):
    for f, ln, needle in check:
        L = rd(FIND if f == 'FINDINGS.md' else OT).split(NL)
        if needle not in L[ln - 1]:
            sys.exit('### %s :%d DOES NOT CARRY %r -- NOTHING WRITTEN' % (f, ln, needle))
    items = [(f, h, conv(t)) for f, h, t in items]
    cells, fired = screens(items, tag, dry)
    if dry:
        for f, h, t in items:
            print('----', f, NL + t)
        return
    if cells != [tuple(x) for x in expect_cells] or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    n = {'FINDINGS.md': len(rd(FIND).split(NL)), 'OPEN_TRAILS.md': len(rd(OT).split(NL))}
    want = {}
    for f, h, t in items:
        want[h] = n[f] + 1 if rd(FIND if f == 'FINDINGS.md' else OT).endswith(NL) else n[f] + 2
        n[f] += len(t.strip(NL).split(NL)) + 1
    for f, h, _t in items:
        guard_absent(FIND if f == 'FINDINGS.md' else OT, h)
    out = []
    for f, h, t in items:
        path = FIND if f == 'FINDINGS.md' else OT
        r = append_to(path, t)
        got = line_of(path, h)
        out.append(dict(file=f, head=h, line=got, append=r))
        if got != want[h]:
            put_json(bank, dict(entry=entry, lines=out, at=utc(), stopped=True))
            sys.exit('### %s LANDED AT :%s, NOT :%d -- STOPPED' % (h[:60], got, want[h]))
    put_json(bank, dict(entry=entry, lines=out, at=utc()))
    print('  ' + ' ; '.join('%s :%s' % (x['file'], x['line']) for x in out))


# ================================================================================ THE READERS, ONE PER ROW SHAPE A ROUTE READS ((R263)(3))
def read_score_row(k, v):
    """a scores row: key N1..N5, H1..H5 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text)."""
    if not re.match(r'^(N[1-5]|H[1-5]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


READERS = ['read_score_row', 'read_head']


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R282)(1), (2), (7)
def _ruling():
    t = rdn('b672_ferry.txt')
    i, j = t.find('RULING (R282) BEGIN'), t.find('RULING (R282) END')
    if i < 0 or j < i:
        sys.exit('### THE FERRY BANK CARRIES NO (R282) -- NOTHING WRITTEN')
    return t[i:j]


def _clause(n):
    r = _ruling()
    m = re.search(r'\n\(%d\) (.*?)(?=\n\(%d\) |\Z)' % (n, n + 1), r, re.S)
    if not m:
        sys.exit('### (R282)(%d) NOT FOUND IN THE FERRY BANK -- NOTHING WRITTEN' % n)
    return m.group(1).strip()


def rules_texts():
    """the three rules of (R282)(2), each read from the ferry bank verbatim between its curly quotes, never retyped; checked against the
    rules bank written at step zero (data/b672_rules.txt), apostrophes read as one."""
    c = _clause(2)
    rows = re.findall(r'row ([123])\b[^“]*“([^”]+)”', c)
    if [r for r, _x in rows] != ['1', '2', '3']:
        sys.exit('### THE THREE RULES NOT READ FROM (R282)(2) -- NOTHING WRITTEN')
    bank = rdn('b672_rules.txt').replace('’', "'")
    for _r, x in rows:
        if ' '.join(x.split()).replace('’', "'") not in bank:
            sys.exit('### RULE %r NOT IN data/b672_rules.txt AS BANKED -- NOTHING WRITTEN' % x[:50])
    return [' '.join(x.split()) for _r, x in rows]


WH = ('*Appended 2026-10-16 by b672 to b671’s entry (:8761), under `(R282)`(1) -- b671 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b671_closing.txt), ITS REFUTED HYPOTHESIS CARRIED WITH ITS MEASURED CAUSE:*')
HR = ('*Appended 2026-10-16 by b672 under `(R282)`(2) -- THREE RULES, ENTERED AT STEP ZERO (relay data/b672_rules.txt, rows are rules with '
      'their sources):*')
HL = '*Appended 2026-10-16 by b672 under `(R282)`(7) -- THE LEDGER SPLIT, A CENSUS ITEM:*'


def _weight():
    return ('\n' + WH + ' Q0’s 163 points narrowed to half-width 10⁻²⁴ -- 146 on-line at σ = ½ by certified sign change, 17 off-line by '
            'bisection on the count, none unresolved -- under the Bessel bar lowered to 2⁻²⁰⁰ (the b667 bar’s consumer unread, the '
            'navigator’s defect (d)) and the one-time dyadic offset replaced by (4a), a third of the depth’s half-width at any depth whose '
            'quarter cannot be read (the seat’s defect (f)); C1 on the completed ζ function by the same (M-on) machinery and C2’s two planted '
            'shifts read as fixed; the b663 control on the narrowed balls: hQtie 18 of 41, no j₀ read, H3 REFUTED, H1, H2 and H4 HELD; the tie '
            'diagnostic reading every failed control INSTRUMENT and none OBJECT, the radius doubling per j to j ≈ 53 and growing five to a '
            'hundred times per j after, the squaring of complex balls named as the cause; two width figures beneath '
            '`W-ORD-EPSTEIN-BALL-WIDTH` (OPEN_TRAILS :14396), about 10⁻³¹ from the amplification as the trigger and about 1.5·10⁻⁴⁰ as the '
            'linear estimate beside it, the H4 reading bank’s range mis-estimate entered; `W-ORD-MAP-ANGLE-FORM` at :14398 with the trigger '
            '“before the next narrowing act”, the ball-width order re-dated behind it, the control half of `W-ORD-EPSTEIN-CERTIFY` open; the '
            'kernel item at :14406 re-dated with the narrowed balls; the sequence line verbatim at :14384 with its five triggers; the methods '
            'table at 11 READY of 12; the hold breached twice by the host during run 2 (1,522 MB and 2,016 MB free against 2,560), the browser '
            'named in the listing, the watcher reaped and restarted under a standing word, the series banked; the seat changed mid-act and the '
            'handover declared with its listing; the sealed scorer carrying b670’s N5 clause and a text-mode read of a binary bank, N5 scored '
            'through a scratch driver in b663’s form (defect (q)); a root-named bank written after the root by the mid-act check and restored '
            'to its bytes, G-ACTROOT-LAST the one declared failure (defect (r)); the two large banks under .gz with hashes; FINDINGS :8761, '
            'OPEN_TRAILS :14412, relay 64158393 (the closing) after 4e3a46d6 (the record), PLACE-papers d6d2d4b, root 9e045502… over 60 '
            'banks; the suite 85 of 86 pre-push, 84 of 86 on the post-push run with one repository’s remote read twice and 85 of 86 on its '
            'rerun, both banked, the closing’s head line carrying the run’s figure; eighteen defects, the navigator’s (a), (d) and (m). '
            'Nothing deposited.\n')


def _rules():
    r1, r2, r3 = rules_texts()
    return ('\n' + HR + ' (1) held from b671’s defect (r), verbatim (relay data/b671_defects.txt, beneath (r)): “' + r1 + '”; (2) from b671’s '
            'finding (FINDINGS :8761): “' + r2 + '”; (3) from b671’s defect (q): “' + r3 + '”.\n')


def _ledger_split():
    ot = os.path.getsize(OT)
    return ('\n' + HL + ' OPEN_TRAILS.md at %s bytes (about 2 MB) no longer fits the Project’s store; a ledger split, archive-3, in the '
            '2026-08-24 form (PLACE-papers archive/2026-08-24-ledger-split: archive-1 and archive-2 of FINDINGS and OPEN_TRAILS and archive-1 '
            'of VERIFICATION_LOOM, with its README), entered as a census item. **Trigger:** “the b680 reading act”. The kernels with no relay '
            'print bank are listed by name beneath this item at b672 Component 3, from the generator’s NO PRINT BANK cells, as the next runner '
            'items.\n' % format(ot, ','))


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, _weight()), ('OPEN_TRAILS.md', HR, _rules()), ('OPEN_TRAILS.md', HL, _ledger_split())],
         'b672_record_lines.json', 'c1', entry=K.B671_ENTRY,
         check=[('FINDINGS.md', K.B671_ENTRY, '## Q0’s 163 points narrowed'), ('OPEN_TRAILS.md', K.B671_TRAIL, '### b671')], dry=dry)


# ================================================================================ COMPONENT 2: THE ROSTER READ AND THE ONE-COPY LIST
# ### The roster: b670's reading (ii) tables (data/b670_correspondence.json: each table's path and the row it was found by) and
# ### E_DIFFICULTY_THEOREM's table ((R282)(3)); each table's stable anchor (the navigator's answer on the anchor): the file of record, the
# ### heading line above the table, the header row's text. A withheld document's anchor is banked as sha256 and length (b670 rules row 5).
# ### The copy of record per W-ORD-ONE-COPY: the highest versioned copy of OPEN_TRAILS :14386 item (b)'s pair, else the roster's own path.
import correspondence_gen as CG    # noqa: E402
WITHHELD = ('TECHNE_TOOLKIT',)
EDIFF = ('E_DIFFICULTY_THEOREM', 'phase2/method/E_DIFFICULTY_THEOREM_v1_0_4.md', '### Correspondence')
HEADING = re.compile(r'^#{1,6} ')


def _vk(p):
    m = re.search(r'_v(\d+(?:_\d+)*)\.md$', p)
    return tuple(int(x) for x in m.group(1).split('_')) if m else ()


def read_pairs():
    """OPEN_TRAILS :14386 item (b): [(unversioned path, [versioned paths])], read from the census line by its own words."""
    t = rd(OT).split(NL)[K.CENSUS_ITEMS - 1]
    if 'THE CENSUS ITEMS FROM THE MIRROR’S SORTING, AND `W-ORD-ONE-COPY`' not in t:
        sys.exit('### OPEN_TRAILS :%d IS NOT b671`S CENSUS LINE -- NOTHING READ' % K.CENSUS_ITEMS)
    b = t[t.index('(b)'):t.index('**`W-ORD-ONE-COPY`**')]
    out = []
    for u, vs in re.findall(r'([\w./-]+\.md) \(([^)]*)\)', b):
        d = os.path.dirname(u)
        out.append((u, [(d + '/' if d else '') + v.strip() for v in vs.split(',')]))
    return out


def _lines(path):
    return open(os.path.join(PP, path), 'rb').read().decode('utf-8').replace('\r\n', '\n').split('\n')


def _anchor_of(path, row_line):
    """The heading line above the table holding `row_line` (1-based) and its header row: (heading, header, i_header)."""
    L = _lines(path)
    k = row_line - 1
    while k > 0 and L[k - 1].lstrip().startswith('|'):
        k -= 1
    h = next((L[i] for i in range(k - 1, -1, -1) if HEADING.match(L[i])), None)
    return h, L[k], k


def _sha(s):
    import hashlib
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def roster(*a):
    dry = 'dry' in a
    co = jl('b670_correspondence.json')
    pairs = dict(read_pairs())
    cor = {u: max(vs, key=_vk) for u, vs in pairs.items()}
    meta = dict((l.split('|')[1].strip(), [x.strip() for x in l.split('|')]) for l in rdn('b586_corroboration.txt').split(NL)
                if l.startswith('| ') and not l.startswith('| document'))
    src = [(t['doc'], t['path'], t['at']) for t in co['tables']]
    eL = _lines(EDIFF[1])
    src.append((EDIFF[0], EDIFF[1], next(i for i in range(eL.index(EDIFF[2]), len(eL)) if eL[i].startswith('|')) + 1))
    out, T_ = [], []
    for doc, p, at in src:
        h, hdr, k = _anchor_of(p, at)
        rec = p if _vk(p) else cor.get(p, p)
        a_ = dict(doc=doc, b670_path=p, path=rec, withheld=doc in WITHHELD,
                  kernels=[x.strip() for x in (meta.get(doc) or ['', '', '', '', '', ''])[5].split(',') if x.strip().startswith('SIDE-')])
        if doc in WITHHELD:
            a_.update(heading_sha256=_sha(h.rstrip()), header_sha256=_sha(hdr.strip()), heading_len=len(h.rstrip()), header_len=len(hdr.strip()))
        else:
            a_.update(heading=h.rstrip(), header=hdr.strip())
        f0 = CG.find_table(_lines(p), a_)
        f1 = CG.find_table(_lines(rec), a_)
        a_['found_b670'] = f0 if isinstance(f0, str) else [f0[0] + 1, f0[1]]
        a_['found_record'] = f1 if isinstance(f1, str) else [f1[0] + 1, f1[1]]
        if not isinstance(f0, str) and not isinstance(f1, str):
            t0, t1 = _lines(p)[f0[0]:f0[1]], _lines(rec)[f1[0]:f1[1]]
            a_['same_table'] = t0 == t1
            a_['rows'] = [len(t0) - 2, len(t1) - 2]
            a_['rows_differing'] = sum(1 for x, y in zip(t0, t1) if x != y) + abs(len(t0) - len(t1))
        out.append(a_)
        an = ('heading sha256 %s (%d chars) ; header sha256 %s (%d chars)' % (a_['heading_sha256'][:16], a_['heading_len'], a_['header_sha256'][:16],
                                                                             a_['header_len'])) if a_['withheld'] else ('heading %r ; header %r' % (h.rstrip()[:70], hdr.strip()[:90]))
        T_ += ['=== %s' % doc,
               '    file read by b670 %s ; the copy of record %s%s' % (p, rec, '' if rec == p else ' (W-ORD-ONE-COPY: the highest versioned copy)'),
               '    the anchor: %s' % an,
               '    found at b670`s file %s ; at the copy of record %s ; the two tables %s' % (
                   (':%d-:%d' % tuple(a_['found_b670'])) if isinstance(a_['found_b670'], list) else a_['found_b670'],
                   (':%d-:%d' % tuple(a_['found_record'])) if isinstance(a_['found_record'], list) else a_['found_record'],
                   ('IDENTICAL' if a_.get('same_table') else 'DIFFER (%d lines; rows %s)' % (a_.get('rows_differing', -1), a_.get('rows'))) if 'same_table' in a_ else 'NOT COMPARED'),
               '    kernels (b586): %s' % (', '.join(a_['kernels']) or '-')]
    nrec = sum(1 for x in out if isinstance(x['found_record'], list))
    same = sum(1 for x in out if x.get('same_table'))
    H = ['b672 -- THE ROSTER READ, (R282)(3) and the navigator`s answer on the anchor (%s)' % utc(), '',
         '### the tables: the 19 of relay data/b670_correspondence.json (b670`s reading (ii), each found by a row`s text) and E_DIFFICULTY_THEOREM`s',
         '### (%s :%s). Each table`s stable anchor: the heading line above it and its header row, found once in the copy of record; the' % (EDIFF[1], eL.index(EDIFF[2]) + 1),
         '### generator and the after-run reading (ii) find tables by it, and b680`s reading (ii) by the same. TECHNE_TOOLKIT`s anchor as sha256 alone.',
         '### The copy of record: W-ORD-ONE-COPY`s highest versioned copy (OPEN_TRAILS :%d item (b)); the generator writes to it alone.' % K.CENSUS_ITEMS, '']
    S = ['', '### ### **TABLES %d ; ANCHOR FOUND AT THE COPY OF RECORD %d ; COPY OF RECORD NOT b670`S FILE %d ; TABLES IDENTICAL IN BOTH COPIES %d.**' % (
        len(out), nrec, sum(1 for x in out if x['path'] != x['b670_path']), same)]
    print(NL.join(T_ + S))
    if dry:
        return
    put_txt('b672_roster_read.txt', H + T_ + S)
    put_json('b672_roster_read.json', dict(at=utc(), tables=out))


def _standing_hits(base):
    """The standing readers naming `base`: relay's tools at HEAD outside the act tools (tools/bNNN_*), git grep -F, by tool and line."""
    r = subprocess.run(['git', '-C', ROOT, 'grep', '-n', '-F', base, 'HEAD', '--', 'tools/', ':(exclude)tools/b[0-9]*'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return [l[len('HEAD:'):] for l in r.stdout.split(NL) if l.strip()]


def onecopy(*a):
    dry = 'dry' in a
    T_, rows = [], []
    mr = set(f.replace('\\', '/') for f in json.load(io.open(os.path.join(T, 'mirror_roster.json'), encoding='utf-8'))['files'])
    for u, vs in read_pairs():
        top = max(vs, key=_vk)
        ub, tb = _lines(u), _lines(top)
        ts = set(tb)
        only = [l for l in ub if l.strip() and l not in ts]
        lu = g(PP, 'log', '-1', '--format=%h %cs', '--', u).strip()
        lt = g(PP, 'log', '-1', '--format=%h %cs', '--', top).strip()
        hits = _standing_hits(os.path.basename(u))
        wh = any(w in u for w in WITHHELD)
        newer = lu.split()[-1] > lt.split()[-1]
        rows.append(dict(unversioned=u, versions=vs, record=top, identical=ub == tb, only_in_unversioned=len(only), last_unversioned=lu,
                         last_record=lt, unversioned_newer=newer, standing_hits=hits, withheld=wh,
                         mirror=dict(unversioned=u in mr, record=top in mr)))
        T_ += ['=== %s' % u,
               '    versioned copies %s ; THE COPY OF RECORD %s' % (', '.join(os.path.basename(v) for v in vs), os.path.basename(top)),
               '    tools/mirror_roster.json carries: the unversioned copy %s ; the copy of record %s' % (
                   'YES' if u in mr else 'no', 'YES' if top in mr else 'no'),
               '    bytes %s ; lines only in the unversioned copy %d ; last commit: unversioned %s, copy of record %s%s' % (
                   'IDENTICAL' if ub == tb else 'DIFFER', len(only), lu, lt, ' ### THE UNVERSIONED COPY MOVED LAST' if newer else ''),
               '    standing readers naming it (relay tools outside the act tools, at HEAD): %d' % len(hits)]
        T_ += ['        %s' % h[:200] for h in hits]
        if only and not wh:
            T_ += ['    the lines only in the unversioned copy (the first 6, 160 characters each):'] + ['        | %s' % l[:160] for l in only[:6]]
    S = ['', '### ### **PAIRS %d ; IDENTICAL %d ; THE UNVERSIONED COPY MOVED LAST %d ; PAIRS WITH A STANDING READER %d (HITS %d) ; UNVERSIONED '
             'COPIES IN THE MIRROR ROSTER %d (THEIR COPY OF RECORD THERE TOO %d).**' % (
        len(rows), sum(1 for r in rows if r['identical']), sum(1 for r in rows if r['unversioned_newer']),
        sum(1 for r in rows if r['standing_hits']), sum(len(r['standing_hits']) for r in rows),
        sum(1 for r in rows if r['mirror']['unversioned']), sum(1 for r in rows if r['mirror']['unversioned'] and r['mirror']['record']))]
    H = ['b672 -- THE ONE-COPY LIST, (R282)(5) under W-ORD-ONE-COPY (%s)' % utc(), '',
         '### rows are the 25 documents of OPEN_TRAILS :%d item (b), each with its versioned copies and the copy of record (the highest' % K.CENSUS_ITEMS,
         '### versioned copy); the bytes compared; the lines the unversioned copy holds and the copy of record does not (counts; the first six',
         '### printed, a withheld document`s none); each copy`s last commit; and the standing readers -- relay tools at HEAD outside the act',
         '### tools -- that name the unversioned file, each by tool and line (the navigator`s answer (4): a move that breaks a standing reader is',
         '### held until that reader`s path is a bank read). Nothing is moved by this route.', '']
    print(NL.join([l for l in T_ if l.startswith('===') or 'bytes' in l or 'standing readers naming' in l] + S))
    if dry:
        return
    put_txt('b672_one_copy.txt', H + T_ + S)
    put_json('b672_one_copy.json', dict(at=utc(), pairs=rows))


# ================================================================================ THE AUTHOR'S ANSWERS (b671's route, carried by the Edit tool)
def _session_rows():
    """the seat's session from K.ANCHOR, then each continuation (K.SESSIONS_AFTER, b646's form) from its own anchor; a continuation whose
    anchor is not a user line stops the route."""
    for sid, anc in ((K.SESSION_ID, K.ANCHOR),) + K.SESSIONS_AFTER:
        start = None
        for i, raw in enumerate(io.open('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, encoding='utf-8', errors='replace'), 1):
            try:
                o = json.loads(raw)
            except ValueError:
                continue
            if start is None and anc in raw.replace('’', "'") and o.get('type') == 'user' and not o.get('isCompactSummary'):
                start = i
            if start is not None:
                yield i, o, start, sid
        if start is None and sid != K.SESSION_ID:
            sys.exit('### THE ANCHOR %r IS NOT A USER LINE OF SESSION %s -- NOTHING WRITTEN' % (anc, sid))


def answers(*a):
    """data/b672_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; every word of the author
    delivered between BEGIN and END after the ruling (pastes unwrapped from the host's wrapper), and the author's plain messages, verbatim."""
    calls, results, words, plain_, start = [], {}, [], [], None
    for i, o, st, sid in _session_rows():
        start = st if sid == K.SESSION_ID else start
        ln = i if sid == K.SESSION_ID else '%s:%d' % (sid[:8], i)
        m = o.get('message') or {}
        cs = m.get('content')
        att = o.get('attachment') or {}
        texts = []
        if att.get('type') == 'queued_command' and isinstance(att.get('prompt'), str):
            texts = [att['prompt']]
        elif o.get('type') == 'user' and not o.get('isCompactSummary'):
            texts = [cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']
            for t in texts:
                if t and not t.lstrip().startswith(('<', 'BEGIN', 'RULING')) and len(t) < 400 and i > st:
                    plain_.append((ln, t.strip()))
        texts = [re.sub(r'(?s)^\s*<pasted_content[^>]*>\s*(.*?)\s*</pasted_content[^>]*>\s*$', r'\1', t or '') for t in texts]
        ask = set(x[1] for x in calls)
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((ln, c['id'], c['input'], o.get('timestamp')))
                ask.add(c['id'])
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask:
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or '')
                results[c.get('tool_use_id')] = (ln, t, o.get('timestamp'))
                texts.append(t)
        for t in texts:
            for mm in re.finditer(r'(?s)(?:\A\s*|=")BEGIN\s*(.*?)\s*END(?=\s*\Z|")', t or ''):
                if K.ANCHOR not in mm.group(1) and 'RULING (' not in mm.group(1)[:20]:
                    words.append((ln, mm.group(1)))
    if start is None:
        sys.exit('### THE ANCHOR IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    L, n = [], 0
    for i, cid, inp, ts in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %s, %s)' % (cid, K.SESSION_ID, i, ts))
        for k, q in enumerate(inp.get('questions', []), 1):
            n += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT', None))
        L += ['RESULT (transcript line %s, %s): %s' % (r[0], r[2], r[1]), '']
    W, seen = [], set()
    for i, w in words:
        if w in seen:
            continue
        seen.add(w)
        W += ['### THE AUTHOR`S WORD (transcript line %s), BEGIN to END, verbatim:' % i] + w.replace('\r', '').split(NL) + ['']
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %s), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b672 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d)%s.' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start,
                ''.join('; the continuation %s from its first user line carrying %r' % (s[:8], a) for s, a in K.SESSIONS_AFTER)), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b672_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b672_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


ROUTES = {'c1': c1, 'roster': roster, 'onecopy': onecopy, 'answers': answers}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b672_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
