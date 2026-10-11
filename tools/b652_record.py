# -*- coding: utf-8 -*-
"""b652_record.py -- THE ACT'S RECORD TOOL, b652 under (R262). ### **THE ONE CONVERSION OF A BACKTICK POSSESSIVE LIVES HERE** ((R262)(2)).

### b651's defects (m) and (n) had one cause: a ledger text landed through b641_record._poss (:255; a backtick before a lower-case letter
### written ’) while the look-ups ran through b551_record.poss (:678; `s written 's, straight) -- in guard_absent (:699), line_of (:704),
### append_to (:684) and the suite's poss (b651_checks :382). From this act `conv` below is the one function: the landing, the guard against a
### second landing, the line look-up, and every suite arm or reader that finds a landed line import it from here and convert by nothing else.
### Its rule is the union of the two it replaces, written typographic: a backtick between a letter, a digit or a closing parenthesis and a
### lower-case letter becomes ’. Applied twice it changes nothing more (a text with no such backtick passes through unchanged).

### Routes: `python tools/b652_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
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
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7ab48879-b65c-45b3-8af8-abdcd7120d6f/scratchpad'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CONV = re.compile(r'(?<=[A-Za-z0-9)])`(?=[a-z])')


def conv(t):
    """### THE ONE CONVERSION ((R262)(2)): a backtick standing as an apostrophe -- after a letter, a digit or `)`, before a lower-case letter --
    ### written ’. Every landing and every look-up of a landed line goes through this function."""
    return CONV.sub('’', t)


def rd(path):
    return io.open(path, encoding='utf-8').read().replace(chr(13), '')


def odd_lines(text):
    return [l[:60] for l in text.split(NL) if l.count('`') % 2]


def append_to(path, text):
    """the text converted by conv alone, refused on an odd-backtick line or a live banned stem, appended as bytes; returns the byte counts."""
    text = conv(text)
    if odd_lines(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE APPEND TO %s: %s' % (path, odd_lines(text)))
    import banned_terms as BT
    live = [m.group(0) for l in text.split(NL) for m in BT.PAT.finditer(l)]
    if live:
        sys.exit('### A BANNED STEM IN THE APPEND TO %s: %s' % (path, live))
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.basename(path), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def guard_absent(path, head):
    if conv(head).encode('utf-8') in open(path, 'rb').read():
        sys.exit('### ALREADY PRESENT IN %s: %s' % (os.path.basename(path), head[:80]))


def line_of(path, head):
    """the first line of the ledger that starts with the head, both read through conv."""
    h = conv(head)
    ls = [i + 1 for i, l in enumerate(rd(path).split(NL)) if l.startswith(h)]
    return ls[0] if ls else None


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


# ================================================================================ THE GUARDED LANDING, THE SCREENS OF b633 AND b641
def screens(items, tag, dry):
    """the screens of b633_record and b641_record over the converted texts: table cells, no-disclosure, the scanner, odd backticks by line,
    unread figures, outside names, the two stems; returns (cells, fired) and prints them."""
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b652_scanfile_%s.md' % tag)
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
    """items [(file, head, text)]: each converted by conv, screened, each head guarded absent and looked up by conv after its append at the
    line the ledger's length predicts; stops at the first line that lands elsewhere; banks [file, head, line, append]."""
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
    print('  cells expected: %s ; equal to the predicted: %s' % (list(expect_cells) or 'NONE', cells == [tuple(x) for x in expect_cells]))
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


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R262)(1) AND (2)
WH = ('*Appended 2026-10-11 by b652 to b651’s entry (:8229), under `(R262)`(1) -- b651 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b651_closing.txt), ITS FOURTEEN DEFECTS NAMED BY SEAT:*')
CH = ('*Appended 2026-10-11 by b652 beneath b651’s trail record (:13874), under `(R262)`(2) -- THE CONVERSION RULE FOR RECORD LOOK-UPS, '
      'STANDING FROM b652:*')


def _weight():
    return ('\n' + WH + ' relay 6b5cbcfa (the act) and 1a4caf67 (the closing); PLACE-papers a6e63c1; the root 51df0cb6… over 50 banks; the suite '
            '85 arms, sealed at relay be271f14, 78 of 85 before and after the push. The data and page rows repaired and the seam row re-graded '
            'DERIVES in the terminal table and the lattice bank (N1 held). The axiom-claim resolver re-binding a claim said of another named '
            'object: b649’s row 2 re-bound to TraceSilence and graded, row 5 UNBOUND, the four real contradictions unchanged, the planted test '
            '7 of 7. The census at v0.8.1 with CLUSTERS-SERVED: 4 of the 14 split kernels serving fewer than two clusters, SIDE-window served '
            'by one; the glossary’s six entries; both pages re-emitted. The four restated lines read against the build banks, none merged. '
            'SIDE-kernel’s 116 blocks read into 396 sentence rows (relay d7ab2fdb), no docstring edited; the two plain comments re-cut on a '
            'local branch, unmerged. The navigator’s 39 rows printed (relay data/b651_navigator_rows.txt: 33 OVERREACHES, 6 UNDERSTATES). '
            'Fourteen defects (relay data/b651_defects.txt): nine the seat’s -- (a) a probe that ran a whole scan, (b) a resolver grammar '
            'first too wide, (c) backticks split across a line, (d) a heredoc that collapsed a backslash, (e) a glossary source misread, (k) a '
            'commit hash read from the wrong end of a log, (l) a positive control that passed, (m) and (n) the record look-ups by the wrong '
            'conversion; five the navigator’s -- (f) the b650_closing citation, (g) the block-for-row wording of (R261)(7), (h) the sentence-row '
            'assumption, (i) the resolver clause, (j) the row count (the ruling letters the citation (g); the bank letters it (f)). After the '
            'closing the seat’s pass over the b651 banks removed a lone carriage return from relay data/b651_author_answers.txt, a bank the '
            'root names; restored from git, its bytes equal the root’s entry and its write time is later than the root’s (relay '
            'data/b652_defects.txt). Nothing deposited.\n')


def _conv_rule():
    return ('\n' + CH + ' one function converts a backtick possessive in a ledger text -- `conv` in the act’s record tool (relay '
            'tools/b652_record.py): a backtick between a letter, a digit or a closing parenthesis and a lower-case letter is written ’ -- and '
            'the same function converts the head a look-up searches for. The landing, the guard against a second landing, the line look-up, and '
            'every suite arm or reader that finds a landed line import it from the record tool and convert by nothing else. b651’s defects '
            '(m) and (n) had one cause: the record landed through b641_record’s conversion (’) while the look-ups ran through b551_record’s '
            '(a straight apostrophe), so the trail route banked no line and five suite arms failed on a record that stood as written '
            '(FINDINGS :8229, OPEN_TRAILS :13874). The suite carries a planted case: a head with a backtick possessive landed in a scratch '
            'ledger and found by the look-up at the line it landed on, the straight conversion read beside it as the control that misses '
            '(relay tools/test_conversion_b652.py).\n')


def c1(*a):
    dry = 'dry' in a
    items = [('FINDINGS.md', WH, _weight()), ('OPEN_TRAILS.md', CH, _conv_rule())]
    land(items, 'b652_record_lines.json', 'c1', entry=8229,
         check=[('FINDINGS.md', 8229, '## The re-cuts opened'), ('OPEN_TRAILS.md', 13874, '### b651 — lane three, act seventy-eight')],
         dry=dry)


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith('_'):
        print('usage: b652_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
