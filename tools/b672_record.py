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


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b672_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b672_findings.json': dict(entry_line=99999, title='stand-in'),
        'b672_trail.json': dict(line=99999),
        'b672_act_root.json': dict(root='0' * 64, previous='9e045502' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
        'b672_mirror.json': dict(zip='stand-in', manifest_md5='0' * 32),
    }


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return _standins().get(name, {}) if STANDIN else {}


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


RUNNER_KEYS = ('kernel', 'branch', 'ref', 'target', 'run_id', 'conclusion', 'artifact_sha256', 'mem_low', 'stopped', 'gate', 'merged', 'tag')


def read_runner_row(r):
    """a row of the last merged run's bank (b669's, read by the standing runner arms) -- every key of RUNNER_KEYS present; raises KeyError.
    Carried from b671_record.py :201-:213 unchanged."""
    missing = [k for k in RUNNER_KEYS if k not in r]
    if missing:
        raise KeyError('runner row without %s' % missing)
    if r['stopped']:
        outcome = 'STOPPED BENEATH THE HOLD ON THE RUNNER'
    elif r['conclusion'] != 'success':
        outcome = 'RUN %s' % (r['conclusion'] or 'NOT CONCLUDED')
    else:
        outcome = 'GATE %s' % (r['gate'] or 'UNREAD')
    return dict(kernel=r['kernel'], outcome=outcome, merged=r['merged'], low=r['mem_low'], above_hold=(r['mem_low'] is not None and r['mem_low'] >= 2560))


CORR_READINGS = ('PRINTED', 'NOT PRINTED', 'NO PRINT BANK', 'ABSENT', 'HELD: DEPOSIT PIN', 'NO TAG', 'NO KERNEL', 'NO DECLARATION',
                 'ROW WITH TOO FEW CELLS', 'INHERITS AN UNREAD ROW')


def read_corr_row(r):
    """a row of the generator's diff bank (data/b672_correspondence_diff.json, a table's `rows`): its line, its kernels, its reading one of
    CORR_READINGS, and a declaration wherever the reading is one the generator reached through a declaration; returns (line, reading)."""
    if not isinstance(r, dict) or not isinstance(r.get('line'), int) or not isinstance(r.get('kernels'), list) or r.get('reading') not in CORR_READINGS:
        raise ValueError('generator row of another shape: %r' % ((r.get('line'), r.get('reading')) if isinstance(r, dict) else r,))
    if r['reading'] in ('PRINTED', 'NOT PRINTED', 'NO PRINT BANK', 'ABSENT') and not r.get('declaration'):
        raise ValueError('a row read through a declaration without one: :%s' % r['line'])
    return r['line'], r['reading']


READERS = ['read_score_row', 'read_head', 'read_runner_row', 'read_corr_row']


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


H_PP = '*Appended 2026-10-16 by b672 under `(R282)`(6) and the navigator’s answer on Component 3’s landing -- **`W-ORD-PROSE-PINS`**:*'
PP_TRIGGER = 'the document’s next re-cut act'


def _prose_pins_text():
    af = jl('b672_correspondence_after.json')
    t = rdn('b672_author_answers.txt')
    i = t.find('W-ORD-PROSE-PINS')
    if i < 0 or PP_TRIGGER not in t[i:i + 600]:
        sys.exit('### W-ORD-PROSE-PINS AND ITS TRIGGER NOT IN THE ANSWERS BANK -- NOTHING WRITTEN')
    rows = [(d['doc'], r['line'], list(dict.fromkeys(q for q, _k, s, _pt in r['pins'] if s == 'BEHIND')), r['cause'])
            for d in af['tables'] for r in d['rows'] if r['cause'].startswith('BEHIND IN CARRIED PROSE')]
    kc = sum(1 for x in rows if 'KERNEL CELL' in x[3])
    return ('\n' + H_PP + ' %d rows of the shaped tables read BEHIND by b670’s method through an old commit in carried prose alone, the kernel '
            'cell’s leading clause at the tag (relay data/b672_correspondence_after.txt; %d in another cell, %d in the kernel cell’s trailing '
            'text), by document and line with the commit each names: %s. Each is a stipulation naming a commit the kernel has moved past, '
            'to be re-pointed or re-dated as historical; the generator carries prose unverified by rule. H2 reads both figures: HELD at the '
            'generator’s claim (0 at the leading clause), REFUTED by b670’s method (these %d). **Trigger:** “%s”.\n' % (
                len(rows), len(rows) - kc, kc, '; '.join('%s :%d (%s)' % (d, ln, ', '.join(q)) for d, ln, q, _c in rows), len(rows), PP_TRIGGER))


def prosepins(*a):
    land([('OPEN_TRAILS.md', H_PP, _prose_pins_text())], 'b672_record_lines_prosepins.json', 'prosepins', entry=None, dry='dry' in a)


def c3(*a):
    dry = 'dry' in a
    land(_c3_texts(), 'b672_record_lines_c3.json', 'c3', entry=None,
         check=[('OPEN_TRAILS.md', LEDGER_SPLIT_LINE, '*Appended 2026-10-16 by b672 under `(R282)`(7) -- THE LEDGER SPLIT'),
                ('OPEN_TRAILS.md', K.CENSUS_ITEMS, 'THE CENSUS ITEMS FROM THE MIRROR’S SORTING')], dry=dry)


# ================================================================================ COMPONENT 3's TWO MEASURED BANKS: H1 AND H3
# ### H1: the generator run again over the written tables, dry (the local tags; no remote call), its print banked whole.
def rerun(*a):
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'correspondence_gen.py'), 'dry'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    out = ((r.stdout or '') + (r.stderr or '')).replace('\r', '')
    m = re.search(r'CELLS CHANGED (\d+) ; FILES CHANGED (\d+)', out)
    L = ['b672 -- (R282)(6) H1: THE GENERATOR RUN AGAIN OVER THE TABLES IT WROTE, DRY (%s), PLACE-papers HEAD %s; exit %d' % (
        utc(), g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), r.returncode), '',
         '### the print of `python -X utf8 tools/correspondence_gen.py dry`, whole:'] + ['    ' + l for l in out.rstrip(NL).split(NL)] + [
        '', '### ### **H1: THE SECOND PASS CHANGES %s CELLS IN %s FILES -- EVERY TABLE ALREADY AT ITS TAG STAYS BYTE-IDENTICAL: %s.**' % (
            m.group(1) if m else '?', m.group(2) if m else '?', 'HELD' if (m and m.group(1) == '0' and m.group(2) == '0' and r.returncode == 0) else 'REFUTED')]
    print(L[-1])
    if 'dry' in a:
        return
    put_txt('b672_gen_rerun.txt', L)


# ### H3 and N3: per file the generator wrote, its line count against the commit before the run, every changed line inside its table's span,
# ### a table row with the cell count it had, no cell left blank that was not blank; the diff bank's cells against the changed cells.
def _table_commit():
    l = [x for x in g(PP, 'log', '--format=%h %s', K.PRE_PP + '..HEAD').split(NL) if 'the Correspondence tables regenerated' in x]
    return l[-1].split()[0] if l else None


def rowskept(*a):
    import correspondence_gen as G_
    tc = _table_commit()
    if not tc:
        sys.exit('### THE GENERATOR`S TABLE COMMIT NOT IN PLACE-papers` LOG -- NOTHING WRITTEN')
    pre = tc + '^'
    ro, dj = jl('b672_roster_read.json'), jl('b672_correspondence_diff.json')
    anchor = {}
    for t in ro['tables']:
        anchor[t['path']] = t
        if t.get('partner'):
            anchor[t['partner']] = t
    files = [x for x in g(PP, 'show', '--name-only', '--format=', tc).split(NL) if x.strip()]
    rows, bad, changed = [], [], 0
    for f in files:
        old = (_show(PP, pre, f) or '').split(NL)
        new = (_show(PP, tc, f) or '').split(NL)
        t = anchor.get(f)
        ft = G_.find_table(new, t) if t else 'NO ANCHOR'
        ch = [i for i, (x, y) in enumerate(zip(old, new)) if x != y]
        changed += len(ch)
        for i in ch:
            if isinstance(ft, str) or not (ft[0] <= i < ft[1]):
                bad.append('%s :%d outside the table' % (f, i + 1))
            if len(G_.spans(old[i])) != len(G_.spans(new[i])):
                bad.append('%s :%d cell count' % (f, i + 1))
            if any(not G_.cell(new[i], sp) for sp in G_.spans(new[i])) and all(G_.cell(old[i], sp) for sp in G_.spans(old[i])):
                bad.append('%s :%d a cell left blank' % (f, i + 1))
        ro_old = sum(1 for l in old if l.lstrip().startswith('|'))
        ro_new = sum(1 for l in new if l.lstrip().startswith('|'))
        if len(old) != len(new) or ro_old != ro_new:
            bad.append('%s lines %d -> %d, table rows %d -> %d' % (f, len(old), len(new), ro_old, ro_new))
        rows.append((f, len(new), len(old) == len(new), ro_old, ro_new, len(ch), ft if isinstance(ft, str) else ':%d-:%d' % (ft[0] + 1, ft[1])))
    ncells = (dj.get('counts') or {}).get('CELLS CHANGED')
    nlist = sum(len(t['changes']) if isinstance(t.get('changes'), list) else (t.get('changes') or 0) for t in dj['tables'])
    pair_cells = sum(p['cells'] for p in dj.get('pairs') or [] if p.get('written'))
    L = ['b672 -- (R282)(6) H3 AND (N3): NO ROW GAINED OR LOST, NO CELL LEFT BLANK, EVERY CHANGE IN THE DIFF BANK (%s)' % utc(), '',
         '### the generator`s table commit PLACE-papers %s against its parent; per file: lines ; equal ; table-row lines before -> after ; lines '
         'changed ; the anchored table`s span' % tc]
    L += ['    %-66s %4d ; %s ; %d -> %d ; %d ; %s' % r_ for r_ in rows]
    L += ['', '### the diff bank (relay data/b672_correspondence_diff.json): cells changed %s, rows listed %d; the partner written identically: '
              '%d cell(s), its row`s change the roster file`s' % (ncells, nlist, pair_cells),
          '### defects: %s' % (bad or 'NONE'),
          '### ### **H3: FILES %d ; LINES CHANGED %d ; ROWS GAINED OR LOST 0 IN %d OF %d FILES ; CHANGED LINES OUTSIDE A TABLE OR WITH A BLANK '
          'OR LOST CELL %d ; DIFF BANK CELLS %s, LISTED %d -- %s.**' % (
              len(files), changed, sum(1 for r_ in rows if r_[2] and r_[3] == r_[4]), len(rows), len(bad), ncells, nlist,
              'HELD' if (not bad and ncells == nlist) else 'REFUTED')]
    print(L[-1])
    if 'dry' in a:
        return
    put_txt('b672_rows_kept.txt', L)


# ================================================================================ THE HYPOTHESES, (R282)(6), READ OFF THE BANKS
def _hyp():
    gr, rk, af, ro, st = rdn('b672_gen_rerun.txt'), rdn('b672_rows_kept.txt'), jl('b672_correspondence_after.json'), jl('b672_roster_read.json'), \
        rdn(K.STATE)
    h1 = re.search(r'\*\*H1: THE SECOND PASS CHANGES (\d+) CELLS IN (\d+) FILES[^*]*: (HELD|REFUTED)\.\*\*', gr)
    h3 = re.search(r'\*\*H3: [^*]* -- (HELD|REFUTED)\.\*\*', rk)
    h2 = af.get('h2') or {}
    two = [t['doc'] for t in ro.get('tables') or [] if isinstance(t.get('partner_found'), list)]
    h5 = '### Appended 2026-10-16 by b672 under (R282)(6) H5' in st and '54 rows to zero (b670: 90)' in st
    return {
        'H1': [h1.group(3) if h1 else 'REFUTED', 'the generator run again, dry, over the tables it wrote: %s cells in %s files (relay data/b672_gen_rerun.txt)' % (
            h1.group(1) if h1 else '?', h1.group(2) if h1 else '?')],
        'H2': ['HELD AT THE GENERATOR’S CLAIM; REFUTED BY b670’S METHOD' if (h2 and h2.get('kernel_cell') == 0 and h2.get('behind')) else
               ('HELD' if h2 and not h2.get('behind') else 'REFUTED'),
               'reading (ii) re-run at the stable anchors over the shaped tables: %s rows behind at the kernel cell`s leading clause, %s by b670`s '
               'method, every one through a commit in carried prose (%s); beside it the remainder %s (relay data/b672_correspondence_after.txt)' % (
                   h2.get('kernel_cell'), h2.get('behind'), h2.get('prose'),
                   ', '.join('%s %d' % kv for kv in sorted((h2.get('remainder') or {}).items())) or 'none')],
        'H3': [h3.group(1) if h3 else 'REFUTED', 'per file the generator wrote, its lines and table rows equal, every changed line a row of its table '
               '(relay data/b672_rows_kept.txt)'],
        'H4': ['NOT HELD' if two else 'HELD', '%d roster tables live in two files, their one-copy partner carrying the same anchored table: nothing '
               'moved this act (the navigator`s answer on the REGISTRY), the carrier `W-ORD-ONE-COPY` (relay data/b672_roster_read.txt)' % len(two)],
        'H5': ['HELD' if h5 else 'REFUTED', 'the dated line beneath relay data/b670_state.txt with the new figure read from relay '
               'data/b672_correspondence_after.txt: 54 rows to zero by b670`s method against b670`s 90, the like-for-like correction (110 at '
               'b670`s tables) beside it'],
    }


def hypotheses(*a):
    H = _hyp()
    for k in H:
        read_score_row(k, H[k])
    L = ['b672 -- (R282)(6): THE HYPOTHESES, EACH READ OFF ITS BANK`S PRINTED LINE (%s)' % utc(), ''] + [
        '  (%s) %s -- %s' % (k, v[0], v[1]) for k, v in sorted(H.items())] + [
        '', '### ### **H1 %s ; H2 %s ; H3 %s ; H4 %s ; H5 %s.**' % tuple(H[k][0] for k in ('H1', 'H2', 'H3', 'H4', 'H5'))]
    print(NL.join(L[2:]))
    if 'dry' in a:
        return
    put_txt('b672_hypotheses.txt', L)
    put_json('b672_hypotheses.json', H)


# ================================================================================ THE LATE ROUTES (b671's, carried by the Edit tool; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for sid, anc in K.SESSIONS_AFTER:
        more = ER.capture('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, anc,
                          'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % sid)
        if not more:
            sys.exit('### THE CONTINUATION SESSION %s READ NO COMMAND (the anchor %r not found as a user line) -- NOTHING WRITTEN' % (sid, anc))
        rows += [dict(r, src=r['src'] + ' ' + sid[:8]) for r in more]
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


MOVE_OR_DELETE = re.compile(r'\bgit\s+(-C\s+\S+\s+)?(mv|rm)\b|\bgit\s+(-C\s+\S+\s+)?branch\s+-[dD]\b|(^|[;&|]\s*|\s)rm\s+-|Remove' + r'-Item|\bos\.remove\b')


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    mv = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    L = ['b672 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1) AND THE MOVES AND DELETES (N4) (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; MOVE OR DELETE COMMANDS %d.**' % (
        len(rows), len(hits), len(lean), len(mv))]
    put_txt('b672_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b672_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean], moves_deletes=[r['n'] for r in mv]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r in mv:
        print('  MOVE OR DELETE #%d: %s' % (r['n'], r['cmd'].split(NL)[0][:200]))


def kernels(*a):
    import b641_record as R41
    put_json('b672_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


DEFECT_ROW = re.compile(r'^    \(([a-z])\) ')


def _defect_short():
    out = []
    L = rdn('b672_defects.txt').split(NL)
    for i, l in enumerate(L):
        if DEFECT_ROW.match(l):
            j = i + 1
            while j < len(L) and L[j].startswith('    ') and not DEFECT_ROW.match(L[j]) and not L[j].startswith('    ###'):
                j += 1
            m = re.match(r'^\(([a-z])\) (.*?)\.(?= |$)', ' '.join(x.strip() for x in L[i:j]))
            if m:
                out.append(m.group(0)[:-1])
    return out


def defects(*a):
    t = rdn('b672_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b672_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b672_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b672_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b672_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands|'
                          r'mirror.*)\.(txt|json|md)$')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b672_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)]
                  + list(K.SHARED_APPENDED))


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if not b_.endswith('.gz') and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b672_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b672'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b672_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith('.gz')][0]
    with tempfile.TemporaryDirectory(prefix='b672_ra_') as tmp:
        cp = os.path.join(tmp, os.path.basename(bank_))
        b_ = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
        b_[0] ^= 0x01
        open(cp, 'wb').write(bytes(b_))
        items2 = [('%s %s' % (bank_, AR.sha256_file(cp)) if it.split()[0] == bank_ else it) for it in J['items']]
    r2 = AR.root_of(items2, J['previous'])
    same = AR.root_of(J['items'], J['previous'])
    late = []
    for it in J['items']:
        p = it.split()
        if p[0].startswith('data/'):
            fp = os.path.join(ROOT, *p[0].split('/'))
            if not os.path.exists(fp) or AR.sha256_file(fp) != p[1]:
                late.append('%s changed' % p[0])
            elif os.path.getmtime(fp) > J.get('at_epoch', 0) + AR.ORDER_SLACK:
                late.append('%s written after the root' % p[0])
    L = ['b672 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b672_root_arm.txt', L)
    put_json('b672_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_final(*a):
    before = _rows_state(json.loads(_show(RELAY, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b672 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b672_table_final.txt', L)
    put_json('b672_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b672_registration_2026-10-16.txt'
FACE = os.path.join(D, 'b672_registration_2026-10-16.txt')


def gatebanks(*a):
    """the gate's steps between the face and the lock (b665's order), each tool's output banked by this route, never by a shell redirect."""
    import gate_hash as G
    env = dict(os.environ, PYTHONIOENCODING='utf-8')

    def runb(args, out):
        r = subprocess.run([sys.executable] + args, capture_output=True, cwd=ROOT, env=env)
        b_ = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            open(p + '.tmp', 'wb').write(b_)
            os.replace(p + '.tmp', p)
        return r.returncode, b_.decode('utf-8', 'replace')
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b672_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b672_regspec.py')], 'b672_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b672_satisfiable.json', '--emit', 'b672'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b672_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b672_census_stepzero.txt'), ('b327_faces_census.py', 'b672_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b672_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b672'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b672_reg_gate.txt', 'data/b672_reg_termscan.txt', 'data/b672_regspec_run.txt', 'data/audit_b672_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES, (N1)-(N5) OF THE FERRY AND THE SEAT'S (S1)-(S3)
# ### carried from b671_record.py :967-:1111 by the Edit tool, every predicate re-written against (R282)'s expectations and this act's banks
import collections                 # noqa: E402
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b671_closing_push_out.txt', 'b670_state.txt')
N5_RELAY_TOOLS = K.GEN_FILES
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
AUTHOR_IDS = ('psinary', 'hotmail', 'orcid', '0009-0008', 'Seale', 'seale')


def TRAIL_HEAD():
    return ('### b672 — lane three, act ninety-nine, the tooling act under (R282): b671 at its weight; three rules; the Correspondence generator '
            'and its four planted cases; the roster’s tables regenerated at their kernels’ tags; the copy of record as REGISTRY names it, nothing moved')


def _calls():
    return jl('b672_author_answers.json').get('calls') or []


def _ledger_adds():
    out = []
    for f in N5_PP:
        old = _show(PP, K.PRE_PP, f) or ''
        now = rd(os.path.join(PP, f))
        out.append(now[len(old):] if now.startswith(old) else now)
    return NL.join(out)


def _first_commit(repo, path, pre):
    """the first commit since the act began that touches `path`: (epoch, short hash), or None."""
    l = [x for x in g(repo, 'log', '--reverse', '--format=%ct %h', pre + '..HEAD', '--', path).split(NL) if x.strip()]
    return (int(l[0].split()[0]), l[0].split()[1]) if l else None


def _pp_written():
    """PLACE-papers files this act wrote beyond the ledgers: the generator's table commit's files and the b651 line's file."""
    tc = _table_commit()
    files = [x for x in g(PP, 'show', '--name-only', '--format=', tc).split(NL) if x.strip()] if tc else []
    return sorted(set(files) | {K.B651_COPY})


def _n1():
    cm = jl('b672_commands.json')
    face = jl('b672_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    unmoved = bool(face) and all(now[k] == list(v) for k, v in face.items())
    loc = g(K.KE, 'rev-parse', '--short=7', K.OPEN_BRANCH).strip()
    rem = g(K.KE, 'rev-parse', '--short=7', 'origin/' + K.OPEN_BRANCH).strip()
    ok = bool(cm) and not cm.get('local_lean') and unmoved and loc == rem == K.OPEN_TIP
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s (relay data/b672_commands.txt); every kernel`s main, tags, branches and '
        'status as the face read them %s; %s at %s locally and %s at its remote-tracking ref' % (
            cm.get('local_lean') if cm else '### UNREAD', unmoved, K.OPEN_BRANCH, loc, rem))


def _n2():
    t = rdn('b672_gen_test.txt')
    four = '### ### **PLANTED CASES 4 ; AS WANTED 4 ; PASS**' in t
    ident = 'PASS bytes identical' in t and 'PASS case (1)`s output run again: identical, 0 cells changed' in t
    bc = _first_commit(RELAY, 'data/b672_gen_test.txt', K.PRE_RELAY)
    tc = _table_commit()
    tct = int(g(PP, 'log', '-1', '--format=%ct', tc).strip()) if tc else None
    order = bool(bc and tct and bc[0] < tct)
    ok = four and ident and order
    return ('HELD' if ok else 'REFUTED'), (
        'the planted cases (relay data/b672_gen_test.txt): four of four as wanted %s, the planted up-to-date table byte-identical after the tool %s; '
        'the bank committed (relay %s) before any table was rewritten (PLACE-papers %s) %s' % (four, ident, bc[1] if bc else '### NONE', tc, order))


def _n3():
    rk = rdn('b672_rows_kept.txt')
    m = re.search(r'\*\*H3: FILES (\d+) ; LINES CHANGED (\d+) ; ROWS GAINED OR LOST 0 IN (\d+) OF (\d+) FILES ; CHANGED LINES OUTSIDE A TABLE OR '
                  r'WITH A BLANK OR LOST CELL (\d+) ; DIFF BANK CELLS (\d+), LISTED (\d+) -- (HELD|REFUTED)\.\*\*', rk)
    ok = bool(m) and m.group(3) == m.group(4) and m.group(5) == '0' and m.group(6) == m.group(7) and m.group(8) == 'HELD'
    return ('HELD' if ok else 'REFUTED'), (
        'per file the generator wrote: no row gained or lost in %s of %s files, changed lines outside a table or with a blank or lost cell %s; '
        'every changed cell in the diff bank with its old and new text, %s cells, %s listed (relay data/b672_rows_kept.txt, '
        'data/b672_correspondence_diff.txt)' % ((m.group(3), m.group(4), m.group(5), m.group(6), m.group(7)) if m else ('?',) * 5))


def _n4():
    cm = jl('b672_commands.json')
    mv = cm.get('moves_deletes') if cm else None
    rows = dict((r['n'], r) for r in (cm.get('rows') or [])) if cm else {}
    moves = [rows[n]['cmd'] for n in (mv or []) if re.search(r'\bgit\s+(-C\s+\S+\s+)?mv\b', rows[n]['cmd'])]
    deletes = [rows[n]['cmd'] for n in (mv or []) if n in rows and not re.search(r'\bgit\s+(-C\s+\S+\s+)?mv\b', rows[n]['cmd'])
               and not re.search(r'\bgit\s+(-C\s+\S+\s+)?branch\s+-d\b', rows[n]['cmd'])]
    v = rd(os.path.join(PP, K.B651_COPY))
    b651 = '*Appended 2026-10-16 by b672, under the author\'s ruling `(R282)`(5) -- b651\'S LINE, CARRIED TO THE COPY OF RECORD:*' in v \
        and '*Appended 2026-10-11 by b651, under the author\'s ruling `(R261)`(3)(d)' in v
    sup = os.path.exists(os.path.join(PP, 'archive', 'superseded'))
    ok = cm is not None and mv is not None and not deletes and not moves and b651 and not sup
    return (('HELD (the move clauses VACUOUS: nothing moved)' if ok else 'REFUTED'),
            'no file deleted: the commands that delete a file %s (relay data/b672_commands.txt; the branch deletes of step zero by name after '
            '--merged listed them); git mv commands %d -- nothing moved, by the navigator`s answer on the REGISTRY, so "every move a git mv on '
            'an explicit path, one per command, after the author`s word" is VACUOUS; archive/superseded made %s; b651`s line on %s, the copy '
            'b651`s ceiling clause names, %s' % (deletes or 'NONE', len(moves), sup, K.B651_COPY, b651))


def _n5():
    face = jl('b672_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    others_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    allowed = set(N5_PP) | set(_pp_written())
    pp_beyond = [x for x in pp_ch if x not in allowed]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b672_|audit_b672_)', x) or re.match(r'^data/terminal_table', x)
                                                or x in N5_RELAY_TOOLS or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b672_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ids = [w for w in AUTHOR_IDS if w in ''.join(rdn(f) for f in ('b672_correspondence_diff.txt', 'b672_correspondence_after.txt'))]
    ok = others_ok and not pp_beyond and not kinds_beyond and not differ and not new_arms and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unsubmitted); no kernel main written, every kernel as the face read it %s; '
            'standing arms added: %s (the act`s arms over its own banks %d); sealed tools not agreeing %s; PLACE-papers beyond the ledgers, the '
            '%d files the generator wrote and b651`s line: %s; relay files of a kind beyond the banks, the act`s tools, the generator and its test, '
            'the root list, b671`s push-out bank and the dated line beneath data/b670_state.txt: %s; "patent" in the ledger lines: %s; author '
            'identifiers in the generator`s banks: %s; outbound requests: the seat`s plain git reads (one ls-remote per kernel repository by the '
            'generator) and pushes to github.com alone, no search made, so no identifier of the author placed in a request' % (
                K.DRAFT, others_ok, new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', len(_pp_written()) - 1, pp_beyond or 'NONE',
                kinds_beyond or 'NONE', pat or 'NONE', ids or 'NONE'))


def scores(*a):
    TF, RA = jl('b672_table_final.json'), jl('b672_root_arm.json')
    _r, _n, sh = seal_hashes()
    S = {
        'N1': _n1(), 'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:500]))
    if 'dry' in a:
        return
    put_json('b672_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else '?'


def _figs():
    dj, af, ro = jl('b672_correspondence_diff.json'), jl('b672_correspondence_after.json'), jl('b672_roster_read.json')
    t = dj.get('tables') or []
    tags = dj.get('tags') or {}
    banks = dj.get('banks') or {}
    h2 = af.get('h2') or {}
    return dict(read=len(t), shaped=sum(1 for x in t if x['status'] == 'SHAPED'), kernels=sum(1 for v in tags.values() if v),
                banks=sum(1 for v in banks.values() if v), nobank=sum(1 for k, v in banks.items() if v is None and tags.get(k)),
                cells=(dj.get('counts') or {}).get('CELLS CHANGED', 0), files=len(dj.get('files') or []),
                absent=(dj.get('counts') or {}).get('ABSENT', 0), notprinted=(dj.get('counts') or {}).get('NOT PRINTED', 0),
                held=(dj.get('counts') or {}).get('HELD: DEPOSIT PIN', 0), behind=(af.get('counts') or {}).get('BEHIND', 0),
                rows=sum(len(x['rows']) for x in af.get('tables') or []), lead=h2.get('kernel_cell'), prose=h2.get('prose'),
                shaped_behind=h2.get('behind'), moved=0, down=len(dj.get('grade_down') or []))


def _num(n):
    return {0: 'no', 1: 'one'}.get(n, str(n))


def _title():
    f = _figs()
    return ('## The Correspondence generator: %d tables regenerated from %d kernels’ tags and %d print banks, %d cells changed, %d '
            'declarations ABSENT at tag, %d kernels without a print bank; %s superseded copy moved; reading (ii) at %d rows behind by b670’s '
            'method, 0 at the leading clause' % (f['shaped'], f['kernels'], f['banks'], f['cells'], f['absent'], f['nobank'], _num(f['moved']),
                                                f['behind']))


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _finding_text():
    S, J, H = jl('b672_scores.json'), jl('b672_act_root.json'), jl('b672_hypotheses.json')
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b672_author_answers.txt'), re.M))
    c1 = _rl_lines('b672_record_lines.json') + ['?'] * 3
    c3 = _rl_lines('b672_record_lines_c3.json') + ['?'] * 6
    pp_ = _rl_lines('b672_record_lines_prosepins.json') + ['?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    mids = re.findall(r'ANSWER CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    hv = ', '.join('%s %s' % (k, (H.get(k) or ['?'])[0]) for k in ('H1', 'H2', 'H3', 'H4', 'H5'))
    e = ['', _title(), '',
         '*Filed at b672 on the author’s ruling `(R282)` and the navigator’s answers (%d questions in %d calls, and the pasted answers). Banks: '
         'relay `data/b672_gen_test.txt`, `data/b672_roster_read.txt`, `data/b672_one_copy.txt`, `data/b672_correspondence_diff.txt`, '
         '`data/b672_correspondence_after.txt`, `data/b672_hypotheses.txt`, `data/b672_act_root.txt`.*' % (n_ans, len(_calls())), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed; the mid-act checks of `(R278)`(4), %d '
         'prints, the last %s of %s OK.' % (cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', len(mids),
                                           mids[-1][1] if mids else '?', mids[-1][0] if mids else '?'), '',
         '**The record lines** (`(R282)`(1), (2), (7)): b671 at its weight (FINDINGS :%s); the three rules (OPEN_TRAILS :%s); the ledger split as '
         'a census item (:%s), the kernels without a print bank beneath it (:%s).' % (c1[0], c1[1], c1[2], c3[0]), '',
         '**The generator** (`(R282)`(4)): relay `tools/correspondence_gen.py` with `tools/test_correspondence_gen.py`, committed alone and again '
         'alone at each answer’s change before the run; it reads each table by its anchor, each kernel’s tag by one ls-remote, the profile from '
         'the latest relay print bank at the tag and the E0 grade from the grade bank, and rewrites the kernel clause’s version and commit, the '
         'one profile token and the leading grade token alone. The four planted cases read as fixed before any table was rewritten, the '
         'up-to-date table byte-identical.', '',
         '**The roster and the copy of record** (`(R282)`(3), (5)): %d tables read at their anchors, %d in the generator’s shape; the one-copy '
         'list of 25 pairs raised before any move; the copy of record as REGISTRY names it (the navigator’s answer on the REGISTRY), so '
         'nothing moved and `W-ORD-ONE-COPY`’s trigger is re-written in full (:%s); b651’s line carried to SIMPLICITY’s v1.1.3.' % (
             f['read'], f['shaped'], c3[5]), '',
         '**The run** (`(R282)`(4), (6)): %d kernels’ tags read, %d of them reached by a print bank; %d cells changed in %d files, no row '
         'gained or lost; ABSENT %d, NOT PRINTED %d, HELD: DEPOSIT PIN %d; %d grade tokens moved downward (`W-ORD-GRADE-MOVED`, :%s), the '
         'print targets owed (`W-ORD-PRINT-TARGETS`, :%s), the absent declarations (`W-ORD-ABSENT-DECLARATIONS`, :%s), the six tables outside '
         'the shape (`W-ORD-TABLE-SHAPE`, :%s).' % (f['kernels'], f['banks'], f['cells'], f['files'], f['absent'], f['notprinted'], f['held'],
                                                    f['down'], c3[2], c3[3], c3[4], c3[1]), '',
         '**Reading (ii)** re-run at the stable anchors: %d rows carrying a commit, %d behind by b670’s method; over the shaped tables %s behind, '
         '0 at the leading clause and every one through a commit in carried prose (`W-ORD-PROSE-PINS`, :%s); b670’s figure of 100 read as 110 '
         'at its own tables, its reader having skipped each anchor row. The hypotheses: %s.' % (
             f['rows'], f['behind'], f['shaped_behind'], pp_[0], hv), '',
         '**The root.** b672 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b670’s reading (ii) and b586’s roster, and corrects b670’s count; '
         'it is re-read by b680’s reading act, which reads the same anchors and prints both figures again, and by each document’s next re-cut '
         'act, where the prose pins, the absent declarations and the downward grades are repaired. It strengthens the programme’s offering of a '
         'corpus a reader can audit: every Correspondence cell the generator writes is a token it read from a named source, and the cells it '
         'did not write are named with their reasons.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; this act wrote no kernel byte.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) “both copies carry the same table” read as an identical table: EXHAUSTIVENESS_LICENSE’s pair written identically, the twelve '
              'pairs already differing named and their partners unwritten (relay data/b672_correspondence_diff.txt); (2) reading (ii)’s change of '
              'method declared in its bank, the tables found by the stable anchors, the rows past each table proper HISTORICAL; (3) H2 printed as '
              'both figures, neither folded into the other')


def _trail_text():
    S, J = jl('b672_scores.json'), jl('b672_act_root.json')
    fj = jl('b672_findings.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b672_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b672_record_lines.json')
    c3 = _rl_lines('b672_record_lines_c3.json') + _rl_lines('b672_record_lines_prosepins.json')
    f = _figs()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R282) ratified.** (1) b671 at its weight. (2) Three rules. (3) The roster’s Correspondence tables. (4) The generator and its '
             'planted cases. (5) One copy of record. (6) The hypotheses. (7) The census items. (8) The mirror export. (9) The draft held at v5, '
             'no kernel byte. (10) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b671’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the rules, the ledger split), :%s (the orders); '
             'this record.' % (c1[0] if c1 else '?', fj.get('entry_line'), ', :'.join(str(x) for x in c1[1:]), ', :'.join(str(x) for x in c3)), '',
             '**Act root:** b672 `%s` (previous `%s`, b671’s; relay data/act_roots.txt), computed after the last bank it names, every one of them '
             'LF.' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d calls (relay data/b672_author_answers.txt), and the navigator’s pasted answers; none '
             'after the root.' % (n_ans, len(_calls())), '',
             '**The generator and the tables:** %d tables regenerated of %d read, %d cells in %d files; ABSENT %d, NOT PRINTED %d, %d kernels '
             'without a print bank; reading (ii) %d behind by b670’s method, 0 at the leading clause; nothing moved.' % (
                 f['shaped'], f['read'], f['cells'], f['files'], f['absent'], f['notprinted'], f['nobank'], f['behind']), '',
             '**The open orders:** `W-ORD-ONE-COPY` with its trigger re-written; `W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; `W-ORD-PRINT-TARGETS`; '
             '`W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; the ledger split at the b680 reading act; the converse on %s at %s, kept, V4 and '
             'V5 at b673.' % (K.OPEN_BRANCH, K.OPEN_TIP), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b672_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b672_scores.json')
    L = ['=' * 104, 'b672 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b672_hypotheses.txt').rstrip(NL).split(NL) + [''] + rdn('b672_defects.txt').rstrip(NL).split(NL)
    put_txt('b672_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b672_scores.json', 'b672_findings.json', 'b672_trail.json', 'b672_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b672_record_lines.json') + ['?']
    f = _figs()
    H = jl('b672_hypotheses.json')
    L = ['b672 -- THE COMPONENTS, BANKED UNDER (R282).', '',
         '### COMPONENT 0 : the citation check (data/b672_citation_check.txt), step zero (data/b672_ferry.txt, data/b672_stepzero.txt, '
         'data/b672_tests_stepzero.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : b671`s weight FINDINGS :%s ; the three rules, the ledger split (data/b672_rules.txt)' % c1[0],
         '### COMPONENT 2 : the generator and its test (tools/correspondence_gen.py, data/b672_gen_test.txt), the roster read, the one-copy list ; '
         'N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the run (data/b672_correspondence_diff.txt) %d cells in %d files, ABSENT %d, NO PRINT BANK kernels %d ; reading (ii) '
         'after (data/b672_correspondence_after.txt) %d behind, 0 at the leading clause ; H %s ; N3 %s ; N4 %s' % (
             f['cells'], f['files'], f['absent'], f['nobank'], f['behind'], ' '.join('%s %s' % (k, (H.get(k) or ['?'])[0]) for k in sorted(H)),
             S['N3'][0], S['N4'][0]),
         '### COMPONENT 4 : the dry-run step (data/b672_reg_gate.txt), the seal (data/b672_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 5 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N1'][0], S['N5'][0])]
    put_txt('b672_components.txt', L)
    print(NL.join(L[2:]))


def _land_one(path, head, e, bank, extra):
    if odd_lines(e):
        sys.exit('### ODD BACKTICKS -- NOTHING WRITTEN: %s' % odd_lines(e)[:3])
    guard_absent(path, head)
    r = append_to(path, e)
    ln = read_head(path, head)
    put_json(bank, dict(extra, line=ln, head=head, append=r))
    return ln


def findings(*a):
    t, e = _finding_text()
    e = conv(e)
    dry = 'dry' in a
    cells, fired = screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells)
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, 'b672_findings.json', dict(title=t))
    j = jl('b672_findings.json')
    j['entry_line'] = ln
    put_json('b672_findings.json', j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = conv(_trail_text())
    dry = 'dry' in a
    cells, fired = screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells)
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b672_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written -- converted by conv and run through the screens their landing runs, the needles the face names read in
    each; prints DRY-RUN STEP : CLEAN and exits 0 only when both screens are quiet and every needle is found. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = conv(text)
        print('  %s (the screens):' % which)
        cells, fired = screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = _face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells and not fired and nd and not miss
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


# ================================================================================ THE MIRROR, AT THE CLOSE ((R282)(8), the b655 form; b670's routes, carried)
import hashlib as _hl   # noqa: E402

MIRROR_TAG = '2026-10-16-b672'
ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % MIRROR_TAG
STAGE = os.path.join(os.environ.get('TEMP', SP), 'mirror-build-%s' % MIRROR_TAG)


def mbuild(*a):
    if os.path.exists(ZIP) or os.path.exists(STAGE):
        sys.exit('### THE ZIP OR ITS STAGE EXISTS -- NOT STARTED')
    loc, rem = g(PP, 'rev-parse', 'HEAD').strip(), (g(PP, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    if loc != rem:
        sys.exit('### PLACE-papers HEAD %s IS NOT THE REMOTE MAIN %s -- NOT STARTED' % (loc[:12], rem[:12]))
    t0 = time.time()
    r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', os.path.join(ROOT, 'tools', 'mirror_build.ps1'), '-DateTag',
                        MIRROR_TAG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_json('b672_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b672':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b672`s -- NOTHING WRITTEN' % last[0])
    line = 'Act root: %s %s' % (last[0], last[1])
    man_p = os.path.join(STAGE, 'MANIFEST.md')
    raw = open(man_p, 'rb').read()
    if b'Act root: ' in raw:
        sys.exit('### THE ROOT LINE IS IN THE STAGED MANIFEST ALREADY -- REFUSING TO WRITE IT TWICE')
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    sep = '\r\n' if '\r\n' in text else '\n'
    out = text.rstrip('\r\n') + sep + sep + line + sep
    before = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    open(man_p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    ps = subprocess.run(['powershell', '-NoProfile', '-Command', "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)],
                        capture_output=True, text=True)
    after = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    put_json('b672_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b672_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
    print(r.stdout[-600:])


def mbank(*a):
    import zipfile
    import b616_record as R6
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    ls = man.decode('utf-8-sig').replace(chr(13), '').split(NL)
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    commits = sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', NL.join(l for l in ls if '|' in l))))
    zb = open(ZIP, 'rb').read()
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b672_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b672 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE MOVES ((R282)(8)): none -- nothing moved this act (the navigator`s answer on the REGISTRY); the roster`s files as before',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b672_mirror.txt', L)
    put_json('b672_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


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


ROUTES = {'c1': c1, 'roster': roster, 'onecopy': onecopy, 'answers': answers, 'after': after, 'c3': c3, 'prosepins': prosepins,
          'rerun': rerun, 'rowskept': rowskept, 'hypotheses': hypotheses, 'commands': commands, 'kernels': kernels, 'defects': defects,
          'root': root, 'root_arm': root_arm, 'table_final': table_final, 'gatebanks': gatebanks, 'scores': scores, 'desk': desk,
          'components': components, 'findings': findings, 'trail': trail, 'drycheck': drycheck,
          'mbuild': mbuild, 'mroot': mroot, 'mverify': mverify, 'mbank': mbank}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b672_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
