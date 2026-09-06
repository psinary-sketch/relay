# -*- coding: utf-8 -*-
"""b335_standing.py -- THE STANDING CLAUSES, EXTRACTED FROM THE FERRIES AND FILED, WITH THEIR PROVENANCE MEASURED.

### ### **WHAT THIS GENERATOR DOES.** ### It reads the fifteen banked ferries b320-b334 (resume pastes excluded:
### they are re-pastes of the same order), carries each standing clause as b334's ferry words it (the reference
### the sortie names) together with a normalized key, counts the ferries whose flattened lower-cased text carries
### the key (any of its alternatives), and writes `tools/FERRY_STANDING.md` ONCE -- versioned, with the citation
### form a ferry uses and every clause's count and carriers. ### **A CLAUSE IS STANDING WHEN A MAJORITY OF THE
### FIFTEEN CARRY IT** (eight or more); below that it is listed as FREQUENT, NOT STANDING. ### The seat adds no
### clause by hand: every clause here is a line of a banked ferry, located in the extract file first.
### ### `--check` re-measures every count live and compares it with the file's; the suite calls it.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OUT = os.path.join(ROOT, 'tools', 'FERRY_STANDING.md')
RUN = os.path.join(D, 'b335_standing_run.txt')
VERSION = 1
FILED = '2026-09-06 (b335)'
MAJORITY = 8

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

FERRIES = [('b320', 'b320_ferry_2026-09-04.txt'), ('b321', 'b321_ferry_2026-09-04.txt'), ('b322', 'b322_ferry_2026-09-04.txt'),
           ('b323', 'b323_ferry_2026-09-04.txt'), ('b324', 'b324_ferry_2026-09-04.txt'), ('b325', 'b325_ferry_2026-09-04.txt'),
           ('b326', 'b326_ferry_2026-09-04.txt'), ('b327', 'b327_ferry_2026-09-05.txt'), ('b328', 'b328_ferry_2026-09-05.txt'),
           ('b329', 'b329_ferry_2026-09-05.txt'), ('b330', 'b330_ferry_2026-09-06.txt'), ('b331', 'b331_ferry_2026-09-06.txt'),
           ('b332', 'b332_ferry_2026-09-06.txt'), ('b333', 'b333_ferry_2026-09-06.txt'), ('b334', 'b334_ferry_2026-09-06.txt')]

# ### (id, section, the wording as the reference ferry carries it, the source ferry and its line, the keys -- ANY matches)
CLAUSES = [
    ('C1', 'CONCURRENCY AND THE READ RULE', 'CONCURRENCY: SOLO (research seat; every read through the extract-to-disk step).', 'b334 lines 1-2',
     ['concurrency: solo (research seat']),
    ('C2', 'CONCURRENCY AND THE READ RULE', 'every read through the extract-to-disk step', 'b334 line 1-2',
     ['every read through the extract-to-disk step']),
    ('C3', 'THE PASTE PROTOCOL', 'FERRY -> CLAUDE CODE -- paste begins (part k of N; confirm receipt-in-full) ... paste ends (part k of N); the executor confirms receipt in full before executing.', 'b334 lines 4-5 and the last line',
     ['confirm receipt-in-full']),
    ('C4', 'THE STANDING SCOPE', 'NO claim about h2, totality, or the roster', 'b334 lines 12-13',
     ['h2, totality', 'totality, h2', 'about totality']),
    ('C5', 'THE STANDING SCOPE', 'every quantity by two routes sharing no code', 'b334 lines 16-17',
     ['two routes sharing no code', 'two routes']),
    ('C6', 'THE STANDING SCOPE', 'the like-for-like rule enforced by name (every comparison names the test function on both sides -- b333\'s species)', 'b334 lines 17-19',
     ['like-for-like']),
    ('C7', 'THE STANDING SCOPE', 'normalizations before counts', 'b334 line 19',
     ['normalizations before counts']),
    ('C8', 'THE STANDING SCOPE', 'the noise-floor gate in the path', 'b334 lines 19-20',
     ['noise-floor gate']),
    ('C9', 'THE REGISTRATION', 'registration sealed before any instrument runs, no counts predicted', 'b334 lines 20-21',
     ['registration sealed before any', 'registration term-scanned', 'registration satisfiability-checked']),
    ('C10', 'THE REGISTRATION', 'no counts predicted', 'b334 line 21',
     ['no counts predicted']),
    ('C11', 'THE STANDING SCOPE', 'needles from the extract file', 'b334 line 21',
     ['needles from the extract file']),
    ('C12', 'THE STANDING SCOPE', 'stem sweep at extended scope', 'b334 lines 21-22',
     ['stem sweep at extended scope']),
    ('C13', 'THE STANDING SCOPE', 'hedge audit', 'b334 line 22',
     ['hedge audit']),
    ('C14', 'THE STANDING SCOPE', 'run files written once per path', 'b334 lines 22-23',
     ['run files written once per path', 'run file written once', 'written once per path']),
    ('C15', 'THE STANDING SCOPE', 'the suite re-run after the push', 'b334 line 23',
     ['the suite re-run after the push', 'suite re-run after the push']),
    ('C16', 'THE STANDING SCOPE', 'nothing deposits', 'b334 line 23',
     ['nothing deposits']),
    ('C17', 'THE STANDING SCOPE', 'every reported number from a committed tool with fixtures', 'b320 lines 23-24',
     ['every reported number from a committed tool with fixtures', 'committed tool with fixtures']),
    ('C18', 'STEP ZERO', 'STEP ZERO: the ferry scan; both censuses; push anything ahead of origin, saying so if nothing is.', 'b334 lines 25-26',
     ['step zero: the ferry scan']),
    ('C19', 'STEP ZERO', 'both censuses (the handoff census and the faces-ledger census, each with its scope)', 'b334 line 25; b320 line 26 (the ledger census with its scope)',
     ['both censuses', 'the ledger census', 'ledger census']),
    ('C20', 'STEP ZERO', 'push anything ahead of origin, saying so if nothing is', 'b334 lines 25-26',
     ['push anything ahead of origin, saying so if nothing is']),
    ('C21', 'EXECUTION', 'EXECUTION: ferry scan first; registration sealed before any instrument runs; the extract step for every read; components in order; full control suite, re-run after the push; pins by ls-remote across all three repos; the hook if PLACE-papers is touched; mirror if it moves. STOP.', 'b334 lines 72-76',
     ['execution: ferry scan first']),
    ('C22', 'EXECUTION', 'the extract step for every read', 'b334 line 73',
     ['the extract step for every read']),
    ('C23', 'EXECUTION', 'components in order', 'b334 lines 73-74',
     ['components in order', 'components in\norder']),
    ('C24', 'EXECUTION', 'full control suite, re-run after the push', 'b334 line 74',
     ['full control suite, re-run after the push']),
    ('C25', 'EXECUTION', 'pins by ls-remote across all three repos', 'b334 lines 74-75',
     ['pins by ls-remote across all three repos']),
    ('C26', 'EXECUTION', 'the hook if PLACE-papers is touched; mirror if it moves (the hook exercised with its result reported either way; the mirror rebuilt AFTER the commit and verified on all three clauses)', 'b334 lines 75-76; b327 lines 92-94',
     ['the hook']),
    ('C27', 'EXECUTION', 'STOP. (the order ends; the executor stops at the closing)', 'b334 line 76',
     ['stop.']),
    ('C28', 'CLOSING', 'CLOSING: the correspondence rows (by the idempotent tool); every result keyed', 'b334 line 61; b327 line 78',
     ['the correspondence rows']),
    ('C29', 'CLOSING', 'every result keyed', 'b334 line 61',
     ['every result keyed']),
    ('C30', 'CLOSING', 'Registration gate; index queried; the act\'s results keyed. Components ordered.', 'b334 lines 69-70',
     ['registration gate; index queried', 'index queried']),
    ('C31', 'CLOSING', 'THE SHADOW: expected nothing; say so.', 'b334 line 70',
     ['the shadow: expected nothing', 'the shadow']),
    ('C32', 'THE STANDING ROWS', 'M-2\'s row unchanged under its cap (SPECIFIED-NOT-STATED, b310)', 'b334 line 64',
     ["m-2's row unchanged under its cap", 'm-2 owed under its cap', 'm-2']),
    ('C33', 'THE STANDING ROWS', 'the seam\'s debt item 1 restated', 'b334 lines 64-65',
     ["the seam's debt item 1 restated"]),
    ('C34', 'THE STANDING ROWS', 'the patent clock restated (carried on the patent seat\'s report, UNCONFIRMED on this seat\'s record)', 'b334 line 65',
     ['the patent clock restated', 'patent clock']),
    ('C35', 'THE FOOT', 'h2 stands exactly where the deposit left it; locks last.', 'b334 lines 82-83',
     ['h2 stands exactly where the deposit left it']),
    ('C36', 'THE FOOT', 'locks last', 'b334 line 83',
     ['locks last']),
    ('C37', 'THE DEVIATION RULE', 'Bank: data/bNNN_<the act\'s name>.txt. Deviation rule standing.', 'b334 line 70 (the bank line)',
     ['deviation rule standing']),
]

SECTIONS = ['CONCURRENCY AND THE READ RULE', 'THE PASTE PROTOCOL', 'THE STANDING SCOPE', 'STEP ZERO', 'THE REGISTRATION', 'EXECUTION', 'CLOSING',
            'THE STANDING ROWS', 'THE FOOT', 'THE DEVIATION RULE']


def flat(path):
    t = io.open(path, encoding='utf-8', errors='replace').read().lower()
    return re.sub(r'\s+', ' ', t)


def measure():
    texts = [(act, flat(os.path.join(D, fn))) for act, fn in FERRIES]
    out = []
    for cid, sec, wording, src, keys in CLAUSES:
        carriers = [act for act, t in texts if any(re.sub(r'\s+', ' ', k.lower()) in t for k in keys)]
        out.append(dict(id=cid, section=sec, wording=wording, source=src, keys=keys, count=len(carriers), carriers=carriers))
    return out


def render(rows):
    n = len(FERRIES)
    L = []
    L.append('# FERRY_STANDING -- the standing clauses of the research seat\'s ferries')
    L.append('')
    L.append('VERSION: %d' % VERSION)
    L.append('FILED: %s' % FILED)
    L.append('CITE AS: `FERRY_STANDING v%d` (a ferry that cites this file carries every STANDING clause below by reference; the ferry scan reports a citation of any other version as a stale citation)' % VERSION)
    L.append('RANGE: the %d banked ferries b320-b334 (`relay/data/b3NN_ferry_<date>.txt`; resume pastes excluded, they are re-pastes)' % n)
    L.append('RULE: a clause is STANDING when a majority of the range carries it (%d or more of %d); a clause below that is listed as FREQUENT, NOT STANDING; the seat adds none by hand -- every clause is a line of a banked ferry, the wording b334\'s where b334 carries it' % (MAJORITY, n))
    L.append('STRUCK CLAUSES: `relay/data/STRUCK_CLAUSES.md` is the record (S-1, U-1, U-2 STRUCK as of b300); it is referenced here and not restated; the ferry scan reads it')
    L.append('THIS FILE BINDS NOTHING BY ITSELF: a ferry that restates a clause is not in conflict with it; a ferry that strikes or amends a clause does so in the ferry, and the next version of this file records it')
    L.append('GENERATOR: `relay/tools/b335_standing.py` (written once; `--check` re-measures every count)')
    L.append('')
    for sec in SECTIONS:
        L.append('## %s' % sec)
        L.append('')
        for r in rows:
            if r['section'] != sec or r['count'] < MAJORITY:
                continue
            L.append('- **%s** %s  — carried by %d of %d (%s); source %s' % (r['id'], r['wording'], r['count'], n, ' '.join(r['carriers']), r['source']))
        L.append('')
    freq = [r for r in rows if r['count'] < MAJORITY]
    L.append('## FREQUENT, NOT STANDING')
    L.append('')
    if freq:
        for r in freq:
            L.append('- **%s** (%s) %s  — carried by %d of %d (%s); source %s' % (r['id'], r['section'], r['wording'], r['count'], n, ' '.join(r['carriers']), r['source']))
    else:
        L.append('- none: every clause carried here is standing')
    L.append('')
    L.append('## HOW A FERRY CITES THIS FILE')
    L.append('')
    L.append('One line in the ferry\'s head, for example: `Standing clauses: FERRY_STANDING v%d, carried by reference.` The ferry then states only what is specific to the act. The scan (`relay/tools/ferry_scan.py`) reads the version cited against the `VERSION:` line here and reports NONE, CURRENT, STALE or NO FILE; a STALE citation is a hit, and the reader rules.' % VERSION)
    L.append('')
    return chr(10).join(L) + chr(10)


def check(rows):
    txt = io.open(OUT, encoding='utf-8').read()
    bad = []
    for r in rows:
        m = re.search(r'\*\*%s\*\*.*?carried by (\d+) of (\d+)' % re.escape(r['id']), txt)
        if not m or int(m.group(1)) != r['count']:
            bad.append((r['id'], r['count'], m.group(1) if m else None))
    ver = re.search(r'^VERSION: (\d+)$', txt, re.M)
    return bad, (int(ver.group(1)) if ver else None)


def main(argv):
    rows = measure()
    lines = []

    def rec(s=''):
        lines.append(s)
        print(s)

    rec('=' * 100)
    rec('b335_standing.py -- THE STANDING CLAUSES, MEASURED OVER %d FERRIES (b320-b334).' % len(FERRIES))
    rec('=' * 100)
    rec('  %-5s %-30s %5s  %s' % ('id', 'section', 'count', 'carriers'))
    for r in rows:
        rec('  %-5s %-30s %5d  %s' % (r['id'], r['section'][:30], r['count'], ' '.join(r['carriers'])))
    standing = [r for r in rows if r['count'] >= MAJORITY]
    rec('  clauses measured %d ; STANDING (>= %d of %d) %d ; FREQUENT, NOT STANDING %d' % (len(rows), MAJORITY, len(FERRIES), len(standing), len(rows) - len(standing)))
    if argv and argv[0] == '--check':
        bad, ver = check(rows)
        rec('  --check : VERSION in file %s ; counts disagreeing with the file %d %s' % (ver, len(bad), bad if bad else ''))
        rec('=' * 100)
        return 0 if (not bad and ver == VERSION) else 1
    if os.path.exists(OUT):
        rec('  ### %s EXISTS -- NOT REWRITTEN (a new version is a new act).' % os.path.basename(OUT))
        rec('=' * 100)
        return 3
    text = render(rows)
    open(OUT + '.tmp', 'wb').write(text.encode('utf-8'))
    os.replace(OUT + '.tmp', OUT)
    back = io.open(OUT, encoding='utf-8').read()
    bad, ver = check(rows)
    rec('  WRITTEN %s : %d bytes ; VERSION %s ; read back: counts disagreeing %d' % (os.path.basename(OUT), len(back.encode('utf-8')), ver, len(bad)))
    rec('=' * 100)
    io.open(RUN, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    return 0 if (back == text and not bad and ver == VERSION) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
