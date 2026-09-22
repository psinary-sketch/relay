# -*- coding: utf-8 -*-
"""b468_precondition.py -- THE GATE. ### **b468 RUNS ONLY WHEN THE (R75) ARTEFACTS ARE ON DISK.**

### The order's own words: *Runs only when the (R75) artefacts are on disk; prints ABSENT per
### artefact otherwise and stops.* ### So this file is the whole of b468 until they arrive, and it
### is written to be ### **A MEASUREMENT AND NOT A GLANCE** -- b466's shape, carried with both of
### its repairs: the WIDE and the NARROWED matcher yields are both printed, because a name matcher
### collects this corpus's own documents; and ### **EVERY `ABSENT` CARRIES A CONTROL** (b404), the
### same searcher run over a file known to be on disk, which must FIND it.
### ### **(R75) NAMES SEVEN ARTEFACTS, NOT FIVE.** ### b466 searched for five; the ruling adds
### arXiv 2608.13637 and ### **CORRECTS THE REPOSITORY'S NAME**: it is `anthropics/formal-math`,
### the `zeta23` project inside it -- ### **NOT `anthropics/zeta-23-lean`**, which is what the
### record has carried since 2026-08-20 and what b466 searched for and did not find.
"""
import hashlib
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def sha256(p):
    try:
        return hashlib.sha256(open(p, 'rb').read()).hexdigest()
    except Exception:
        return None


TREES = [D, os.path.join(ROOT, 'reports'), PP, os.path.join('D:', os.sep)]
# ### ### **BARE `anthropic` AND BARE `claude` CANNOT DISCRIMINATE, AND THE FIRST FORM PROVED IT.**
# ### It marked `HERITAGE/A_METHODOLOGY_FOR_DETERMINED_SYSTEMS_v1_0.md` PRESENT -- this corpus's own
# ### methodology document -- because line 364 carries an ### **AI-DISCLOSURE SENTENCE**: *"Editorial
# ### workflow assisted by Claude (Anthropic)."* ### **A DISCLOSURE IS NOT AN ARTEFACT**, and under
# ### (R75) the hazard is structural rather than incidental: the order asks for `the Claude paper`
# ### and `the methodology note`, and this corpus's own documents name Claude and carry a methodology.
# ### ### **BOTH YIELDS STAY ON THE RECORD.** ### The narrowed form requires a mark that belongs to
# ### THIS RESULT AND NOTHING ELSE -- the repository names, the arXiv id, the authors, the constants.
OWNER_WIDE = re.compile(r'anthropic|claude|zeta.?23|formal.?math|2608\.?13637|alpoge|furman'
                        r'|67\.2\s*%|0\.6725|41\.6\s*%', re.I)
OWNER = re.compile(r'zeta.?23|formal.?math|2608\.?13637|alpoge|furman|0\.6725'
                   r'|67\.2\s*%|41\.6\s*%', re.I)
DISCLOSURE = re.compile(r'assisted by Claude|\(Anthropic\)|AI disclosure', re.I)

# ### ### **THE SEVEN (R75) NAMES, EACH WITH THE PATTERNS THAT WOULD FIND IT.**
ARTEFACTS = [
    ('the Claude paper', [r'claude.*(paper|riemann|zeta|proportion)', r'riemann.*zeta.*paper',
                          r'proportion.*\.(pdf|txt|md)$', r'zeta.?23.*\.pdf$']),
    ('the Anthropic informal note', [r'informal.?note', r'anthropic.*note']),
    ('the methodology note', [r'methodolog']),
    ('the transcripts', [r'transcript']),
    ('arXiv 2608.13637 (Alpoge-Furman), latest version', [r'2608\.?13637', r'alpoge', r'furman']),
    ('a clone of anthropics/formal-math at its HEAD SHA', [r'formal.?math']),
    ('the zeta23 project inside it', [r'zeta.?23']),
]


def walk(tree, depth=4):
    """### A bounded walk. ### **`D:\\` IS WALKED SHALLOWLY** so a clone at top level is seen without
    ### descending every tree on the volume; the depth is printed so the search is reproducible."""
    base = tree.rstrip(os.sep).count(os.sep)
    for dp, dns, fns in os.walk(tree):
        if os.sep + '.git' in dp:
            dns[:] = []
            continue
        if dp.count(os.sep) - base >= depth:
            dns[:] = []
        yield dp, dns, fns


def by_name(pats, depth_for_root=3):
    hits = []
    for tree in TREES:
        d = depth_for_root if tree == os.path.join('D:', os.sep) else 8
        for dp, dns, fns in walk(tree, d):
            for fn in fns + dns:
                low = fn.lower()
                if any(re.search(p, low) for p in pats):
                    hits.append(os.path.join(dp, fn))
    return sorted(set(hits))


def owned(path):
    """### **RETURNS `(narrow, wide, why)`** so the two yields can be printed side by side."""
    base = os.path.basename(path)
    if OWNER.search(base):
        return True, True, 'the name carries a mark unique to this result'
    if os.path.isdir(path):
        return False, bool(OWNER_WIDE.search(base)), 'a directory, matched on its name only'
    try:
        if os.path.getsize(path) > 4000000:
            return False, False, 'too large to read'
    except Exception:
        return False, False, 'unreadable'
    txt = read(path)[:400000]
    wide = bool(OWNER_WIDE.search(txt)) or bool(OWNER_WIDE.search(base))
    narrow = bool(OWNER.search(txt))
    why = ''
    if wide and not narrow:
        why = ('### **AN AI-DISCLOSURE LINE, NOT AN ARTEFACT**' if DISCLOSURE.search(txt)
               else 'matched only on a non-discriminating word')
    return narrow, wide, why


def main():
    rec('=' * 104)
    rec('b468 -- THE PRECONDITION. ### **(R75)\x27s SEVEN ARTEFACTS, SEARCHED FOR RATHER THAN ASSUMED.**')
    rec('=' * 104)
    rec('  trees : relay/data ; relay/reports ; PLACE-papers ; D:\\ (depth 3, directories included)')
    rec('  ### ### **DIRECTORIES ARE MATCHED AS WELL AS FILES**, because two of the seven are a')
    rec('  ### CLONE and a PROJECT INSIDE ONE -- and b466\x27s searcher looked only at file names,')
    rec('  ### which is a searcher that cannot find a repository even when one is there.')
    out = []
    for label, pats in ARTEFACTS:
        wide = by_name(pats)
        judged = [(h,) + owned(h) for h in wide]
        narrowed = [h for h, n, w, why in judged if n]
        whys = {h: why for h, n, w, why in judged}
        state = 'PRESENT' if narrowed else 'ABSENT'
        rec('')
        rec('  %-52s ### **%s**' % (label, state))
        rec('    by name, WIDE     : %d' % len(wide))
        for h in wide[:5]:
            rec('      %-58s %s' % (os.path.relpath(h, 'D:' + os.sep)[:58],
                                    'OWNED' if h in narrowed
                                    else ('### REJECTED -- ' + (whys.get(h) or 'not this result'))))
        rec('    by name, NARROWED : %d' % len(narrowed))
        for h in narrowed[:5]:
            rec('      %-60s sha256 %s' % (os.path.relpath(h, 'D:' + os.sep)[:60],
                                           (sha256(h) or 'DIRECTORY')[:16]))
        out.append(dict(artefact=label, state=state, wide=len(wide), narrowed=len(narrowed)))

    ctl = by_name([r'^b358_source_lagarias'])
    rec('')
    rec('  ### ### **THE CONTROL** -- the same searcher over a file known to be on disk:')
    rec('    b358_source_lagarias0404394.txt : %s   ### **CONTROL %s**'
        % ('FOUND' if ctl else 'NOT FOUND', 'FIRES' if ctl else 'FAILS -- THE SEARCHER IS BROKEN'))
    absent = [o['artefact'] for o in out if o['state'] == 'ABSENT']
    rec('')
    rec('  ### ### **PRESENT : %d. ### ABSENT : %d.**' % (len(out) - len(absent), len(absent)))
    ok = not absent and bool(ctl)
    rec('  ### ### **VERDICT : %s**'
        % ('THE PRECONDITION IS MET -- b468 RUNS' if ok
           else 'THE PRECONDITION IS NOT MET -- b468 PRINTS ABSENT PER ARTEFACT AND STOPS'))
    rec('=' * 104)
    io.open(os.path.join(D, 'b468_precondition.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(dict(artefacts=out, absent=absent, control_fires=bool(ctl), met=ok),
              io.open(os.path.join(D, 'b468_precondition.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
