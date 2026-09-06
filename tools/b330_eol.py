# -*- coding: utf-8 -*-
"""b330_eol.py -- THE KERNEL REPOSITORY'S LINE-ENDING HYGIENE, WRITTEN AND VERIFIED.

### ### **THE DEFECT:** ### `core.autocrlf=true` checks the kernel's files out with CRLF while every blob
### is LF, so a working file differs from its blob on raw bytes on a clean tree (b309 D6, b310, b329's
### post-push `G-ORDER`), and every instrument that hashes or byte-compares a working file must carry a
### normalisation that is git's doing and not the act's. ### The papers repository fixed this on
### 2026-08-14 with `.gitattributes` (`* text=auto eol=lf`); the kernel repository never had one.

### ### **TWO PHASES, TWO RUN FILES.** ### `--before` writes the attributes file (mirroring the papers
### repository's, with the kernel's own incident in the comment) and counts the tracked files whose
### working copy is CRLF; the commit, push and re-checkout are git's, done by explicit command and
### recorded in the bank; `--after` counts again and requires the profile's working file to equal its
### blob at HEAD ON RAW BYTES after the kernel tool has regenerated it.
"""
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
ATTR = os.path.join(SIDE, '.gitattributes')
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TEXT = """# Disk bytes must equal blob bytes.
#
# core.autocrlf=true was checking every text file out with CRLF while every blob is LF,
# so a working file differed from its blob on raw bytes on a CLEAN tree: the profile
# AXIOM_PRINTS.txt failed a raw byte comparison at b309 (D6), the kernel tool had to
# normalise at b310, and b329's post-push gate fired on the registration's raw hash and
# on file times rewritten by the checkout. Every instrument that hashes or byte-compares
# a working file was carrying a normalisation that is git's doing and not the act's.
#
# eol=lf makes checkout match storage, as the papers repository's .gitattributes does
# (2026-08-14). Do not remove without re-verifying the profile against its blob raw.
* text=auto eol=lf
"""

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def git(*args):
    return subprocess.run(['git', '-C', SIDE] + list(args), capture_output=True).stdout.decode('utf-8', 'replace')


def eol_census():
    out = git('ls-files', '--eol')
    counts = {}
    for ln in out.splitlines():
        parts = ln.split()
        if len(parts) >= 3:
            key = (parts[0], parts[1])
            counts[key] = counts.get(key, 0) + 1
    crlf = sum(v for (i, w), v in counts.items() if w == 'w/crlf')
    lf = sum(v for (i, w), v in counts.items() if w == 'w/lf')
    return counts, crlf, lf


def profile_raw_vs_blob():
    raw = io.open(PROFILE, 'rb').read()
    blob = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:AXIOM_PRINTS.txt'], capture_output=True).stdout
    return raw == blob, len(raw), len(blob), raw.count(b'\r\n')


def main(argv):
    phase = 'after' if '--after' in argv else 'before'
    rec('=' * 100)
    rec('b330 -- THE KERNEL REPOSITORY\'S LINE-ENDING HYGIENE. ### PHASE: %s.' % phase.upper())
    rec('=' * 100)
    pp = io.open(os.path.join(PP, '.gitattributes'), encoding='utf-8').read()
    rec('  the papers repository\'s rule, read from its file : %r' % [ln for ln in pp.splitlines() if ln and not ln.startswith('#')])
    rec('  core.autocrlf in the kernel repository            : %s' % git('config', '--get', 'core.autocrlf').strip())
    counts, crlf, lf = eol_census()
    rec('  tracked files by (index, working) line endings   : %s' % {('%s %s' % k): v for k, v in sorted(counts.items())})
    rec('  working copies CRLF : %d ; LF : %d' % (crlf, lf))
    eq, nr, nb, ncr = profile_raw_vs_blob()
    rec('  AXIOM_PRINTS.txt raw bytes == blob at HEAD : %s  (working %d bytes, blob %d bytes, CRLF pairs in working %d)' % (eq, nr, nb, ncr))
    if phase == 'before':
        if os.path.exists(ATTR):
            rec('  .gitattributes already present -- NOT rewritten')
        else:
            open(ATTR, 'wb').write(TEXT.encode('utf-8'))
            back = io.open(ATTR, 'rb').read()
            rec('  .gitattributes WRITTEN : %d bytes ; rule line present : %s ; no BOM : %s ; LF endings : %s'
                % (len(back), b'* text=auto eol=lf' in back, not back.startswith(b'\xef\xbb\xbf'), b'\r\n' not in back))
        rec('  ### the commit, the push from a push-* branch and the re-checkout are git\'s, by explicit command;')
        rec('  ### then `--after` after the kernel tool has regenerated the profile.')
        rec('=' * 100)
        return 0
    ok = eq and crlf == 0 and os.path.exists(ATTR)
    rec('  ### **THE PROFILE\'S WORKING FILE EQUALS ITS BLOB ON RAW BYTES : %s ; NO TRACKED WORKING COPY IS CRLF : %s**' % (eq, crlf == 0))
    rec('  attributes file tracked at HEAD : %s' % ('.gitattributes' in git('ls-files', '.gitattributes')))
    rec('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    code = main(sys.argv[1:])
    name = 'b330_eol_after.txt' if '--after' in sys.argv[1:] else 'b330_eol_before.txt'
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
