# -*- coding: utf-8 -*-
"""b696_record.py -- THE ACT'S RECORD TOOL, b696 under (R306).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b696's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b695_record.py in stages: the helpers, the guarded landing, the readers, step zero's rowgen and branches
### routes, the answers and defects routes first (stage one); Component 1's weight line at Component 1; the faces draft at Component 3; the
### late routes at Component 4. b695's re-cut routes (tie, dispatch, runner, prints, quote, cut, faces, trails) are not carried: this act
### re-cuts nothing and dispatches no runner (N1). Every python child is started as `python -X utf8`, no environment mapping passed.
### Routes: `python tools/b696_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
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
import b696_worklist as K          # noqa: E402

SP = K.SP
STANDIN = 'standin' in sys.argv[2:]          # ### the dry-run step's stand-ins, by argument (environment variables left as they are)
RELAY = ROOT
ACT, PREV = 'b696', 'b695'


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
    none a number any bank carries; a stand-in run writes no bank (b695's, carried)."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b696_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b696_findings.json': dict(entry_line=99999, title='stand-in'),
        'b696_trail.json': dict(line=99999),
        'b696_act_root.json': dict(root='0' * 64, previous='a8405976' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b696's)
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


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R306)(1)
WH = ('*Appended 2026-10-20 by b696 to b695’s entry (:9592), under `(R306)`(1) -- b695 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b695_closing.txt):*')
WB = (' “b695 closed: relay aa70ac82, PLACE-papers 5ed6e31; suite 121 of 122; root a84059769e7dd478…; 2 prompts answered; 4 defects” '
      '(data/b695_closing.txt :1), the closing a0478dee pushed and read back at relay main (data/b695_closing_push_out.txt :5). b694’s weight '
      'line at FINDINGS :9578 and the corrigendum for (k) and (l) at :9580, the corrigenda bank appended at rows (9) and (10), the sealed face and '
      'the hashes bank unedited. The re-cut: SIDE-interfaces named by b652’s order and b674’s rule read in its written order -- OVERREACHES, then '
      'rows of any kind, then the larger table -- three kernels at one row outside, decided at step (iii), six rows to five; the reading '
      'accepted, the rule’s order as banked governing over the row count alone (data/b695_tie.txt :43-:47). The root module’s header bullets '
      'carrying the table’s ACTION verbatim at 69b143b, comment lines alone; the workflow 9b4c484 and the print list 58854f0 alone on main; runs '
      '39487947819 and 39488049232 DERIVES, the 11 prints equal line for line; the quotation search finding 4 quoting lines, each carried as it '
      'stands; merged --no-ff at c8bd217, tagged v0.2.1 naming v0.2; the distance 1 to 0; no Correspondence cell naming the kernel '
      '(data/b695_cut.txt :4-:9, :24). The Weil-face line regenerated on the author’s two words, the caveat checked character for character and '
      'the autocorrelation written h ⋆ h~, the control differing from the page by the one carried INSTRUMENTS.md keystone row, the line at the '
      'faces page’s :734; N4 scored not met as worded and met in substance. W-ORD-WITNESS-TAIL-BALLS’s trigger re-read at OPEN_TRAILS :15198; '
      'CORRESPONDENCE-DOMINANCE the eleventh spec row, W-ORD-H2-BRIDGE annotated at :15200. The suite 121 of 122 before and after the push, '
      'G-RULE-BINARY-HASHES declared on the face, reading b694’s PNG against its frozen hashes bank (data/b695_closing.txt :105-:108); N1-N3, N5 '
      'and S1-S3 HELD (data/b695_scores_close.json); the sealed tools 9 of 9 (data/b695_closing.txt :15); the root a8405976 over 74 banks '
      '(data/b695_root_banks.txt); mirror-refresh-2026-10-20-b695.zip CLEAN with the root line. Four defects: (a) the seat’s deletes before the '
      'citation check, (b) the corrigendum tool’s earlier form repaired before landing, (c) the navigator’s N4 wording, (d) the N3 scorer’s '
      'earlier form caught by the pre-run (data/b695_defects.txt :6-:27). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B695_ENTRY,
         check=[('FINDINGS.md', K.B695_ENTRY, '## SIDE-interfaces re-cut: 1 row outside LICENSED/CITED to 0'),
                ('OPEN_TRAILS.md', K.B695_TRAIL, '### b695')], dry=dry)


# ================================================================================ COMPONENT 1: THE ARM REPAIR RUN AT HEAD, (R306)(2)
def armrun(*a):
    """G-RULE-BINARY-HASHES as repaired in tools/rule_arms.py, run at HEAD over this act's sources: (i) the live reading, b694's PNG read
    through the corrigenda bank's row (9); (ii) b694's (k) with the corrigenda withheld (CONTROLS) -- wanted FAIL; (iii) a planted frozen row
    naming another path with no corrigendum -- wanted FAIL; (iv) the same planted row with a corrigendum citing its bank and line, the path as
    it stands and the equal sha256 -- wanted OK; (v) the arm's own plant (a binary the root names itself) -- wanted FAIL. Each print counted.
    data/b696_arm_binary.txt (.json)."""
    import rule_arms as RA
    nm = 'G-RULE-BINARY-HASHES'
    S = RA.sources(ACT, 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID, K.ANCHOR, K.PARTS, None, K.PRE_RELAY, K.PRE_PP)
    plant_b = dict(path='data/b999_planted.png', act=999, sha='1' * 64, root=True, in_root=False, carried_by=[],
                   frozen=[('data/b999_planted_hashes.txt', 4, 'data/b998_planted.png | ' + '1' * 64)])
    plant_c = dict(row=99, bank='data/b999_planted_hashes.txt', line=4, path='data/b999_planted.png', sha='1' * 64, at=999)
    ctl = [p for n_, _r, p in RA.CONTROLS if n_ == nm]
    own = [p for n_, _r, _f, p in RA.ARMS if n_ == nm][0]
    cases = [('(i) LIVE at HEAD', S, True),
             ('(ii) b694 (k), the corrigenda withheld (CONTROLS)', ctl[0](S) if ctl else None, False),
             ('(iii) a planted frozen row naming another path, no corrigendum', RA._p(S, 'binaries', S['binaries'] + [plant_b]), False),
             ('(iv) the planted row with its corrigendum', RA._p(RA._p(S, 'binaries', S['binaries'] + [plant_b]), 'corrigenda', S['corrigenda'] + [plant_c]), True),
             ('(v) the arm`s own plant (the root naming a binary)', own(S), False)]
    rows, L = [], ['%s -- (R306)(2): G-RULE-BINARY-HASHES AS REPAIRED, RUN AT HEAD %s (%s)' % (ACT, g(ROOT, 'rev-parse', '--short=8', 'HEAD').strip(), utc()), '',
                   '### rows are runs: the case | wanted | read (OK or FAIL) | rows read | rows failing | AS WANTED ; the arm`s print beneath each.',
                   '### the corrigenda bank`s rows read: %s' % ['(%d) %s :%d -> %s %s' % (c['row'], c['bank'], c['line'], c['path'], c['sha'][:16]) for c in S['corrigenda']], '']
    for lab, R_, want in cases:
        ok, n_, b_, note = RA.reading(nm, R_) if R_ is not None else (None, 0, 0, '### NO CONTROL')
        rows.append(dict(case=lab, want='OK' if want else 'FAIL', read='OK' if ok else 'FAIL', rows=n_, failing=b_, as_wanted=bool(ok) == want, note=note))
        L += ['  %-62s | wanted %-4s | read %-4s | rows %3d | failing %d | AS WANTED %s' % (lab, 'OK' if want else 'FAIL', 'OK' if ok else 'FAIL', n_, b_,
                                                                                         bool(ok) == want), '      ' + note]
    L += ['', '### ### **CASES %d ; AS WANTED %d ; THE LIVE READING %s ; b694`S PNG BY CORRIGENDUM %s ; THE FROZEN ROW WITH NO CORRIGENDUM FAILS %s.**' % (
        len(rows), sum(r['as_wanted'] for r in rows), rows[0]['read'], 'OK BY CORRIGENDUM' in rows[0]['note'] and 'b694_circuit' in rows[0]['note'],
        rows[1]['read'] == 'FAIL' and rows[2]['read'] == 'FAIL')]
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('%s_arm_binary.txt' % ACT, L)
    put_json('%s_arm_binary.json' % ACT, dict(at=utc(), head=g(ROOT, 'rev-parse', 'HEAD').strip(), rows=rows, corrigenda=S['corrigenda']))
    print(NL.join(L))


# ================================================================================ COMPONENT 3: THE FACES ROW, (R306)(4) -- DRAFTED AND HELD
CAVEAT_OLD = 'tail bounds float with a safety factor, not balls (W-ORD-WITNESS-TAIL-BALLS); the zero tail on P3, derived and not compiled'
CAVEAT_NEW = 'tail bounds as certified balls (b696), the zero tail on P3, derived and not compiled'
NODES_SRC, NODES_ROW = 'b695_nodes_zeta.txt', 168


def facesrow(*a):
    """(R306)(4), the order discharged (data/b696_witness_balls.txt): the Weil-face line of relay data/b695_nodes_zeta.txt :168 printed as it
    stands; the successor drafted with the tail-bound caveat replaced by (R306)(4)'s words, read from the banked ruling (data/b696_ferry.txt),
    the remainder unchanged; the check printed (the old caveat once, the new once, every other character equal); held for b697's regeneration
    prompt. Nothing is written to a node list or a page. data/b696_faces_rows.txt."""
    import difflib
    wv = _vl('%s_witness_balls.txt' % ACT)
    if 'THE ORDER DISCHARGED' not in wv:
        sys.exit('### THE ORDER IS NOT DISCHARGED (%s) -- NO SUCCESSOR DRAFTED ((R306)(4))' % wv)
    fl = [l for l in rdn('b696_ferry.txt').split(NL) if l.startswith('(4) THE FACES ROW')]
    m = re.search(r'“(tail bounds as certified balls.*?)”', fl[0]) if len(fl) == 1 else None
    if not m or m.group(1) != CAVEAT_NEW:
        sys.exit('### (R306)(4)`s CAVEAT AS BANKED %r IS NOT THE ROUTE`S %r -- NOTHING WRITTEN' % (m and m.group(1), CAVEAT_NEW))
    row = rdn(NODES_SRC).split(NL)[NODES_ROW - 1]
    page = rd(os.path.join(PP, K.FACES_PAGE)).split(NL)
    if row.count(CAVEAT_OLD) != 1:
        sys.exit('### THE ROW CARRIES THE OLD CAVEAT %d TIMES -- NOTHING WRITTEN' % row.count(CAVEAT_OLD))
    new = row.replace(CAVEAT_OLD, CAVEAT_NEW)
    i = row.index(CAVEAT_OLD)
    same = new[:i] == row[:i] and new[i + len(CAVEAT_NEW):] == row[i + len(CAVEAT_OLD):]
    on_page = [k for k, l in enumerate(page, 1) if CAVEAT_OLD in l]
    d = list(difflib.unified_diff(row.split('; '), new.split('; '), 'data/b695_nodes_zeta.txt :168 (split at "; ")', 'the successor (split at "; ")',
                                  n=0, lineterm=''))
    L = ['%s -- COMPONENT 3, (R306)(4): THE WEIL-FACE LINE`S SUCCESSOR, DRAFTED AND HELD FOR b697`S REGENERATION PROMPT (%s)' % (ACT, utc()), '',
         '### the order: %s' % wv.strip('#* '),
         '### rows are drafted node-list rows: (A) the row as it stands, (B) the successor, (C) the check. Nothing written to a node list or a page.', '',
         '  (A) THE ROW AS IT STANDS, relay data/%s :%d (the page carries it at PLACE-papers %s :%s):' % (NODES_SRC, NODES_ROW, K.FACES_PAGE,
                                                                                                         ', :'.join(str(k) for k in on_page) or '### NONE'),
         row, '',
         '  (B) THE SUCCESSOR, DRAFTED, NOT WRITTEN, HELD FOR b697 -- the tail-bound caveat replaced by (R306)(4)`s words (relay data/b696_ferry.txt,',
         '      (4)), the remainder of the row unchanged:',
         new, '',
         '  (C) THE CHECK: the old caveat in the row %d time(s) ; the new caveat in the successor %d time(s) ; every character outside the caveat equal %s ;' % (
             row.count(CAVEAT_OLD), new.count(CAVEAT_NEW), same),
         '      the diff, the row split at "; ":'] + ['      ' + l for l in d] + [
         '', '  ### THE SEAT`S NOTE FOR THE AUTHOR, beside the draft and not in it: the remainder unchanged carries b694`s margin "-7.7752874967979 ±',
         '      1.43e-18", whose radius was the float tail; with the ball the margin at a = 32 reads 7.7752874967979 +- 3.68e-23',
         '      (relay data/b696_witness_balls.txt :14). The row`s radius is left as (R306)(4) orders, raised for b697`s prompt.', '',
         '### ### **THE ORDER DISCHARGED ; ONE SUCCESSOR DRAFTED, HELD FOR b697 ; THE CAVEAT REPLACED ONCE, THE REST EQUAL %s ; NOTHING WRITTEN TO A NODE '
         'LIST OR A PAGE.**' % same]
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('%s_faces_rows.txt' % ACT, L)
    print(NL.join(L[-8:]))


# ================================================================================ THE REPAIRS BANK: (R306)(2) AND THE CARRY-TIME READING
REPAIR_BASE = '7b791453'     # ### relay HEAD before the repair (step zero's commit): tools/rule_arms.py as b691 left it


def repairs(*a):
    """data/b696_tool_repairs.txt: rows are repairs with the defect or order they answer, each diff beneath its row (unified, the file at
    REPAIR_BASE against the working tree). Row (1) is (R306)(2)'s, the one edit to a shared tool; carry-time repairs to this act's own tools
    are added as rows by Component 4."""
    import difflib
    old = _show(ROOT, REPAIR_BASE, 'tools/rule_arms.py') or ''
    new = rd(os.path.join(T, 'rule_arms.py'))
    d1 = list(difflib.unified_diff(old.split(NL), new.split(NL), 'tools/rule_arms.py at relay %s' % REPAIR_BASE, 'tools/rule_arms.py (b696)', lineterm=''))
    ab = _vl('%s_arm_binary.txt' % ACT)
    L = ['%s -- THE REPAIRS: (R306)(2), THE ONE EDIT TO A SHARED TOOL, AND THE CARRY-TIME READING (%s)' % (ACT, utc()), '',
         '### rows are repairs with the defect or order they answer: the tool and its part ; what it answers ; the form. Each diff beneath its',
         '### row, written by this route (difflib over the file, relay at %s against the working tree).' % REPAIR_BASE, '',
         '  (1) tools/rule_arms.py G-RULE-BINARY-HASHES (a shared tool, by the Edit tool) -- ANSWERS (R306)(2) and b694`s defect (k) (relay',
         '      data/b694_defects.txt :43-:51; data/b695_defects.txt; FINDINGS :9580): b694`s circuit figure`s hashes bank, frozen and root-named,',
         '      names its PNG under b692`s path at :4, so the arm failed on it in every act since. THE FORM: sources() keeps, for each binary, the',
         '      rows of its act`s root-named text banks carrying its sha256 (its frozen rows) and reads the corrigenda bank`s rows of the form',
         '      "(N) relay data/<bank> :<line>, ... THE CORRECTION: the file stands as data/<path>, sha256 <64 hex>" across their wrapped lines;',
         '      reading() reads a binary with no carrying bank OK where a corrigendum row cites one of its frozen rows by bank and line, names its',
         '      path as it stands and its equal sha256, the correction printed beside the frozen row; with no such row it fails as before.',
         '      CONTROLS gains b694 (k) with the corrigenda withheld. Run at HEAD (relay data/b696_arm_binary.txt): %s' % ab.strip('#* '), '']
    L += ['      ' + l for l in d1] + ['']
    L += ['### ### **REPAIRS 1 ; THE SHARED TOOL EDITED tools/rule_arms.py, ONE ARM AND ONE CONTROL ; DIFF LINES %d ; NO FROZEN BANK EDITED.**' % len(d1)]
    put_txt('%s_tool_repairs.txt' % ACT, L)
    print(L[-1])


def _vl(name):
    return ([x for x in rdn(name).split(NL) if x.startswith('### ### **')] or ['### NOT READ'])[-1]


# ================================================================================ THE READERS, ONE PER ROW SHAPE A ROUTE READS ((R263)(3))
BRANCH_FATES = ('DELETED', 'KEPT', 'RAISED')


def read_branch_row(r):
    """a row of data/b696_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
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
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b696_rowgen_<stage>.txt."""
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


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R306)(5))
# ### b695 (a) taught the order: the citation check and the readfirst bank first, then the branches read and banked BEFORE any delete
# ### (`branches before`: each tip, merged into main by ancestry, the remote's heads), then the deletes one per message, then `branches`
# ### reads each fate against the tips banked before.
def _remote_heads(repo):
    out = {}
    for l in g(repo, 'ls-remote', '--heads', 'origin').split(NL):
        x = l.split()
        if len(x) == 2 and x[1].startswith('refs/heads/'):
            out[x[1][len('refs/heads/'):]] = x[0]
    return out


def branches(*a):
    """`branches before`: data/b696_branches_before.json -- every branch (R306)(5) names, its tip resolved to 40 hex, merged into main by
    ancestry, and the remote's heads read once per repository; written before any delete. `branches`: data/b696_branches.txt (.json) -- each
    branch's fate read now (absent locally, or absent at the remote for the one remote delete) against the tips banked before."""
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
        sys.exit('### data/b696_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in _remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R306)(5): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b696_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after.']
    L += ['  %-18s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[]))
    print(NL.join(L[4:]))


# ================================================================================ THE ANSWERS BANK (b695's route, carried)
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
    """data/b696_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
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


# ================================================================================ THE DEFECTS BANK (b695's route and its row reader, carried)
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
ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, c1=c1, armrun=armrun, repairs=repairs, facesrow=facesrow)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b696_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
