# -*- coding: utf-8 -*-
"""reg_seal.py -- `W-ORD-REG-HASH`, built b263.

### WHY THIS EXISTS. b262 was cut by an API drop mid-act. ### On resume the ferry asked for the
### registration's hash "vs the banked line" and ### **THERE WAS NO BANKED LINE.** ### The only
### surviving evidence that the registration was unchanged was an mtime ordering and a term scan --
### both real, both weaker than a hash taken at writing time.
### ### **A HASH TAKEN AFTERWARDS IS A DESCRIPTION. ### A HASH BANKED AT WRITING TIME IS PROOF.**
###
### THE OBVIOUS OBJECTION, AND ITS ANSWER, BECAUSE IT IS WHY THIS IS A TOOL AND NOT A HABIT:
### ### **A FILE CANNOT CONTAIN ITS OWN HASH.** ### So the seal hashes ### EVERY BYTE ABOVE THE
### ### SEAL BLOCK ### and appends the block. ### Verification recomputes over the same prefix.
### ### That is a fixed point: sealing is idempotent and verifying is total.
###
### ### THE REACH, STATED SO THE TOOL IS NOT TRUSTED BEYOND IT:
### ### **IT PROVES THE BODY HAS NOT CHANGED SINCE THE SEAL WAS WRITTEN. ### IT PROVES NOTHING
### ### ABOUT ### WHEN ### THE SEAL WAS WRITTEN.** ### A forger who edits the body and re-seals
### ### produces a consistent file. ### **THIS RAISES THE COST OF AN UNDETECTED EDIT FROM ZERO TO
### ### DELIBERATE -- THE SAME REACH `audit_emit` CLAIMS FOR ITS SIDECARS, AND NO MORE.**
### ### What makes it evidence in practice is that the seal is COMMITTED with the act: after the
### ### push, git's own history dates it, and a later re-seal is a visible diff.

### ### **THE LOCK BLOCK, ADDED AT b358 BY THE AUTHOR'S RULING (R3), PROSPECTIVE ONLY.** ### The ruling
### retires *sealed* for a registration: ### **A REGISTRATION IS LOCKED, IT PRODUCES A LOCK BLOCK, AND ITS
### ### BARS ARE LOCKED BARS.** ### `--lock` writes that block. ### **NOTHING IS EDITED AND NOTHING IS
### ### RETIRED IN THE FILE:** ### `--seal` is untouched, `split_body` now recognises EITHER mark, and
### **EVERY REGISTRATION SEALED BEFORE THIS LINE STILL VERIFIES BYTE-FOR-BYTE UNCHANGED** -- which is
### checked by `--selftest`, on both marks, both polarities. ### The hash semantics are identical: the
### digest covers every byte ABOVE the block, and the clock sits outside the hash exactly as before.
### ### **THE FILENAME STILL SAYS `reg_seal`.** ### The ruling says filenames migrate at convenience, and
### renaming a tool that fifty banked registrations name in their own text is not convenience.

Usage:
    python reg_seal.py --lock <file>      write the LOCK block (refuses if already locked or sealed)
    python reg_seal.py --seal <file>      write the seal block (retired wording; kept working)
    python reg_seal.py --verify <file>    recompute and compare; exit 1 on mismatch
    python reg_seal.py --selftest         both marks, both polarities, on temporary files
"""
import datetime
import hashlib
import io
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BAR = '=' * 100
MARK = '### THE REGISTRATION SEAL (emitted by tools/reg_seal.py; do not retype).'
# ### **THE LOCK MARK (b358, ruling R3).** ### A second mark, never a replacement: `split_body` accepts
# ### either, so a file carrying the old mark verifies exactly as it always did.
LOCKMARK = '### THE REGISTRATION LOCK (emitted by tools/reg_seal.py; do not retype).'
MARKS = (MARK, LOCKMARK)
PREFIX = '### sha256 of every byte ABOVE this block : '
# ### ### **THE SEAL'S OWN CLOCK, ADDED AT b344 BY THE ORDER'S WORDS** -- *"have reg_seal.py record the seal's UTC
# ### instant inside the seal block it writes"*. ### **WHY:** b342's order arm was declared a defective bar because a
# ### lawful post-seal marking rewrites the registration file, and the seal block carried a hash and a byte count but
# ### no time, so a component written between the seal and the marking could not be told from one written before the
# ### seal. ### **THE LIMIT, STATED WHERE THE LINE IS WRITTEN: THE CLOCK IS OUTSIDE THE HASH.** ### `digest` and
# ### `cmd_verify` are untouched; they cover the bytes ABOVE the block, so every seal written before this line existed
# ### still verifies unchanged, and a clock line altered after the fact does not make a file fail. ### It records when
# ### the seal was written by a tool that meant to record it. ### **IT RECOVERS NOTHING SEALED BEFORE IT, b342's OWN
# ### TIMESTAMP INCLUDED.**
CLOCK = '### sealed at (UTC) : '


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def split_body(text):
    """### RETURN (body, hex_or_None). ### The body is everything above the seal OR lock bar.
    ### ### **EITHER MARK IS ACCEPTED, AND THE EARLIEST ONE WINS**, so a registration sealed before b358
    ### splits exactly where it always did."""
    hits = [text.find(BAR + '\n' + m) for m in MARKS]
    hits = [h for h in hits if h >= 0]
    if not hits:
        return text, None
    i = min(hits)
    body = text[:i]
    tail = text[i:]
    for line in tail.split('\n'):
        if line.startswith(PREFIX):
            return body, line[len(PREFIX):].strip()
    return body, ''


def digest(body):
    return hashlib.sha256(body.encode('utf-8')).hexdigest()


def gate_record_check(path, body):
    """### **`(R56)`, b443: THE SEAL REFUSES A REFUSED GATE IN THE TOOL, NOT IN THE SHELL.**

    ### b354 sealed against a refusal because the seal was chained to a filter's exit code. ### b443 sealed
    ### against a refusal because PowerShell's semicolon runs the next command whatever the exit code.
    ### A cure that lives in the caller is only as good as the caller's shell. ### **So the seal reads the
    ### lock gate's own record for the face it is about to seal**, `<stem>_lockgate.json` beside the face,
    ### where `<stem>` is the file name before `_registration`, and returns `(ok, reasons)`.
    ### It refuses when the record is ABSENT, names a DIFFERENT FACE, says the lock is NOT PERMITTED, or
    ### carries a `face_sha` that is not this body's digest -- a gate run against an earlier face.
    ### ### **An absent record is a refusal, not a pass: an absent claim is not a true one.**
    """
    import json
    base = os.path.basename(path)
    stem = base.split('_registration')[0] if '_registration' in base else os.path.splitext(base)[0]
    rec_path = os.path.join(os.path.dirname(os.path.abspath(path)), '%s_lockgate.json' % stem)
    if not os.path.exists(rec_path):
        return False, ['NO GATE RECORD -- %s is absent; the lock gate was not run for this face'
                       % os.path.basename(rec_path)]
    try:
        rec = json.loads(io.open(rec_path, encoding='utf-8').read())
    except Exception as e:                                         # noqa: BLE001
        return False, ['GATE RECORD UNREADABLE -- %s: %s' % (os.path.basename(rec_path), str(e)[:80])]
    reasons = []
    if rec.get('face') != base:
        reasons.append('GATE RECORD NAMES A DIFFERENT FACE -- %r, not %r' % (rec.get('face'), base))
    if rec.get('face_sha') != digest(body):
        reasons.append('GATE RECORD IS STALE -- it read face sha256 %s, this body is %s'
                       % (str(rec.get('face_sha'))[:16], digest(body)[:16]))
    if rec.get('permits') is not True:
        failing = [g for g in (rec.get('gates') or []) if not g.get('passed')]
        reasons.append('THE LOCK GATE REFUSED -- %s of %s gates passing'
                       % (rec.get('gates_passing'), rec.get('gates_read')))
        for g in failing:
            reasons.append('    refusing arm : %s (%s) -- %s'
                           % (g.get('gate'), g.get('file'), g.get('why') or 'did not pass'))
        if not failing:
            reasons.append('    refusing arm : not itemised in the record')
    return (not reasons), reasons


def cmd_seal(path):
    text = io.open(path, encoding='utf-8').read()
    body, existing = split_body(text)
    if existing is not None:
        print('  ### REFUSED -- already sealed. ### Use --verify.')
        print('  banked : %s' % existing)
        return 2
    h = digest(body)
    block = (BAR + '\n' + MARK + '\n' + PREFIX + h + '\n'
             + '### bytes sealed : %d\n' % len(body.encode('utf-8'))
             + CLOCK + stamp() + '   ### NOT COVERED BY THE HASH ABOVE; it records when this block was written.\n'
             + '### ### **RECOMPUTE WITH `python tools/reg_seal.py --verify ' + os.path.basename(path)
             + '`.**\n' + BAR + '\n')
    io.open(path, 'a', encoding='utf-8', newline='\n').write(block)
    print('  file          : %s' % path)
    print('  bytes sealed  : %d' % len(body.encode('utf-8')))
    print('  sha256 banked : %s' % h)
    print('  ### **SEALED. ### The hash covers every byte above the seal block.**')
    return 0


def cmd_lock(path):
    """### WRITE THE LOCK BLOCK (b358, ruling R3). ### Same digest, same fixed point, new wording.
    ### ### **IT REFUSES A FILE THAT ALREADY CARRIES EITHER MARK**, so a locked registration cannot be
    ### sealed on top and a sealed one cannot be locked on top."""
    text = io.open(path, encoding='utf-8').read()
    body, existing = split_body(text)
    if existing is not None:
        print('  ### REFUSED -- already locked or sealed. ### Use --verify.')
        print('  banked : %s' % existing)
        return 2
    ok, reasons = gate_record_check(path, body)
    if not ok:
        print('  ### ### **REFUSED -- THE SEAL WILL NOT LOCK A FACE ITS GATE DID NOT PERMIT** (`R56`).')
        for r_ in reasons:
            print('  %s' % r_)
        print('  ### Nothing was written.')
        return 3
    h = digest(body)
    block = (BAR + '\n' + LOCKMARK + '\n' + PREFIX + h + '\n'
             + '### bytes locked : %d\n' % len(body.encode('utf-8'))
             + '### locked at (UTC) : ' + stamp()
             + '   ### NOT COVERED BY THE HASH ABOVE; it records when this block was written.\n'
             + '### ### **RECOMPUTE WITH `python tools/reg_seal.py --verify ' + os.path.basename(path)
             + '`.**\n' + BAR + '\n')
    io.open(path, 'a', encoding='utf-8', newline='\n').write(block)
    print('  file          : %s' % path)
    print('  bytes locked  : %d' % len(body.encode('utf-8')))
    print('  sha256 banked : %s' % h)
    print('  ### **LOCKED. ### The hash covers every byte above the lock block.**')
    return 0


def selftest(verbose=True):
    """### BOTH MARKS, BOTH POLARITIES, ON TEMPORARY FILES. ### **THE ARM THAT MATTERS IS THE THIRD:**
    ### a body carrying the OLD mark must still split and verify, or b358's change broke fifty banked
    ### registrations."""
    import tempfile
    def say(s):
        if verbose:
            print(s)
    ok = True
    body = 'a registration body\n### with two lines\n'
    import json

    def gate(pth, **kw):
        rec_ = dict(face=os.path.basename(pth), face_sha=digest(body), permits=True,
                    gates_read=8, gates_passing=8, gates=[])
        rec_.update(kw)
        io.open(os.path.join(os.path.dirname(pth), 'r_lockgate.json'), 'w', encoding='utf-8').write(
            json.dumps(rec_))

    for label, writer, mark in (('--lock', cmd_lock, LOCKMARK), ('--seal', cmd_seal, MARK)):
        p = os.path.join(tempfile.mkdtemp(prefix='regseal_'), 'r.txt')
        io.open(p, 'w', encoding='utf-8', newline='\n').write(body)
        gate(p)
        import contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            rc = writer(p)
            rc2 = cmd_verify(p)
            rc3 = writer(p)          # ### must REFUSE a second write
        txt = io.open(p, encoding='utf-8').read()
        g = (rc == 0 and rc2 == 0 and rc3 == 2 and mark in txt
             and split_body(txt)[1] == digest(body))
        ok = ok and g
        say('    %-8s writes, verifies, refuses a second write : %s' % (label, g))
        # ### THE NEGATIVE POLARITY: a changed body must FAIL.
        io.open(p, 'w', encoding='utf-8', newline='\n').write(txt.replace('two lines', 'three lines'))
        with contextlib.redirect_stdout(io.StringIO()):
            rc4 = cmd_verify(p)
        ok = ok and (rc4 == 1)
        say('    %-8s a changed body FAILS verification            : %s' % (label, rc4 == 1))
    # ### **`(R56)` FIXTURES, BOTH POLARITIES.** ### Four ways the gate record must REFUSE, each checked to
    # ### write NOTHING and to name its reason; one clean record that must PERMIT.
    import contextlib
    cases = [
        ('absent record', None, 'NO GATE RECORD'),
        ('the gate refused', dict(permits=False, gates_passing=7,
                                  gates=[dict(gate='the banned-term scan on the face',
                                              file='r_reg_termscan.txt', passed=False,
                                              why='the record does not carry the gate`s own pass phrase')]),
         'refusing arm : the banned-term scan on the face'),
        ('a different face', dict(face='other_registration.txt'), 'NAMES A DIFFERENT FACE'),
        ('a stale digest', dict(face_sha='0' * 64), 'IS STALE'),
    ]
    for label, kw, needle in cases:
        p = os.path.join(tempfile.mkdtemp(prefix='regseal56_'), 'r.txt')
        io.open(p, 'w', encoding='utf-8', newline='\n').write(body)
        if kw is not None:
            gate(p, **kw)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = cmd_lock(p)
        unwritten = io.open(p, encoding='utf-8').read() == body
        g = (rc == 3 and unwritten and needle in buf.getvalue())
        ok = ok and g
        say('    (R56) --lock REFUSES on %-18s, writes nothing, names why : %s' % (label, g))
    p = os.path.join(tempfile.mkdtemp(prefix='regseal56_'), 'r.txt')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(body)
    gate(p)
    with contextlib.redirect_stdout(io.StringIO()):
        rc = cmd_lock(p)
    g = (rc == 0 and LOCKMARK in io.open(p, encoding='utf-8').read())
    ok = ok and g
    say('    (R56) --lock PERMITS a clean, current, matching gate record       : %s' % g)
    say('    ### the seal mark and the lock mark are different strings : %s' % (MARK != LOCKMARK))
    ok = ok and (MARK != LOCKMARK)
    return ok


def cmd_verify(path):
    text = io.open(path, encoding='utf-8').read()
    body, banked = split_body(text)
    if banked is None:
        print('  ### NO SEAL FOUND in %s.' % path)
        print('  ### **AN UNSEALED REGISTRATION IS NOT A FAILURE OF THIS TOOL -- IT IS THE STATE')
        print('  ### b262 WAS IN, AND IT IS EXACTLY WHAT `W-ORD-REG-HASH` EXISTS TO END.**')
        return 1
    now = digest(body)
    ok = (now == banked)
    print('  file          : %s' % path)
    print('  bytes sealed  : %d' % len(body.encode('utf-8')))
    print('  banked        : %s' % banked)
    print('  recomputed    : %s' % now)
    print('  ### ### **%s**' % ('SEAL INTACT -- the body is byte-for-byte what was sealed.' if ok
                                else 'SEAL BROKEN -- THE BODY HAS CHANGED SINCE SEALING.'))
    return 0 if ok else 1


def cmd_reseal(path):
    """### RE-SEAL AFTER A LAWFUL EDIT. ### **IT PRINTS BOTH HASHES AND WRITES THE SUPERSEDED ONE
    ### INTO THE NEW BLOCK**, so a re-seal is a VISIBLE event and not a silent one.
    ### ### **A TOOL THAT COULD RE-SEAL WITHOUT LEAVING A TRACE WOULD UNDO ITS OWN POINT.**"""
    text = io.open(path, encoding='utf-8').read()
    body, old = split_body(text)
    if old is None:
        print('  ### NO SEAL TO REPLACE. ### Use --seal.')
        return 2
    h = digest(body)
    block = (BAR + '\n' + MARK + '\n' + PREFIX + h + '\n'
             + '### bytes sealed : %d\n' % len(body.encode('utf-8'))
             + CLOCK + stamp() + '   ### NOT COVERED BY THE HASH ABOVE; it records when this block was written.\n'
             + '### ### **RE-SEALED. ### SUPERSEDED HASH : %s**\n' % old
             + '### The prior seal was broken by a lawful edit; the act that made it says which.\n'
             + '### ### **RECOMPUTE WITH `python tools/reg_seal.py --verify %s`.**\n'
             % os.path.basename(path) + BAR + '\n')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(body + block)
    print('  file          : %s' % path)
    print('  superseded    : %s' % old)
    print('  sha256 banked : %s' % h)
    print('  ### **RE-SEALED, AND THE SUPERSEDED HASH IS WRITTEN INTO THE BLOCK.**')
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] != '--selftest' and len(argv) < 2:
        print(__doc__)
        return 2
    if argv[0] == '--selftest':
        ok = selftest(True)
        print('  ### %s' % ('PASS' if ok else '### FAIL ###'))
        return 0 if ok else 1
    if argv[0] == '--lock':
        return cmd_lock(argv[1])
    if argv[0] == '--seal':
        return cmd_seal(argv[1])
    if argv[0] == '--verify':
        return cmd_verify(argv[1])
    if argv[0] == '--reseal':
        return cmd_reseal(argv[1])
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
