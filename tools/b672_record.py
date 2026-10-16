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
    part = {}
    for u, vs in pairs.items():
        part[u], part[max(vs, key=_vk)] = max(vs, key=_vk), u
    for doc, p, at in src:
        h, hdr, k = _anchor_of(p, at)
        rec = p if _vk(p) else cor.get(p, p)
        # ### the navigator's answer on the REGISTRY: the copy of record is as REGISTRY names it, and the generator writes to the roster's file
        # ### (b670's) for each table, and to its one-copy partner too where the partner carries an identical table
        a_ = dict(doc=doc, b670_path=p, path=p, highest_versioned=rec, partner=part.get(p), withheld=doc in WITHHELD,
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
        if a_['partner']:
            fp = CG.find_table(_lines(a_['partner']), a_)
            a_['partner_found'] = fp if isinstance(fp, str) else [fp[0] + 1, fp[1]]
            if not isinstance(fp, str) and not isinstance(f0, str):
                tp = _lines(a_['partner'])[fp[0]:fp[1]]
                t0 = _lines(p)[f0[0]:f0[1]]
                a_['partner_identical'] = tp == t0
                a_['partner_lines_differing'] = sum(1 for x, y in zip(t0, tp) if x != y) + abs(len(t0) - len(tp))
        out.append(a_)
        an = ('heading sha256 %s (%d chars) ; header sha256 %s (%d chars)' % (a_['heading_sha256'][:16], a_['heading_len'], a_['header_sha256'][:16],
                                                                             a_['header_len'])) if a_['withheld'] else ('heading %r ; header %r' % (h.rstrip()[:70], hdr.strip()[:90]))
        pf = a_.get('partner_found')
        T_ += ['=== %s' % doc,
               '    THE FILE WRITTEN: %s (the roster`s file, b670`s) ; its one-copy partner %s%s' % (
                   p, a_['partner'] or '-',
                   '' if not a_['partner'] else (' -- %s' % pf if isinstance(pf, str) else (' carries the table at :%d-:%d, %s' % (
                       pf[0], pf[1], 'IDENTICAL: WRITTEN TOO' if a_.get('partner_identical') else
                       'DIFFERING IN %d LINES: NOT WRITTEN' % a_.get('partner_lines_differing', -1))))),
               '    the highest versioned copy (W-ORD-ONE-COPY`s presumption, corrected by the navigator`s answer on the REGISTRY): %s' % rec,
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
         '### THE FILE WRITTEN (the navigator`s answer on the REGISTRY, which corrects (R282)(5)): the roster`s file for each table, b670`s; and its',
         '### one-copy partner (OPEN_TRAILS :%d item (b)) too where the partner carries an identical table, so that no identical pair diverges' % K.CENSUS_ITEMS,
         '### while W-ORD-ONE-COPY is open; a partner whose table already differs is named and not written. Nothing moves this act.', '']
    S = ['', '### ### **TABLES %d ; ANCHOR FOUND AT THE ROSTER`S FILE %d ; WITH A ONE-COPY PARTNER %d ; PARTNER CARRYING THE TABLE %d ; PARTNER`S TABLE '
             'IDENTICAL (WRITTEN TOO) %d ; ANCHOR FOUND AT THE HIGHEST VERSIONED COPY %d ; TABLES IDENTICAL THERE %d.**' % (
        len(out), sum(1 for x in out if isinstance(x['found_b670'], list)), sum(1 for x in out if x['partner']),
        sum(1 for x in out if isinstance(x.get('partner_found'), list)), sum(1 for x in out if x.get('partner_identical')), nrec, same)]
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


# ================================================================================ COMPONENT 3: b670'S READING (ii) RE-RUN, AT THE STABLE ANCHORS
# ### b670's method (tools/b670_record.py corr): a row is a table line carrying a backticked commit; each commit resolved in the kernels
# ### b586 lists for the document, else in every local kernel clone (marked *); set against that kernel's tag (git describe --tags --abbrev=0
# ### main, peeled -- local; the run's one ls-remote per repository was the generator's, data/b672_correspondence_diff.json, printed beside):
# ### AT THE TAG, BEHIND, OFF THE TAG'S LINE, UNRESOLVED, NO TAG; a row is BEHIND when any of its commits is. THE CHANGE OF METHOD, declared:
# ### each table is found by its stable anchor (data/b672_roster_read.json) and not by a row's text, and its span is b670's (the table to
# ### b670's span end) -- the rows past the table proper are HISTORICAL; E_DIFFICULTY_THEOREM's span is its table. b680 reads the same.
HEX7 = re.compile(r'`([0-9a-f]{7,40})`')
ALLK = sorted(x for x in os.listdir('D:/') if x.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', x, '.git')))


def _anc(kd, a, b):
    return subprocess.run(['git', '-C', kd, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0


def _ltag(k):
    t = g('D:/' + k, 'describe', '--tags', '--abbrev=0', 'main').strip()
    return (t, g('D:/' + k, 'rev-parse', '--short', t + '^{commit}').strip()) if t else ('NO TAG', '')


def _has(k, q):
    return subprocess.run(['git', '-C', 'D:/' + k, 'cat-file', '-e', q + '^{commit}'], capture_output=True).returncode == 0


def after(*a):
    dry = 'dry' in a
    ro, dj, co = jl('b672_roster_read.json'), jl('b672_correspondence_diff.json'), jl('b670_correspondence.json')
    gen = dict((t['doc'], t) for t in dj['tables'])
    b670 = dict((t['doc'], t) for t in co['tables'])
    tags, out, tot = {}, [], {}
    import collections
    cat = collections.Counter()
    for t in ro['tables']:
        L = _lines(t['path'])
        ft = CG.find_table(L, t)
        gt = gen[t['doc']]
        if isinstance(ft, str):
            out.append(dict(doc=t['doc'], found=ft, rows=[]))
            continue
        j, e = ft
        end = b670[t['doc']]['end'] if t['doc'] in b670 and b670[t['doc']].get('end') else e
        cols = CG.columns(L[j])
        greading = dict((r['line'], r.get('reading')) for r in gt.get('rows', []))
        rows = []
        for i in range(j + 1, max(end, e)):
            l = L[i]
            if not l.lstrip().startswith('|'):
                continue
            pins = HEX7.findall(l)
            if not pins:
                continue
            res = []
            for q in pins:
                hit = [k for k in t['kernels'] if _has(k, q)] or [k + '*' for k in ALLK if k not in t['kernels'] and _has(k, q)]
                if not hit:
                    res.append((q, None, 'UNRESOLVED', '-'))
                    continue
                k = hit[0].rstrip('*')
                if k not in tags:
                    tags[k] = _ltag(k)
                tc = tags[k][1]
                st = 'NO TAG' if not tc else ('AT THE TAG' if _anc('D:/' + k, tc, q) else ('BEHIND' if _anc('D:/' + k, q, tc) else 'OFF THE TAG`S LINE'))
                res.append((q, hit[0], st, g('D:/' + k, 'describe', '--tags', '--abbrev=0', q).strip() or 'NO TAG AT OR BEFORE IT'))
            sts = [r_[2] for r_ in res]
            reading = 'BEHIND' if 'BEHIND' in sts else ('UNRESOLVED' if all(s == 'UNRESOLVED' for s in sts) else
                                                     ('AT THE TAG' if all(s in ('AT THE TAG', 'UNRESOLVED') for s in sts) else sts[0]))
            # ### the cause, for the rows the generator's tables hold
            if gt['status'] != 'SHAPED':
                why = 'NOT IN SHAPE'
            elif i >= e:
                why = 'HISTORICAL'
            elif greading.get(i + 1) in ('ABSENT', 'HELD: DEPOSIT PIN', 'INHERITS AN UNREAD ROW', 'ROW WITH TOO FEW CELLS', 'NO TAG'):
                why = greading.get(i + 1)
            elif reading == 'BEHIND':
                # ### the generator's claim is the kernel cell's leading clause (its version and commit tokens); a behind commit anywhere else
                # ### -- the kernel cell's trailing prose or another cell -- is carried prose (the navigator's answers on readings (1) and (8))
                sp = CG.spans(l)
                kc = CG.cell(l, sp[cols['kernel']]) if cols['kernel'] is not None and len(sp) > cols['kernel'] else ''
                lead = [tx for _k, toks in CG.parse_kernel_cell(kc) for _s, _e, kind, tx in toks if kind == 'hex']
                if any(r_[2] == 'BEHIND' and any(r_[0].startswith(x) or x.startswith(r_[0]) for x in lead) for r_ in res):
                    why = 'BEHIND AT THE LEADING CLAUSE'
                elif any(r_[2] == 'BEHIND' and ('`%s`' % r_[0]) in kc for r_ in res):
                    why = 'BEHIND IN CARRIED PROSE (THE KERNEL CELL`S TRAILING TEXT)'
                else:
                    why = 'BEHIND IN CARRIED PROSE (ANOTHER CELL)'
            else:
                why = 'SHAPED, ' + reading
            rows.append(dict(line=i + 1, pins=res, reading=reading, cause=why))
            cat[(reading, why)] += 1
        out.append(dict(doc=t['doc'], path=t['path'], found=[j + 1, e], end=end, status=gt['status'], rows=rows))
    n = sum(len(d['rows']) for d in out)
    rd_ = collections.Counter(r['reading'] for d in out for r in d['rows'])
    shaped_behind = [(d['doc'], r) for d in out for r in d['rows'] if d.get('status') == 'SHAPED' and r['reading'] == 'BEHIND']
    h2 = [x for x in shaped_behind if x[1]['cause'].startswith('BEHIND ')]
    h2k = [x for x in h2 if x[1]['cause'] == 'BEHIND AT THE LEADING CLAUSE']
    T_ = ['b672 -- COMPONENT 3, (R282)(6) H2: b670`S READING (ii) RE-RUN AFTER THE GENERATOR (%s)' % utc(), '',
          '### the method: b670`s (tools/b670_record.py corr) -- a row is a table line carrying a backticked commit, each commit resolved in the',
          '### kernels b586 lists for the document (else every local clone, marked *) and set against the kernel`s tag (local describe on main).',
          '### THE CHANGE OF METHOD, DECLARED (the navigator`s answer on the anchor): each table found by its stable anchor (relay',
          '### data/b672_roster_read.json) and not by a row`s text; the span b670`s (the table to b670`s span end), the rows past the table proper',
          '### HISTORICAL; E_DIFFICULTY_THEOREM`s span its table. b680`s reading (ii) uses the same anchors. The files: the roster`s, as written.',
          '### THE TAGS (local; the generator`s one ls-remote per repository beside, relay data/b672_correspondence_diff.json):']
    T_ += ['    %-34s %s at %s ; the generator`s read %s' % (k, v[0], v[1], (dj['tags'].get(k) or ['-', ''])[0] + ' ' + ((dj['tags'].get(k) or ['', ''])[1] or '')[:7]
                                                            if k in dj['tags'] else 'NOT READ BY THE GENERATOR') for k, v in sorted(tags.items())]
    T_ += ['', '### THE ROWS WITH A COMMIT (document :line ; reading ; cause ; each commit, its kernel, its reading, its tag); a withheld document`s rows by count']
    for d in out:
        if isinstance(d.get('found'), str):
            T_.append('=== %-36s ### ANCHOR NOT FOUND: %s' % (d['doc'], d['found']))
            continue
        cn = collections.Counter(r['reading'] for r in d['rows'])
        T_.append('=== %-36s %s :%d-:%d (span to :%d) %s ; rows with a commit %d ; %s' % (d['doc'], d['path'], d['found'][0], d['found'][1], d['end'],
                                                                                         d['status'], len(d['rows']), dict(cn) or 'NONE'))
        for r in d['rows']:
            if d['doc'] in WITHHELD:
                continue
            T_.append('    :%-5d %-12s %-40s %s' % (r['line'], r['reading'], r['cause'], ' ; '.join('%s %s %s %s' % (q, k or '-', s, pt) for q, k, s, pt in r['pins'])))
    T_ += ['', '### THE ROWS BY READING AND CAUSE:'] + ['    %-12s %-42s %d' % (k[0], k[1], v) for k, v in sorted(cat.items())]
    # ### like with like: b670's reader began at the row after the row it found each table by (range(i0 + 1, j)), so each anchor row went
    # ### unread (defect (e), b670's); this reading reads it. The rows new to this reading, set against b670's rows in the same files.
    newrows = []
    for d in out:
        bt = b670.get(d['doc'])
        if bt and bt.get('rows') is not None and 'found' in d and not isinstance(d['found'], str):
            bl = set(r['line'] for r in bt['rows'])
            newrows += [(d['doc'], r['line'], r['line'] == bt.get('at')) for r in d['rows'] if r['line'] not in bl]
    T_ += ['', '### LIKE WITH LIKE: the rows with a commit new to this reading against b670`s, in b670`s tables (document :line ; b670`s anchor row?):']
    T_ += ['    %s :%d ; %s' % (x[0], x[1], 'b670`S ANCHOR ROW, WHICH ITS READER SKIPPED' if x[2] else '### NOT b670`S ANCHOR ROW') for x in newrows] or ['    none']
    T_ += ['### ### **b670`S TABLES: ROWS WITH A COMMIT %d = b670`S 100 + %d ANCHOR ROWS ITS READER SKIPPED + %d OTHER ; E_DIFFICULTY_THEOREM`S TABLE, NEW TO '
           'THE ROSTER, %d.**' % (n - sum(len(d['rows']) for d in out if d['doc'] == EDIFF[0]), sum(1 for x in newrows if x[2]),
                                   sum(1 for x in newrows if not x[2]), sum(len(d['rows']) for d in out if d['doc'] == EDIFF[0]))]
    rem = collections.Counter(r['cause'] for d in out for r in d['rows'] if r['reading'] == 'BEHIND' and not r['cause'].startswith('BEHIND '))
    pro = collections.Counter(r['cause'] for _d, r in h2 if r['cause'] != 'BEHIND AT THE LEADING CLAUSE')
    T_ += ['', '### ### **ROWS WITH A COMMIT %d (b670: 100) ; AT THE TAG %d (b670: 3) ; BEHIND %d (b670: 90) ; UNRESOLVED %d (b670: 2) ; OTHER %d (b670: 5).**' % (
        n, rd_['AT THE TAG'], rd_['BEHIND'], rd_['UNRESOLVED'], n - rd_['AT THE TAG'] - rd_['BEHIND'] - rd_['UNRESOLVED']),
        '### ### **H2, OVER THE SHAPED TABLES, BY b670`S METHOD: ROWS BEHIND %d -- AT THE LEADING CLAUSE (THE GENERATOR`S CLAIM) %d ; BY A COMMIT IN '
        'CARRIED PROSE ALONE %d (%s) ; BESIDE IT, THE REMAINDER BEHIND BY NAME: %s.**' % (
            len(h2), len(h2k), len(h2) - len(h2k), '; '.join('%s %d' % kv for kv in sorted(pro.items())) or 'none',
            '; '.join('%s %d' % kv for kv in sorted(rem.items())) or 'none')]
    print(NL.join([l for l in T_ if l.startswith('===') or l.startswith('### ### **') or (l.startswith('    ') and l.strip()[:1].isupper() and 'BEHIND' in l[:20])]))
    print(NL.join(T_[T_.index('### THE ROWS BY READING AND CAUSE:'):]))
    if dry:
        return
    put_txt('b672_correspondence_after.txt', T_)
    put_json('b672_correspondence_after.json', dict(at=utc(), tags=tags, tables=out, counts=dict(rd_), causes={'%s | %s' % k: v for k, v in cat.items()},
                                                    h2=dict(behind=len(h2), kernel_cell=len(h2k), prose=len(h2) - len(h2k), remainder=dict(rem))))


# ================================================================================ COMPONENT 3: THE RECORD LINES OF THE RUN
# ### Every figure and list read from the run's banks (data/b672_correspondence_diff.json, _after.json, _roster_read.json, _one_copy.json)
# ### and every quoted trigger read from the answers bank (data/b672_author_answers.txt) between its curly quotes, never retyped.
LEDGER_SPLIT_LINE = 14438
H_NPB = ('*Appended 2026-10-16 by b672 beneath the ledger-split item (:%d), under `(R282)`(7) -- THE KERNELS WITH NO RELAY PRINT BANK AT '
         'THEIR TAG, THE NEXT RUNNER ITEMS:*' % LEDGER_SPLIT_LINE)
H_TS = '*Appended 2026-10-16 by b672 under `(R282)`(4) and the navigator’s answer on readings 5–8 -- **`W-ORD-TABLE-SHAPE`**:*'
H_GM = '*Appended 2026-10-16 by b672 under `(R282)`(4) and the navigator’s answer on the four tabs -- **`W-ORD-GRADE-MOVED`**:*'
H_PT = '*Appended 2026-10-16 by b672 under `(R282)`(4) and the navigator’s answer on the NOT PRINTED cells -- **`W-ORD-PRINT-TARGETS`**:*'
H_AD = '*Appended 2026-10-16 by b672 under `(R282)`(6) and the navigator’s answer on the ABSENT count -- **`W-ORD-ABSENT-DECLARATIONS`**:*'
H_OC = ('*Appended 2026-10-16 by b672 under `(R282)`(5) and the navigator’s answer on the REGISTRY, beneath b671’s census items (:%d) -- '
        '**`W-ORD-ONE-COPY`**, ITS TRIGGER RE-WRITTEN IN FULL; NOTHING MOVED:*' % K.CENSUS_ITEMS)


def _quoted(after_words, n=1):
    """the n-th curly-quoted text after `after_words` in the answers bank, whitespace joined."""
    t = rdn('b672_author_answers.txt')
    i = t.find(after_words)
    if i < 0:
        sys.exit('### %r NOT IN THE ANSWERS BANK -- NOTHING WRITTEN' % after_words)
    q = re.findall(r'“([^”]+)”', t[i:])
    if len(q) < n:
        sys.exit('### NO QUOTED TEXT AFTER %r -- NOTHING WRITTEN' % after_words)
    return ' '.join(q[n - 1].split())


def _c3_texts():
    import collections
    dj, af, ro, oc = jl('b672_correspondence_diff.json'), jl('b672_correspondence_after.json'), jl('b672_roster_read.json'), jl('b672_one_copy.json')
    tables = dict((t['doc'], t) for t in dj['tables'])
    # ### the kernels with no print bank at their tag, each with its NO PRINT BANK cells
    npb = sorted(k for k, v in dj['banks'].items() if v is None and dj['tags'].get(k))
    npb_txt = '; '.join('%s at %s (%d cell%s)' % (k, dj['tags'][k][0], (dj['by_kernel'].get(k) or {}).get('NO PRINT BANK', 0),
                                                   '' if (dj['by_kernel'].get(k) or {}).get('NO PRINT BANK', 0) == 1 else 's') for k in npb)
    t1 = ('\n' + H_NPB + ' %d kernels whose tag no relay print bank reaches (relay data/b672_correspondence_diff.txt, the print banks read '
          'beside each tag): %s. Each is a runner build at its tag with the declarations its roster rows cite in print_targets.txt; until then '
          'its rows read NO PRINT BANK AT <tag> and their grade tokens UNREFRESHED.\n' % (len(npb), npb_txt))
    # ### W-ORD-TABLE-SHAPE: the six tables, each with its header (a withheld document's by its column count alone)
    six = [t for t in ro['tables'] if tables[t['doc']]['status'].startswith('NOT IN')]
    six_txt = '; '.join(('%s (`%s`, its header withheld under b670’s rules row 5, %d characters)' % (t['doc'], t['path'], t['header_len']))
                        if t.get('withheld') else ('%s (`%s`, its header “%s”)' % (t['doc'], t['path'], t['header'].strip().strip('|').strip()))
                        for t in six)
    t2 = ('\n' + H_TS + ' %d roster tables outside the generator’s shape (no kernel, terminal or profile column), read and left byte-identical '
          'by the generator, each with its header: %s. Bringing a table into the shape changes its form and is not the generator’s to do. '
          '**Trigger:** “%s”.\n' % (len(six), six_txt, _quoted('W-ORD-TABLE-SHAPE, entered for the six tables with the trigger')))
    # ### W-ORD-GRADE-MOVED: the downward grade moves
    gd = dj.get('grade_down') or []
    t3 = ('\n' + H_GM + ' %d status cells whose leading grade token the generator moved downward to the grade bank’s E0 grade (relay '
          'data/terminal_table.json), listed before the write (relay data/b672_correspondence_diff.txt): %s. A downgrade produces a repair or '
          'a named order, and a cell alone closes nothing. **Trigger:** “%s”.\n' % (
              len(gd), '; '.join('%s :%d (%s) %s → %s' % (d['doc'], d['line'], d['kernel'], d['old'], d['new']) for d in gd),
              _quoted('W-ORD-GRADE-MOVED, with the trigger')))
    # ### W-ORD-PRINT-TARGETS: the NOT PRINTED declarations by kernel (the kernel the generator read the row at: its profile change's)
    chk = dict(((c['doc'], c['line']), (c['kernel'], c['new'])) for t in dj['tables'] if isinstance(t.get('changes'), list) for c in t['changes']
               if c['column'] == 'profile')
    byk, left = collections.defaultdict(list), []
    for t in dj['tables']:
        for r in t['rows']:
            if r.get('reading') == 'NOT PRINTED':
                k, new = chk.get((t['doc'], r['line'])) or ((r['kernels'][0] if r['kernels'] else '-'), '')
                byk[k].append('`%s` (%s :%d)' % (r['declaration'], t['doc'], r['line']))
                if 'NOT PRINTED AT' not in new:
                    left.append('%s :%d' % (t['doc'], r['line']))
    npt = sum(len(v) for v in byk.values())
    t4 = ('\n' + H_PT + ' %d declarations present at their kernel’s tag that the kernel’s qualifying print bank did not print (the navigator '
          'named 46 from the dry run at the highest versioned copies; the run at the roster’s files reads %d): %d profile cells read NOT '
          'PRINTED AT <tag> with the verified profile and its pin beside, and %d were left as they stood, holding no single profile token (%s). '
          'By kernel: %s. The repair is a print, not a word. **Trigger:** “%s”.\n' % (
              npt, npt, npt - len(left), len(left), ', '.join(left) or 'none',
              ' | '.join('%s (%d): %s' % (k, len(v), ', '.join(v)) for k, v in sorted(byk.items())),
              _quoted('W-ORD-PRINT-TARGETS, listed by kernel, with the trigger')))
    # ### W-ORD-ABSENT-DECLARATIONS
    ab = [(t['doc'], r['line'], r.get('declaration'), (r['kernels'] or ['-'])[0]) for t in dj['tables'] for r in t['rows'] if r.get('reading') == 'ABSENT']
    abl = ['%s :%d' % (d, ln) for d, ln, _x, _k in ab if 'ABSENT AT' not in (chk.get((d, ln)) or ('', ''))[1]]
    t5 = ('\n' + H_AD + ' %d table rows whose declaration their kernel does not declare at its tag, each keeping its pin -- %d profile cells '
          'reading ABSENT AT <tag>, %d left as they stood, holding no single profile token (%s) -- by document and kernel: %s. Each is a '
          'sentence citing a terminal the kernel does not hold, to be re-cut to what the kernel holds or re-pointed to the declaration that '
          'replaced it; H2 counts them beside its figure, not in it. **Trigger:** “%s”.\n' % (
              len(ab), len(ab) - len(abl), len(abl), ', '.join(abl) or 'none', '; '.join('%s :%d `%s` (%s)' % x for x in ab),
              _quoted('W-ORD-ABSENT-DECLARATIONS, listed by document and kernel, with the trigger')))
    # ### W-ORD-ONE-COPY: the trigger re-written in full, the pairs beneath with their readers
    pp = []
    for r in oc['pairs']:
        hits = ['%s :%s' % tuple(h.split(':', 2)[:2]) for h in r['standing_hits']]
        pp.append('`%s` (its highest versioned copy %s%s)' % (r['unversioned'], os.path.basename(r['record']),
                                       ('; relay readers: ' + ', '.join(hits)) if hits else '; no relay reader'))
    t6 = ('\n' + H_OC + ' the copy of record is as REGISTRY names it -- REGISTRY is the source of truth -- and `(R282)`(5)’s presumption '
          'that the highest versioned copy is the copy of record is the navigator’s defect, entered (relay data/b672_defects.txt (c)); the '
          'generator wrote the roster’s file for each table, and the partner copy where it carried an identical table. **Trigger:** “%s”. '
          'The %d pairs, each with its relay readers by tool and line (relay data/b672_one_copy.txt; REGISTRY’s file column besides, read '
          'at the move: :214, :663, :227, :681, :909, :1056 for the four struck): %s.\n' % (
              _quoted('trigger re-written in full'), len(pp), '; '.join(pp)))
    return [('OPEN_TRAILS.md', H_NPB, t1), ('OPEN_TRAILS.md', H_TS, t2), ('OPEN_TRAILS.md', H_GM, t3), ('OPEN_TRAILS.md', H_PT, t4),
            ('OPEN_TRAILS.md', H_AD, t5), ('OPEN_TRAILS.md', H_OC, t6)]


def c3(*a):
    dry = 'dry' in a
    land(_c3_texts(), 'b672_record_lines_c3.json', 'c3', entry=None,
         check=[('OPEN_TRAILS.md', LEDGER_SPLIT_LINE, '*Appended 2026-10-16 by b672 under `(R282)`(7) -- THE LEDGER SPLIT'),
                ('OPEN_TRAILS.md', K.CENSUS_ITEMS, 'THE CENSUS ITEMS FROM THE MIRROR’S SORTING')], dry=dry)


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


ROUTES = {'c1': c1, 'roster': roster, 'onecopy': onecopy, 'answers': answers, 'after': after, 'c3': c3}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b672_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
