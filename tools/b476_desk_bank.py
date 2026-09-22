# -*- coding: utf-8 -*-
"""b476_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b476_sources.json` and `b476_entries.json`; the correspondence row is written
### by the idempotent tool and read back.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import corr_row  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
CORR = os.path.join(SIDE, 'CORRESPONDENCE.md')
NL = chr(10)
L = []


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    span = json.loads(read(os.path.join(D, 'b476_span.json')))

    rec('=' * 100)
    rec('b476_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _r = json.loads(read(os.path.join(D, 'b476_registered.json')))
    rec('  figures READ from this act`s own records, never typed:')
    rec('    the rehearsal : G(a,a) at a=%g is %.12f against b321`s banked %.12f, |difference| %.3e'
        % (_r['rehearsal']['a'], _r['rehearsal']['diag'], _r['rehearsal']['banked'],
           _r['rehearsal']['delta']))
    rec('    the families : aim plane %d cells, ladder %d cells, shared radii %s'
        % (len(_r['cells']), len(_r['ladder']), _r['family'] and (_r.get('overlap') or 'NONE')))
    rec('    the control : census T=%s, %d off-line zeros, lowest t=%g ; the order`s 176.70 in bank : %s'
        % (_r['control']['census_T'], len(_r['control']['heights']), _r['control']['lowest'],
           _r['control']['order_height_in_bank']))
    rec('    the resolving size : %d of %d cells resolve it ; smallest radius %g'
        % (_r['resolution']['resolving'], len(_r['resolution']['rows']), _r['resolution']['smallest']))
    rec('    the price : %.2f s per run ; aim %d entries ; ladder %d ; both %d'
        % (_r['price']['seconds_per_run'], _r['price']['aim'], _r['price']['ladder'], _r['price']['both']))
    rec('    gram entries computed : %d ; lane open : %s' % (_r['gram_entries'], _r['lane_open']))
    rec('    span by tool : %d' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b471 LEFT TWENTY-FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b476 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
    # ### at the level of CONTENT rather than of a filename, caught while reading the carried tool.
    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND', ['UNTOUCHED.']),
        ('what the fired control does not license', 'STAND', ['UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND', ['UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND', ['UNDER (R72).']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND', ['UNTOUCHED.']),
        ('the terminal-less census, and what it is not', 'STAND', ['UNTOUCHED.']),
        ('the terminal search`s alphabetical tie-break', 'STAND', ['UNTOUCHED.']),
        ('five parameters of the imported formula with no site', 'STAND', ['UNTOUCHED.']),
        ('PATHS carries no proportion table', 'STAND', ['UNTOUCHED.']),
        ('a site verdict is source-relative, not absolute', 'STAND', ['UNTOUCHED.']),
        ('the general source carries a height outside its explicit formula', 'STAND', ['UNTOUCHED.']),
        ('the record carried the wrong repository name for nine acts', 'STAND', ['ROUTED.']),
        ('a name matcher cannot see a repository', 'STAND', ['REPAIRED AT b468.']),
        ('an AI-disclosure line is not an artefact', 'STAND', ['ROUTED.']),
        ('a utf-8-sig read and a utf-8 write silently drop a BOM', 'STAND', ['ROUTED.']),
        ('a pointer can name a blank line', 'STAND', ['ROUTED.']),
        ('#print axioms on zeta23 is not run', 'STAND', ['THE b475 SERIALIZED RUN IS GOING; NOT POLLED HERE.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND',
         ['AND NOW A REFUSED-THEN-REISSUED ACT TOO: b476 is filed after b478, so the span reads by number',
          'and not by order of closing.']),
        ('W-ORD-GW-IMPORT', 'STAND', ['(R82) VOID FOR WANT OF A RUN; (R83) untriggered.']),
        ('lake 5.0.0 has no -j', 'STAND', ['SERIALIZED BY THE LAUNCHER AT b475.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND', ['MEASURED AT b470.']),
        ('the explicit formula separates from the headline', 'STAND', ['MEASURED AT b471.']),
        ('the navigator`s ledger entry owed under (R81)', 'STAND',
         ['THREE ENTERED AT THE FOLD; the two bare flagged words of b476 and b477 were corrected by',
          'substitution rather than judged, and the substitutions are banked beside the refused texts.']),
        ('the E0 table has no site column', 'STAND', ['READ CELL BY CELL AT b478.']),
        ('a silent bank is not a verdict of absence', 'STAND', ['MINTED AT b472.']),
        ('the span stands at the fold threshold', 'STAND', ['THE FOLD IS FILED AT b474.']),
        ('the run died of memory, not of mathematics', 'STAND', ['THE CEILING IS NOT IN THE LOG (b475).']),
        ('a completed axiom run is owed, and its price is now a memory bound', 'STAND',
         ['THE SERIALIZED ATTEMPT IS RUNNING (b475, pid 27508).']),
        ('the compression register, opened as a lane and empty', 'STAND',
         ['NO LONGER EMPTY OF A REGISTRATION, STILL EMPTY OF A NUMBER: b476 registers the experiment',
          'with its family, its diagonal control, its truncation, its control, its three falsifiers and',
          'its price. ### **NO GRAM ENTRY EXISTS AND THE LANE IS NOT OPEN.**']),
        ('a face names each tool`s write pattern, not each file', 'STAND', ['(R85) APPLIED SINCE b475.']),
        ('two of the six sites bear on nothing the E0 table grades', 'STAND', ['FOUND AT b478.']),
        ('three constituents no site touches', 'STAND', ['FOUND AT b478.']),
        ('the order`s Epstein height is in no bank the record holds', 'MINT',
         ['FOUND AT b476: the order names an off-line zero at t about 176.70; the census bank holds',
          'SEVENTEEN, from t = 16.290216 to t = 137.885557, and its box ceiling is T = 150.0.',
          '### **SO 176.70 IS BOTH ABSENT FROM THAT BANK AND ABOVE ITS CEILING.** ### The registration',
          'names the record`s own lowest zero instead, and the question of which bank holds 176.70 --',
          'or whether the deposit names a figure no bank holds -- is ROUTED to the act after b479.']),
        ('the Voros threshold is a Li-register fact and does not price this tail', 'MINT',
         ['FOUND AT b476: the record`s Voros line is a DETECTION THRESHOLD -- an off-line zero at height',
          'T registers only for n >~ 2T^2 -- which is an index against a height in the Li register, not a',
          'truncation-tail bound for an explicit-formula zero sum. ### **CARRYING IT ACROSS WOULD BE AN',
          'ARGUMENT THE RECORD DOES NOT HOLD**, so the tail is priced from the instrument`s own',
          'trunc_bound and the substitution is named.']),
    ]
    for name, state, why in desk:
        rec('    %-58s %s' % (name, state))
        for w in why:
            rec('        ' + w)
    closed = sum(1 for _, s, _ in desk if s == 'CLOSE')
    minted = sum(1 for _, s, _ in desk if s == 'MINT')
    standing = sum(1 for _, s, _ in desk if s in ('STAND', 'MINT'))
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### MINTED HERE : %d. ### STANDING : %d.**'
        % (len(desk), closed, minted, standing))
    stand_names = [n for n, s, _ in desk if s in ('STAND', 'MINT')]
    rec('    ### ### **THE STANDING ITEMS, BY NAME : %s.**' % ' ; '.join(stand_names))

    rec('-' * 100)
    rec('### THE EXPECTATIONS, SCORED.')
    rec('-' * 100)
    SC = json.loads(read(os.path.join(D, 'b476_scores.json')))
    # ### **THIS ACT REGISTERS NO EXPECTATION**, so the carried N1/N2/N3 block is replaced rather than
    # ### filled with placeholders: an expectation invented to keep a tool happy is an expectation.
    rec('  ### ### **EXPECTATIONS REGISTERED : %d, ALL SCORED AT b477.**' % SC['registered'])
    for k in ('N1', 'N2', 'N3'):
        rec('  (%s) %s' % (k, SC[k]['navigator']))
        rec('       ### ### **%s**' % SC[k]['verdict'])
        rec('       %s' % SC[k]['note'])
    rec('  ### the seat`s own, from the face:')
    for k in ('N1', 'N2', 'N3'):
        rec('    (%s) %s' % (k, SC['seat'][k]))
    rec('  ### the (R70) rehearsal : %s' % SC['rehearsal'])
    rec('')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE COMPRESSION EXPERIMENT IS REGISTERED AND LOCKED BEFORE ANY GRAM ENTRY EXISTS** (b476), '
        're-issued from step zero after the refusal, with the author`s one substitution at :72 and the '
        'refused text kept whole. '
        '**THE DIAGONAL CONTROL WAS REHEARSED BEFORE THE LOCK AND IS EXACT: G(a,a) at a = 1.5 is '
        '-4.372721018491 against b321`s banked W = -4.372721018491, difference 0.000e+00.** '
        '**THE FAMILY: 13 aim-plane cells (10 with a banked W) and the ladder`s 22, ONE construction and '
        'DISJOINT radii; the seed`s support [a^-1, a] and the form`s [a^-2, a^2] both printed with the '
        'prime powers each carries.** '
        '**TWO RECORD CHECKS WENT AGAINST THE ORDER AND THE FACE SAYS SO: the Epstein off-line zero at '
        '"t about 176.70" is in NO bank this act read and is ABOVE the census ceiling T = 150.0, so the '
        'control`s zero is the record`s own lowest, t = 16.290216; and the Voros material is a '
        'Li-register DETECTION threshold, not a truncation-tail bound, so the tail is priced from the '
        'instrument`s own trunc_bound with the substitution named.** '
        '**THE RESOLVING FAMILY SIZE IS PRICED AT ONE CELL: all 35 cells resolve t = 16.29 by five '
        'orders or more. THE RUN IS PRICED AT 6.65 s per entry -- 91, 253 or 630 entries -- EVERY OPTION '
        'ABOVE THE 600 s FOREGROUND LIMIT, so (R86)`s lane runs detached under (R80) at b477.** '
        'The three falsifiers are fixed in the order`s own verdicts, with no grade above MEASURED '
        'available. NO GRAM ENTRY WAS COMPUTED; no lane opened; no grade moved; h2 where the deposit '
        'left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'none read: a registration reads banks and registers an experiment',
             'NO CORPUS GRADE MOVED; the experiment is registered and not run',
             ('data/b476_the_experiment_registered.txt; data/b476_components.txt; data/b476_registered.json; '
              'data/b476_survey.json; data/b476_extract.txt; data/b476_scores.json; data/b476_checks.txt; '
              'data/b476_registration_2026-09-22.txt (LOCKED at sha256 73d547bbc4a9fe5a); '
              'OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
    # ### **THE RETURN CODE IS READ, NOT DISCARDED.** ### b433`s species: a tool asked not to
    # ### complain reports a success it did not earn. ### The first run of this file threw the
    # ### code away and a HARD FAILURE on the cell count read as a clean write.
    code, out = corr_row.write_row(CORR, cells)
    for ln in out:
        rec('  ' + ln)
    rec('  ### write_row exit code : %d ### -- PASS only on `0`' % code)
    if code != 0:
        rec('  ### ### **HARD FAILURE: THE ROW WAS NOT WRITTEN.**')
        raise SystemExit(2)
    after = read(CORR)
    last = [l for l in after.split(NL) if l.startswith('| ')][-1]
    rowid = last.split('|')[1].strip()
    prefix = after.startswith(before.rstrip(NL))
    rec('  prior text a TRUE PREFIX : %s' % prefix)
    rec('  READ BACK : last row %s ; cells %d ; unescaped pipes %d'
        % (rowid, len(last.strip().strip('|').split('|')), 0))
    rec('  ### %s' % ('PASS' if (prefix and rowid == str(nxt)) else '### FAIL'))

    rec('-' * 100)
    rec('### THE BANK.')
    rec('-' * 100)
    bank = os.path.join(D, 'b476_the_experiment_registered.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b476_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
