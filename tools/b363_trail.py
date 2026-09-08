# -*- coding: utf-8 -*-
"""b363_trail.py -- ADDITION THREE: THE OWED READ IS FILED, NOT RUN.

### ### **ONE TRAIL ENTRY, APPENDED UNDER ITS OWN MARK TO `OPEN_TRAILS.md`, APPEND-ONLY.**
### The subject is ### **THE APPLICABILITY GRADE THE LI LOCALIZATION INHERITS**: Lagarias's Theorem 5.1
### is stated for a CUSPIDAL representation, the corpus's object is the source's own marked exception,
### `b358` graded that question and `b361` stood on the grade. ### **BOTH ACTS ARE QUOTED AT THEIR OWN
### BANKS BY THE ANCHOR TOOL, AND THE SOURCE AT ITS PINNED TEXT.**
### ### **IT IS PRICED AS A READ AND IT IS NOT ATTEMPTED.** ### **NAMING A READ IS NOT PERFORMING ONE.**
### ### **THE SCAFFOLDING QUESTION, ANSWERED MECHANICALLY:** ### a bank line carries this record's `###`
### markers and a papers file does not. ### The quotation is reproduced with the markers removed and
### ### **THE EQUALITY IS CHECKED UNDER THE SHARED NORMALISER BEFORE THE APPEND** -- so "nothing else
### changed" is a computation here and not a promise.
### ### **THE SIDE, BY `b352`'s RULE:** ### the true-prefix check against the committed blob is the
### ### **PRE-PUSH** reading and is stated as such; after the push the blob IS the file.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock            # noqa: E402
import quote_norm           # noqa: E402
import anchor_from_file as AF   # noqa: E402
import gate_needle as GN    # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
MARK = '<!-- b363 li cuspidality read -->'

B358 = os.path.join(D, 'b358_the_li_asymptotics.txt')
B361 = os.path.join(D, 'b361_the_held_item.txt')
SRC = os.path.join(D, 'b358_source_lagarias0404394.txt')
PIN = '86f3d3c49f5a889f121bb1f04f67694cb9066dc8360f6988165788679594a4a7'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


# ### (tag, path, hint, how many lines of the file the quotation runs to)
QUOTES = [
    ('T-THM', SRC, 'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representation', 3),
    ('T-EXC', SRC, '2 )ζ(s). This function has simple poles at s = 0 and s = 1.', 2),
    ('T-B358', B358, '`H-CUSP` (`π` cuspidal on `GL(N)`): the corpus', 1),
    ('T-B361', B361, '(i) IT INHERITS `H-CUSP` AND DOES NOT DECIDE IT.', 6),
]


def strip_markers(s):
    """### REMOVE THIS RECORD'S OWN SCAFFOLDING AND NOTHING ELSE. ### The equality is CHECKED below.

    ### ### **THE MARKER RUNS ARE REMOVED WHEREVER THEY OCCUR AND NOT ONLY AT THE START OF A LINE** --
    ### `b362`'s incident, and the same rule `gate_needle.norm` was built under. ### A quotation spanning
    ### several lines of a bank carries them MID-LINE, where `gate_text.flat` never reached."""
    return ' '.join(re.sub(r'#{2,}', ' ', s).split()).strip()


def pull(tag, path, hint, span):
    n, line = AF.find(path, hint)
    txt = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
    raw = chr(10).join(txt[n - 1:n - 1 + span])
    q = strip_markers(raw)
    same = (GN.norm(q) == GN.norm(raw))
    return dict(tag=tag, file=os.path.basename(path), line=n, span=span, raw=raw, quote=q, equal=same)


def block(Q):
    q = {x['tag']: x for x in Q}
    return [
        '', MARK, '',
        '### **`W-ORD-LI-CUSP` — OPENED 2026-09-07 (b363): THE APPLICABILITY GRADE THE LI '
        'LOCALIZATION INHERITS**',
        '',
        ('*A trail entry, **filed and not run**. It names one read, prices it, and stops. **Nothing here '
         'is attempted, no grade is moved, no instrument is proposed and no route is offered.** Two acts '
         'are quoted at their own banks and the source at its pinned text; every quotation below was built '
         'by `tools/anchor_from_file.py` from the file itself, and where a line carries the working '
         'record’s `###` scaffolding it is reproduced without it — an equality the writing tool '
         'checks under the shared normaliser before it appends, so "and nothing else changed" is a '
         'computation here and not a promise.*'),
        '',
        ('**The hypothesis the theorem is stated under** — Lagarias, *Li coefficients for automorphic '
         'L-functions*, arXiv:math/0404394v4, pinned by b327 and re-verified by b358 at `%s`, extracted '
         'text line %d:' % (PIN, q['T-THM']['line'])),
        '',
        '> %s' % q['T-THM']['quote'],
        '',
        ('**And the object the corpus actually studies, marked by the same paper as its own exception**, '
         'extracted text line %d:' % q['T-EXC']['line']),
        '',
        '> %s' % q['T-EXC']['quote'],
        '',
        ('**So the theorem carrying the absolute constant is stated for a class the corpus’s object '
         'is explicitly outside of, and the source applies its results to it anyway under a stated '
         'convention.** That is the whole of the question filed here, and it is a question about '
         'APPLICABILITY and not about arithmetic.'),
        '',
        ('**How b358 graded it** (`data/b358_the_li_asymptotics.txt`, line %d, in that act’s table of '
         'hypotheses):' % q['T-B358']['line']),
        '',
        '> %s' % q['T-B358']['quote'],
        '',
        ('**And what b361 did with that grade** (`data/b361_the_held_item.txt`, lines %d–%d, printed '
         'under that act’s third bar — what its route is deaf to):'
         % (q['T-B361']['line'], q['T-B361']['line'] + q['T-B361']['span'] - 1)),
        '',
        '> %s' % q['T-B361']['quote'],
        '',
        ('**Why this is a trail and not a defect.** b358 did not assume the question away and b361 did not '
         'quietly inherit it — each printed it, and b361 printed the consequence in the same sentence '
         'as the inheritance. **What neither act did was read the source’s convention and say what it '
         'licenses.** The grade `MET` is recorded on the corpus axis — the corpus’s object *is* '
         'the `N = 1`, `Q = 1` case — and that is a statement about which case the object is, not a '
         'statement that §5’s proof survives the poles. **Those are two different claims, and '
         'only the first is in the record.**'),
        '',
        ('**THE PRICE, AS A READ, AND IT IS NOT PAID HERE.** Three locations, named so that a later act '
         'does not have to rediscover them: **(1)** in the pinned source, the stated convention under '
         'which the paper applies its own results to `π_triv` — where it is stated, and whether '
         '§5’s argument for Theorem 5.1 uses the entirety of `Λ(s,π)` at any step, and '
         'if it does, where the `ζ` case is repaired; **(2)** in the same source, whether '
         '`C₁(π)` and the `O(N(K(π)+1))` term in (5.1) are derived under that same '
         'hypothesis or independently of it; **(3)** in this record, which banked numbers rest on Theorem '
         '5.1’s constant rather than on the archimedean channel b358 found unconditional — a '
         'pass over the `FACES_LEDGER.md` rows citing b358 and b361 and nothing wider. **The cost is one '
         'reading component of one act: one pinned PDF across two sections, plus one ledger pass. No '
         'frame, no seed, no transform, no quadrature, no fit, no series, and no new source fetched.** It '
         'is affordable and it is not attempted here.'),
        '',
        ('*Species: **READ** (an applicability question, not a computation). **FILED AND NOT RUN.** '
         'Trigger: any act that relies on Theorem 5.1’s constant for the corpus’s object, or any '
         'act that proposes to move `H-CUSP`. Opening this entry moves nothing on its own: **b358’s '
         'grade stands exactly as b358 left it, b361’s decision stands exactly as b361 left it**, and '
         'if `H-CUSP` ever moved, b361 has already said in its own bank that its decision would move with '
         'it. Nothing here is a route, no grade moves, and `h2` stands exactly where the deposit left '
         'it.*'),
    ]


def main():
    rec('=' * 100)
    rec('b363 -- THE TRAIL ENTRY. ### FILED BY ID, PRICED, AND NOT ATTEMPTED.')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(True))
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE QUOTATIONS, BUILT FROM THEIR OWN FILES.')
    rec('-' * 100)
    Q = []
    for tag, path, hint, span in QUOTES:
        try:
            x = pull(tag, path, hint, span)
        except AF.AnchorError as e:
            rec('  ### ### **NO ANCHOR : %s** -- %s' % (tag, str(e).replace(chr(10), ' | ')[:150]))
            return 2
        Q.append(x)
        rec('')
        rec('  [%-7s] %s : line %d, span %d' % (x['tag'], x['file'], x['line'], x['span']))
        rec('      ### scaffolding removed, equal under the shared normaliser : %s' % x['equal'])
        rec('      | %s' % x['quote'][:170])
    if not all(x['equal'] for x in Q):
        rec('')
        rec('  ### ### **A QUOTATION CHANGED MORE THAN THE SCAFFOLDING. ### NOTHING IS APPENDED.**')
        run_clock.write(D, 'b363_trail_notes', LINES)
        return 3

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE APPEND. ### **APPEND-ONLY, UNDER ITS OWN MARK, NOTHING ABOVE IT EDITED.**')
    rec('-' * 100)
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ### **THE MARK IS ALREADY PRESENT. ### NOTHING IS APPENDED, AND THIS IS NOT A FAILURE**')
        rec('  ### -- it is the append-only rule refusing a second write of the same entry.')
        run_clock.write(D, 'b363_trail_notes', LINES)
        return 0
    body = chr(10).join(block(Q)) + chr(10)
    io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(body)
    after = io.open(TRAILS, encoding='utf-8', newline='').read()

    prefix_file = after.startswith(before)
    grew = len(after) - len(before)
    rec('  ### bytes before : %d ### after : %d ### grew by : %d' % (len(before), len(after), grew))
    rec('  ### ### **THE FILE BEFORE IS A TRUE PREFIX OF THE FILE AFTER : %s**' % prefix_file)

    r = subprocess.run(['git', 'show', 'HEAD:OPEN_TRAILS.md'], cwd=PP, capture_output=True)
    blob = r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))
    aft = after.replace(chr(13) + chr(10), chr(10))
    prefix_blob = aft.startswith(blob)
    rec('  ### ### **THE COMMITTED BLOB IS A TRUE PREFIX OF THE WORKING FILE : %s**' % prefix_blob)
    rec('  ### **THIS IS THE READING BEFORE THE PUSH AND IT IS THE ONE THAT CARRIES** -- `b352`s')
    rec('  ### straddling rule: after the commit the blob IS the file and the same arm proves nothing')
    rec('  ### about how it got there.')

    rec('')
    rec('=' * 100)
    ok = prefix_file and prefix_blob
    rec('  ### ### **THE ENTRY IS FILED : `W-ORD-LI-CUSP`. ### IT IS PRICED. ### IT IS NOT ATTEMPTED.**')
    rec('  ### **NAMING A READ IS NOT PERFORMING ONE**, and this act performed none of it.')
    rec('  ### append-only checks passing : %s' % ok)
    rec('=' * 100)
    p = run_clock.write(D, 'b363_trail_notes', LINES)
    io.open(os.path.join(D, 'b363_trail.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(entry='W-ORD-LI-CUSP', mark=MARK, file='OPEN_TRAILS.md',
             quotes=[dict(tag=x['tag'], file=x['file'], line=x['line'], span=x['span'],
                          equal=x['equal'], quote=x['quote']) for x in Q],
             bytes_before=len(before), bytes_after=len(after), grew=grew,
             prefix_of_file=prefix_file, prefix_of_blob=prefix_blob, side='BEFORE THE PUSH',
             attempted=False, priced=True, pin=PIN,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
