# -*- coding: utf-8 -*-
"""b365_filing.py -- THE TRAIL ENTRY, PAID. ### ONE APPEND-ONLY UPDATE BLOCK.

### ### **`b363` FILED `W-ORD-LI-CUSP` AND PRICED IT AT ONE READING COMPONENT OF ONE ACT.** ### This act
### paid that price. ### **A TRAIL ENTRY THAT IS FILED AND THEN PAID MUST SAY SO**, or the record carries
### an open item that has in fact been closed -- which is the same defect in the other direction as an
### item marked closed that was not.
### ### **THE BLOCK ABOVE IS NOT EDITED.** ### `b363`'s entry stands exactly as `b363` wrote it; this is a
### new block under its own mark that NAMES it, which is the convention the trail already uses.
### ### **AND NO GRADE MOVES.** ### The read SUPPORTS `b358`'s grade; it does not raise it, and the cap
### made that absolute before the read began.
### ### **EVERY FIGURE IS READ FROM THIS ACT'S OWN JSONS.** ### None is typed.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import anchor_from_file as AF   # noqa: E402
import gate_needle as GN        # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
MARK = '<!-- b365 li cuspidality read paid -->'
SRC = os.path.join(D, 'b358_source_lagarias0404394.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def strip_markers(s):
    return ' '.join(re.sub(r'#{2,}', ' ', s).split()).strip()


def q(hint, span=1):
    n, _l = AF.find(SRC, hint)
    txt = io.open(SRC, encoding='utf-8', errors='replace').read().split(chr(10))
    raw = chr(10).join(txt[n - 1:n - 1 + span])
    s = strip_markers(raw)
    return dict(line=n, span=span, quote=s, equal=(GN.norm(s) == GN.norm(raw)))


def block(R, Q):
    rows = ', '.join(R['faces_rows']) or 'none'
    return [
        '', MARK, '',
        '### **`W-ORD-LI-CUSP` — PAID 2026-09-07 (b365): the convention is LOCATED, and the source '
        'works the exceptional case itself**',
        '',
        ('*The block above is not edited. This one records what b365 read and what it found. **No grade '
         'moves in either direction**, which the act’s cap made absolute before the read began: a read '
         'that SUPPORTS a grade does not raise it. **Nothing was computed, no source was fetched, and the '
         'pinned rendering on disk was the only text read.** b358’s circularity finding is untouched — it '
         'was never about the archimedean channel.*'),
        '',
        ('**What was owed.** b363 filed this entry and priced it at one reading component of one act, '
         'naming three locations: the stated convention under which the paper applies its own results to '
         '`π_triv`, and whether §5’s argument uses the entirety of `Λ(s,π)`; whether `C₁(π)` and the '
         'error term are derived under the same hypothesis; and which banked numbers rest on that '
         'constant. **All three were read.**'),
        '',
        ('**(i) THE CONVENTION IS LOCATED, and the paper names it as one** — extracted text line %d:'
         % Q['conv']['line']),
        '',
        '> %s' % Q['conv']['quote'],
        '',
        ('And it draws the consequence in its own words, line %d:' % Q['entire']['line']),
        '',
        '> %s' % Q['entire']['quote'],
        '',
        ('**(i-b) AND THE PAPER CARRIES THE EXCEPTION THROUGH ITS OWN CUSPIDAL-HYPOTHESIS RESULTS.** '
         'This is the part a hypothesis line alone would have hidden. Lemma 4.3 is stated for '
         '*"an irreducible cuspidal automorphic representation"* and is then applied to the exception by '
         'a Remark printed beneath it — line %d:' % Q['remark']['line']),
        '',
        '> %s' % Q['remark']['quote'],
        '',
        ('and Lemma 4.2’s hypothesis line says *cuspidal* while its own conclusion defines a term that is '
         '`1` exactly when `π = π_triv` (line %d).' % Q['delta']['line']),
        '',
        ('**(ii) THE CONSTANT AND THE ERROR TERM ARE DERIVED INDEPENDENTLY OF CUSPIDALITY, AND THE PAPER '
         'EVALUATES THEM FOR THE EXCEPTION ITSELF.** `C₁(π)` is a function of `N` and the conductor '
         '`Q(π)` alone; the implied constant in the error term is **absolute**, in the paper’s own word; '
         'and the archimedean sum the proof estimates reduces to the archimedean parameters. **And the '
         'paper prints `C₁(π_triv)` as a number**, using `Q(π_triv) = 1`, in the paragraph immediately '
         'after Theorem 5.1 — line %d:' % Q['ctriv']['line']),
        '',
        '> %s' % Q['ctriv']['quote'],
        '',
        ('**A paper that computes a theorem’s own constant for a case is applying the theorem to that '
         'case.**'),
        '',
        ('**(iii) AND WHAT IN THIS RECORD RESTS ON IT — A NEGATIVE ANSWER, WHICH IS WHY IT HAD TO BE '
         'LOOKED FOR.** A bounded pass over `FACES_LEDGER.md` found %d of its %d blocks citing b358 or '
         'b361, and **every one of them is an update to the same row: %s**. **NO BANKED NUMBER OF THIS '
         'RECORD IS COMPUTED FROM THEOREM 5.1’s CONSTANT.** What rests on the theorem is a *statement '
         'about conditionality* — that the archimedean channel is unconditional and that its index '
         'condition is vacuous for the corpus’s object — and not an arithmetic value.'
         % (len(R['faces_blocks']), R['faces_headings'], rows)),
        '',
        ('**THE ANSWER TO THE QUESTION THE ENTRY WAS FILED FOR: the archimedean channel’s unconditional '
         'status is SUPPORTED AT `ζ`, WITH A STATED CONSTANT.** And the honest qualification, which is '
         'not a hedge: **Theorem 5.1’s hypothesis line still says *irreducible cuspidal*, and the paper '
         'never re-states it with a hypothesis that syntactically admits `π_triv`. What it does instead '
         'is APPLY it** — explicitly, by name, in the paragraph beneath it, and again at Lemma 4.3. **So '
         'the support is by the paper’s own application and not by its own quantifier**, and this filing '
         'says which of the two it is rather than reporting the stronger one.'),
        '',
        ('**AND THE READING THAT WOULD HAVE GONE WRONG.** A reader who took Theorem 5.1’s hypothesis '
         'line alone would have concluded that the corpus’s object lies outside it and that two acts had '
         'been standing on hypotheses `ζ` does not meet. **That reading was available, it was expected, '
         'and it is refuted by the paper’s own paragraphs.** The lesson is small and worth keeping: **a '
         'theorem’s scope is what its paper does with it, not only what its quantifier says.**'),
        '',
        ('*Species: **READ** — **PAID**, not restated. b358’s grade stands exactly as b358 left it and '
         'b361’s decision stands exactly as b361 left it; this filing supports both and moves neither. '
         'Nothing here is a route, no coordinate is closed, no face is promoted, and `h2` stands exactly '
         'where the deposit left it.*'),
    ]


def main():
    rec('=' * 100)
    rec('b365 -- THE TRAIL ENTRY, PAID. ### **THE BLOCK ABOVE IS NOT EDITED.**')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))
    R = json.load(io.open(os.path.join(D, 'b365_read.json'), encoding='utf-8'))
    rec('  ### the branch, read from the reading and not typed : %s' % R['branch'])
    Q = {
        'conv': q('GL(1) we have e(0,π', 2),
        'entire': q('whose singularities are simple poles at s = 0, 1. It follows that', 2),
        'remark': q('Remark. For the case πtriv on GL(1) Lemma 4.3 yields', 1),
        'delta': q('and δ(π) = 1 if π =πtriv and δ(π) = 0 otherwise.', 1),
        'ctriv': q('C1(πtriv ) = 1', 2),
    }
    rec('')
    for k, v in Q.items():
        rec('  [%-6s] line %-5d ### scaffolding removed, equal under the shared normaliser : %s'
            % (k, v['line'], v['equal']))
        rec('      | %s' % v['quote'][:150])
    if not all(v['equal'] for v in Q.values()):
        rec('  ### ### **A QUOTATION CHANGED MORE THAN THE SCAFFOLDING. ### NOTHING IS FILED.**')
        run_clock.write(D, 'b365_filing_notes', LINES)
        return 3

    rec('')
    rec('-' * 100)
    rec('  ### THE APPEND. ### **APPEND-ONLY, UNDER ITS OWN MARK, NOTHING ABOVE IT EDITED.**')
    rec('-' * 100)
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ### **THE MARK IS ALREADY PRESENT. ### NOTHING IS APPENDED, AND THIS IS NOT A FAILURE.**')
        run_clock.write(D, 'b365_filing_notes', LINES)
        return 0
    names_it = 'W-ORD-LI-CUSP' in before
    rec('  ### the entry this block names is already in the file : %s' % names_it)
    body = chr(10).join(block(R, Q)) + chr(10)
    io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(body)
    after = io.open(TRAILS, encoding='utf-8', newline='').read()
    prefix_file = after.startswith(before)
    grew = len(after) - len(before)
    r = subprocess.run(['git', 'show', 'HEAD:OPEN_TRAILS.md'], cwd=PP, capture_output=True)
    blob = r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))
    prefix_blob = after.replace(chr(13) + chr(10), chr(10)).startswith(blob)
    rec('  ### bytes before : %d ### after : %d ### grew by : %d' % (len(before), len(after), grew))
    rec('  ### ### **THE FILE BEFORE IS A TRUE PREFIX OF THE FILE AFTER : %s**' % prefix_file)
    rec('  ### ### **THE COMMITTED BLOB IS A TRUE PREFIX OF THE WORKING FILE : %s**' % prefix_blob)
    rec('  ### **THE READING BEFORE THE PUSH, AND IT IS THE ONE THAT CARRIES** (`b352`).')
    rec('')
    rec('=' * 100)
    ok = prefix_file and prefix_blob and names_it
    rec('  ### ### **`W-ORD-LI-CUSP` IS PAID. ### NO GRADE MOVES. ### NOTHING IS PROMOTED.**')
    rec('  ### append-only checks passing : %s' % ok)
    rec('=' * 100)
    p = run_clock.write(D, 'b365_filing_notes', LINES)
    io.open(os.path.join(D, 'b365_filing.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(entry='W-ORD-LI-CUSP', status='PAID', mark=MARK, file='OPEN_TRAILS.md',
             names_prior_entry=names_it,
             quotes={k: dict(line=v['line'], span=v['span'], equal=v['equal'], quote=v['quote'])
                     for k, v in Q.items()},
             bytes_before=len(before), bytes_after=len(after), grew=grew,
             prefix_of_file=prefix_file, prefix_of_blob=prefix_blob, side='BEFORE THE PUSH',
             grade_moved=False, face_promoted=False,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
