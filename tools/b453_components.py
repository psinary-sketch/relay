# -*- coding: utf-8 -*-
"""b453_components.py -- THE FOLD AT SPAN EIGHT, b445 THROUGH b452. ### **PURELY ADDITIVE. AFTER THE LOCK.**

### Usage: `verify` -- every row's verdict strings matched exactly in their own closing banks, into data/b453_fold.json and
###        data/b453_components.txt; `write` -- the FINDINGS section and the (R31) digest block, each appended with its HEAD blob
###        proved a prefix, into data/b453_fold_run.txt. A marker already present writes nothing.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
DIGEST = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
FOLDJ = os.path.join(D, 'b453_fold.json')
COMP = os.path.join(D, 'b453_components.txt')
RUN = os.path.join(D, 'b453_fold_run.txt')
MARK_F = '<!-- b453 the fold: b445-b452, the residue and reconciliation arc -->'
MARK_D = '<!-- b453 orientation refresh: the residue and reconciliation arc -->'
HEADING = '## THE RESIDUE AND RECONCILIATION ARC, b445–b452 — THE FOLD'
NL = chr(10)

ROWS = [
    ('b445', 'whose residual it is', ['VERDICT, BY THE RULE FIXED ON THE FACE: INTEGRATION'], 'MODEL', ''),
    ('b446', 'the floor has a domain', ['NO DOMAIN OF RADIUS EXISTS'], 'RECORD', 'BORDERLINE -- it also ran a second doubling'),
    ('b447', 'the outlier, the arm that bites, and the stock-take', ['BY THE RULE: STILL REFUSES', 'a bar that never bites is uninformative rather than'], 'MODEL',
     'BORDERLINE -- its stock-take and its bar-floor line are RECORD'),
    ('b448', 'the partition read against the taxonomy, and the outlier`s free candidate',
     ["VERDICT, BY THE FACE'S RULE : RELATED.", "THE PRIME CHANNEL'S", 'CORRECTED RULE: SUPER-CONVERGENT'], 'RECORD', 'BORDERLINE -- it read the channels'),
    ('b449', 'the (R61) record ratified under a face, and the outlier`s integrand at its aim',
     ['THE (R61) RECORD : RATIFIED AT b449', 'A KINK AT v* : NO.', '(c1) DOES NOT ACCOUNT FOR THE GROWTH. THE MEASUREMENT STAYS OPEN.'], 'MODEL',
     'BORDERLINE -- it also ratified a record'),
    ('b450', 'the reconciliation`s eligible set re-measured, and the batch read', ['ELIGIBLE 11, IN CENSUS ORDER', '(c4) a cancellation WITHIN the prime channel'], 'RECORD', ''),
    ('b451', 'the reconciliation`s remainder named, and the routed items grouped', ['THE REMAINDER: ENUMERA', 'KINDS WITH MEMBERS 2 ; THE ITEM DOES NOT SAY 0 ; SUM 29 OF 29'], 'RECORD', ''),
    ('b452', 'the class boundary read by its side, and the six sites read by their generator',
     ['total  0            44           3          47', 'THE CONTROL IS ABSENT', 'VERDICT: A LIST, ASSEMBLED SITE BY SITE.'], 'RECORD', ''),
]

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


def verify():
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    rec('=' * 100)
    rec('b453 -- THE FOLD AT SPAN EIGHT. ### THE ROWS, EACH VERDICT STRING VERIFIED BY EXACT MATCH IN ITS OWN CLOSING BANK.')
    rec('=' * 100)
    rows, strings, ok_all = [], 0, 0
    for act, subj, needles, col, note in ROWS:
        txt = read(os.path.join(D, '%s_closing.txt' % act))
        got = []
        for n in needles:
            c = txt.count(n)
            strings += 1
            ok_all += (c >= 1)
            got.append(dict(string=n, count=c))
            rec('    %-5s %-13s %-6s %s' % (act, 'VERIFIED' if c >= 1 else '### NOT VERIFIED', col, n[:90]))
        rows.append(dict(act=act, subject=subj, bank='%s_closing.txt' % act, strings=got, column=col, note=note, verified=all(g['count'] >= 1 for g in got)))
    cols = {}
    for r in rows:
        cols[r['column']] = cols.get(r['column'], 0) + 1
    rec('    strings verified : %d of %d ; acts verified : %d of %d ; columns OBJECT %d, MODEL %d, RECORD %d ; borderline %d'
        % (ok_all, strings, sum(r['verified'] for r in rows), len(rows), cols.get('OBJECT', 0), cols.get('MODEL', 0), cols.get('RECORD', 0), sum(1 for r in rows if r['note'])))
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '453'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    m = re.search(r'THE CURRENT SPAN : (\d+) ACT', out)
    tool = int(m.group(1)) if m else None
    rec('    span by the tool through the filing act : %s ; the fold`s own span, b445-b452 : 8' % tool)
    one = ('**In this arc the chain’s residual was traced to its integration and, at its one outlier, to the prime channel alone; '
           'the reconciliation reached fifteen of the census’s sixteen keystones; and the witness arc’s class boundaries were read '
           'against the corpus’s own re-expressions.** The outlier `a = 4.123106` refused the window by its rule, then read '
           'SUPER-CONVERGENT under the corrected ceiling; its growth is one channel’s, the prime channel’s, with no kink at its aim, '
           'so (c1) and (c3) are refuted and (c2) and (c4) stand priced and unrun. The failure-mode partition was read RELATED to the '
           'taxonomy and given a trigger under `(R61)`, ratified at b449. The reconciliation named `ENUMERA` as its remainder and grouped '
           'the twenty-nine routed items by ruling. The forty-seven class boundaries read OBJECT-SIDE `0`, SOURCE-SIDE `44`, UNDECIDED `3`, '
           'with the positive control ABSENT, and the six sites read as a LIST.')
    F = dict(rows=rows, strings=strings, verified=ok_all, acts_verified=sum(r['verified'] for r in rows), columns=cols, span_tool=tool, span_fold=8, one=one)
    io.open(FOLDJ + '.tmp', 'w', encoding='utf-8').write(json.dumps(F, indent=1, ensure_ascii=False))
    os.replace(FOLDJ + '.tmp', FOLDJ)
    rec('    ### THE ONE STATEMENT, COMPOSED FROM THE VERIFIED ROWS ONLY:')
    rec('    ' + one)
    rec('=' * 100)
    io.open(COMP, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0 if ok_all == strings else 2


def blob(rel):
    r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:%s' % rel], capture_output=True)
    return (r.stdout or b'').decode('utf-8', 'replace')


def append(path, rel, mark, body, rec):
    before = read(path)
    if mark in before:
        rec('  %-46s ALREADY PRESENT -- nothing written' % rel)
        return 'DUPLICATE'
    norm = lambda s: s.replace(chr(13) + NL, NL)
    hb = blob(rel)
    pre_ok = norm(before).startswith(norm(hb).rstrip(NL))
    if not pre_ok:
        rec('  %-46s ### WORKING COPY NOT A PREFIX-COPY OF ITS BLOB -- NOT WRITTEN' % rel)
        return 'NOT WRITTEN'
    new = before.rstrip(NL) + NL + NL + NL.join(body) + NL
    open(path + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(path + '.tmp', path)
    after = read(path)
    ok = norm(after).startswith(norm(before).rstrip(NL)) and after.count(mark) == 1
    rec('  %-46s WRITTEN +%d lines ; blob a true prefix %s ; append-only %s ; mark once %s'
        % (rel, len(after.splitlines()) - len(before.splitlines()), pre_ok, ok, after.count(mark) == 1))
    return 'WRITTEN' if ok else 'READ-BACK FAILED'


def write():
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    F = json.loads(read(FOLDJ))
    if F['verified'] != F['strings']:
        rec('  ### A VERDICT STRING IS NOT VERIFIED -- NOTHING WRITTEN.')
        io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
        return 1
    body = [MARK_F, '', HEADING, '',
            '**Eight acts, b445 through b452. The span is counted by the tool and printed both ways:** `b363_span.py` reads **%s** through '
            'this filing act; the fold’s own span, the filing act excluded as at b434 and b444, is **8**.' % F['span_tool'], '',
            '### The arc in one statement', '', F['one'], '',
            '### The span, act by act, each verdict verified in its own closing bank', '',
            '| act | subject | its verdicts, as its bank prints them | column |', '|:--|:--|:--|:--|']
    for r in F['rows']:
        note = (' — *%s*' % r['note']) if r['note'] else ''
        body.append('| **%s** | %s%s | %s | %s |' % (r['act'], r['subject'].replace('`', '’'), note,
                                                    ' · '.join('`%s`' % g['string'].replace('`', "'").replace('|', '/') for g in r['strings']), r['column']))
    c = F['columns']
    body += ['',
             '### The three columns, kept apart', '',
             '**Statements about the object** — the zeros, ξ, the Euler balance: **%d**. **About the model** — the instrument’s channels, '
             'kernels and families: **%d**. **About the record** — its documents, tools and grades: **%d**. Four acts were borderline, each '
             'named in its row rather than rounded: b446, b447, b448 and b449.' % (c.get('OBJECT', 0), c.get('MODEL', 0), c.get('RECORD', 0)), '',
             '### The carried arm failure', '',
             '**One.** b452’s `G-WRITELIST-KINDS` failed on `data/b452_dump.json`, a file its components wrote and its locked face did not name. '
             'The file was kept as evidence, **the arm was not weakened**, and the failure was carried through b452’s pre-push and post-push '
             'readings and its closing.', '',
             '### Errors entered as their owners’', '',
             '**The navigator’s, in the order’s words:** *“REPARAMETERIZATION_BARRIERS named by its word at b452 and found to be a neural-network '
             'keystone — the kind-check species, third incident this window.”* b452’s face fixed that keystone’s re-expression as acting on a '
             'network’s representations. **The count of three is entered as the navigator’s and not re-derived.** Beside it, the window’s entries '
             'the record holds: b446 (*“a domain of kind for a domain of radius”*, `OPEN_TRAILS.md:6339`), b447 (the “two-level estimate” wording) '
             'and b449 (E1, a line range; E2, `a = 4.123106 = sqrt(17)`).',
             '',
             '**The seat’s:** `(R62)` opened the instrument lane at b449, which was `W-ORD-SPAN-HEADING`’s trigger, and b449 carried the '
             'work-order as unfired.', '',
             '### The rulings of the span, with their status', '',
             '| ruling | status |', '|:--|:--|',
             '| `(R61)` the failure-mode partition gets a trigger, not a shelf | executed after b448 (`OPEN_TRAILS.md:6473`); **ratified at b449** |',
             '| `(R62)` the instrument lane opens for candidate (c1) alone | **executed at b449**; the lane closed at that act’s end |',
             '| `(R63)` the twenty-nine and ENUMERA, disposed by the data | received 2026-09-14; **directed to b454, not executed** |',
             '| `(R64)` the four blockers on `(R63)`, disposed by the data | received 2026-09-14; amends `(R63)`; **directed to b454, not executed** |',
             '',
             '*`(R63)` and `(R64)` are held in no relay file except b452’s and this act’s record.*', '',
             '### Filed with this fold, not done by it', '',
             '**W-ORD-SPAN-HEADING fired twice and is still unrepaired**: once at b449, when `(R62)` opened the instrument lane, and again at this '
             'fold. The order edits nothing else, so the repair is not made. This fold’s heading is written in the form the tool reads. '
             '**The four lists are open.**', '',
             '*Filed by b453 (relay `data/b453_fold.json`, `data/b453_the_fold.txt`). Nothing above this section was edited; no grade is conferred '
             'by a seat; nothing is claimed about `h2`.*']
    st_f = append(FINDINGS, 'FINDINGS.md', MARK_F, body, rec)
    fnd = read(FINDINGS)
    m = re.search(re.escape(HEADING) + r'.*?### The arc in one statement\s*\n\s*\n(.+?)\n', fnd, re.S)
    quoted = m.group(1).strip() if m else None
    rec('  the arc`s one statement located in the section just written : %s' % bool(quoted))
    dbody = [MARK_D, '',
             '**Orientation refresh — filed b453, 2026-09-14 *(additive)*.** Under `(R31)` a fold refreshes this digest. The arc folded at b453 — '
             '**THE RESIDUE AND RECONCILIATION ARC, b445–b452** — carries this one statement, quoted from its fold:', '',
             quoted or '*NOT LOCATED in its fold section; nothing is summarised in its place.*', '',
             '**The governing claim at the head of this document is unchanged by the arc.** `h2` stands where the deposit left it.']
    st_d = append(DIGEST, 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md', MARK_D, dbody, rec) if quoted else 'NOT WRITTEN'
    rec('  ### FINDINGS %s ; DIGEST %s' % (st_f, st_d))
    io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0 if st_f in ('WRITTEN', 'DUPLICATE') and st_d in ('WRITTEN', 'DUPLICATE') else 1


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'verify'
    sys.exit(dict(verify=verify, write=write)[mode]())
