# -*- coding: utf-8 -*-
"""b377_branch.py -- COMPONENT 3: ### **THE BRANCH, APPLIED AND NOT CHOSEN.**

### The order fixes the branch and this file executes it:
###   ### **ARM 1 -- APPEND**, only if the document names terminals ### **AND EVERY ONE OF THEM IS
###   ### LOCATED IN ITS KERNEL ON DISK AND CHECKED THERE.**
###   ### **ARM 2 -- ROUTE**, if the document names no terminal ### **OR** ### names one that cannot be
###   located. ### **AND NOTHING IS REPAIRED.**
### ### **IF A SINGLE NAMED TERMINAL CANNOT BE LOCATED, THE WHOLE DOCUMENT TAKES ARM 2** -- a table
### right in four rows and wrong in one is a table a stranger cannot trust.

### ### **THE PIN IS THIS ACT'S OWN READING OF THE KERNEL'S HEAD** ### -- `(R9)`'s forward half. ### It
### is never copied from another document and never taken from a row.

### ### **AND THE HEADING DISCRIMINATOR IS NOT COSMETIC.** ### This corpus writes emphasis as `###
### **LIKE THIS**`, which is indistinguishable from a markdown heading to a naive regex -- `b376`'s own
### axis-B predicate and this act's first reconnaissance both tripped on it. ### **A REAL HEADING IS
### ### `#`s THEN TEXT; AN EMPHASIS RUN IS `#`s THEN `**`.**

### ### **NO DECLARATION IS MOVED, NO CLASS IS RULED AND NO EXISTING BYTE IS CHANGED.** ### Every write
### this file makes is an APPEND to the end of the file.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

MARK = '<!-- b377 correspondence addendum; pins read at this act -->'

# ### **A REAL MARKDOWN HEADING, NOT AN EMPHASIS RUN.**
REAL_HEADING = re.compile(r'^#{1,6}[ \t]+(?!\*\*)')
CORR_WORD = re.compile(r'correspondence', re.I)

# ### **A BACKTICKED LEAN IDENTIFIER, DOTTED OR BARE.** ### The bare form is what this corpus's older
# ### tables use, and a predicate that only knew the dotted form is what scored these documents `B-`.
TICKED = re.compile(r'`([A-Za-z_][A-Za-z0-9_₀-₉\'!?]*(?:\.[A-Za-z_][A-Za-z0-9_₀-₉\'!?]*)*)`')

# ### **WHAT IS NOT A TERMINAL, EXCLUDED BY NAME AND SAID OUT LOUD RATHER THAN SILENTLY DROPPED.**
NOT_TERMINAL = re.compile(
    r'^(SIDE-|PLACE-|TECHNE)|^(np|numpy|scipy|os|sys|io|re|json|math)\.'
    r'|\.(md|py|lean|txt|json|toml|yml|yaml)$'
    r'|^(true|false|none|nil|Prop|Type|Sort|main|HEAD|README|AGENTS|FINDINGS|REGISTRY)$',
    re.I)
# ### **AND A BARE WORD WITH NO UNDERSCORE AND NO DOT IS A NAMESPACE OR A NOUN, NOT A TERMINAL.**
# ### `CriticalPassShadow` is a namespace the document itself annotates as `(4 terminals)`; writing it
# ### into a row as if it were one would be exactly the false promise BAR 3 exists to prevent.
LOOKS_LIKE_TERMINAL = re.compile(r'_|\.')

DECL = re.compile(r'^[ \t]*(?:@\[[^\]]*\][ \t]*)?(?:private[ \t]+|protected[ \t]+|noncomputable[ \t]+|'
                  r'partial[ \t]+|unsafe[ \t]+)*'
                  r'(theorem|lemma|def|abbrev|instance|structure|inductive|example)[ \t]+')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def kernels():
    """### **ENUMERATED FROM DISK, NEVER TYPED** (`b373`)."""
    root = 'D:' + os.sep
    out = []
    for n in sorted(os.listdir(root)):
        p = os.path.join(root, n)
        if n.startswith('SIDE-') and os.path.isdir(os.path.join(p, '.git')):
            out.append((n, p))
    return out


KERNELS = kernels()


def corr_regions(lines):
    """### **REGIONS UNDER A REAL `Correspondence` HEADING**, emphasis runs excluded."""
    out = []
    for i, l in enumerate(lines):
        if REAL_HEADING.match(l) and CORR_WORD.search(l):
            j = i + 1
            while j < len(lines):
                if REAL_HEADING.match(lines[j]) and not CORR_WORD.search(lines[j]):
                    break
                j += 1
            out.append((i + 1, j))
    return out


def candidates(txt):
    """### **EVERY BACKTICKED IDENTIFIER THE DOCUMENT NAMES, WITH THE REJECTS PRINTED.**"""
    keep, rejected = [], []
    for m in sorted(set(TICKED.findall(txt))):
        if NOT_TERMINAL.search(m) or not LOOKS_LIKE_TERMINAL.search(m):
            rejected.append(m)
        else:
            keep.append(m)
    return sorted(keep), sorted(rejected)


def locate(name):
    """### **SEARCH EVERY KERNEL ON DISK FOR A DECLARATION OF THIS NAME, AT ITS COMMITTED HEAD.**

    ### The search is over `git grep` at `HEAD`, so it reads the ### **BLOB** ### and not a working
    ### copy. ### A dotted name is looked for by its LAST segment, because Lean declares
    ### `theorem foo` inside `namespace Bar` and the fully-qualified form rarely appears at the
    ### declaration site. ### **THE NAMESPACE IS THEN VERIFIED IN THE SAME FILE.**
    """
    last = name.split('.')[-1]
    ns = name.split('.')[0] if '.' in name else None
    hits = []
    for kname, kpath in KERNELS:
        r = git(kpath, 'grep', '-n', '-E',
                r'^[ \t]*(@\[[^]]*\][ \t]*)?(private |protected |noncomputable |partial |unsafe )*'
                r'(theorem|lemma|def|abbrev|instance|structure|inductive) +' + re.escape(last)
                + r'\b', 'HEAD')
        if r.returncode != 0 or not r.stdout.strip():
            continue
        for ln in r.stdout.split(chr(10)):
            if not ln.strip():
                continue
            parts = ln.split(':', 3)
            if len(parts) < 4:
                continue
            _ref, path, lineno, code = parts[0], parts[1], parts[2], parts[3]
            ok_ns = True
            if ns:
                rf = git(kpath, 'show', 'HEAD:' + path)
                ok_ns = (('namespace ' + ns) in rf.stdout) or (ns in path.replace('/', '.'))
            hits.append(dict(kernel=kname, path=path, line=int(lineno), code=code.strip()[:130],
                             namespace_confirmed=ok_ns))
    return hits


def head_of(kname):
    """### **THE PIN: THIS ACT'S OWN READING OF THAT KERNEL'S HEAD.** ### `(R9)`'s forward half."""
    for n, p in KERNELS:
        if n == kname:
            return git(p, 'rev-parse', 'HEAD').stdout.strip()
    return None


def profile_from_document(txt, name):
    """### **THE AXIOM PROFILE AS THE DOCUMENT ITSELF STATES IT**, never computed here (section (F))."""
    for ln in txt.split(chr(10)):
        if ('`' + name + '`') in ln:
            m = re.search(r'`\{[^`]*\}`|axiom-free|\*\*no axioms\*\*|no axioms', ln, re.I)
            if m:
                return m.group(0)
    return None


def addendum(rel, rows, pins):
    """### **THE APPENDED BLOCK. ### IT ADDS; IT REPLACES NOTHING.**"""
    L = ['', MARK, '',
         '## Correspondence addendum — pins read at b377 (2026-09-08)',
         '',
         ('> ### **THE TABLE(S) ABOVE ARE PRESERVED UNCHANGED. THIS BLOCK IS APPENDED AND EDITS '
          'NOTHING.** *It exists because the standing taxonomy obliges a Tier K document to state, '
          'for each load-bearing claim, its **grade · terminal · pin** — and the pin was the element '
          'this document did not carry. Every terminal below was located in its kernel repository and '
          'read at that kernel\'s committed head by the act that wrote this row; the pin is that head. '
          'No pin here is copied from another document or from another row.*'),
         '',
         ('> ### **WHAT THIS BLOCK DOES NOT CLAIM.** *Locating a terminal says the terminal EXISTS AT '
          'THAT NAME in that kernel at that pin. It does not say this document\'s sentence about it is '
          'right, and the claim column reproduces the document\'s own wording. The axiom profile is '
          'reproduced as this document states it and was not recomputed. No class was ruled, no '
          'declaration moved and no existing row changed.*'),
         '',
         '| claim (as this document states it) | kernel | fully-qualified terminal | axiom profile | grade | pin (read at b377) |',
         '|:--|:--|:--|:--|:--|:--|']
    for r in rows:
        L.append('| %s | `%s` | `%s` | %s | %s | `%s` |'
                 % (r['claim'], r['kernel'], r['terminal'], r['profile'], r['grade'], r['pin']))
    L += ['',
          ('*Pins are full commit hashes of each kernel repository\'s `main` at the moment this block '
           'was written: ' + '; '.join('`%s` = `%s`' % (k, v) for k, v in sorted(pins.items())) + '.*'),
          '']
    return chr(10).join(L) + chr(10)


def main():
    rec('=' * 100)
    rec('b377 -- COMPONENT 3: ### **THE BRANCH, APPLIED AND NOT CHOSEN.**')
    rec('=' * 100)
    rec('')
    R = json.load(io.open(os.path.join(D, 'b377_reads.json'), encoding='utf-8'))
    SIX, TWO = R['six'], R['two']
    rec('  ### kernel repositories enumerated from disk : %d' % len(KERNELS))
    rec('  ### the branch population (declare TIER K, score `B-`) : %d' % len(SIX))
    rec('  ### reported and left (declare TIER K, score `NOT DETERMINABLE`) : %d' % len(TWO))
    rec('')
    rec('  ### **THE OBLIGATION, IN THE TAXONOMY`S OWN WORDS:** ### *every such claim states its')
    rec('  ### **grade . terminal . pin**, and the axiom profile is written in full.*')
    rec('')

    results, pins_used = [], {}
    for rel in SIX:
        path = os.path.join(PP, rel.replace('/', os.sep))
        txt = io.open(path, encoding='utf-8', errors='replace').read()
        lines = txt.split(chr(10))
        regions = corr_regions(lines)
        cands, rejects = candidates(txt)
        rec('-' * 100)
        rec('  ### `%s`' % rel)
        rec('-' * 100)
        rec('    real Correspondence headings : %d %s'
            % (len(regions), ['line %d' % a for a, _b in regions] or ''))
        rec('    backticked identifiers kept as terminal candidates : %d' % len(cands))
        rec('    rejected as not-a-terminal : %d %s' % (len(rejects), rejects[:8]))
        located, missing, ambiguous = [], [], []
        for c in cands:
            hits = locate(c)
            good = [h for h in hits if h['namespace_confirmed']]
            krn = sorted(set(h['kernel'] for h in good))
            if len(krn) == 1:
                located.append(dict(name=c, hit=good[0], n_hits=len(good), kernels=krn))
                rec('      LOCATED   %-52s %s:%s' % (c[:52], good[0]['kernel'], good[0]['path']))
            elif len(krn) > 1:
                # ### **A NAME DECLARED IN MORE THAN ONE KERNEL CANNOT BE WRITTEN INTO A ROW.**
                # ### ### **CHOOSING THE FIRST WOULD BE THE ACT INVENTING THE CORRESPONDENCE THE
                # ### ### DOCUMENT DID NOT STATE**, and BAR 3 exists to stop exactly that.
                ambiguous.append(dict(name=c, kernels=krn))
                missing.append(c)
                rec('      ### ### **AMBIGUOUS** %-42s ### declared in %d kernels : %s'
                    % (c[:42], len(krn), krn))
            else:
                missing.append(c)
                rec('      ### ### **NOT LOCATED** %-42s ### in any of %d kernels'
                    % (c[:42], len(KERNELS)))
        arm = 1 if (located and not missing) else 2
        why = ''
        if not cands:
            why = 'the document names no terminal this act can read as one'
        elif missing:
            nl = len(missing) - len(ambiguous)
            why = ('%d of %d named terminals did not resolve to exactly one kernel (%d located '
                   'nowhere, %d declared in more than one); ### **ONE UNRESOLVED TERMINAL SENDS THE '
                   'WHOLE DOCUMENT TO ARM 2**' % (len(missing), len(cands), nl, len(ambiguous)))
        else:
            why = ('every one of the %d named terminals was located at its kernel and resolves '
                   'to EXACTLY ONE kernel' % len(cands))
        rec('    ### ### **ARM %d -- %s**' % (arm, 'APPEND' if arm == 1 else 'ROUTE'))
        rec('    ### why : %s' % why)

        rows, wrote = [], False
        if arm == 1:
            if MARK in txt:
                rec('    ### ALREADY APPENDED -- the mark is present. ### NOTHING WRITTEN.')
                wrote = True
            else:
                for L1 in located:
                    k = L1['hit']['kernel']
                    pin = head_of(k)
                    pins_used[k] = pin
                    prof = profile_from_document(txt, L1['name']) or '*as tabulated above*'
                    rows.append(dict(claim='as tabulated above for `%s`' % L1['name'],
                                     kernel=k, terminal=L1['name'], profile=prof,
                                     grade='**LOCATED-AT-PIN** — the terminal is declared in this '
                                           'kernel at this commit; the grade of the *claim* is '
                                           'unchanged from the row above',
                                     pin=pin))
                # ### **THE FOOTNOTE NAMES ONLY THE KERNELS THIS DOCUMENT'S OWN ROWS USE.**
                # ### ### **A PIN FOR A KERNEL THE DOCUMENT DOES NOT REFERENCE IS A TRUE FACT IN THE
                # ### ### WRONG DOCUMENT**, and it implies a relationship the document never stated.
                mine = {r['kernel']: r['pin'] for r in rows}
                before = io.open(path, encoding='utf-8', newline='').read()
                io.open(path, 'a', encoding='utf-8', newline=chr(10)).write(addendum(rel, rows, mine))
                after = io.open(path, encoding='utf-8', newline='').read()
                blob = git(PP, 'show', 'HEAD:' + rel).stdout
                ao = after.startswith(before)
                pi = (blob.replace(chr(13) + chr(10), chr(10))
                      in after.replace(chr(13) + chr(10), chr(10)))
                rec('    ### bytes %d -> %d ; append-only %s ; committed blob still a substring %s'
                    % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao, pi))
                wrote = ao and pi
                if not wrote:
                    rec('    ### ### **HARD FAILURE -- THE APPEND WAS NOT AN APPEND.**')
        results.append(dict(file=rel, corr_headings=len(regions), candidates=cands,
                            rejected=rejects, located=[x['name'] for x in located],
                            located_kernels={x['name']: x['kernels'] for x in located},
                            not_resolved=missing, ambiguous=ambiguous, arm=arm, why=why,
                            rows=rows, appended=(arm == 1 and wrote)))

    # ------------------------------------------------- THE AMENDMENT'S FIRST CLAUSE: REPORT AND LEAVE
    rec('')
    rec('=' * 100)
    rec("  ### THE AMENDMENT`S FIRST CLAUSE -- ### **NOT DETERMINABLE IS NOT ABSENT.**")
    rec('=' * 100)
    nd = []
    for rel in TWO:
        path = os.path.join(PP, rel.replace('/', os.sep))
        txt = io.open(path, encoding='utf-8', errors='replace').read()
        lines = txt.split(chr(10))
        regions = corr_regions(lines)
        cands, _rej = candidates(txt)
        conc = bool(re.search(r'\bKernel Concordance\b|\bconcordance\b', txt, re.I))
        rec('  ### `%s`' % rel)
        rec('    ### **WHAT THE READ COULD NOT DECIDE:** ### whether this document carries the')
        rec('    ### apparatus. ### `b376``s axis B scans TABLE ROWS; this document names its terminals')
        rec('    ### in prose or under a concordance (concordance language present : %s), and ### **A'
            % conc)
        rec('    ### ### TABLE SCAN IS THE WRONG INSTRUMENT FOR THAT ARCHITECTURE** -- which the corpus')
        rec('    ### itself said when it made `CONCORDANCE-CARRIED` its own class.' )
        rec('    ### real Correspondence headings : %d ; backticked terminal candidates : %d'
            % (len(regions), len(cands)))
        rec('    ### **WHAT WOULD DECIDE IT:** ### a read of the prose that names the terminals, one')
        rec('    ### claim at a time, checking each named terminal at its kernel -- ### **A HAND READ,')
        rec('    ### ### NOT A SCAN**, because the naming is in sentences and not in cells.')
        rec('    ### ### **AND IT IS NOT REPAIRED, NOT ROUTED AS LACKING, AND NOT COUNTED AMONG THE')
        rec('    ### ### SIX.**')
        rec('')
        nd.append(dict(file=rel, corr_headings=len(regions), candidates=len(cands),
                       concordance_language=conc,
                       could_not_decide='whether the apparatus is present, because the naming is in '
                                        'prose or a concordance and axis B scans table rows',
                       what_would_decide='a hand read of the naming sentences, checking each named '
                                         'terminal at its kernel',
                       repaired=False, routed_as_lacking=False, counted_among_the_six=False))

    a1 = [r for r in results if r['arm'] == 1]
    a2 = [r for r in results if r['arm'] == 2]
    rec('=' * 100)
    rec('  ### ### **ARM 1 (APPEND) : %d ### / ### ARM 2 (ROUTE) : %d ### of %d**'
        % (len(a1), len(a2), len(results)))
    rec('  ### ### **TERMINALS WRITTEN THAT WERE NOT LOCATED AND CHECKED : %d**'
        % sum(1 for r in results for _row in r['rows'] if _row['terminal'] not in r['located']))
    rec('  ### ### **TERMINALS WRITTEN THAT RESOLVE TO MORE THAN ONE KERNEL : %d**'
        % sum(1 for r in results for _row in r['rows']
              if len(r['located_kernels'].get(_row['terminal'], [])) != 1))
    rec('  ### ### ### **A NAME DECLARED IN TWO KERNELS IS NOT A TERMINAL THIS ACT CAN WRITE INTO A')
    rec('  ### ### ### ROW.** ### Choosing the first would be the act inventing a correspondence the')
    rec('  ### ### ### document did not state.')
    rec('  ### ### **NOT-DETERMINABLE DOCUMENTS REPAIRED : 0 ### / ROUTED AS LACKING : 0 ### / '
        'COUNTED AMONG THE SIX : 0**')
    rec('  ### pins read from a kernel head by this act : %d %s'
        % (len(pins_used), sorted(pins_used)))
    rec('  ### ### **NO DECLARATION WAS MOVED, NO CLASS WAS RULED AND NO EXISTING BYTE WAS CHANGED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b377_branch_notes', LINES)
    io.open(os.path.join(D, 'b377_branch.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(kernels=len(KERNELS), six=results, not_determinable=nd,
                        arm1=len(a1), arm2=len(a2), pins=pins_used, mark=MARK,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
