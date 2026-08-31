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

Usage:
    python reg_seal.py --seal <file>      write the seal block (refuses if already sealed)
    python reg_seal.py --verify <file>    recompute and compare; exit 1 on mismatch
"""
import hashlib
import io
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BAR = '=' * 100
MARK = '### THE REGISTRATION SEAL (emitted by tools/reg_seal.py; do not retype).'
PREFIX = '### sha256 of every byte ABOVE this block : '


def split_body(text):
    """### RETURN (body, seal_hex_or_None). ### The body is everything above the seal bar."""
    i = text.find(BAR + '\n' + MARK)
    if i < 0:
        return text, None
    body = text[:i]
    tail = text[i:]
    for line in tail.split('\n'):
        if line.startswith(PREFIX):
            return body, line[len(PREFIX):].strip()
    return body, ''


def digest(body):
    return hashlib.sha256(body.encode('utf-8')).hexdigest()


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
             + '### ### **RECOMPUTE WITH `python tools/reg_seal.py --verify ' + os.path.basename(path)
             + '`.**\n' + BAR + '\n')
    io.open(path, 'a', encoding='utf-8', newline='\n').write(block)
    print('  file          : %s' % path)
    print('  bytes sealed  : %d' % len(body.encode('utf-8')))
    print('  sha256 banked : %s' % h)
    print('  ### **SEALED. ### The hash covers every byte above the seal block.**')
    return 0


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
    if len(argv) < 2:
        print(__doc__)
        return 2
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
