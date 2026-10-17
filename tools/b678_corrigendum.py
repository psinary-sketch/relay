# -*- coding: utf-8 -*-
"""b678_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R288)(2): the 36 sentences of W-ORD-Q0-CLASS-LINES answered by one generated FINDINGS
entry, no ledger line rewritten or pinned in place.

### Reads relay data/b676_q0_lines.json, its TO RE-CUT rows, each through `read_recut_row`; for each row prints the file, the line, the sentence
### quoted verbatim and the corrected reading in one clause citing FINDINGS :8881 (b675's finding) and Zeta23/Defs.lean :142 (the strip field
### at SIDE-explicit-formula e36ea31). The reading is the clause CLAUSES gives for the row's reason; a row whose reason has no one-clause
### reading from the finding is left in the bank as CARRIED with its reason and counted. A sentence the survey cut inside an open code span
### (its backticks unpaired) is quoted with the ledger's own bytes through to the span's closing backtick, still verbatim, and said so.
### The row count is diffed against the hand count before any write. Routes:
###   `dry`   -> the entry printed, the counts printed, data/b678_corrigendum_dry.txt in the scratchpad; nothing written to a ledger;
###   `land`  -> the entry appended to FINDINGS through b678_record's guarded landing (its screens), data/b678_corrigendum.txt (.json).
### Written by the Write tool at b678 and committed alone; it writes the two banks named and the one FINDINGS entry.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv   # noqa: E402  ### the one conversion

BANK = 'b676_q0_lines.json'
HAND_COUNT = 36                 # ### the seat's hand count of the bank's TO RE-CUT rows (data/b676_q0_lines.txt, read row by row at b678)
CITE = '(FINDINGS :8881; Zeta23/Defs.lean :142 at e36ea31)'
TITLE = '## Q0 outside the kernel’s configuration class at v0.32: 36 sentences on 35 ledger lines read against b675’s finding'
CLAUSES = {
    '"the Epstein configuration"': 'read “the Epstein configuration” as the banked Epstein zero set, which is no configuration of the type',
    '"the Q0 configuration"': 'read “the Q0 configuration” as Q0’s banked points, which form no configuration of the type',
    'the Epstein instance named as an instance': 'read the Epstein instance as the theorem applied on its stated premises, Q0’s zero set itself no '
                                                 'member of the configuration type',
    'the Epstein instance of the detector`s configuration': 'read the Epstein instance as the detector applied on its stated premises, not to a '
                                                            'configuration the type admits',
    'Q0`s points as "the configuration`s points"': 'read Q0’s points as its banked zeros, not a configuration’s points',
    'Q0 named inside "the compiled class"': 'read Q0 as outside the compiled class, its zero set no configuration of the type',
    'the Q0 witness read as an instance of a theorem over a configuration': 'read the Q0 witness as a numerical reading on Q0’s banked zeros, not '
                                                                            'an instance of a theorem over a configuration',
    'the Q0 cell read as an instance of the configuration theorem': 'read the Q0 cell as a numerical reading on Q0’s banked zeros, not an instance '
                                                                    'of the configuration theorem',
    'the Q0 bank read as "the configuration" (the object named in the line`s first sentence)': 'read the Q0 bank as Q0’s banked zeros, not a '
                                                                                                'configuration',
    'Z_Q entered as an instance on premises over a configuration': 'read Z_Q’s entry as premises stated over a configuration that Q0’s zero set '
                                                                   'cannot supply',
    'the Epstein instance a page row': 'read the Epstein row as the theorem on its stated premises, Q0’s zero set no configuration of the type',
    'the Epstein count`s "configuration" presumed to exist': 'read the count as a count of Q0’s zeros, no configuration of the type presumed to '
                                                            'exist',
    'Q0 as "the real configuration"': 'read Q0 as a real form whose zero set is no configuration of the type',
    'Q0`s points as a configuration`s': 'read Q0’s points as its banked zeros, not a configuration’s',
    'every hypothesis of a configuration theorem read as certified at Q0': 'read the hypotheses as certified on Q0’s banked points, the type’s '
                                                                           'strip field failing at Q0',
    'the instance on premises over a configuration': 'read the instance as resting on premises over a configuration that Q0’s zero set cannot '
                                                     'supply',
    'Q0 read as a configuration whose target is false': 'read the configuration as the one the premises would supply, which Q0’s zero set does '
                                                        'not, the strip field failing there',
    'Z_Q`s zeros as "the zero configuration" to construct': 'read Z_Q’s zeros as a list to certify, no configuration of the type constructible '
                                                            'from them at v0.32',
    'Q0 as "the real configuration" (the object named at (2) of the line)': 'read Q0 as a real form whose zero set is no configuration of the type',
}


def rd(p):
    return io.open(p, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(p) else ''


def read_recut_row(r):
    """a TO RE-CUT row of data/b676_q0_lines.json: a ledger file, a line (an int), a kind (sentence or line), the sentence, its reason;
    returns (file, line, sentence, reason)."""
    if not isinstance(r, dict) or r.get('file') not in ('FINDINGS.md', 'OPEN_TRAILS.md') or not isinstance(r.get('line'), int) \
            or r.get('kind') not in ('sentence', 'line') or not (r.get('s') or '').strip() or r.get('reading') != 'TO RE-CUT' or not r.get('why'):
        raise ValueError('recut row of another shape: %r' % (str(r)[:120],))
    return r['file'], r['line'], r['s'], r['why']


def _quote(f, ln, s):
    """the sentence verbatim; where its backticks are unpaired (the survey cut it inside a code span), the ledger's own bytes from the
    sentence's start through the span's closing backtick, and the extension named."""
    if conv(s).count('`') % 2 == 0:
        return s, None
    led = rd(os.path.join(PP, f)).split(NL)[ln - 1]
    i = led.find(s)
    j = led.find('`', i + len(s)) if i >= 0 else -1
    if i < 0 or j < 0:
        return None, 'the sentence leaves a code span open and the ledger line does not carry it whole'
    return led[i:j + 1], 'quoted through the closing backtick of the span the survey cut (FINDINGS :%d as it stands)' % ln if f == 'FINDINGS.md' else \
        'quoted through the closing backtick of the span the survey cut (OPEN_TRAILS :%d as it stands)' % ln


def compose():
    j = json.load(io.open(os.path.join(D, BANK), encoding='utf-8'))
    rows = [read_recut_row(h) for h in j['hits'] if h.get('reading') == 'TO RE-CUT']
    out, carried = [], []
    for f, ln, s, why in rows:
        cl = CLAUSES.get(why)
        q, ext = _quote(f, ln, s)
        if cl is None or q is None:
            carried.append(dict(file=f, line=ln, s=s, why=why, reason=('no one-clause reading from the finding written for the reason %r' % why)
                                if cl is None else ext))
            continue
        out.append(dict(file=f, line=ln, s=s, quote=q, extended=ext, why=why, reading='%s %s' % (cl, CITE)))
    return rows, out, carried


def entry_text(out, carried):
    nf = sum(1 for r in out if r['file'] == 'FINDINGS.md')
    L = ['', TITLE, '',
         'Thirty-six sentences on 35 ledger lines -- 25 in FINDINGS, 11 in OPEN_TRAILS -- place Q0 or the Epstein function in the kernel’s '
         'configuration class, and b675’s finding contradicts each as worded: ZeroConfig carries the closed strip as a field of the type '
         '(Zeta23/Defs.lean :142 at SIDE-explicit-formula e36ea31), so Q0’s zero set, with zeros off that strip, is no configuration of the type '
         '(FINDINGS :8881). Each sentence is read below as corrected, %d in FINDINGS and %d in OPEN_TRAILS, %d carried; the ledger lines '
         'themselves stand as written and are pinned to nothing. Nothing here proves RH or GRH.' % (nf, len(out) - nf, len(carried)), '',
         '*Filed at b678 on the author’s ruling `(R288)`(2): generated by relay `tools/b678_corrigendum.py` from the TO RE-CUT rows of relay '
         '`data/b676_q0_lines.json`, banked as relay `data/b678_corrigendum.txt`; it answers `W-ORD-Q0-CLASS-LINES` (OPEN_TRAILS :14556).*', '']
    for r in out:
        L.append('- %s :%d -- “%s” -- %s%s.' % (r['file'].replace('.md', ''), r['line'], r['quote'], r['reading'],
                                               (' (%s)' % r['extended']) if r['extended'] else ''))
    L += ['', '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return NL.join(L)


def bank_lines(rows, out, carried, landed_line=None):
    L = ['b678 -- THE CORRIGENDUM, (R288)(2): THE TO RE-CUT ROWS OF relay data/b676_q0_lines.json ANSWERED BY ONE GENERATED FINDINGS ENTRY',
         '', '### rows are the bank`s TO RE-CUT rows: file :line | the reason | the corrected reading (one clause, both cites) | the quote`s form ;',
         '### the carried rows after them with their reasons. The ledger lines are not rewritten and receive no pin.', '']
    for r in out:
        L.append('  %s :%d | %s | %s | %s' % (r['file'], r['line'], r['why'], r['reading'], r['extended'] or 'the sentence verbatim'))
    L += ['', '### CARRIED (left in the bank with their reasons): %d' % len(carried)] + [
        '  %s :%d | %s | %s' % (c['file'], c['line'], c['why'], c['reason']) for c in carried]
    L += ['', '### THE COUNT: the bank`s TO RE-CUT rows %d ; the hand count %d ; %s ; rows written %d ; carried %d ; written + carried %d' % (
        len(rows), HAND_COUNT, 'EQUAL' if len(rows) == HAND_COUNT else '### DIFFER', len(out), len(carried), len(out) + len(carried)),
          '', '### ### **TO RE-CUT ROWS %d ; HAND COUNT %d ; WRITTEN %d ; CARRIED %d ; LEDGER LINES %d ; THE ENTRY AT FINDINGS :%s.**' % (
              len(rows), HAND_COUNT, len(out), len(carried), len(set((r['file'], r['line']) for r in out)), landed_line or 'NOT YET WRITTEN')]
    return L


def main(route):
    rows, out, carried = compose()
    if len(rows) != HAND_COUNT:
        sys.exit('### THE BANK`S TO RE-CUT ROWS %d DIFFER FROM THE HAND COUNT %d -- NOTHING WRITTEN' % (len(rows), HAND_COUNT))
    text = entry_text(out, carried)
    if route == 'dry':
        import b678_record as REC
        REC.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text)[:1500])
        print(NL.join(bank_lines(rows, out, carried)[-3:]))
        return
    import b678_record as REC
    REC.land([('FINDINGS.md', TITLE, text)], 'b678_corrigendum_landing.json', 'corrigendum', dry=False)
    ln = (REC.jl('b678_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(rows, out, carried, ln)
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b678_corrigendum.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    j = (json.dumps(dict(entry_line=ln, title=TITLE, rows=out, carried=carried, bank_rows=len(rows), hand_count=HAND_COUNT), indent=1,
                    ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, 'b678_corrigendum.json')
    open(p + '.tmp', 'wb').write(j)
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b678_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
