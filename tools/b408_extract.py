# -*- coding: utf-8 -*-
"""b408_extract.py -- EXTRACT-TO-DISK. ### EVERY READ AND EVERY COUNT THIS ACT MAKES.

### ### (A) The span, by the tool, read-only and then banked under this act's own stem.
### ### (B) The other two mechanism classes, in the classes document's own words, and the barrier
###     keystone's toolkit `T` -- WHICH OF THE THREE SOURCES IT NAMES AND WHICH IT DOES NOT.
### ### (C) The corpus swept for either class examined AS A CHANNEL, with the search printed.
### ### (D) The E0 gate's eight constituents, located BY THE TABLE'S OWN HEADING.
### ### (E) The four dresses, quoted from their own banks.
### ### (F) Row `U1`'s cost and its yield, counted from the banks.
### ### (G) The routed prices, and the suites' arms across four acts.
###
### ### **EVERY WRITE ENCODES BEFORE IT OPENS**, and ### **NO RUN RECORD IS READ FROM A DIRECTORY
### ### LISTING** -- `run_clock.latest` is used where one is read at all.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b408_extract.txt')
SCRATCH = os.path.join(D, '_b408')
PP = r'D:\MY-DOwnloads\PLACE-papers'
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
MC = os.path.join(PP, 'day1', 'Seven_Mechanism_Classes.md')
FIND = os.path.join(PP, 'FINDINGS.md')

L = []
MISS = []


def say(s=''):
    L.append(s)
    print(s)


def write_text(path, text):
    io.open(path, 'wb').write(text.encode('utf-8'))


def pull(path, hint, label, span=False, width=470):
    try:
        if span:
            ln0, run = AF.find_span(path, hint)
            txt = '\n'.join(run)
        else:
            ln0, txt = AF.find(path, hint)
    except AF.AnchorError as e:
        MISS.append(label)
        say('  ### ANCHOR MISS -- %s' % label)
        say('      %s' % str(e).splitlines()[0][:180])
        return None
    say('  ### %s   [%s, line %d]' % (label, os.path.basename(path), ln0))
    for ln in txt.splitlines():
        for k in range(0, max(len(ln), 1), width):
            say('      | %s' % ln[k:k + width])
    return txt


def main():
    if not os.path.isdir(SCRATCH):
        os.makedirs(SCRATCH)
    say('=' * 100)
    say('b408_extract.py -- THE SURVEY, EXTRACTED TO DISK BEFORE THE FACE IS WRITTEN.')
    say('=' * 100)
    if not AF.self_test(verbose=False):
        say('  ### REFUSING TO QUOTE THROUGH A TOOL THAT FAILS ITS OWN FIXTURES.')
        return 2
    say('  anchor tool self-test : PASS')

    # ------------------------------------------------------------------ (A) THE SPAN
    say()
    say('-' * 100)
    say('### (A) THE SPAN, BY THE TOOL. ### **THE NAVIGATOR`S COUNT IS NOT CONSULTED HERE.**')
    say('-' * 100)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'b363_span.py')],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    span_out = r.stdout or ''
    write_text(os.path.join(SCRATCH, 'span_readonly.txt'), span_out)
    for ln in span_out.split('\n'):
        if re.search(r'THE CURRENT SPAN|last fold covers|FILED BY|next span STARTS|runs through|'
                     r'DECLARED THRESHOLD|FOLDS RUN|reached the shortest', ln):
            say('      %s' % ln.rstrip()[:170])
    m = re.search(r'THE CURRENT SPAN : (\d+) ACT', span_out)
    span = int(m.group(1)) if m else None
    say('  ### ### **THE TOOL`S COUNT : %s ACTS. ### `(R1)`S THRESHOLD : 9.**' % span)
    say('  ### ### **THE FOLD IS %s.**'
        % ('DUE' if (span or 0) >= 9 else 'NOT DUE -- %d SHORT' % (9 - (span or 0))))

    # ------------------------------------------------------------------ (B) THE CLASSES
    say()
    say('-' * 100)
    say('### (B) THE OTHER TWO CHANNELS, IN THE CLASSES DOCUMENT`S OWN WORDS.')
    say('-' * 100)
    pull(MC, '**Class C\u2083 (archimedean).**', 'C3 -- THE ARCHIMEDEAN CLASS')
    pull(MC, '**Class C\u2084 (global coherence).**', 'C4 -- THE GLOBAL CLASS')
    pull(MC, '**Class C\u2085 (multiplicative).**', 'C5 -- THE ONE b407 ALREADY MET')
    say()
    pull(MC, 'every derivation chain from \u03b8 to a zero-location constraint factors through',
         'AND THE EXHAUSTIVENESS: THREE, AND NO FOURTH')
    pull(MC, 'Independence: C\u2083 (archimedean) is not derivable from',
         'AND THEIR INDEPENDENCE, IN THE DOCUMENT`S OWN PROOF')
    say()
    say('  ### **AND WHAT THE BARRIER KEYSTONE`S OWN TOOLKIT `T` CONTAINS:**')
    t37 = pull(IB, '**Theorem 3.7 (Euler-product barrier against T).**',
               'THE TIER-1 TOOLKIT, LISTED')
    pull(IB, 'The one structural feature T deliberately omits',
         'AND THE ONE IT EXCLUDES BY CONSTRUCTION, WITH ITS REASON')
    if t37:
        say('  ### ### **WHICH OF THE THREE SOURCES `T` NAMES, COUNTED OFF ITS OWN LIST:**')
        say('      `C3` archimedean -- the functional equation is `T1` : %s'
            % ('YES' if 'T1 functional equation' in t37 else 'NO'))
        say('      `C5` multiplicative -- the Euler product : EXCLUDED BY CONSTRUCTION')
        c4_terms = ['PSL', 'modular symmetry', '(ST)', 'global coherence']
        say('      `C4` global -- any of %s : %s'
            % (c4_terms, 'YES' if any(x in t37 for x in c4_terms) else 'NO -- NOT NAMED AT ALL'))

    # ------------------------------------------------------------------ (C) THE SWEEP
    say()
    say('-' * 100)
    say('### (C) THE CORPUS SWEPT FOR EITHER CLASS EXAMINED **AS A CHANNEL**.')
    say('-' * 100)
    say('  ### **THE PREDICATE, FIXED BEFORE THE SWEEP:** ### a line naming the class AND one of')
    say('  ### the channel words the corollary uses -- `channel`, `kappa`, `bright`, `dark`,')
    say('  ### `interface`, `transmission`. ### **NAMING A CLASS IS NOT EXAMINING IT AS A CHANNEL.**')
    CLS = {'C3': re.compile(r'C\u2083|\bC3\b|archimedean class'),
           'C4': re.compile(r'C\u2084|\bC4\b|PSL\u2082|modular symmetry')}
    CHAN = re.compile(r'channel|kappa|\u03ba|bright|P-dark|dark interface|transmission coefficient',
                      re.I)
    bs = chr(92)
    scopes = []
    for root, dirs, files in os.walk(PP):
        dirs[:] = [d for d in dirs if d not in ('.git', 'archive', 'outputs')]
        for f in sorted(files):
            if f.endswith('.md'):
                p = os.path.join(root, f)
                scopes.append(('papers/' + os.path.relpath(p, PP).replace(bs, '/'), p))
    for f in sorted(os.listdir(D)):
        if f.endswith('.txt') and not f.startswith('b408'):
            scopes.append(('relay/data/' + f, os.path.join(D, f)))
    say('  ### files in scope : %d (live papers `.md` + every banked relay record)' % len(scopes))
    for cname, crx in CLS.items():
        hits = []
        for rel, p in scopes:
            try:
                src = io.open(p, encoding='utf-8', errors='replace').read().split('\n')
            except OSError:
                continue
            for i, ln in enumerate(src, 1):
                if crx.search(ln) and CHAN.search(ln):
                    hits.append((rel, i, ln.strip()[:150]))
        say('')
        say('  ### ### **%s -- LINES NAMING IT BESIDE A CHANNEL WORD : %d**' % (cname, len(hits)))
        for rel, i, ln in hits[:12]:
            say('      %-46s:%-6d %s' % (rel, i, ln))
        if len(hits) > 12:
            say('      ... and %d more' % (len(hits) - 12))
        if not hits:
            say('      ### ### **ABSENT. ### THE SEARCH IS PRINTED ABOVE AND IT RETURNED NOTHING.**')

    # ------------------------------------------------------------------ (D) THE CONSTITUENTS
    say()
    say('-' * 100)
    say("### (D) THE E0 GATE'S EIGHT CONSTITUENTS, LOCATED BY THE TABLE'S OWN HEADING.")
    say('-' * 100)
    head = pull(FIND, '### The E0 gate: every constituent unfolded to its owner',
                'THE E0 GATE, BY ITS HEADING')
    src = io.open(FIND, encoding='utf-8').read().split('\n')
    i0 = src.index(head.rstrip('\n'))
    rows = [(n + 1, x) for n, x in enumerate(src[i0:i0 + 20], start=i0)
            if x.startswith('| **K')][:8]
    for n, x in rows:
        say('  ### line %d' % n)
        for j in range(0, min(len(x), 1500), 150):
            say('      | %s' % x[j:j + 150])
    if len(rows) != 8:
        MISS.append('THE E0 GATE TABLE (%d of 8)' % len(rows))
    write_text(os.path.join(SCRATCH, 'e0_rows.txt'), '\n'.join(x for _n, x in rows))

    # ------------------------------------------------------------------ (E) THE FOUR DRESSES
    say()
    say('-' * 100)
    say('### (E) THE FOUR DRESSES, QUOTED FROM THEIR OWN BANKS.')
    say('-' * 100)
    pull(os.path.join(D, 'b405_the_rows_law_restated.txt'),
         'countermodel and any instance of the shape it is about',
         'DRESS 1 -- b405, THE COMPILED COUNTERMODEL', span=True)
    pull(os.path.join(D, 'b406_the_sites_without_an_existential.txt'),
         'NO INNER EXISTENTIAL', 'DRESS 2 -- b406, THE FORM THAT DOES NOT TRANSPOSE', span=True)
    pull(os.path.join(D, 'b407_the_barriers_own_instance.txt'),
         'THE ONE THAT FAILS IS THE ONE ABOUT', 'DRESS 3 -- b407, THE WRONG KIND OF OBJECT',
         span=True)
    pull(os.path.join(D, 'b407_the_barriers_own_instance.txt'),
         'AND THAT IS A RESEMBLANCE, NOT AN INSTANCE',
         'DRESS 4 -- b407, THE EXACT RESEMBLANCE REFUSED', span=True)

    # ------------------------------------------------------------------ (F) THE ROW
    say()
    say('-' * 100)
    say("### (F) ROW `U1`'S COST AND ITS YIELD, COUNTED FROM THE BANKS.")
    say('-' * 100)
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:FACES_LEDGER.md'],
                          capture_output=True).stdout.decode('utf-8')
    row = [x for x in blob.split('\n') if x.startswith('| U1 |')][0]
    write_text(os.path.join(SCRATCH, 'U1_row_at_HEAD.txt'), row)
    c5, c7 = row.rstrip().split('|')[5], row.rstrip().split('|')[7]
    say('    row `U1` at HEAD : %d bytes ; cell 5 %d ; cell 7 %d'
        % (len(row.encode('utf-8')), len(c5.encode('utf-8')), len(c7.encode('utf-8'))))
    sites = re.findall(r'\*\*\((i{1,3}|iv|v|vi)\) ', c5)
    say('    sites entered, by their own markers        : %d %s' % (len(sites), sites))
    added = sorted(set(re.findall(r'added 2026-\d\d-\d\d \((b\d\d\d)\)', c5)))
    restated = sorted(set(re.findall(r'\((b\d\d\d)\)', c7)))
    say('    acts that ENTERED a site (cell 5 says so)  : %s' % (added or 'none stated'))
    say('    acts that RESTATED the refusal (cell 7)    : %s' % (restated or 'none stated'))
    say('    coordinates added (cell 5)                 : %d'
        % c5.count('THE ROW GAINS TWO COORDINATES') * 2)
    for lbl, needle in (('bridges typed, by the row`s own words', 'types no bridge between'),
                        ('grades conferred, by the row`s own words', 'NO GRADE IS CONFERRED')):
        say('    %-42s : PRESENT %s' % (lbl, needle in row))
    acts = sorted(set(re.findall(r'\bb(3\d\d|4\d\d)\b', c5 + c7)))
    say('    ### acts named anywhere in the row          : %d %s' % (len(acts), acts))

    # ------------------------------------------------------------------ (G) PRICES AND ARMS
    say()
    say('-' * 100)
    say('### (G) THE ROUTED PRICES, AND THE SUITES` ARMS ACROSS FOUR ACTS.')
    say('-' * 100)
    say('  ### **THE ROUTED PRICES, FOUND BY READING EACH CLOSING FOR ITS OWN `ROUTED` LINES:**')
    for act in ('b405', 'b406', 'b407'):
        p = os.path.join(D, '%s_closing.txt' % act)
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        found = [ln.strip()[:150] for ln in txt.split('\n')
                 if re.search(r'ROUTED TO THE AUTHOR|ROUTED, WITH|ROUTED WITH ITS PRICE', ln)]
        say('      %s : %d line(s)' % (act, len(found)))
        for f in found:
            say('          %s' % f)
    say()
    say('  ### **THE SUITES` ARMS, BY NAME, ACROSS FOUR ACTS:**')
    suites = {}
    for act in ('b404', 'b405', 'b406', 'b407'):
        p = os.path.join(D, '%s_checks.txt' % act)
        if not os.path.exists(p):
            p = os.path.join(D, '%s_checks_run.txt' % act)
        if not os.path.exists(p):
            say('      %s : NO SUITE RECORD FOUND' % act)
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        names = sorted(set(re.findall(r'^  (G-[A-Z0-9-]+)\s', txt, re.M)))
        suites[act] = set(names)
        say('      %s : %d arms' % (act, len(names)))
    write_text(os.path.join(SCRATCH, 'suite_arms.txt'),
               '\n'.join('%s %s' % (a, ' '.join(sorted(s))) for a, s in suites.items()))
    if len(suites) >= 2:
        keys = sorted(suites)
        core = set.intersection(*[suites[k] for k in keys])
        say('  ### ### **ARMS PRESENT IN ALL %d SUITES (THE STANDING CORE) : %d**'
            % (len(keys), len(core)))
        say('      %s' % sorted(core))
        for i in range(1, len(keys)):
            a, b = keys[i - 1], keys[i]
            carried = suites[a] & suites[b]
            new = suites[b] - suites[a]
            say('      %s -> %s : carried %d ; NEW %d ; of %d (%.0f%% carried)'
                % (a, b, len(carried), len(new), len(suites[b]),
                   100.0 * len(carried) / max(len(suites[b]), 1)))

    say()
    say('=' * 100)
    say('  ### ### **ANCHOR MISSES : %d** %s' % (len(MISS), MISS or ''))
    say('  ### **NOTHING IS WRITTEN TO ANY LEDGER, ROW, KEY OR STANDING FILE BY THIS TOOL.**')
    say('=' * 100)
    write_text(OUT, '\n'.join(L) + '\n')
    return 0 if not MISS else 1


if __name__ == '__main__':
    sys.exit(main())
