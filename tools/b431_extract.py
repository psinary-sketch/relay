# -*- coding: utf-8 -*-
"""b431_extract.py -- THE SURVEY FOR b431: THE LongGapsBetweenPrimes GRADING AND THE TYPE-D QUESTION.
### **THE CORPUS AND THIS MACHINE ONLY. ### NOTHING IS FETCHED HERE AND NO FOREIGN REPOSITORY IS
### CLONED BY THIS TOOL.** ### The one network read this act has already made -- an `ls-remote` of
### the author's address at step zero -- is RECORDED here as a fact about step zero and is declared
### on the face, not hidden inside it.
### ### **THE CORPUS SIDE OF THE TYPE-D QUESTION IS UNFOLDED HERE, FROM SOURCE**, so that the
### comparison the order asks for is between two statements and never between two names.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
EFF = os.path.join('D:', os.sep, 'SIDE-effects')
MOD1 = os.path.join(EFF, 'SIDEEffects', 'Phase15', 'Module1.lean')
KEY = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
FERRY = os.path.join(D, 'b431_ferry.txt')
OUT = os.path.join(D, 'b431_extract.txt')
NL = chr(10)
L, MISS = [], []
READS = [0]


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


def read(p):
    READS[0] += 1
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception as exc:
        MISS.append('%s : %s' % (os.path.basename(p), exc))
        return ''


def fold(s):
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('**', '').replace('`', '')
                  .replace(chr(0x2019), "'").replace(chr(0x2014), '--')).strip()


def wrap(text, width=92, indent='        '):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(indent + line)
            line = w
        else:
            line = (line + ' ' + w).strip()
    if line:
        out.append(indent + line)
    return out


def decl(src, kind, name, span=14):
    """### A DECLARATION QUOTED AT ITS LINE, from the module's own source."""
    for i, ln in enumerate(src.splitlines(), 1):
        if re.match(r'^\s*(?:noncomputable\s+)?%s\s+%s\b' % (kind, re.escape(name)), ln):
            return i, NL.join(src.splitlines()[i - 1:i - 1 + span])
    return None, ''


def main(argv):
    rule('=')
    say('b431_extract.py -- THE SURVEY. ### THE GRADING\'S SUBJECTS, AND THE TYPE-D QUESTION\'S.')
    rule('=')
    say('  ### NOTHING IS FETCHED BY THIS TOOL. ### NO FOREIGN REPOSITORY IS CLONED HERE.')
    say()

    # ### =========================================================================================
    rule()
    say('  (1) THE ADDRESSES, AS THE AUTHOR SUPPLIED THEM -- QUOTED, NOT RESOLVED HERE.')
    rule()
    ft = read(FERRY)
    for pat, lbl in ((r'github\.com/openai/LongGapsBetweenPrimes', 'the Lean repository'),
                     (r'LongGapsBetweenPrimes\.lean', 'the file the theorem is named in'),
                     (r'cdn\.openai\.com/pdf/[0-9a-f-]+/' + NL + r'?long_gaps\.pdf',
                      'the paper')):
        m = re.search(pat, ft.replace(NL, ''))
        m2 = re.search(pat, ft)
        say('    %-34s : %s' % (lbl, (m2 or m).group(0).replace(NL, '') if (m2 or m)
                                else '### NOT FOUND IN THE PASTE ###'))
        if not (m or m2):
            MISS.append('address not found in the paste: %s' % lbl)
    say('    ### **AND ONE FACT ABOUT STEP ZERO, RECORDED RATHER THAN HIDDEN.** ### The repository')
    say('    ### address was resolved by `ls-remote` at step zero, BEFORE this act\'s face was')
    say('    ### locked, while the seat was establishing that leg 2 could run at all. ### **THAT')
    say('    ### IS A NETWORK READ BEFORE THE LOCK AND THE FACE DECLARES IT.** ### The pin it')
    say('    ### returned is recorded below; the components re-read it AFTER the lock and print')
    say('    ### both, so a difference would be visible rather than absorbed.')
    sz = os.path.join(D, 'b431_stepzero_lsremote.txt')
    say('    step-zero ls-remote record : %s'
        % ('PRESENT' if os.path.exists(sz) else '### TO BE WRITTEN BY STEP ZERO ###'))
    if os.path.exists(sz):
        for ln in read(sz).splitlines()[:3]:
            say('        %s' % ln.strip()[:92])
    say()

    # ### =========================================================================================
    rule()
    say('  (2) THE CORPUS SIDE OF THE TYPE-D QUESTION, UNFOLDED FROM SOURCE.')
    rule()
    src = read(MOD1)
    say('    SIDE-effects SIDEEffects/Phase15/Module1.lean : %s'
        % ('%d lines' % len(src.splitlines()) if src else '### ABSENT ###'))
    try:
        head = subprocess.run(['git', '-C', EFF, 'rev-parse', 'HEAD'],
                              capture_output=True, text=True).stdout.strip()
    except Exception as exc:
        head = '### %s' % exc
    say('    SIDE-effects HEAD                            : %s' % head)
    say()
    # ### **THE KEYSTONE NAMES THE LEMMA; THE LEMMA IS READ AT ITS OWN SOURCE.**
    for kind, nm in (('theorem', 'no_type_d_conspiracies'), ('theorem', 'crt_exhaustiveness'),
                     ('def', 'TypeD'), ('def', 'to_modular'), ('def', 'ofPeriodic'),
                     ('theorem', 'ofPeriodic_eval')):
        i, body = decl(src, kind, nm, 10)
        say('    %-24s %s' % (nm, ('line %d' % i) if i else '### NOT LOCATED ###'))
        for ln in (body.splitlines()[:8] if body else []):
            say('        %s' % ln.rstrip()[:92])
        if not i:
            MISS.append('declaration not located: %s' % nm)
        say()
    # ### THE STRUCTURES THE STATEMENT QUANTIFIES OVER.
    for nm in ('StructuralCoupling', 'ModularCoupling'):
        i, body = decl(src, 'structure', nm, 12)
        say('    structure %-18s %s' % (nm, ('line %d' % i) if i else '### NOT LOCATED ###'))
        for ln in (body.splitlines()[:10] if body else []):
            say('        %s' % ln.rstrip()[:92])
        say()

    # ### =========================================================================================
    rule()
    say('  (3) WHAT THE KEYSTONE\'S PROSE SAYS THE LEMMA IS.')
    rule()
    kt = read(KEY)
    say('    phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md : %s'
        % ('%d lines' % len(kt.splitlines()) if kt else '### ABSENT ###'))
    for i, ln in enumerate(kt.splitlines(), 1):
        if re.search(r'no_type_d_conspiracies|CRT exhaustiveness|Chinese Remainder', ln):
            say('      line %d:' % i)
            for w in wrap(fold(ln)[:700], 88, '          '):
                say(w)
    say()

    # ### =========================================================================================
    rule()
    say('  (4) THE PROTOCOL THIS ACT IS HELD TO -- b429\'S, AS b430 APPLIED IT.')
    rule()
    b430 = read(os.path.join(D, 'b430_components.txt'))
    for needle in ('THE SEAL THIS RUN READ OFF THE LOCKED FACE',
                   'the pin the build was made at', 'DEFINITION-ENCODED',
                   'VERDICT : SYMMETRIC'):
        hit = [ln.strip() for ln in b430.splitlines() if needle in ln]
        say('    %-44s : %s' % (needle[:44], hit[0][:60] if hit else '### ABSENT ###'))
    say('    ### **b430 SETTLED THAT THE PROTOCOL IS SYMMETRIC ON ONE TRIAL.** ### This act runs')
    say('    ### it on a second stranger, so the same four clauses must hold here too.')
    say()
    say('    ### AND THE BUILD PRACTICALITIES b429 LEARNED ON THIS MACHINE, CARRIED:')
    say('      ### **`lake` HAS NO `-j` FLAG IN THIS VERSION.** ### Default parallelism OOMs at')
    say('      ### ~12 lean processes; the cure is to build failing modules ONE AT A TIME.')
    say('      ### A missing `*.olean.private` is fixed by re-running `lake exe cache get`.')
    say('      ### `ELAN_HOME` must point at `D:` -- `C:` has under 2 GiB free.')
    say('      ### **KILLING `lake` MID-CLONE CORRUPTS `.lake/packages/mathlib`**; the cure is')
    say('      ### `rm -rf` and a fresh clone, never a repair in place.')
    say()

    rule('=')
    say('  ### READS ATTEMPTED : %d' % READS[0])
    say('  ### MISSES          : %d' % len(MISS))
    for m_ in MISS:
        say('      %s' % m_)
    say('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rule('=')
    txt = NL.join(L) + NL
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(txt)
    os.replace(OUT + '.tmp', OUT)
    print(txt)
    print('  written: %s' % os.path.basename(OUT))
    return 0 if os.path.exists(OUT) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
