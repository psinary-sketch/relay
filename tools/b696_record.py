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
    S0 = RA.sources(ACT, 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID, K.ANCHOR, K.PARTS, None, K.PRE_RELAY, K.PRE_PP)
    # ### the binaries of the acts already rooted: this act's own read by the suite after its root (before it the arm reads no root for them)
    own = [b['path'] for b in S0['binaries'] if b['act'] >= int(ACT[1:])]
    S = RA._p(S0, 'binaries', [b for b in S0['binaries'] if b['act'] < int(ACT[1:])])
    plant_b = dict(path='data/b999_planted.png', act=999, sha='1' * 64, root=True, in_root=False, carried_by=[],
                   frozen=[('data/b999_planted_hashes.txt', 4, 'data/b998_planted.png | ' + '1' * 64)])
    plant_c = dict(row=99, bank='data/b999_planted_hashes.txt', line=4, path='data/b999_planted.png', sha='1' * 64, at=999)
    ctl = [p for n_, _r, p in RA.CONTROLS if n_ == nm]
    plant_own = [p for n_, _r, _f, p in RA.ARMS if n_ == nm][0]
    cases = [('(i) LIVE at HEAD, the rooted acts` binaries', S, True),
             ('(ii) b694 (k), the corrigenda withheld (CONTROLS)', ctl[0](S) if ctl else None, False),
             ('(iii) a planted frozen row naming another path, no corrigendum', RA._p(S, 'binaries', S['binaries'] + [plant_b]), False),
             ('(iv) the planted row with its corrigendum', RA._p(RA._p(S, 'binaries', S['binaries'] + [plant_b]), 'corrigenda', S['corrigenda'] + [plant_c]), True),
             ('(v) the arm`s own plant (the root naming a binary)', plant_own(S), False)]
    rows, L = [], ['%s -- (R306)(2): G-RULE-BINARY-HASHES AS REPAIRED, RUN AT HEAD %s (%s)' % (ACT, g(ROOT, 'rev-parse', '--short=8', 'HEAD').strip(), utc()), '',
                   '### rows are runs: the case | wanted | read (OK or FAIL) | rows read | rows failing | AS WANTED ; the arm`s print beneath each.',
                   '### the corrigenda bank`s rows read: %s' % ['(%d) %s :%d -> %s %s' % (c['row'], c['bank'], c['line'], c['path'], c['sha'][:16]) for c in S['corrigenda']],
                   '### the binaries of the acts already rooted, b680 to %s: %d ; this act`s own, read by the suite after its root: %s' % (
                       PREV, len(S['binaries']), own or 'NONE'), '']
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
REPAIR_BASE = K.REPAIR_BASE  # ### relay HEAD before the repair (step zero's commit): tools/rule_arms.py as b691 left it


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
    rec5 = rd(os.path.join(T, 'b695_record.py'))
    me = rd(os.path.join(T, 'b696_record.py'))
    d2 = list(difflib.unified_diff(_fn_src(rec5, 'branches'), _fn_src(me, 'branches'), 'tools/b695_record.py branches (sealed at b695)',
                                   'tools/b696_record.py branches (this act)', lineterm=''))
    d3 = list(difflib.unified_diff(_fn_src(rec5, 'outbound'), _fn_src(me, 'outbound'), 'tools/b695_record.py outbound (sealed at b695)',
                                   'tools/b696_record.py outbound (this act)', lineterm=''))
    L += ['  (2) tools/b696_record.py branches, carried from tools/b695_record.py -- ANSWERS b695`s defect (a) (relay data/b695_defects.txt :6-:11):',
          '      b695 deleted its branches before its citation check and rebuilt their tips from git`s delete replies. THE FORM: `branches before`',
          '      banks every named branch`s tip, its ancestry in main and the remotes` heads before any delete; `branches` reads each fate after the',
          '      deletes against the tips banked before, the one remote delete among them.', '']
    L += ['      ' + l for l in d2] + ['']
    L += ['  (3) tools/b696_record.py outbound, carried from tools/b695_record.py -- ANSWERS N5`s "no identifier of the author in any outbound',
          '      request": this act`s one request outside the session`s tools is tools/b696_tails_source.py`s fetch of NIST DLMF section 5.11.',
          '      THE FORM: that request read from the tool`s own source (its URL and its one header) and counted among the outbound requests.', '']
    L += ['      ' + l for l in d3] + ['']
    L += ['### ### **REPAIRS 3 ; THE SHARED TOOL EDITED tools/rule_arms.py, ONE ARM AND ONE CONTROL ; TWO CARRIED ROUTES OF THE RECORD TOOL ; DIFF '
          'LINES %d ; NO FROZEN BANK EDITED.**' % (len(d1) + len(d2) + len(d3))]
    put_txt('%s_tool_repairs.txt' % ACT, L)
    print(L[-1])


def _fn_src(src, name):
    L = src.split(NL)
    i = next((k for k, l in enumerate(L) if l.startswith('def %s(' % name)), None)
    if i is None:
        return []
    j = i + 1
    while j < len(L) and (not L[j] or L[j][0] in ' \t#' or L[j].startswith(')')):
        j += 1
    while j > i + 1 and not L[j - 1].strip():
        j -= 1
    return L[i:j]


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


# ================================================================================ THE CAPTURE AND THE COMMANDS (b695's, carried; ONE SESSION FOR THREE ACTS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
# ### the previous act's window: b695 ran in this same session; from the call that combined its post-push parts to this act's anchor line
PREV_ACT, PREV_SESSION, PREV_ANCHOR = 'b695', K.SESSION_ID, 'RULING (R305) BEGIN'


def _bg_calls():
    out = set()
    for _i, o, _st, _sid in _session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and (c.get('input') or {}).get('run_in_background'):
                out.add((o.get('timestamp'), (c.get('input') or {}).get('command')))
    return out


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    rows.sort(key=lambda r: r['ts'])
    bg = _bg_calls()
    for i, r in enumerate(rows):
        r['n'] = i + 1
        r['bg'] = (r.get('ts'), r.get('cmd')) in bg
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')
SED = re.compile(r'(^|[;&|(]\s*|\s)sed\s')
PY_PRINT_READ = re.compile(r'python[^\n]*\s-c\s')
REDIRECT_ANY = re.compile(r'(?<![<>=\-\w])(?:\d?>>?|&>)(?!&)\s*\S')
PIPE_FILTER = re.compile(r'\|\s*(?:head|tail|wc|grep|cut|sort|uniq|awk|less|more|tr)\b')
SED_KIND = 'R sed in any form (data/b685_rules.txt row (2))'


def local_lean(cmd):
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def sed_cmd(cmd):
    return SED.search(QUOTED.sub('""', cmd)) is not None


def _anchor_ts(anchor, session=SESSION):
    for ln in io.open(session, encoding='utf-8', errors='replace'):
        if anchor in ln:
            try:
                j = json.loads(ln)
            except ValueError:
                continue
            if j.get('type') == 'user' and not j.get('isCompactSummary'):
                return j.get('timestamp')
    return None


def prev_capture():
    """G-EDIT-ROUTE's window over the previous act: b695, in this same session, from the call that combined its post-push parts into
    data/b695_checks_postpush.txt to the user line carrying this act's anchor (b695's repair (1), carried)."""
    rows = ER.capture(SESSION, PREV_ANCHOR, SUBAGENTS)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV_ACT in r['cmd'] and '--combine' in r['cmd']]
    end = _anchor_ts(K.ANCHOR)
    if not first or not end:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE OR THIS ACT`S ANCHOR IS NOT IN THE SESSION`S CAPTURE -- NOTHING READ')
    out = [dict(r, src='%s %s' % (PREV_ACT, r['src'])) for r in rows if first[0] <= r['ts'] < end]
    for i, r in enumerate(out):
        r['n'] = 'p%d' % (i + 1)
    return out


def edit_route_offences(rows):
    out = []
    for r in rows:
        o = list(ER.offences(r['cmd']))
        if r['tool'] in ('Bash', 'PowerShell') and sed_cmd(r['cmd']) and not any(k.startswith('S sed') for k, _ in o):
            o.append((SED_KIND, r['cmd'].split(NL)[0][:120]))
        if o:
            out.append((r, o))
    return out


MOVE_OR_DELETE = re.compile(r'\bgit\s+(-C\s+\S+\s+)?(mv|rm)\b|\bgit\s+(-C\s+\S+\s+)?branch\s+-[dD]\b|--delete\b|(^|[;&|]\s*|\s)rm\s+-|Remove'
                            + r'-Item|\bos\.remove\b')
REDIRECT_NULL = re.compile(r'\d?>\s*/dev/null')
SHELL_VAR = re.compile(r'\$(?:\?|\{[^}]*\}|[A-Za-z_]\w*|\d)')


def delete_shape(cmd):
    """(R306)(5) and the ferry: a delete command names one branch and carries no glob and no variable in any half; b693's reader, carried."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    vs = SHELL_VAR.findall(c)
    return names, [ch for ch in '*?[' if ch in SHELL_VAR.sub('', c)], vs


def chained_after(cmd):
    """data/b694_rules.txt row (1): anything chained after a delete in the same command (`;`, `&&`, `||`, `|`), read outside quoted strings."""
    c = QUOTED.sub('""', cmd)
    m = re.search(r'(--delete\s+\S+|branch\s+-[dD]\s+\S+)', c)
    return bool(m) and bool(re.search(r'[;&|]', c[m.end():]))


IDENT = ('psinary', 'hotmail', 'seale', 'york', 'orcid', '0009-0008')


def outbound():
    """the outbound requests other than git: the session's web searches, subagent prompts and fetches; and the one request a tool of this act
    makes, tools/b696_tails_source.py's fetch of NIST DLMF section 5.11, read from the tool's own source (its URL and its one header)."""
    out = []
    for i, o, _st, _sid in _session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') in ('WebSearch', 'Agent', 'WebFetch'):
                inp = c.get('input') or {}
                text = inp.get('query') or inp.get('prompt') or inp.get('url') or ''
                out.append(dict(line=i, tool=c['name'], ts=o.get('timestamp'), text=text))
    src = rd(os.path.join(T, 'b696_tails_source.py'))
    m = re.search(r"^URL = '([^']+)'", src, re.M)
    h = re.search(r"headers=(\{[^}]*\})", src)
    out.append(dict(line='-', tool='tools/b696_tails_source.py (urllib)', ts=jl('%s_author_answers.json' % ACT).get('at') or '-',
                    text='%s %s' % (m.group(1) if m else '### NO URL', h.group(1) if h else '### NO HEADER')))
    for r in out:
        r['identifiers'] = [w for w in IDENT if w in r['text'].lower()]
    return out


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = edit_route_offences(rows)
    prev = prev_capture()
    phits = edit_route_offences(prev)
    sh_ = [r for r in rows if r['tool'] in ('Bash', 'PowerShell')]
    lean = [r for r in sh_ if local_lean(r['cmd'])]
    mv = [r for r in sh_ if MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in sh_ if re.search(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py dispatch\b', QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in sh_ if (r.get('bg') or re.search(r'Start-Process|\bnohup\b|run_in_background', QUOTED.sub('""', r['cmd'])))]
    seds = [r for r in sh_ if sed_cmd(r['cmd'])]
    nulls = [r for r in sh_ if REDIRECT_NULL.search(QUOTED.sub('""', r['cmd']))]
    redir = [r for r in sh_ if REDIRECT_ANY.search(QUOTED.sub('""', r['cmd']))]
    pipes = [r for r in sh_ if PIPE_FILTER.search(QUOTED.sub('""', r['cmd']))]
    pyreads = [r for r in sh_ if PY_PRINT_READ.search(r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    chained = [r['n'] for r in mv if delete_shape(r['cmd'])[0] and chained_after(r['cmd'])]
    halves = dict((r['n'], len([x for x in re.split(r'&&|\|\||;|\|', QUOTED.sub('""', r['cmd'])) if x.strip()])) for r in mv)
    ob = outbound()
    L = ['%s -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % (ACT, utc()), '',
         '### the source: the seat`s session %s from its first user line carrying %r, with its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (b695, this same session %s, from its post-push combine to this act`s '
              'anchor): %d commands from %s, its offences printed whole (%d):' % (PREV_SESSION[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (%d):' % len(disp)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN, BY THEIR TEXT OR THE TOOL`S run_in_background PARAMETER (%d):' % len(
        detach)] + (['  #%d %s%s' % (r['n'], '[run_in_background] ' if r.get('bg') else '', r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING sed IN ANY FORM (data/b685_rules.txt row (2)) (%d):' % len(seds)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in seds] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT ONTO /dev/null, read outside quoted strings (%d):' % len(nulls)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], r['cmd'].split(NL)[0][:200]) for r in nulls] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT OF ANY STREAM, read outside quoted strings (%d):' % len(redir)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in redir] or ['  NONE'])
    L += ['', '### THE COMMANDS PIPING INTO A SHELL FILTER (head, tail, wc, grep and the like), read outside quoted strings (%d):' % len(pipes)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in pipes] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT RUN AN INTERPRETER`S ONE-LINE PROGRAM (python -c), each its first line (%d):' % len(pyreads)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:220]) for r in pyreads] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R306)(5) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
              'nothing chained after): ' + ('; '.join('#%d deletes %s, halves %d, globs %s, variables %s, chained after %s' % (
                  n, d, halves.get(n, 0), gl or 'none', vs or 'none', n in chained) for n, d, gl, vs in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git (web searches, subagent prompts and fetches, and the tails source`s one fetch), each with the '
              'author`s identifiers found in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    good = sum(1 for n, d, gl, vs in shapes if len(d) == 1 and not gl and not vs and n not in chained)
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; REDIRECTS ONTO /dev/null %d ; '
              'REDIRECTS OF ANY STREAM %d ; PIPES INTO A SHELL FILTER %d ; ONE-LINE PROGRAMS %d ; MOVE OR DELETE COMMANDS %d ; BRANCH DELETES OF ONE '
              'BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(nulls), len(redir), len(pipes), len(pyreads), len(mv), good, len(shapes), len(ob),
                  sum(1 for r in ob if r['identifiers']))]
    put_txt('%s_commands.txt' % ACT, [l.replace('\r', '') for l in L])
    put_json('%s_commands.json' % ACT, dict(at=utc(), anchor=K.ANCHOR, rows=rows,
                                           offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                           prev=dict(act=PREV_ACT, session=PREV_SESSION, rows=len(prev),
                                                     offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                           local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                           seds=[r['n'] for r in seds], null_redirects=[r['n'] for r in nulls], redirects=[r['n'] for r in redir],
                                           pipes=[r['n'] for r in pipes], py_programs=[r['n'] for r in pyreads], moves_deletes=[r['n'] for r in mv],
                                           delete_shapes=[dict(n=n, deletes=d, globs=gl, variables=vs, halves=halves.get(n), chained=n in chained)
                                                          for n, d, gl, vs in shapes],
                                           outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r, o in phits:
        print('  PREVIOUS-ACT OFFENCE #%s %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


# ================================================================================ THE LATE ROUTES (b695's, carried with b696's names)
def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle', 'SIDE-bijection', 'SIDE-class-number-anomaly',
                                   'SIDE-spinor', 'SIDE-li-map', 'SIDE-rcurve', 'SIDE-archimedean', 'SIDE-interfaces']


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    put_json('%s_kernels_face.json' % ACT, dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (no kernel written by this act; none written after this read)' % len(ks))


def seal_hashes():
    import hashlib
    rec_ = (jl('%s_seal_hashes.json' % ACT).get('tools') or {}) if os.path.isfile(os.path.join(D, '%s_seal_hashes.json' % ACT)) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def root_banks_state(banks, rev='HEAD'):
    import hashlib
    head = g(ROOT, 'rev-parse', rev).strip()
    rem = (g(ROOT, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    rows = []
    for b in banks:
        st = g(ROOT, 'status', '--porcelain', '--', b).strip()
        r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (head, b)], capture_output=True)
        p = os.path.join(ROOT, *b.split('/'))
        now = open(p, 'rb').read() if os.path.exists(p) else None
        eq = r.returncode == 0 and now is not None and hashlib.sha256(r.stdout).hexdigest() == hashlib.sha256(now).hexdigest()
        rows.append(dict(bank=b, status=st or 'clean', at_head=r.returncode == 0, equal=eq))
    return dict(head=head, remote=rem, rows=rows, clean=all(x['status'] == 'clean' and x['equal'] for x in rows) and bool(rows),
                pushed=bool(head) and head == rem)


ROOT_EXCLUDE = re.compile(r'^b696_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*|close_sentence|witness_balls_units)\.?(txt|json|md|jsonl|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('%s_' % ACT) and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(K.SHARED_APPENDED))


def rootbanks(*a):
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['%s -- G-ROOT-BANKS-COMMITTED`S READING: THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ;'
         ' carried by HEAD ; HEAD`s blob equal to the file' % (ACT, utc()), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('%s_root_banks.txt' % ACT, L)
    put_json('%s_root_banks.json' % ACT, dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/%s_seal_hashes.json' % ACT in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### G-ROOT-BANKS-COMMITTED: A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', ACT] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('%s_act_root.json' % ACT)
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='%s_ra_' % ACT) as tmp:
        cp_ = os.path.join(tmp, os.path.basename(bank_))
        b_ = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
        b_[0] ^= 0x01
        with open(cp_, 'wb') as fh:
            fh.write(bytes(b_))
        items2 = [('%s %s' % (bank_, AR.sha256_file(cp_)) if it.split()[0] == bank_ else it) for it in J['items']]
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
    L = ['%s -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % (ACT, utc()), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '-')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('%s_root_arm.txt' % ACT, L)
    put_json('%s_root_arm.json' % ACT, dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_final(*a):
    before = _rows_state(json.loads(_show(ROOT, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['%s -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (ACT, utc(), r.returncode, g(ROOT, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('%s_table_final.txt' % ACT, L)
    put_json('%s_table_final.json' % ACT, dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                              gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


def _g2_of(path):
    t = rd(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _standing():
    import b695_worklist as K695
    return sorted(set(_g2_of(os.path.join(ROOT, *K.B695_FACE.split('/')))) - set(K695.ACT_ARMS))


def standing(*a):
    """the standing arms b696 carries: b695's face's (G2) arms less b695's act arms (R264)(2); printed only."""
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


def armsecs(*a):
    st = _standing()
    rows, phases, runs = [], {}, {}
    for p in K.PARTS:
        j = jl('%s_arm_seconds_%s.json' % (ACT, p))
        phases[p] = j.get('phases') or {}
        runs[p] = j.get('run_secs')
        for nm, s in (j.get('arms') or {}).items():
            rows.append(dict(arm=nm, part=p, secs=s, standing=nm in st))
    srows = sorted([r for r in rows if r['standing']], key=lambda r: -r['secs'])
    miss = sorted(set(st) - set(r['arm'] for r in srows))
    L = ['%s -- THE STANDING ARMS` SECONDS AT HEAD, BY PART, FROM THE PRE-RUN (%s): the per-part seconds of the six parts' % (ACT, utc()), '',
         '### the source: data/b696_arm_seconds_<part>.json, written by tools/b696_checks.py at its pre-run, each arm`s seconds the sum of its',
         '### three readings (LIVE on the sources, NEG on a copy, POS on a mutated copy); each part`s run seconds and its phases -- the sources',
         '### built once for all its arms -- printed beside, not divided among them. standing-b2 carries no arm and is clocked by its run alone.',
         '### Rows are standing arms, slowest first:']
    L += ['  %-46s %-11s %8.3f s' % (r['arm'], r['part'], r['secs']) for r in srows]
    L += ['', '### THE PARTS` SECONDS: ' + ' | '.join('%s %s s' % (p, runs[p]) for p in K.PARTS),
          '### THE PARTS` PHASES (seconds): ' + ' | '.join('%s: %s' % (p, '; '.join('%s %.0f' % kv for kv in ph.items())) for p, ph in phases.items()),
          '### the standing arms not clocked: %s' % (miss or 'NONE'),
          '', '### ### **STANDING ARMS CLOCKED %d OF %d ; THE THREE SLOWEST %s ; THEIR SECONDS SUMMED %.1f.**' % (
              len(srows), len(st), ', '.join('%s (%s, %.2f s)' % (r['arm'], r['part'], r['secs']) for r in srows[:3]) or 'NONE',
              sum(r['secs'] for r in srows))]
    put_txt('%s_arm_seconds.txt' % ACT, L)
    put_json('%s_arm_seconds.json' % ACT, dict(at=utc(), rows=srows, phases=phases, run_secs=runs, standing=len(st), clocked=len(srows), missing=miss,
                                              slowest=[r['arm'] for r in srows[:3]]))
    print(L[-1])


# ================================================================================ THE SCORES: (N1)-(N5) OF (R306)'S FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and commits and not the entry; the entry reads the scorer's bank. `scores`
# ### writes data/b696_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there and is read at the close.
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b695_closing_push_out.txt')


def read_score_row(k, v):
    """a scores row: key N1..N5 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text)."""
    if not re.match(r'^(N[1-5]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


READERS += ['read_score_row', 'read_head']


def _git_ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t.isdigit() else None


def _iso_epoch(s):
    import calendar
    try:
        return calendar.timegm(time.strptime((s or '')[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', *K.PP_WRITTEN)
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _files_of(repo, rev):
    return sorted(x for x in g(repo, 'show', '--name-only', '--pretty=format:', rev).split(NL) if x.strip())


def _wb():
    """the witness balls' json, read out of its gz bank (rows, units in the order they were banked, the verdict)."""
    import gzip
    try:
        return json.loads(gzip.decompress(open(os.path.join(D, '%s_witness_balls.json.gz' % ACT), 'rb').read()).decode('utf-8'))
    except Exception:
        return {}


def _n1():
    cm = jl('%s_commands.json' % ACT)
    ok = bool(cm) and not cm.get('local_lean') and not cm.get('dispatches')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches: %s (relay data/b696_commands.txt, %d commands read)' % (
            cm.get('local_lean') if cm else 'unread', cm.get('dispatches') if cm else 'unread', len(cm.get('rows') or [])))


def _n2():
    calls = jl('%s_author_answers.json' % ACT).get('calls') or []
    j = _wb()
    bu = [u for u in j.get('units') or [] if u.get('route') == 'bounds']
    first = _iso_epoch(bu[0].get('at')) if bu else None
    plan_t = _git_ct(ROOT, K.STEPZERO_BANKS)
    plan_in = 'data/b696_tails_plan.txt' in _files_of(ROOT, K.STEPZERO_BANKS) and 'data/b696_source_dlmf_5_11.txt' in _files_of(ROOT, K.STEPZERO_BANKS)
    ask = [c for c in calls if c.get('line')]
    p_t = _iso_epoch((ask[-1].get('ts') if ask else '') or '')
    plan = rdn('b696_tails_plan.txt')
    cites = 'data/b696_source_dlmf_5_11.txt' in plan and ':393-:399' in plan and ':105-:107' in plan and 'data/b685_count.txt' in plan \
        and 'data/b685_search.txt :65-:66' in plan
    src = rdn('b696_source_dlmf_5_11.txt').split(NL)
    src_ok = len(src) > 399 and 'sec}^{2n+1}' in src[397] and '5.11.2' in src[104]
    ok = bool(first) and bool(p_t) and p_t < first and bool(plan_t) and plan_t < first and plan_in and cites and src_ok
    return ('HELD' if ok else 'REFUTED'), (
        'the tails plan and its source banked at step zero (relay %s, committed at %s: %s); the plan raised as one prompt at %s; the first ball`s '
        'unit (the two bounds printed with their lines) at %s, after both: %s; each tail ball`s source bound cited by line in the plan (DLMF '
        '(5.11.2) :105-:107 and its remainder :393-:399, b685`s constants, HSW at data/b685_search.txt :65-:66): %s; the source`s lines carrying '
        'what the plan cites: %s' % (K.STEPZERO_BANKS, plan_t, plan_in, p_t, first, bool(first and p_t and plan_t and p_t < first and plan_t < first),
                                     cites, src_ok))


def _n3():
    cv = _vl('%s_witness_balls_controls.txt' % ACT)
    m = re.search(r'THE TAIL BALLS SHRINK AS PREDICTED (\d+) OF (\d+)', cv)
    wb = rdn('%s_witness_balls.txt' % ACT)
    p3 = 'THE ONE PREMISE IT RESTS ON' in wb and 'P3' in wb.split(NL)[5] and re.search(r'^### DERIVED, NOT COMPILED', wb, re.M) is not None
    ok = bool(m) and m.group(1) == m.group(2) and int(m.group(1)) > 0 and p3
    return ('HELD' if ok else 'REFUTED'), (
        'each tail ball at two heights with the factor its bound predicts (relay data/b696_witness_balls_controls.txt): %s; the zero-tail ball naming '
        'P3 as the one premise it rests on (relay data/b696_witness_balls.txt :6-:7): %s' % (m.group(0) if m else '### NOT READ', p3))


def _n4():
    j = _wb()
    us = j.get('units') or []
    zi = [i for i, u in enumerate(us) if u.get('route') == 'zeta']
    qi = [i for i, u in enumerate(us) if u.get('route') in ('q0', 'c2')]
    order = bool(zi) and bool(qi) and max(zi) < min(qi)
    cv = _vl('%s_witness_balls_controls.txt' % ACT)
    c1 = re.search(r'C1 (\d+) OF (\d+) NONNEGATIVE BEYOND THE BALL RADIUS', cv)
    rows = j.get('rows') or []
    one = len(rows) == 17 and all(r.get('old_radius') and r.get('new_radius') and r.get('reading') and r.get('reading_b694') for r in rows)
    guard = 'NO Q0 TERM COMPUTED (N4)' in rd(os.path.join(T, 'b696_witness_balls.py'))
    ok = order and bool(c1) and c1.group(1) == c1.group(2) == '16' and one and guard
    return ('HELD' if ok else 'REFUTED'), (
        'the zeta control nonnegative beyond its ball radius at every width (%s) and banked before any Q0 term (the units` order, every zeta unit '
        'before the first Q0 unit: %s; the tool`s refusal: %s); every width`s reading, old radius and new radius in one row (relay '
        'data/b696_witness_balls.txt, %d rows): %s' % (c1.group(0) if c1 else '### NOT READ', order, guard, len(rows), one))


def _kernels_moved():
    t0 = _iso_epoch(_anchor_ts(K.ANCHOR) or '')
    moved, tags = [], []
    for k in dict.fromkeys(_kerns()):
        p = 'D:/' + k
        for l in g(p, 'log', '--format=%h %ct', 'main').split(NL)[:40]:
            x = l.split()
            if len(x) == 2 and x[1].isdigit() and t0 and int(x[1]) > t0:
                moved.append((k, x[0]))
        for l in g(p, 'for-each-ref', '--format=%(refname:short) %(creatordate:unix)', 'refs/tags').split(NL):
            x = l.split()
            if len(x) == 2 and x[1].isdigit() and t0 and int(x[1]) > t0:
                tags.append((k, x[0]))
    return t0, moved, tags


def _amended_after(repo, lock):
    out = []
    for l in g(repo, 'reflog', '--date=unix', '--format=%gd %gs').split(NL):
        m = re.match(r'HEAD@\{(\d+)\} (commit \(amend\).*)$', l.strip())
        if m and lock and int(m.group(1)) >= lock:
            out.append(m.group(2)[:60])
    return out


def _one_git_write():
    """the standing rule arm G-RULE-ONE-GIT-WRITE's own reading over this act's session (tools/rule_arms.py, as sealed by this act)."""
    import rule_arms as RA
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    try:
        S = RA.sources(ACT, SESSION, K.ANCHOR, K.PARTS, lock, K.PRE_RELAY, K.PRE_PP)
        ok, n, b, note = RA.reading('G-RULE-ONE-GIT-WRITE', S)
    except Exception as e:
        return False, 'the rule arm raised %s' % type(e).__name__
    return ok, note[:200]


def _n5():
    import rule_arms as RA
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    t0, moved, tags = _kernels_moved()
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b696_', x)]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b696_|audit_b696_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA) or x in ('tools/' + t for t in K.REPAIRED_TOOLS))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    arms_added = sorted(set(RA.NAMES) - set(K.STANDING_ADDED) - set(_g2_of(os.path.join(ROOT, *K.B695_FACE.split('/')))))
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock)) if lock else []
    ob = jl('%s_commands.json' % ACT).get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    chained = [d['n'] for d in (jl('%s_commands.json' % ACT).get('delete_shapes') or []) if d.get('chained')]
    gw_ok, gw_note = _one_git_write()
    ok = k_ok and not moved and not tags and not pp_beyond and not kinds_beyond and shared_tools == ['tools/rule_arms.py'] and not differ \
        and not arms_added and not amended and not ident and not pat and not chained and gw_ok
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; kernel main commits '
            'since the act began: %s; tags made since the act began: %s; no standing arm added (tools/rule_arms.py`s names beyond b695`s face): %s; '
            'shared tools edited: %s (the (R306)(2) repair, the one); sealed tools not agreeing: %s; commits amended after the seal: %s; deletes with '
            'anything chained after: %s; one git write per message (G-RULE-ONE-GIT-WRITE`s reading: %s): %s; no page or node list written '
            '(PLACE-papers beyond FINDINGS and OPEN_TRAILS): %s; relay files of a kind beyond the act`s banks and tools, the shared tool`s repair, '
            'the table, the root list and b695`s push-out bank: %s; "patent" in the lines written: %s; outbound requests other than git %d, an '
            'identifier of the author in %s' % (
                K.DRAFT, k_ok, moved or 'NONE', tags or 'NONE', arms_added or 'NONE', shared_tools or 'NONE', differ or 'NONE', amended or 'NONE',
                chained or 'NONE', gw_note, gw_ok, pp_beyond or 'NONE', kinds_beyond or 'NONE', pat or 'NONE', len(ob),
                [r['line'] for r in ident] or 'NONE'))


def _s_scores():
    import collections
    TF, RA_ = jl('%s_table_final.json' % ACT), jl('%s_root_arm.json' % ACT)
    _r, _n, sh = seal_hashes()
    return {
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))
               if TF else 'waits on the final table (relay data/b696_table_final.json)'),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally' if RA_
               else 'waits on the root and its arm (relay data/b696_root_arm.json), computed after the entry'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }


def scores(*a):
    """`scores [dry]` writes data/b696_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b696_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        return
    if close:
        put_json('%s_scores_close.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('%s_scores.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def scores_line(S):
    """the entry's scores line, composed from the scores bank alone (the act arm G-ENTRY-SCORES-EQUAL composes it the same way and compares)."""
    return '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.'


# ================================================================================ THE RECORD: THE ENTRY BEFORE THE ROOT, THE TRAIL CARRYING IT
def TRAIL_HEAD():
    return ('### b696 — lane two, act one hundred and twenty-three, the research act under (R306): b695 at its weight; the binary-hashes arm '
            'reading a corrigendum; the Weil-face witness at Q0 with its tail bounds as certified balls')


def _calls():
    return jl('%s_author_answers.json' % ACT).get('calls') or []


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _figs():
    """the figures the title and the entry carry, each read from its bank by a needle that passes a dotted name and leaves a closing period."""
    wv = _vl('%s_witness_balls.txt' % ACT)
    fw = re.search(r'FOUND AT WIDTHS ([\d, ]+?) ;', wv)
    nm = re.search(r'THE NARROWEST MARGIN AT a = (\d+), ([\d.]+ \+- [\d.e-]+)', wv)
    wb = rdn('%s_witness_balls.txt' % ACT).split(NL)
    r32 = [l for l in wb if l.startswith('  N | 32 ')]
    at = re.search(r'\| \(a\) ([\d.e-]+) \+-', r32[0]) if r32 else None
    zt = re.search(r'\| \(b\) ([\d.e-]+) \+-', r32[0]) if r32 else None
    old = re.search(r'old radius ([\d.e-]+)', r32[0]) if r32 else None
    cv = _vl('%s_witness_balls_controls.txt' % ACT)
    c3 = re.search(r'C3 (\d+) OF (\d+) AGREE', cv)
    sh = re.search(r'THE TAIL BALLS SHRINK AS PREDICTED (\d+) OF (\d+)', cv)
    ab = _vl('%s_arm_binary.txt' % ACT)
    cases = re.search(r'CASES (\d+) ; AS WANTED (\d+)', ab)
    widths = [w.strip() for w in fw.group(1).split(',')] if fw else []
    return dict(widths=widths, first=widths[0] if widths else '-', narrow=nm.group(2) if nm else '-', narrow_a=nm.group(1) if nm else '-',
                arch=at.group(1) if at else '-', zero=zt.group(1) if zt else '-', old=old.group(1) if old else '-',
                c3='%s of %s' % c3.groups() if c3 else '-', shrink='%s of %s' % sh.groups() if sh else '-',
                cases='%s of %s' % (cases.group(2), cases.group(1)) if cases else '-', discharged='THE ORDER DISCHARGED' in wv)


def _title():
    f = _figs()
    return ('## The Weil-face witness at Q0 with its tail bounds as certified balls: FOUND at every width from a = %s, the archimedean tail %s and the '
            'zero tail %s on P3; G-RULE-BINARY-HASHES reading a corrigendum for a frozen row' % (f['first'], f['arch'], f['zero']))


def _finding_text():
    """the FINDINGS entry, composed before the root: its scores line from the scores bank alone (data/b686_rules.txt row (1)); the root is
    carried by the trail record."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'With both of its tail bounds held as certified balls, the Weil-face witness at Q0 reads as before: P − PR + A for Z_Q at the off-line '
         'zero lies wholly below 0 at a = %s, the narrowest margin at a = %s, %s, its radius now the ball`s where b694`s was a float bound of %s; '
         'the identity holds at every cell with the zero tail as a ball on P3, and the ζ control stays nonnegative.' % (
             ', '.join(f['widths']), f['narrow_a'], f['narrow'], f['old']), '',
         '*Filed at b696 on the author’s ruling `(R306)` and the author’s words at its prompts; %d questions put. Banks: relay '
         '`data/b696_tails_plan.txt`, `data/b696_source_dlmf_5_11.txt`, `data/b696_witness_balls.txt`, `data/b696_witness_balls_controls.txt`, '
         '`data/b696_witness_balls_hashes.txt`, `data/b696_faces_rows.txt`, `data/b696_arm_binary.txt`, `data/b696_tool_repairs.txt`.*' % n_ans, '',
         '**The tails** (`(R306)`(3)): the plan was written and raised before any term. The archimedean tail beyond R = 4000 is bounded from the '
         'digamma expansion (DLMF 5.11.2) with its remainder bound at n = 1, sourced by line from the banked section, and |sinc w| ≤ 1/|w| on the '
         'line, in closed form in arb; it enters the sum’s radius. The zero tail above the certified height 151.59 is bounded through P3’s count '
         'law with b685’s constants a and c as balls; it enters the identity’s tolerance, which decides whether a width carries a reading; P3, '
         'derived and not compiled, is the one premise it rests on. At a = 32 the archimedean ball is %s and the zero-tail ball %s.' % (
             f['arch'], f['zero']), '',
         '**The re-read** (`(R306)`(3)(c)): every width of b694’s witness recomputed through its window, prime sum and integral, imported '
         'unedited, with the float tails replaced; every width that read FOUND at b694 reads FOUND with the ball radius, none changed; the '
         'order is discharged.', '',
         '**The controls** (`(R306)`(3)(d)-(e)): the ζ control read first at every width of both families; the identity at %s cells; each tail '
         'ball shrinking with its height by the factor its bound predicts at %s cells; T1 as re-worded -- the integral over [4000, 8000] at '
         'a = 32 lies inside the ball at 4000, and the midpoints at 128 and 256 bits agree within the 256-bit ball; T2 as before.' % (
             f['c3'], f['shrink']), '',
         '**The faces row** (`(R306)`(4)): the Weil-face line’s successor drafted with its caveat as the ruling words it -- “tail bounds as '
         'certified balls (b696), the zero tail on P3, derived and not compiled” -- the remainder unchanged, held for b697; nothing written to a '
         'node list or a page.', '',
         '**The arm** (`(R306)`(2)): G-RULE-BINARY-HASHES reads a frozen hashes row as carried where the corrigenda bank cites that bank and line '
         'with the corrected path and the equal sha256, the correction printed beside the frozen row; b694’s PNG reads so through row (9); with '
         'the corrigendum withheld, and for a planted row with none, the arm fails as before (%s cases as wanted). b695 at its weight (FINDINGS '
         ':%s).' % (f['cases'], c1_[0]), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed and raised before the component that cites '
         'them; %d answers checked before they were acted on.' % (cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-',
                                                                  checks), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b694’s witness and its plan, b685’s count law and b687’s P3 status, '
         'b695’s faces line and the corrigenda bank; it is re-read by b697, which raises the faces row. It strengthens the programme’s offering '
         'of a located clause: the Weil face at Q0 standing on certified tails, its one remaining premise P3 named.', '',
         '**Carried to:** b697 (the faces row’s regeneration prompt); `W-ORD-EPSTEIN-COUNT-LEAN` (P3’s Lean form); `W-ORD-B518-FLOAT` (b700); '
         'the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the zero tail read where it enters, the identity`s tolerance, the archimedean tail in the sum`s radius (the plan`s (1), entered as '
              'the navigator`s); (2) the zeta zero tail bounded with |delta| < 1/2 from 0 < beta < 1 and HSW, no hypothesis on zeta`s zeros above '
              '151.59; (3) T1 (ii) the integral over [4000, 8000] read against the ball at 4000, beside the ordered (i) and (iii); (4) the successor`s '
              'remainder carrying b694`s float radius left unchanged as ordered, noted for b697')


def _trail_text():
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    f = _figs()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R306) ratified.** (1) b695 at its weight. (2) The binary-hashes arm repaired. (3) W-ORD-WITNESS-TAIL-BALLS taken up. (4) The faces '
             'row`s caveat. (5) The branches. (6) The readfirst bank. (7) The draft held at v5. (8) The act after.', '',
             '**Entered:** FINDINGS.md:%s (b695`s weight), :%s (the entry); this record.' % (c1_[0], fj.get('entry_line')), '',
             '**Act root:** b696 `%s` (previous `%s`, b695`s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s (relay data/b696_author_answers.txt); none after the root.' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The order:** `W-ORD-WITNESS-TAIL-BALLS` (OPEN_TRAILS :15166, its trigger re-read at :15198) DISCHARGED by this act: the two tail '
             'bounds as certified balls, the witness re-read, FOUND at every width b694 found, the narrowest margin at a = %s, %s (relay '
             'data/b696_witness_balls.txt); the caveat removable at b697`s regeneration, the successor drafted (relay data/b696_faces_rows.txt).' % (
                 f['narrow_a'], f['narrow']) if f['discharged'] else
             '**The order:** `W-ORD-WITNESS-TAIL-BALLS` CARRIED (relay data/b696_witness_balls.txt).', '',
             '**The kernels:** none written; no runner dispatched; no lean or lake on this host.', '',
             '**The banks:** the plan relay data/b696_tails_plan.txt and its source data/b696_source_dlmf_5_11.txt; the witness relay '
             'data/b696_witness_balls.txt, its controls, its json and hashes; the faces draft relay data/b696_faces_rows.txt; the arm relay '
             'data/b696_arm_binary.txt and data/b696_tool_repairs.txt.', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b696_closing.txt).', '',
             '**The open orders:** `W-ORD-B518-FLOAT` (the reading act b700); `W-ORD-H2-BRIDGE` (annotated at :15200); `W-ORD-EPSTEIN-COUNT-LEAN` and '
             'the regularity-uses bank (b698, on the author`s word).', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b696_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S, C = jl('%s_scores.json' % ACT), jl('%s_scores_close.json' % ACT)
    L = ['=' * 104, '%s -- THE DESK.' % ACT, '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s%s' % (
        k2, S[k2][0], S[k2][1], ('  ### AT THE CLOSE: %s -- %s' % (C[k2][0], C[k2][1])) if (S[k2][0] == 'PENDING' and C.get(k2)) else '')
        for k2 in SCORE_KEYS]
    L += [''] + rdn('%s_defects.txt' % ACT).rstrip(NL).split(NL)
    put_txt('%s_desk_notes.txt' % ACT, L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('%s_scores.json' % ACT, '%s_findings.json' % ACT, '%s_trail.json' % ACT, '%s_act_root.json' % ACT))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    L = ['%s -- THE COMPONENTS, BANKED UNDER (R306).' % ACT, '',
         '### COMPONENT 0 : the citation check (data/b696_citation_check.txt), step zero (data/b696_ferry.txt, data/b696_readfirst.txt, '
         'data/b696_stepzero.txt, data/b696_tests_stepzero.txt, data/b696_rowgen_stepzero.txt, data/b696_branches.txt), the tails plan raised '
         '(data/b696_tails_plan.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b695`s weight FINDINGS :%s ; the arm repaired and run at HEAD (data/b696_arm_binary.txt, data/b696_tool_repairs.txt)' % c1_[0],
         '### COMPONENT 2 : the tails as balls (data/b696_witness_balls.txt, data/b696_witness_balls_controls.txt) ; N2 %s ; N3 %s ; N4 %s' % (
             S['N2'][0], S['N3'][0], S['N4'][0]),
         '### COMPONENT 3 : the faces successor drafted and held (data/b696_faces_rows.txt)',
         '### COMPONENT 4 : the carry-time reading (data/b696_tool_repairs.txt), the dry-run steps (data/b696_reg_gate.txt), the seal '
         '(data/b696_seal_hashes.json), the suite in six parts, the per-part seconds (data/b696_arm_seconds.txt) ; S3 %s' % S['S3'][0],
         '### COMPONENT 5 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('%s_components.txt' % ACT, L)
    print(NL.join(L[2:]))


def _land_one(path, head, e, bank, extra):
    if odd_lines(e):
        sys.exit('### ODD BACKTICKS -- NOTHING WRITTEN: %s' % odd_lines(e)[:3])
    guard_absent(path, head)
    r = append_to(path, e)
    ln = read_head(path, head)
    put_json(bank, dict(extra, line=ln, head=head, append=r, at=utc()))
    return ln


def findings(*a):
    t, e = _finding_text()
    e = conv(e)
    dry = 'dry' in a
    cells_, fired = screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells_)
        return
    if not os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, '%s_findings.json' % ACT, dict(title=t))
    j = jl('%s_findings.json' % ACT)
    j['entry_line'] = ln
    put_json('%s_findings.json' % ACT, j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = conv(_trail_text())
    dry = 'dry' in a
    cells_, fired = screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells_)
        return
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(OT, TRAIL_HEAD(), e, '%s_trail.json' % ACT, {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


FACE_REL = 'data/b696_registration_2026-10-20.txt'
FACE = os.path.join(D, 'b696_registration_2026-10-20.txt')


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them, converted by conv and run
    through the screens their landing runs, the needles the face names read in each; DRY-RUN STEP : CLEAN only when both screens are quiet and
    every needle is found. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = conv(text)
        print('  %s (the screens):' % which)
        cells_, fired = screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = _face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells_ and not fired and nd and not miss
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells_ or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


def gatebanks(*a):
    """the gate's steps between the face and the lock (b665's order), each tool's output banked by this route, never by a shell redirect."""
    import gate_hash as G

    def runb(args, out):
        r = subprocess.run([sys.executable, '-X', 'utf8'] + args, capture_output=True, cwd=ROOT)
        b_ = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            with open(p + '.tmp', 'wb') as fh:
                fh.write(b_)
            os.replace(p + '.tmp', p)
        return r.returncode, b_.decode('utf-8', 'replace')
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], '%s_reg_termscan.txt' % ACT)
    rc2, t2 = runb([os.path.join(T, '%s_regspec.py' % ACT)], '%s_regspec_run.txt' % ACT)
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/%s_satisfiable.json' % ACT, '--emit', ACT], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_%s_reg_satisfiable.txt' % ACT).split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', '%s_census_stepzero.txt' % ACT), ('b327_faces_census.py', '%s_faces_census_stepzero.txt' % ACT),
                      ('b303_pins.py', '%s_pins_stepzero.txt' % ACT)):
        rc, t = runb([os.path.join(T, tool), ACT], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/%s_reg_gate.txt' % ACT, 'data/%s_reg_termscan.txt' % ACT, 'data/%s_regspec_run.txt' % ACT, 'data/audit_%s_reg_satisfiable.txt' % ACT):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b695's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
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
    put_json('%s_mirror_build.json' % ACT, dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != ACT:
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT %s`s -- NOTHING WRITTEN' % (last[0], ACT))
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
    with open(man_p, 'wb') as fh:
        fh.write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    ps = subprocess.run(['powershell', '-NoProfile', '-Command', "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)],
                        capture_output=True, text=True)
    after = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    put_json('%s_mirror_root.json' % ACT, dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_txt('%s_mirror_verify.txt' % ACT, (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('%s_mirror_verify.txt' % ACT)
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['%s -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % (ACT, utc()),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b696 (the last export b695`s, D:/MY-DOwnloads/mirror-refresh-2026-10-20-b695.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


# ================================================================================ THE ROUTES
ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, c1=c1, armrun=armrun, repairs=repairs, facesrow=facesrow,
              commands=commands, kernels=kernels, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final, armsecs=armsecs,
              scores=scores, desk=desk, components=components, findings=findings, trail=trail, drycheck=drycheck, gatebanks=gatebanks,
              mbuild=mbuild, mroot=mroot, mverify=mverify, mbank=mbank, standing=standing)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b696_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
