# -*- coding: utf-8 -*-
"""b697_record.py -- THE ACT'S RECORD TOOL, b697 under (R307).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b697's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b696_record.py (and b695_record.py's re-cut and faces routes) in stages: the helpers, the guarded landing, the
### readers, step zero's rowgen and branches routes, the answers and defects routes first (stage one); Component 1's weight line; the faces
### routes at Component 2; the re-cut routes at Component 3; the late routes at Component 5. Every python child is started as `python -X utf8`,
### no environment mapping passed.
### Routes: `python tools/b697_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
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
import b697_worklist as K          # noqa: E402

SP = K.SP
STANDIN = 'standin' in sys.argv[2:]          # ### the dry-run step's stand-ins, by argument (environment variables left as they are)
RELAY = ROOT
ACT, PREV = 'b697', 'b696'


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
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank (b696's, carried)."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b697_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b697_findings.json': dict(entry_line=99999, title='stand-in'),
        'b697_trail.json': dict(line=99999),
        'b697_act_root.json': dict(root='0' * 64, previous='8d5b3d9d' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return _standins().get(name, {}) if STANDIN else {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def grc(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').returncode


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def _vl(name):
    return ([x for x in rdn(name).split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b697's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, '%s_scanfile_%s.md' % (ACT, tag))
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


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R307)(1)
WH = ('*Appended 2026-10-21 by b697 to b696’s entry (:9624), under `(R307)`(1) -- b696 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b696_closing.txt):*')
WB = (' “b696 closed: relay 564e9bb9, PLACE-papers 345da1a; suite 118 of 118; root 8d5b3d9d32ec5804…; 3 prompts answered; 4 defects” '
      '(data/b696_closing.txt :1), the closing 77b55588 pushed and read back at relay main (data/b696_closing_push_out.txt :5). '
      'W-ORD-WITNESS-TAIL-BALLS DISCHARGED: the archimedean tail a certified ball from DLMF (5.11.2) and its remainder bound, fetched, banked '
      'and cited by line (data/b696_source_dlmf_5_11.txt :393-:399), 3.68e-23 at a = 32 where b694’s float bound was 1.43e-18; the zero tail a '
      'certified ball on P3’s count law with b685’s constants a and c as balls, P3 named as its one premise, 4.02e-9 at a = 32 where the float '
      'was 2.41e-4, entering the identity’s tolerance that gates each width’s reading and not the sum’s radius (data/b696_witness_balls.txt '
      ':14; data/b696_tails_plan.txt :6-:17); every width b694 read FOUND reading FOUND with the ball radius, a = 32 to 192, the narrowest '
      'margin at a = 32, −7.7752874967979 ± 3.68e-23 (:33); the ζ control nonnegative at 16 of 16 widths before any Q0 term, the identity at '
      '34 of 34 cells, every tail ball shrinking with its height as its bound predicts at 33 of 33, T1 as re-worded holding '
      '(data/b696_witness_balls_controls.txt). G-RULE-BINARY-HASHES reading a frozen row as carried where a corrigendum covers it, b694’s PNG '
      'through corrigenda row (9), the planted row with no corrigendum failing, 5 of 5 (data/b696_arm_binary.txt), the one shared-tool edit '
      'sealed with the act. The faces successor drafted and held, the seat noting beside it that the unchanged remainder still carries b694’s '
      '“± 1.43e-18” (data/b696_faces_rows.txt :11, :22). The suite 118 of 118 before and after the push, every control behaving, no failure '
      'carried; all eight scores HELD (data/b696_scores_close.json); the sealed tools 11 of 11 (data/b696_closing.txt :17); the root 8d5b3d9d '
      'over 56 banks; no lean on the host, no runner dispatched; mirror-refresh-2026-10-20-b696.zip CLEAN with the root line. Four defects, '
      '(a)-(c) the navigator’s -- the height row b681’s hashes bank does not carry, the page’s line number cited on the node list, the zero '
      'tail written into the sum’s radius -- and (d) the seat’s bank-route KeyError, repaired before any bank was written '
      '(data/b696_defects.txt :6-:31). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B696_ENTRY,
         check=[('FINDINGS.md', K.B696_ENTRY, '## The Weil-face witness at Q0 with its tail bounds as certified balls'),
                ('OPEN_TRAILS.md', K.B696_TRAIL, '### b696')], dry=dry)


# ================================================================================ COMPONENT 2: THE FACES ROW, (R307)(2)
RADIUS_OLD, RADIUS_NEW = '± 1.43e-18', '± 3.68e-23'
CAVEAT_B696 = ('tail bounds as certified balls (b696), the zero tail on P3, derived and not compiled; a numerical reading at a certified object, '
               'consistent with Weil’s criterion at an instance with zeros off the line — not a theorem about Q0')
HEAD_OLD = ("*(Appended under the author's word on (R305)(4), 2026-10-20, b695, drafted under (R304)(4), 2026-10-20, b694, through the node "
            "list's backmatter record.)*")
HEAD_NEW = ("*(Appended under the author's word on (R305)(4), 2026-10-20, b695, drafted under (R304)(4), 2026-10-20, b694, regenerated under the "
            "author's word on (R307)(2), 2026-10-21, b697, drafted under (R306)(4), 2026-10-20, b696, through the node list's backmatter record.)*")


def _caveat_new():
    """(R307)(2)'s caveat, read from the banked ruling (data/b697_ferry.txt), the quotation opening "tail bounds as certified balls (b696);"."""
    fl = [l for l in rdn('b697_ferry.txt').split(NL) if l.startswith('(2) THE WEIL-FACE ROW')]
    m = re.search(r'“(tail bounds as certified balls \(b696\);.*?)”', fl[0]) if len(fl) == 1 else None
    return m.group(1) if m else ''


def successor():
    """the row as (R307)(2) orders it: b696's successor (data/b696_faces_rows.txt :11) with the radius read from the a = 32 row and the caveat
    read from the ruling; the node list's head extended in b688's form (the regeneration and the drafting named)."""
    fr = rdn('b696_faces_rows.txt').split(NL)
    s = fr[10]
    cav = _caveat_new()
    out = s.replace(RADIUS_OLD, RADIUS_NEW).replace(CAVEAT_B696, cav).replace(HEAD_OLD, HEAD_NEW)
    return s, out, cav


def facesrows(*a):
    """(R307)(2): the page's line :734 and the node list's :168; b696's successor verbatim; the two readings -- the radius against
    data/b696_witness_balls.txt :14, the caveat against data/b696_tails_plan.txt :12-:14 -- and the row they give, printed before any page
    is touched. data/b697_faces_rows.txt."""
    page = rd(os.path.join(PP, K.FACES_PAGE)).split(NL)
    nz = rdn('b695_nodes_zeta.txt').split(NL)
    wb = rdn('b696_witness_balls.txt').split(NL)
    tp = rdn('b696_tails_plan.txt').split(NL)
    s, new, cav = successor()
    r32 = wb[13]
    m = re.search(r'S -?([\d.]+) \+- ([\d.e-]+)', r32)
    radius_ok = bool(m) and m.group(2) == RADIUS_NEW.split()[1] and s.count(RADIUS_OLD) == 1
    cav_ok = bool(cav) and s.count(CAVEAT_B696) == 1 and new.count(cav) == 1
    head_ok = s.count(HEAD_OLD) == 1
    L = ['%s -- COMPONENT 2, (R307)(2): THE WEIL-FACE ROW, BOTH ROWS AND THE TWO READINGS, PRINTED BEFORE ANY PAGE IS TOUCHED (%s)' % (ACT, utc()), '',
         '### rows are face rows: (A) the line as the page carries it, (B) b696`s successor verbatim, (C) the two readings, (D) the row they give.', '',
         '  (A) THE LINE AS THE PAGE CARRIES IT, PLACE-papers %s :734 (from relay data/b695_nodes_zeta.txt :168, equal %s):' % (
             K.FACES_PAGE, nz[167].startswith('# backmatter:') and nz[167][len('# backmatter: '):] in page[733]),
         page[733], '',
         '  (B) b696`S SUCCESSOR, VERBATIM, relay data/b696_faces_rows.txt :11:', s, '',
         '  (C) THE TWO READINGS:',
         '      (i) THE RADIUS: the successor`s unchanged remainder carries %r ; the a = 32 row (relay data/b696_witness_balls.txt :14) reads the' % RADIUS_OLD,
         '          margin %s with the ball radius %s -> %r, the replacement the author`s word at (R307)(2) ; the old figure once in the row %s' % (
              m.group(1) if m else '?', m.group(2) if m else '?', RADIUS_NEW, radius_ok),
         '      (ii) THE CAVEAT: (R306)(4)`s words %r read against b696`s plan note (relay data/b696_tails_plan.txt :12-:14: "It enters THE' % CAVEAT_B696[:60],
         '          IDENTITY`S TOLERANCE, not the sum`s radius ... the identity gates the reading") -> the caveat as (R307)(2) words it, read from',
         '          relay data/b697_ferry.txt (2): %r ; (R306)(4)`s caveat once in the row and the new once in (D) %s' % (cav, cav_ok),
         '      (iii) THE HEAD, the seat`s, in b688`s form (data/b690_nodes_zeta.txt :167): the backmatter record`s head names the regeneration',
         '          and the drafting ("regenerated under the author`s word on (R307)(2), 2026-10-21, b697, drafted under (R306)(4), 2026-10-20,',
         '          b696"), its old form once in the row %s -- raised with the row, strikeable' % head_ok, '',
         '  (D) THE ROW THE READINGS GIVE, for data/b697_nodes_zeta.txt :168 where the word is regenerate:', new, '',
         '### the plan`s note, verbatim (relay data/b696_tails_plan.txt :12-:14):'] + ['    ' + x.strip() for x in tp[11:14]] + [
         '', '### ### **ROWS PRINTED 4 (A, B, C, D) ; THE RADIUS %s -> %s %s ; THE CAVEAT READ FROM (R307)(2) %s ; THE HEAD IN b688`S FORM %s ; NO PAGE '
         'TOUCHED.**' % (RADIUS_OLD, RADIUS_NEW, radius_ok, cav_ok, head_ok)]
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('%s_faces_rows.txt' % ACT, L)
    print(NL.join(L))


def nodes(*a):
    """the author's word at the faces prompt (regenerate): data/b697_nodes_zeta.txt -- b695's list with :168 replaced by (D) of
    data/b697_faces_rows.txt and nothing else; refused unless every other line is equal and (D) is the route's own successor()."""
    old = rdn('b695_nodes_zeta.txt').split(NL)
    fr = rdn('%s_faces_rows.txt' % ACT).split(NL)
    d = [l for i, l in enumerate(fr) if i > 0 and fr[i - 1].startswith('  (D) THE ROW THE READINGS GIVE')]
    _s, new, _c = successor()
    if len(d) != 1 or d[0] != new or not old[K.NODES_ROW - 1].startswith('# backmatter:') or 'the Weil face at Q0' not in old[K.NODES_ROW - 1]:
        sys.exit('### (D) IS NOT THE ROUTE`S SUCCESSOR OR :168 IS NOT THE WEIL-FACE ROW -- NOTHING WRITTEN')
    out = old[:K.NODES_ROW - 1] + [new] + old[K.NODES_ROW:]
    diff = [i + 1 for i in range(len(old)) if old[i] != out[i]]
    if diff != [K.NODES_ROW] or len(out) != len(old):
        sys.exit('### THE NEW LIST DIFFERS BEYOND :168 %s -- NOTHING WRITTEN' % diff)
    if 'dry' in a:
        print('  the new list: %d lines, differing from b695`s at %s' % (len(out), diff))
        return
    p = os.path.join(D, os.path.basename(K.NODES_NEW))
    with open(p + '.tmp', 'wb') as fh:
        fh.write(NL.join(out).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print('  written %s: %d lines, differing from b695`s at %s' % (K.NODES_NEW, len(out), diff))


def faces(*a):
    """b695's form (tools/b695_record.py faces), carried without the carried-row allowance: the control (b695's list re-emits the committed
    page byte for byte) and the emission of data/b697_nodes_zeta.txt, both by tools/chain_page.py --from-output data/b643_probe_out_zeta.txt
    into the scratchpad (no lean); the diff printed; with `write`, the control and the emission clean first, the page written by the generator
    itself (its --out the page), read back equal to the emission, and the diff banked as data/b697_faces_diff.txt."""
    import difflib
    import hashlib
    page = os.path.join(PP, K.FACES_PAGE)
    probe = os.path.join(ROOT, *K.PROBE.split('/'))

    def emit(nodes_, out):
        r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'chain_page.py'), '--nodes', os.path.join(ROOT, *nodes_.split('/')),
                            '--probe-dir', SP, '--out', out, '--from-output', probe], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.returncode, ((r.stdout or '') + (r.stderr or '')).strip().split(NL)[-1:]
    committed = open(page, 'rb').read()
    head = (_show(PP, 'HEAD', K.FACES_PAGE) or '').encode('utf-8')
    cpath, npath = os.path.join(SP, 'b697_faces_control.md'), os.path.join(SP, 'b697_faces_emit.md')
    rc0, t0 = emit(K.NODES, cpath)
    ctl = open(cpath, 'rb').read() if os.path.exists(cpath) else b''
    control = rc0 == 0 and ctl == committed
    rc1, t1 = emit(K.NODES_NEW, npath)
    new = open(npath, 'rb').read() if os.path.exists(npath) else b''
    ca, cb = committed.decode('utf-8').split(NL), new.decode('utf-8').split(NL)
    # the diff from the matcher without autojunk: unified_diff's own matcher junks the page's frequent blank line and pulled the equal :735
    # into the :734 hunk (a dry run printed lines added 3, removed 3 for a two-line change)
    ops = [o for o in difflib.SequenceMatcher(None, ca, cb, autojunk=False).get_opcodes() if o[0] != 'equal']
    real = [(i1 + 1, i2, j1 + 1, j2) for op, i1, i2, j1, j2 in ops]
    d = ['--- committed', '+++ b697']
    for op, i1, i2, j1, j2 in ops:
        d += ['@@ -%d,%d +%d,%d @@' % (i1 + 1, i2 - i1, j1 + 1, j2 - j1)] + ['-' + l for l in ca[i1:i2]] + ['+' + l for l in cb[j1:j2]]
    add = sum(j2 - j1 for op, i1, i2, j1, j2 in ops)
    rem = sum(i2 - i1 for op, i1, i2, j1, j2 in ops)
    changed = sorted(set(i for i in range(min(len(ca), len(cb))) if ca[i] != cb[i]))
    written, back = False, False
    if 'write' in a:
        if rc1 != 0 or not control:
            sys.exit('### THE CONTROL OR THE EMISSION FAILED -- THE PAGE IS NOT WRITTEN (control %s ; emission exit %d)' % (control, rc1))
        rc2, t2 = emit(K.NODES_NEW, page)
        written = rc2 == 0
        back = open(page, 'rb').read() == new
    _s, row, cav = successor()
    L = ['b697 -- COMPONENT 2, (R307)(2): THE WEIL-FACE LINE THROUGH THE GENERATOR, ON THE AUTHOR`S WORD AT THE FACES PROMPT (%s)' % utc(), '',
         '### the generator: relay tools/chain_page.py --from-output relay %s (no elaboration; no lean on this host)' % K.PROBE,
         '### the control: b695`s list (relay %s) re-emits the committed page byte for byte: %s (%d bytes ; exit %d ; the committed page equal to HEAD`s '
         'blob %s)' % (K.NODES, control, len(ctl), rc0, committed.replace(b'\r\n', b'\n') == head.replace(b'\r\n', b'\n')),
         '### the new list: relay %s (b695`s with :168 replaced, data/b697_faces_rows.txt (D)); emitted %d bytes, exit %d, sha256 %s' % (
             K.NODES_NEW, len(new), rc1, hashlib.sha256(new).hexdigest()[:16]),
         '### the lines that differ, committed -> b697, by number: %s (expected :3, the list`s name, and :734, the backmatter line) ; lines added %d, '
         'removed %d ; the opcodes %s' % ([':%d' % (i + 1) for i in changed], add, rem, '; '.join(':%d-:%d -> :%d-:%d' % r for r in real))] + [
         '### the diff:'] + ['    ' + l for l in d] + [
         '', '### the page written by the generator and read back equal to the emission: %s' % (back if 'write' in a else 'NOT YET (dry)'),
         '### the page carries the row`s radius %s and (R307)(2)`s caveat verbatim: %s ; the page no longer carries "%s": %s' % (
             RADIUS_NEW, RADIUS_NEW in new.decode('utf-8') and cav in new.decode('utf-8'), RADIUS_OLD, RADIUS_OLD not in new.decode('utf-8')), '',
         '### ### **CONTROL EQUAL %s ; LINES DIFFERING %s ; PAGE WRITTEN %s.**' % (control, ', '.join(':%d' % (i + 1) for i in changed) or 'NONE',
                                                                               written and back)]
    if 'write' in a:
        put_txt('%s_faces_diff.txt' % ACT, L)
    print(NL.join(L[2:6] + L[-5:]))
    print('  the diff`s lines, each cut at 90 characters (%d lines):' % len(d))
    for l in d:
        print('    %r' % l[:90])


# ================================================================================ THE READERS, ONE PER ROW SHAPE A ROUTE READS ((R263)(3))
BRANCH_FATES = ('DELETED', 'KEPT', 'RAISED')


def read_branch_row(r):
    """a row of data/b697_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


READERS = ['read_branch_row']


# ================================================================================ STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE (b670's route, carried)
def roster():
    """the 19 roster tables of data/b586_corroboration.txt :34, at the paths that bank read (carried from b670_record.py :548-:552)."""
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b697_rowgen_<stage>.txt."""
    stage = a[0] if a and a[0] not in ('dry',) else 'stepzero'
    R = roster()
    paths = [os.path.join(PP, p) for _n, p in R]
    miss = [p for p in paths if not os.path.exists(p)]
    if len(R) != 19 or miss:
        sys.exit('### THE ROSTER IS NOT 19 PATHS AT HEAD: %d, missing %s' % (len(R), miss))
    t0 = time.time()
    con = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'rowgen', 'rowgen.py'), 'constellation', PP] + paths,
                         capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=500)
    dif = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'rowgen', 'diff_rowpin.py'), os.path.join(T, 'rowgen', 'namemap.json')] + paths,
                         capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=500)
    secs = int(time.time() - t0)
    co, do = (con.stdout or '') + (con.stderr or ''), (dif.stdout or '') + (dif.stderr or '')
    tail = lambda t: [l for l in t.replace(chr(13), '').split(NL) if l.strip()][-12:]   # noqa: E731
    L = ['%s -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (ACT, stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('%s_rowgen_%s.txt' % (ACT, stage), L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R307)(5); b696's form)
def _remote_heads(repo):
    out = {}
    for l in g(repo, 'ls-remote', '--heads', 'origin').split(NL):
        x = l.split()
        if len(x) == 2 and x[1].startswith('refs/heads/'):
            out[x[1][len('refs/heads/'):]] = x[0]
    return out


def branches(*a):
    """`branches before`: data/b697_branches_before.json -- every branch (R307)(5) names, its tip resolved to 40 hex, merged into main by
    ancestry, and the remote's heads read once per repository; written before any delete. `branches`: data/b697_branches.txt (.json) -- each
    branch's fate read now against the tips banked before."""
    if a and a[0] == 'before':
        rows, remotes = [], {}
        for repo, bs in K.DELETE:
            remotes[repo] = _remote_heads(repo)
            for b in bs:
                tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/%s^{commit}' % b).strip()
                merged = bool(tip) and grc(repo, 'merge-base', '--is-ancestor', tip, 'main') == 0
                rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, at_remote=remotes[repo].get(b)))
        for repo, b in K.DELETE_REMOTE:
            tip = remotes.get(repo, {}).get(b, '')
            merged = bool(tip) and grc(repo, 'merge-base', '--is-ancestor', tip, 'main') == 0
            rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=merged, at_remote=tip))
        put_json('%s_branches_before.json' % ACT, dict(at=utc(), rows=rows, remotes=remotes))
        for r in rows:
            print('  %-18s %-28s %-6s %s merged %s at the remote %s' % (os.path.basename(r['repo']), r['branch'], r['where'], (r['tip'] or '### NONE')[:12],
                                                                       r['merged'], (r['at_remote'] or 'no')[:12]))
        return
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b697_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in _remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R307)(5): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b697_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after.']
    L += ['  %-18s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[]))
    print(NL.join(L[4:]))


# ================================================================================ THE ANSWERS BANK (b696's route, carried)
def _session_rows():
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
    """data/b697_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
    every word of the author delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim; a word opened by
    BEGIN with no END noted (b689's route)."""
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
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion' and o.get('type') == 'assistant':
                calls.append((ln, c['id'], c['input'], o.get('timestamp')))
                ask.add(c['id'])
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask and o.get('type') == 'user':
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or '')
                results[c.get('tool_use_id')] = (ln, t, o.get('timestamp'))
                texts.append(t)
        for t in texts:
            for mm in re.finditer(r'(?s)(?:\A\s*|="|="\(for the seat, verbatim\):\s*)BEGIN\s*(.*?)\s*END(?=\s*\Z|")', t or ''):
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
    for cid, (i, t, _ts) in results.items():
        for mm in re.finditer(r'="BEGIN(?:(?!END").)*?"(?=, "|\.\s|$)', t or '', re.S):
            if not re.search(r'END"\s*$', mm.group(0)):
                W += ['### NOTE (transcript line %s): a word opened by BEGIN and carrying NO END marker -- %r ... %r; its text is the RESULT line '
                      'above.' % (i, mm.group(0)[2:80], mm.group(0)[-60:]), '']
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %s), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### %s -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                ACT, n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('%s_author_answers.txt' % ACT, [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('%s_author_answers.json' % ACT, dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                                for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE DEFECTS BANK (b696's route and its row reader, carried)
DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short(act=ACT):
    out = []
    L = rdn('%s_defects.txt' % act).split(NL)
    for i, l in enumerate(L):
        if DEFECT_ROW.match(l):
            j = i + 1
            while j < len(L) and L[j].startswith('    ') and not DEFECT_ROW.match(L[j]) and not L[j].startswith('    ###'):
                j += 1
            m = re.match(r"^\(([a-z]'?)\) (.*?)\.(?= |$)", ' '.join(x.strip() for x in L[i:j]))
            if m:
                out.append(m.group(0)[:-1])
    return out


def defects(*a):
    t = rdn('%s_defects.txt' % ACT)
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('%s_defects.json' % ACT, dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


# ================================================================================ THE ROUTES
ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, c1=c1, facesrows=facesrows, nodes=nodes, faces=faces)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b697_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
