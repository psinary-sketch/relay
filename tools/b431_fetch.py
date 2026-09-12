# -*- coding: utf-8 -*-
"""b431_fetch.py -- THE PAPER, FETCHED AND PINNED BY DIGEST. ### **THE ONLY FETCHING TOOL OF b431.**

### ### **WHY THIS FILE EXISTS AT ALL.** ### The paper was first fetched from an ad-hoc script typed
### at the shell. ### It resolved, it pinned, and the digest it wrote is correct -- and ### **NO
### ### COMMITTED TOOL PRODUCED IT**, so nothing in the bank could reproduce the number or fail
### trying. ### That is the same species as b347's rule (every reported figure from a committed tool
### with fixtures) and it was caught by this act's own suite noticing that no tool of b431 contains
### a fetch at all. ### **A FIGURE WITH NO TOOL BEHIND IT IS A FIGURE NOBODY CAN CHECK.**

### ### **IT IS IDEMPOTENT AND IT IS A VERIFIER SECOND TIME ROUND.** ### If the paper is already on
### disk it is re-hashed and compared with the banked pin; ### **A MISMATCH IS A HARD FAILURE AND
### ### NOT A RE-PIN**, because silently adopting a new digest is how a moved target passes for a
### fixed one.
"""
import hashlib
import io
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
EXT = os.path.join('D:', os.sep, '_b431_external')
PDF = os.path.join(EXT, 'long_gaps.pdf')
TXT = os.path.join(EXT, 'long_gaps.txt')
PIN = os.path.join(D, 'b431_paper_pin.txt')
NL = chr(10)

# ### **THE ADDRESS IS THE AUTHOR'S, SPELLED ONCE, AND NOTHING IS CONSTRUCTED FROM IT.**
URL = ('https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/long_gaps.pdf')
UA = {'User-Agent': 'Mozilla/5.0 (relay b431 research seat)'}


def banked_digest():
    m = re.search(r'sha256 : ([0-9a-f]{64})', io.open(PIN, encoding='utf-8').read()) \
        if os.path.exists(PIN) else None
    return m.group(1) if m else None


def main(argv):
    print('=' * 100)
    print('b431_fetch.py -- THE PAPER, FETCHED AND PINNED. ### THE ONLY FETCHING TOOL OF THIS ACT.')
    print('=' * 100)
    prior = banked_digest()
    print('  address            : %s' % URL)
    print('  banked digest      : %s' % (prior or '(none yet)'))

    if os.path.exists(PDF):
        data = open(PDF, 'rb').read()
        h = hashlib.sha256(data).hexdigest()
        print('  on disk            : %d bytes, sha256 %s' % (len(data), h))
        if prior and h != prior:
            # ### **A MISMATCH IS A HARD FAILURE.** ### Re-pinning here would make a moved target
            # ### look like a fixed one, which is the whole reason a pin exists.
            print('  ### HARD FAILURE -- THE BYTES ON DISK DO NOT MATCH THE BANKED PIN.')
            print('  ### The banked digest is NOT overwritten. The author rules.')
            return 2
        if prior:
            print('  ### **RE-VERIFIED AGAINST THE BANKED PIN : MATCH.** ### Nothing refetched.')
            return 0
    else:
        data = None

    if data is None:
        try:
            req = urllib.request.Request(URL, headers=UA)
            with urllib.request.urlopen(req, timeout=120) as r:
                data, status = r.read(), r.status
        except Exception as exc:
            # ### READING (7): AN UNREACHABLE ADDRESS IS PRINTED WITH THE HOST'S RESPONSE AND THE
            # ### ACT STOPS THERE RATHER THAN SUBSTITUTING.
            print('  ### UNREACHABLE : %s' % exc)
            print('  ### **NO GRADE IS CONFERRED AGAINST A CLAIM THIS ACT COULD NOT READ.**')
            return 2
        os.makedirs(EXT, exist_ok=True)
        open(PDF + '.tmp', 'wb').write(data)
        os.replace(PDF + '.tmp', PDF)
        print('  fetched            : status %s, %d bytes' % (status, len(data)))

    h = hashlib.sha256(data).hexdigest()
    if prior and h != prior:
        print('  ### HARD FAILURE -- FETCHED BYTES DIFFER FROM THE BANKED PIN. Not overwritten.')
        return 2
    txt = ('b431 -- THE PAPER, FETCHED AFTER THE LOCK AND PINNED BY DIGEST.' + NL +
           '  url    : %s' % URL + NL +
           '  status : 200' + NL +
           '  bytes  : %d' % len(data) + NL +
           '  sha256 : %s' % h + NL)
    open(PIN + '.tmp', 'wb').write(txt.encode('utf-8'))
    os.replace(PIN + '.tmp', PIN)
    print('  sha256             : %s' % h)

    # ### THE TEXT LAYER, EXTRACTED ONCE SO EVERY LATER READ IS OF THE SAME BYTES.
    try:
        import pypdf
        r = pypdf.PdfReader(PDF)
        t = NL.join((p.extract_text() or '') for p in r.pages)
        io.open(TXT, 'w', encoding='utf-8', newline=NL).write(t)
        print('  text layer         : %d pages, %d chars' % (len(r.pages), len(t)))
        print('  ### **THE EXTRACTION IS LOSSY AND THE ACT SAYS SO**: ligatures survive as single')
        print('  ### code points and mathematics arrives as running text. ### Every clause this act')
        print('  ### quotes was read back against this file, and a clause that could not be found')
        print('  ### in it is reported as NOT FOUND rather than reconstructed.')
    except Exception as exc:
        print('  ### text layer NOT extracted : %s' % exc)
        return 2
    print('=' * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
