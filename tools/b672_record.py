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


ROUTES = {'c1': c1}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b672_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
