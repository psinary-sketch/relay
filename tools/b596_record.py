# -*- coding: utf-8 -*-
"""b596_record.py -- THE ACT'S RECORD TOOL, UNDER (R206). ### ONE SUBCOMMAND PER BANK.

### ### b596: LANE THREE, ACT TWENTY-THREE -- W-ORD-SIMPLICITY-FACE: THE PROPORTION OF SIMPLE ZEROS WALKED IN THE VENDORED SET,
### THE TITLE'S CLAUSE STATED AS A SALT-CHECKED PROP, THE FACES' SILENCE ON MULTIPLICITY ENTERED ON THE PAGE, SIMPLICITY'S
### CLAIMS READ AGAINST THEM.
### Subcommands write only `data/b596_*` unless the docstring names another file. Every bank is written through `put_txt` /
### `put_json` (encode, temp file, `os.replace`). No platform call. The templates are b595_record.py and b590_record.py.
### ### **NO SENTENCE OF THE DELIBERATION TREE'S BODY IS CARRIED HERE**: the one sentence the act adds to the tree's section (v)
### lives in the scratchpad (`SP/tree_sentence.txt`) and in TECHNE-Core only; relay carries its sha256 and the line number.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
EFK = 'D:/SIDE-explicit-formula'
UP = os.path.join(ROOT, 'data', 'anthropic-zeta23', 'formal-math').replace('\\', '/')
PRE_PP = 'ba5f0ea'
PRE_RELAY = '0cfe7354'
PRE_TE = 'f089761'
PRE_TE_HEAD = 'da89d83'
PRE_KER = 'c404e72'
STEPZERO = '46248b4a'
UPIN = '3635e74826a4c1fcece7d1cd2b6fa75e43a00510'
TAG = 'v0.17'
BRANCH = 'simplicity-b596'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/4d816814-ed14-4689-b5cb-96db62728606/scratchpad'
TREE_REL = 'modules/2026-10/DELIBERATION_TREE.md'
SIMP = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
KFILES = dict(simp='SIDEExplicitFormula/Simplicity.lean', salt='SIDEExplicitFormula/SaltCheckSimplicity.lean')
AXF = 'AxiomCheckSimplicity.lean'
NS = 'SIDEExplicitFormula.Simplicity.'
STD3 = ['propext', 'Classical.choice', 'Quot.sound']
NEW_NODES = [NS + 'allSimple', NS + 'simplicity', NS + 'simplicity_iff', NS + 'SimpleProportion', NS + 'exceptional_mass_le_third']

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def jl(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _Q():
    import b566_record as R6
    return R6.Q


DEFECTS = [
    '(a) THE SEAT PATCHED ITS OWN UNSEALED RECORD TOOL THROUGH A PYTHON HEREDOC, NOT THE EDIT TOOL, against the ferry`s procedural '
    'line: two string replacements (the work-list read range 1-32 to 1-31, its file having 31 lines; the vendored `def` line 200 to '
    '199), each asserted to occur once. Neither string carried a backslash or a quote, so the bytes are the ones intended; found by '
    'the seat at once, before the seal, and every later edit to an act tool goes through the Edit tool.',
    '(b) TWO KERNEL FILES WERE PLACED BY `cp`, NOT THE WRITE TOOL THE FACE`S (W) ROW NAMES: SIDEExplicitFormula/Simplicity.lean and '
    'SaltCheckSimplicity.lean were copied onto the branch from the scratchpad drafts the Write tool had written (AxiomCheckSimplicity.lean '
    'went through the Write tool); the bytes are the drafts`, printed with their sha256 before the build (data/b596_statements_*.txt). '
    'The seat`s, logged on the author`s word.',
    '(c) THE FIRST RE-EMISSION OF THE PAGES WAS STOPPED BY THE HARNESS`S MEMORY-PRESSURE REAPER while the session was idle (free memory '
    'then ~2 GB, Chrome holding ~4 GB): no page, relay bank or corpus file was written, no lean, lake or python process was left, a '
    'partial probe output stayed in the scratchpad. The author answered: retry in the background with Chrome closed, the reaper '
    'setting unchanged.',
    '(d) THE PAGE ARMS` FIRST RUN AFTER THE TAG STARTED FROM THE WRONG DIRECTORY: issued in parallel with the page commits, it ran '
    'from PLACE-papers and Python found no tools/b596_record.py (exit 2); nothing was read or written. Re-run alone at once, 4 of 4.',
    '(e) THE FIRST RE-EMISSION PRINTED `NO TAG` FOR SimpleProportion (the first structure node any page carried; the generator`s '
    'entry-tag pattern read no `structure`). Found by reading the page diff before the commit; the page was committed as generated '
    'and the author answered (prompt 3): a structure`s entry tag added to the Component 4 generator commit, the page right at '
    'd774fb5. By that answer G-GEN-EDIT (one non-backmatter line) and G-ANSWERS-BANKED (a third prompt) are refuted in their '
    'letter, the cause the navigator`s.',
]


def defects():
    put_txt('b596_defects.txt', ['### b596 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


# ================================================================================ READING (1): THE READS
RELAY = ROOT.replace('\\', '/')
READS = [
    ('PLACE-papers OPEN_TRAILS, the work-order whole and the standing line', PP, PRE_PP, 'OPEN_TRAILS.md',
     [12012, 12014, 12016, 12018, 12026, 12228, 12246]),
    ('PLACE-papers FINDINGS, b595`s entry', PP, PRE_PP, 'FINDINGS.md', [6834, 6836]),
    ('relay the lemma-walk instrument`s last bank (b572)', RELAY, 'HEAD', 'data/b572_lemmas.txt', [1, 2, 3, 4, 6, 7, 8, 9]),
    ('SIDE-explicit-formula the vendored statement layer (Theorems A, B, C as Props)', EFK, PRE_KER, 'Zeta23/Statement.lean',
     [1, 2, 3, 4, 5, 6, 7, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 77, 78, 80, 81, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187,
      188, 189, 190, 191, 192, 194, 195, 196, 198, 199, 200, 202, 203, 204]),
    ('SIDE-explicit-formula the configuration structure (Zeta23 ZeroConfig)', EFK, PRE_KER, 'Zeta23/Defs.lean', list(range(126, 146)) + [158, 159, 173, 174]),
    ('SIDE-explicit-formula the genuine configuration', EFK, PRE_KER, 'Zeta23/Statement/SeamClosed.lean', [38, 40, 41, 42, 44, 45, 51, 52]),
    ('SIDE-explicit-formula the schema (WeilConfig, h2_sign_cfg, online, the forward half)', EFK, PRE_KER, 'SIDEExplicitFormula/Schema/Config.lean',
     [1, 2, 3, 4, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 42, 43, 45, 46, 52, 53]),
    ('SIDE-explicit-formula the ζ instance', EFK, PRE_KER, 'SIDEExplicitFormula/Schema/Instances.lean', [22, 23, 24, 25, 32, 33, 34, 35, 36, 37, 38, 41, 42]),
    ('SIDE-explicit-formula the house form: the salt-check gate (b590)', EFK, PRE_KER, 'SIDEExplicitFormula/Schema/SaltCheckEpstein.lean',
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 105, 106, 107, 125, 126, 127, 128, 129, 130]),
    ('SIDE-explicit-formula the house form: a module at INTERFACES (b590)', EFK, PRE_KER, 'SIDEExplicitFormula/Schema/Epstein.lean',
     [1, 2, 3, 4, 41, 42, 43, 44, 45, 46, 57, 58, 59, 60]),
    ('SIDE-explicit-formula the module that states h2_sign_iff_rh', EFK, PRE_KER, 'SIDEExplicitFormula/Seam.lean', [101, 102]),
    ('PLACE-papers the ζ page, its head and its back matter', PP, PRE_PP, PAGE, [1, 3, 29, 31, 33, 35, 71, 73, 74]),
    ('PLACE-papers SIMPLICITY_OF_RIEMANN_ZEROS (current version), head, version, Abstract, tier block, version history', PP, PRE_PP, SIMP,
     [1, 3, 11, 17, 24, 26, 429, 469, 496, 498, 500, 528, 530, 532]),
    ('relay SIMPLICITY`s work-list, whole', RELAY, 'HEAD', 'data/b558_editions/SIMPLICITY_OF_RIEMANN_ZEROS.txt', list(range(1, 32))),
    ('relay the generator`s head, its node-list reader, its emitter and its hold', RELAY, 'HEAD', 'tools/chain_page.py', [4, 5, 6, 7, 57, 112, 458, 473, 479, 556, 558, 559]),
    ('relay push_gated.sh, its head', RELAY, 'HEAD', 'tools/push_gated.sh', list(range(1, 12))),
    ('relay b595`s answers bank, its head', RELAY, 'HEAD', 'data/b595_author_answers.txt', [1, 3, 4, 9]),
    ('relay b595`s closing push-out, its head', RELAY, 'HEAD', 'data/b595_closing_push_out.txt', list(range(1, 6))),
]


def reads():
    L = ['b596 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev + '^{}').strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:400]))
    L += ['', '### TECHNE-Core DELIBERATION_TREE.md (private) @ %s -- read for section (v)`s place only: heading at :%s; no line of its text '
          'is printed here.' % (g(TE, 'rev-parse', '--short=8', 'HEAD').strip(),
                                [i for i, l in enumerate(g(TE, 'show', 'HEAD:' + TREE_REL).split(NL), 1) if l.startswith('## (v) ')])]
    put_txt('b596_reads.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B595_ENTRY_HEAD = '## The deliberation tree: the relay’s prompts since b577'
STANDING_595 = '*Appended 2026-10-02 by b595 to the precedence order (:12228)'
WORK_ORDER = '### `W-ORD-SIMPLICITY-FACE`'
HELD_LINE = '*Appended 2026-10-01 by b584 to the order of the editions (:11884)'


def weight_line():
    """### PLACE-papers FINDINGS: b595's weight, one appended line addressed to b595's entry, the verdicts as (R206)(1) reads them."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B595_ENTRY_HEAD)
    if entry != 6836:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    head = '*Appended 2026-10-02 by b596 to b595’s entry (:%d), under `(R206)`(1) -- b595 AT ITS WEIGHT:*' % entry
    Q.guard_absent(Q.FIND, head)
    text = ('\n%s the deliberation tree at TECHNE-Core modules/2026-10/ (sha256 abe55c0c…), 44 nodes, 1,691 words of body outside '
            'the tables, its extraction committed alone before it; relay holding pointers, digests and classifications alone, the '
            'no-disclosure arm at 60 needles and 0 hits. H33a REFUTED -- the relay banks hold 12 prompts with questions and no options, '
            'the transcripts all 44; the standing line at OPEN_TRAILS :12246 is the repair. H33b REFUTED at 35 of 41 (85.4%%, cap 80%%), '
            'the divergences at nodes 4, 5, 9, 12, 32, 35; two of the navigator’s five named divergences were not divergences. H33c '
            'HOLDS (no reversal; amendments at 5, 9, 11, 25). H33d refuted in its letter on the table (its verbatim quotations of the '
            'record: 37 ceiling hits, 9 stems) and held on the body (0 and 0); the quotations are record under the name-and-title '
            'exception, and the hypothesis as fixed did not say so. (N1), (N2), (N5) REFUTED, (N5) by the author’s own answer. The two '
            'history lines (FACES v0.2 74381f3; BALPOS v0.9.5 078ccf7, seven cells re-pinned, the two v0.9.4 citations left); the :4787 '
            'search 24 occurrences in 9 files. Defects (a)-(e) the seat’s, caught before any write. The suite read 70 of 70.\n' % head)
    r = Q.append_to(Q.FIND, text)
    put_json('b596_weight_line.json', dict(entry=entry, line=Q.line_of(Q.FIND, head), head=head, append=r))
    print('  weight line :%s' % Q.line_of(Q.FIND, head))


def rule_lines():
    """### PLACE-papers OPEN_TRAILS: (R206)(2)'s three items -- (i) and (ii) in one line addressed to b595's standing line (:12246),
    ### (iii) the batch-refresh standing line beneath it; then W-ORD-QUANTIFIER-COLUMN, (R206)(3). Three appended lines."""
    Q = _Q()
    p = Q.line_of(Q.OT, STANDING_595)
    if p != 12246:
        sys.exit('### THE ADDRESSED LINE MOVED: standing line %s -- NOTHING WRITTEN' % p)
    h1 = '*Appended 2026-10-02 by b596 to the standing line (:%d), under `(R206)`(2)(i)-(ii) -- THE SEAT’S ITEMS RULED:*' % p
    h2 = ('*Appended 2026-10-02 by b596 beneath the standing line (:%d), under `(R206)`(2)(iii) -- THE DELIBERATION TREE REFRESHED IN '
          'BATCHES, STANDING:*' % p)
    h3 = ('### `W-ORD-QUANTIFIER-COLUMN` -- THE QUANTIFIER SHAPE OF EACH NODE, A PAGE COLUMN, PRICED, NOT STARTED, appended 2026-10-02, '
          'b596, under the author’s ruling (R206)(3)')
    for h in (h1, h2, h3):
        Q.guard_absent(Q.OT, h)
    t1 = ('\n%s (i) b595’s reading of “beside the method document” as the sibling folder `modules/2026-10/` is accepted: the method '
          'document stays in `modules/2026-08/` beside the drafts it grew from, and the tree sits in the month it was written. (ii) The '
          'scoring weight of the tree’s section (v) -- an agreement later reversed nets −1 -- stands as written, the seat’s proposal '
          'under the author’s ratification by `(R206)`; the author strikes or re-weights it at a closing, and the section’s text says '
          'the weight was set by the author at `(R206)` (one sentence, TECHNE-Core, committed alone, not pushed).\n' % h1)
    t2 = ('\n%s the tree is refreshed in batches: when five or more acts’ prompts have accrued since its version, or on the author’s '
          'word, the seat writes the next version as a housekeeping commit at the following act’s step zero, the nodes added and the '
          'counts re-run, the scoring rule unchanged. b595’s three prompts (relay data/b595_author_answers.txt) join the tree at v0.2, '
          'which is not b596’s.\n' % h2)
    t3 = ('\n%s\n\n**Items.** The pages’ node tables take one column reading, from the Lean statement, the quantifier shape of each node: '
          'FINITE (a decidable or bounded statement -- a cell, a window, a count up to T), UNIVERSAL (∀ over the zeros, the primes or the '
          'integers, with no bound), LIMIT (a Filter.Tendsto or an asymptotic), FAMILY (∀ over a class of objects -- every primitive χ, '
          'every configuration). The generator (relay tools/chain_page.py) reads the column from the statement’s leading binders and '
          'prints it; a node whose shape the reader cannot classify is printed as such and the author rules. The reason is the author’s '
          'question at b595: the programme’s finite facts and its infinite equivalences sit in the same table with no mark that tells '
          'them apart, and the mark is in the statements already.\n\n**Price:** one generator edit with a test, both pages re-emitted, '
          'one line in each page’s head naming the column. **Trigger:** the author’s word. **Expected:** the ζ page’s RH-equivalents '
          'read UNIVERSAL; the detector reads FAMILY; the ladder’s rungs read FINITE.\n' % h3)
    out = []
    for h, t in ((h1, t1), (h2, t2), (h3, t3)):
        r = Q.append_to(Q.OT, t)
        out.append(dict(head=h, line=Q.line_of(Q.OT, h), append=r))
    put_json('b596_rule_lines.json', dict(standing=p, lines=out))
    for o in out:
        print('  line :%s' % o['line'])


def tree_sentence(*a):
    """### TECHNE-Core DELIBERATION_TREE.md: the one sentence of (R206)(2)(ii) appended to section (v)'s paragraph that names the
    ### weight as the seat's proposal; the sentence text read from SP/tree_sentence.txt. `dry` prints the sha256s only."""
    p = os.path.join(TE, *TREE_REL.split('/'))
    b = open(p, 'rb').read()
    eol = b'\r\n' if b'\r\n' in b else b'\n'
    ls = b.split(eol)
    sent = io.open(os.path.join(SP, 'tree_sentence.txt'), encoding='utf-8').read().strip()
    v = [i for i, l in enumerate(ls) if l.startswith(b'## (v) ')]
    vi = [i for i, l in enumerate(ls) if l.startswith(b'## (vi) ')]
    tgt = [i for i in range(v[0], vi[0]) if b"seat's proposal" in ls[i]] if len(v) == 1 and len(vi) == 1 else []
    if len(tgt) != 1:
        sys.exit('### THE PARAGRAPH IS NOT FOUND ONCE IN SECTION (v): %s -- NOTHING WRITTEN' % tgt)
    i = tgt[0]
    new = list(ls)
    new[i] = ls[i].rstrip() + b' ' + sent.encode('utf-8')
    nb = eol.join(new)
    rec = dict(line=i + 1, before=sha(b), after=sha(nb), sentence_sha256=sha(sent), eol=eol.decode())
    print('  section (v) paragraph at :%d ; file sha256 before %s after %s ; sentence sha256 %s' % (i + 1, rec['before'][:16], rec['after'][:16],
                                                                                                    rec['sentence_sha256'][:16]))
    if a and a[0] == 'dry':
        return
    open(p + '.tmp', 'wb').write(nb)
    os.replace(p + '.tmp', p)
    put_json('b596_tree_sentence.json', rec)


# ================================================================================ COMPONENT 2: THE WALK
NAME_NEEDLES = ['thmB₀_mult', 'thmB_mult', 'two_thirds_simple', 'thmB₀', 'thmB', 'ThmB_statement', 'N0simple', 'N0s', 'Nsimple',
                'simple_on_critical_line']
BOUND_NEEDLES = [r'2 / 3', r'1 / 2 - ε', r'two thirds', r'2/3']


def _grep(repo, rev, pat, *paths):
    out = g(repo, 'grep', '-n', '-I', '-E', pat, rev, '--', *paths)
    rows = []
    for l in out.split(NL):
        if not l.strip():
            continue
        _r, path, n, text = l.split(':', 3)
        rows.append((path, int(n), text.strip()))
    return rows


def walk():
    """### (R206)(4)(a): the vendored module list at the kernel's v0.16 tree (Zeta23/, vendored at 3635e748), the walk for the
    ### proportion by name and by its bound, every hit with path and line; the upstream module that holds it named at the pin with
    ### its statement quoted; the attribution and the bound in the modules' own words; H29a; the fact correction."""
    mods = sorted(x for x in g(EFK, 'ls-tree', '-r', '--name-only', PRE_KER, 'Zeta23/').split(NL) if x.endswith('.lean'))
    hdr_pin = sorted(set(re.sub(r'\s+', ' ', l.split(':', 3)[3]) for l in g(EFK, 'grep', '-n', '^Pin', PRE_KER, '--', 'Zeta23/').split(NL) if l.strip()))
    L = ['b596 -- COMPONENT 2: THE WALK FOR THE PROPORTION OF SIMPLE ZEROS, (R206)(4)(a). ### written at (UTC) %s' % utc(),
         '### the instrument: git grep over the vendored modules at SIDE-explicit-formula %s (the v0.16 tree), each module`s header pin %s ; '
         'then the upstream clone (relay data/anthropic-zeta23/formal-math, untracked) at the pin %s' % (PRE_KER, hdr_pin, UPIN[:8]), '',
         '### (1) THE VENDORED MODULE LIST -- %d modules' % len(mods)]
    L += ['    ' + m for m in mods]
    hits_name, hits_bound = {}, {}
    for nd in NAME_NEEDLES:
        hits_name[nd] = _grep(EFK, PRE_KER, r'(^|[^A-Za-z0-9_])' + re.escape(nd) + r'($|[^A-Za-z0-9_₀])', 'Zeta23/')
    for bd in BOUND_NEEDLES:
        hits_bound[bd] = _grep(EFK, PRE_KER, re.escape(bd), 'Zeta23/')
    L += ['', '### (2) THE WALK BY NAME (a needle bounded on both sides by a non-identifier character)']
    for nd in NAME_NEEDLES:
        L.append('  ## %-24s %d hit(s)' % (nd, len(hits_name[nd])))
        L += ['      %s:%d  %s' % (p, n, t[:200]) for p, n, t in hits_name[nd]]
    L += ['', '### (3) THE WALK BY THE BOUND']
    for bd in BOUND_NEEDLES:
        L.append('  ## %-24s %d hit(s)' % (repr(bd), len(hits_bound[bd])))
        L += ['      %s:%d  %s' % (p, n, t[:200]) for p, n, t in hits_bound[bd]]
    # ### the vendored statement of the simple-on-the-line proportion, its own words
    st = g(EFK, 'show', '%s:Zeta23/Statement.lean' % PRE_KER).split(NL)
    vend = dict(def_line=199, doc_line=198, text=[st[197], st[198], st[199]], header=[st[2], st[3], st[4], st[5]], canon=st[24], scope=[st[178], st[179], st[180], st[181], st[182]])
    thm_in_vendored = [x for x in hits_name['thmB₀_mult'] + hits_name['thmB_mult'] + hits_name['two_thirds_simple']]
    L +=['', '### (4) THE VENDORED STATEMENT, IN ITS OWN WORDS (Zeta23/Statement.lean at %s)' % PRE_KER]
    L += ['    :%d %s' % (i, st[i - 1]) for i in (3, 4, 5, 6, 25, 179, 180, 181, 182, 183, 198, 199, 200, 202, 203, 204)]
    L += ['    ### the vendored set holds the simple-on-the-line statement as `Zeta23.ThmB_statement`, a Prop (a `def`), at the bound 1/2 '
          '(its docstring :198 "The statement of Theorem B (1/2, dyadic ε-form)"); its header :179-:183 names the theorems that prove it '
          '(Zeta23/Final.lean, Zeta23/Main.lean) as elsewhere; no `theorem` or `lemma` of the vendored set concludes a lower bound on '
          '`N0simple` (the name walk above: %d hits for thmB₀_mult / thmB_mult / two_thirds_simple).' % len(thm_in_vendored)]
    # ### upstream at the pin
    fm = g(UP, 'show', '%s:Zeta23/FinalMult.lean' % UPIN).split(NL)
    fn = g(UP, 'show', '%s:Zeta23/Final.lean' % UPIN).split(NL)
    rm = g(UP, 'show', '%s:README.md' % UPIN).split(NL)
    up_hits = _grep(UP, UPIN, r'theorem thmB₀_mult\b', 'Zeta23/')
    L += ['', '### (5) THE UPSTREAM MODULE THAT HOLDS IT, AT THE PIN %s (anthropics/formal-math, the zeta23 formalization; relay`s clone '
          'at HEAD %s)' % (UPIN, g(UP, 'rev-parse', '--short=8', 'HEAD').strip()),
          '    the declaration: %s' % ['%s:%d' % (p, n) for p, n, _t in up_hits]]
    L += ['    Zeta23/FinalMult.lean :%d %s' % (i, fm[i - 1]) for i in range(347, 355)]
    L += ['    Zeta23/Final.lean :%d %s' % (i, fn[i - 1]) for i in range(85, 90)]
    L += ['    Zeta23/Final.lean :%d %s' % (i, fn[i - 1]) for i in range(304, 309)]
    L += ['    README.md :%d %s' % (i, rm[i - 1][:400]) for i in (1, 8, 9, 31, 32)]
    b468 = rd('b468r_closing.txt').split(NL)
    L += ['', '### (6) THE ATTRIBUTION, IN THE MODULES` OWN WORDS, AND THE RECORD`S',
          '    the vendored header (Statement.lean :3-:6): %s' % ' | '.join(x.strip() for x in vend['header']),
          '    the vendored body: "Copyright (c) 2026 Anthropic, PBC" and "Canonical text: the paper" (:18, :25)',
          '    the upstream README :8: %s' % rm[7][:300],
          '    relay data/b468r_closing.txt :39-:41 (the arXiv byline): %s' % ' '.join(x.strip() for x in b468[38:41])[:400]]
    present = bool(up_hits) and not thm_in_vendored
    verdict = 'REFUTED' if not thm_in_vendored else 'HOLDS'
    corr = ('FACT CORRECTION TO THE WORK-ORDER (OPEN_TRAILS :12014, item (a)), recorded here and not to the module: the work-order names '
            '“the Alpöge–Furman proportion (at least 2/3 of ζ’s zeros simple and on the line)”. In the modules’ own words: (i) the '
            'vendored set holds the simple-on-the-line statement only as the Prop `Zeta23.ThmB_statement`, at the bound 1/2 '
            '(Zeta23/Statement.lean :198-:200), and proves no bound on `N0simple`; (ii) the bound 2/3 for zeros simple and on the line, '
            'counted against all zeros with multiplicity on the dyadic window (T, 2T], in the ε-form, is `Zeta23.thmB₀_mult` at the '
            'upstream pin (Zeta23/FinalMult.lean :350, “this is the paper’s [thm:B]; Zeta23/Final.lean has the Cauchy–Schwarz form '
            'with 1/2”, :348), outside the vendored set; (iii) the 2/3 that the vendored statement layer carries is Theorem A’s, '
            'DISTINCT zeros on the line (`ThmA_statement`, `N0star`), not simple ones; (iv) the modules attribute the work to “the '
            'paper” under Anthropic’s copyright, the upstream README names it “More than two thirds of the zeros of the Riemann zeta '
            'function lie on the critical line” (Claude; Anthropic, 2026), and the name Alpöge–Furman is the arXiv byline of '
            '2608.13637 (relay data/b468r_closing.txt :39-:41), whose text says the argument was discovered and written by Claude.')
    L += ['', '### (7) H29a -- “the proportion is in the vendored set by name”: %s. %s' % (
        verdict, 'No theorem of the proportion is in the vendored set by any name; its statement at 1/2 is there as a Prop, and the '
                 'theorem at 2/3 is upstream at Zeta23/FinalMult.lean :350.' if verdict == 'REFUTED' else 'present.'),
          '', '### (8) ' + corr]
    put_txt('b596_lemmas.txt', L)
    put_json('b596_lemmas.json', dict(modules=mods, hits_name={k: v for k, v in hits_name.items()}, hits_bound={k: v for k, v in hits_bound.items()},
                                      vendored=vend, upstream=['%s:%d' % (p, n) for p, n, _t in up_hits], upstream_stmt=fm[349:351],
                                      H29a=verdict, upstream_present=present, correction=corr))
    print('  modules %d ; H29a %s ; upstream %s' % (len(mods), verdict, ['%s:%d' % (p, n) for p, n, _t in up_hits]))


# ================================================================================ COMPONENT 3: THE PROP -- STATEMENTS, PRINTS, E0
DECL = re.compile(r'^(theorem|def|structure|noncomputable def|abbrev) (\S+)')


def _headers(text):
    ls = text.split(NL)
    out = []
    for i, l in enumerate(ls):
        m = DECL.match(l)
        if not m:
            continue
        h = [l]
        j = i
        while not re.search(r':=|\bwhere\b', ls[j]) and j + 1 < len(ls):
            j += 1
            h.append(ls[j])
        out.append(dict(kind=m.group(1), name=m.group(2), line=i + 1, head=NL.join(h)))
    return out


def statements(key, suffix=''):
    """### the statements of one kernel file as written in the working tree of the branch, printed before its build."""
    rel = KFILES[key]
    b = open(os.path.join(EFK, rel), 'rb').read()
    hs = _headers(b.decode('utf-8'))
    L = ['b596 -- THE STATEMENTS OF %s, PRINTED %s' % (rel, 'BEFORE THE BUILD' if not suffix else 'AGAIN AFTER THE FILE CHANGED (the first print kept beside)'), '']
    if suffix:
        first = {d['name']: d['head'] for d in jl('b596_statements_%s.json' % key)['decls']}
        now = {d['name']: d['head'] for d in hs}
        L += ['### against the first print: headers unchanged %s ; changed %s ; added %s ; gone %s' % (
            sorted(n for n in now if first.get(n) == now[n]), sorted(n for n in now if n in first and first[n] != now[n]),
            sorted(set(now) - set(first)), sorted(set(first) - set(now))), '']
    L += ['### written at (UTC) %s ; the branch %s (checked out: %s) ; the file`s sha256 %s ; its bytes %d' % (
        utc(), BRANCH, g(EFK, 'branch', '--show-current').strip(), sha(b), len(b)), '']
    for h in hs:
        L.append('### :%d %s %s' % (h['line'], h['kind'], h['name']))
        L += ['    ' + x for x in h['head'].split(NL)]
    put_txt('b596_statements_%s%s.txt' % (key, suffix), L)
    put_json('b596_statements_%s%s.json' % (key, suffix), dict(file=rel, sha256=sha(b), at=utc(), decls=hs))


def build_bank(key, logpath):
    """### the watchdog's build log copied into relay data/b596_build_<key>.txt with a head line."""
    src = io.open(logpath, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    hdr = ('### b596 -- COMPONENT 3: THE BUILD OF %s ON %s, ONE MODULE PER CALL, THE WATCHDOG`S LOG (lean resident cap 3500 MB, free '
           'floor 900 MB; the seat starts no call below the 2560 MB hold), copied from the seat`s scratchpad' % (key, BRANCH))
    put_txt('b596_build_%s.txt' % key.split('.')[-1].lower(), [hdr, ''] + src.rstrip(NL).split(NL))


def prints(logpath):
    """### the Lean output of the axiom-check run (the watchdog's log, its `  | ` lines), banked as data/b596_prints.txt / .json."""
    import b569_record as R9
    src = io.open(logpath, encoding='utf-8').read().replace(chr(13), '')
    out = [l[4:] for l in src.split(NL) if l.startswith('  | ')]
    ex = [l for l in src.split(NL) if l.startswith('### EXIT')]
    txt = NL.join(out)
    ax = R9.prints_axioms(txt)
    L = ['b596 -- THE PRINTS: `lake env lean %s` at SIDE-explicit-formula %s (checked out: %s, HEAD %s), the watchdog`s run' % (
        AXF, BRANCH, g(EFK, 'branch', '--show-current').strip(), g(EFK, 'rev-parse', '--short=7', 'HEAD').strip()),
         '### %s' % (ex[-1] if ex else '### NO EXIT LINE'), ''] + out
    put_txt('b596_prints.txt', L)
    put_json('b596_prints.json', dict(axioms=ax, sorry=[n for n, a in ax.items() if 'sorryAx' in a],
                                      std3=all(set(a) <= set(STD3) for a in ax.values()), exit=ex[-1] if ex else None,
                                      errors=sum(1 for l in out if ': error' in l or l.startswith('error')), text=txt))
    print('  prints', len(ax), 'std3', all(set(a) <= set(STD3) for a in ax.values()))


def e0(key):
    """### every declaration of one kernel file graded by the shared E0 rule (tools/e0_rule.py) at the branch tip, with its print."""
    import b569_record as R9
    import e0_rule as E0
    st = jl('b596_statements_%s_final.json' % key) if os.path.exists(os.path.join(D, 'b596_statements_%s_final.json' % key)) \
        else jl('b596_statements_%s.json' % key)
    P0 = jl('b596_prints.json')['axioms']
    tip = g(EFK, 'rev-parse', BRANCH).strip()
    src = g(EFK, 'show', '%s:%s' % (tip, st['file']))
    rows = {}
    L = ['b596 -- THE E0 READ OF %s AT THE BRANCH TIP %s (%s)' % (st['file'], tip[:7], BRANCH)] + E0.RULE_TEXT + [
        '### the file at the tip is the one printed before the build: %s' % (sha(src) == st['sha256']), '']
    for d in st['decls']:
        n = NS + ('SaltCheck.' if key == 'salt' else '') + d['name']
        kind = 'theorem' if d['kind'] == 'theorem' else 'def'
        head, _ln = R9.header_of(src, d['name'])
        gr, why, _b = E0.grade(head or '', kind)
        ax = P0.get(n)
        rows[n] = dict(grade=gr if kind == 'theorem' else 'DEF', why=why, axioms=ax, std3=ax is not None and set(ax) <= set(STD3), head=head, kind=kind)
        L.append('    %-34s %-10s %s  -- %s' % (d['name'], rows[n]['grade'], 'std3' if rows[n]['std3'] else ax, (why or '')[:140]))
    gate = all(r['std3'] for r in rows.values()) and all(r['head'] is not None or r['kind'] == 'def' for r in rows.values())
    L.append('### ### **THE GATE: %s** -- declarations %d, theorems %d (DERIVES %d, INTERFACES %d)' % (
        'PASS' if gate else 'FAIL', len(rows), sum(1 for r in rows.values() if r['kind'] == 'theorem'),
        sum(1 for r in rows.values() if r['grade'] == 'DERIVES'), sum(1 for r in rows.values() if r['grade'] == 'INTERFACES')))
    put_txt('b596_e0_%s.txt' % key, L)
    put_json('b596_e0_%s.json' % key, dict(rows=rows, gate=gate, tip=tip, file=st['file'], same_file=sha(src) == st['sha256']))


FED_PAT = r'zeroMult|analyticOrderAt|allSimple|Simplicity\.simplicity|\bsimplicity\b|multiplicit|\.mult\b'
OWN = ('SIDEExplicitFormula/Simplicity.lean', 'SIDEExplicitFormula/SaltCheckSimplicity.lean', 'AxiomCheckSimplicity.lean')


def _decl_heads(text):
    """### every theorem/lemma header (keyword to `:=`) of a file, with its line."""
    out = []
    for m in re.finditer(r'^[ \t]*(?:@\[[^\]]*\][ \t]*)?(?:(?:private|protected|nonrec)[ \t]+)*(theorem|lemma)[ \t]+(\S+)(.*?):=', text, re.M | re.S):
        out.append((text[:m.start()].count(NL) + 1, m.group(2), ' '.join((m.group(2) + m.group(3)).split())))
    return out


# ### the classifier, in two shapes. LOOSE: a conclusion naming the clause's equation or its Prop at all. STRICT: a conclusion that IS
# ### the clause (the Prop alone, or ∀ over the nontrivial zeros of zeroMult = 1) or its negation (¬ the Prop, or ∃ a nontrivial zero
# ### of multiplicity ≠ 1). A loose hit that is not strict is READ: printed with the seat's hand reading, and an unread one counts.
CLAUSE_RX = re.compile(r'(zeroMult\s*\S+\s*=\s*1|\bsimplicity\b|allSimple\s+zetaWeilConfig)')
NEG_RX = re.compile(r'(¬\s*\(?\s*(?:SIDEExplicitFormula\.)?(?:Simplicity\.)?simplicity|zeroMult\s*\S+\s*(?:≠\s*1|≥\s*2|>\s*1|=\s*2))')
STRICT_POS = re.compile(r'^\s*((SIDEExplicitFormula\.)?(Simplicity\.)?simplicity|allSimple\s+zetaWeilConfig|'
                        r'∀\s*\(?ρ[^,]*,\s*(Zeta23\.)?IsNontrivialZero\s+ρ\s*→\s*(Zeta23\.)?zeroMult\s+ρ\s*=\s*1)\s*$')
STRICT_NEG = re.compile(r'^\s*(¬\s*\(?\s*(SIDEExplicitFormula\.)?(Simplicity\.)?simplicity\s*\)?|'
                        r'∃\s*\(?ρ[^,]*,\s*(Zeta23\.)?IsNontrivialZero\s+ρ\s*∧\s*(Zeta23\.)?zeroMult\s+ρ\s*(≠\s*1|≥\s*2|>\s*1))\s*$')
def _strict_controls():
    """### each strict shape on a conclusion it must read and one it must not; RETURNS the four results (all True to pass)."""
    return dict(pos_reads=bool(STRICT_POS.search(' ∀ (ρ : ℂ), Zeta23.IsNontrivialZero ρ → Zeta23.zeroMult ρ = 1')),
                pos_refuses=not STRICT_POS.search(' (zetaZeros hs).simple = {ρ | zeroMult ρ = 1}'),
                neg_reads=bool(STRICT_NEG.search(' ∃ ρ, IsNontrivialZero ρ ∧ zeroMult ρ ≥ 2')),
                neg_refuses=not STRICT_NEG.search(' zetaZeroConfig.mult = zeroMult'))


HAND = {('Zeta23/Statement.lean', 'zetaZeros_simple'):
        'a set identity: the simple points of the configuration are {ρ | zeroMult ρ = 1}; it names the clause`s set and asserts no '
        'point in it or out of it'}


def h29b():
    """### H29b: the salt-check compiled at the standard three, and the federation searched (git grep at every kernel's HEAD) for a
    ### theorem whose header names the clause's constants; each hit classified CONCLUDES / NEGATES / OTHER on its conclusion (the
    ### header after its last top-level colon), the act's own files marked OWN. data/b596_h29b.txt / .json."""
    es, ep = jl('b596_e0_salt.json'), jl('b596_e0_simp.json')
    pr = jl('b596_prints.json')
    txt = pr['text']
    sat = es['rows'].get(NS + 'SaltCheck.allSimple_satisfiable', {})
    nf = es['rows'].get(NS + 'SaltCheck.allSimple_not_forced', {})
    rows, kernels, files = fed_walk()
    bad = [r for r in rows if r['cls'] in ('CONCLUDES', 'NEGATES') or (r['cls'] == 'READ' and not r['reading'])]
    chk = {}
    for n in ('allSimple_satisfiable', 'allSimple_not_forced'):
        i = txt.find(NS + 'SaltCheck.' + n + ' :')
        chk[n] = txt[i:i + 400].split(NL + NS)[0] if i >= 0 else ''
    salt = bool(sat.get('std3')) and bool(nf.get('std3')) and all(chk.values())
    clean = ep.get('gate') is True and es.get('gate') is True and not pr.get('sorry')
    verdict = 'HOLDS' if salt and clean and not bad else 'REFUTED'
    L = ['b596 -- COMPONENT 3: H29b, THE TITLE`S PROP SALT-CHECKED AND THE FEDERATION SEARCHED, (R206)(4)(b)', '',
         '### allSimple_satisfiable : %s -- a configuration of the schema, target held, Weil-positive on classK, a point, every point simple'
         % sat.get('axioms'),
         '### allSimple_not_forced : %s -- the same with a point of multiplicity two: the fields, the target and Weil positivity do not '
         'imply the clause' % nf.get('axioms')] + ['    ' + l for v in chk.values() for l in v.split(NL)] + [
         '### the E0 gates: Simplicity.lean %s, SaltCheckSimplicity.lean %s ; sorryAx in the prints: %s' % (ep.get('gate'), es.get('gate'), pr.get('sorry') or 'NONE'),
         '', '### THE FEDERATION WALK: git grep -E "%s" at HEAD of every kernel (%d), %d files; every theorem/lemma header naming a '
         'constant of the clause, its conclusion classified' % (FED_PAT, len(kernels), files)]
    for r in rows:
        L.append('    %-9s %s %s:%d %s -- %s' % (r['cls'], r['kernel'], r['file'], r['line'], r['name'], r['conclusion'][:160]))
        if r['cls'] == 'READ':
            L.append('              ### the seat`s hand reading: %s' % (r['reading'] or '### NONE -- COUNTED AGAINST H29b'))
    L += ['### headers %d ; CONCLUDES %d ; NEGATES %d ; READ %d (hand-read %d) ; OTHER %d ; OWN %d' % (
        len(rows), sum(r['cls'] == 'CONCLUDES' for r in rows), sum(r['cls'] == 'NEGATES' for r in rows), sum(r['cls'] == 'READ' for r in rows),
        sum(r['cls'] == 'READ' and bool(r['reading']) for r in rows), sum(r['cls'] == 'OTHER' for r in rows), sum(r['cls'] == 'OWN' for r in rows)),
          '### the strict shapes, each exercised: %s' % _strict_controls(),
          '', '### ### **H29b %s.**' % verdict]
    put_txt('b596_h29b.txt', L)
    put_json('b596_h29b.json', dict(H29b=verdict, satisfiable=sat, not_forced=nf, check=chk, rows=rows, kernels=kernels, files=files, bad=bad))
    print('  H29b', verdict, 'headers', len(rows), 'bad', len(bad))


def fed_walk():
    """### the federation walk: every kernel's HEAD, every theorem/lemma header naming a constant of the clause, its conclusion
    ### classified. RETURNS (rows, kernels, files)."""
    kernels = sorted(d for d in os.listdir('D:/') if d.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d, '.git')))
    rows, files = [], 0
    for k in kernels:
        rep = 'D:/' + k
        out = g(rep, 'grep', '-l', '-I', '-E', FED_PAT, 'HEAD', '--', '*.lean')
        for f in [x.split(':', 1)[1] for x in out.split(NL) if x.strip()]:
            files += 1
            t = g(rep, 'show', 'HEAD:' + f)
            for ln, name, head in _decl_heads(t):
                if not re.search(FED_PAT, head):
                    continue
                concl = head
                depth, cut = 0, -1
                for i, ch in enumerate(head):
                    if ch in '([{⟨':
                        depth += 1
                    elif ch in ')]}⟩':
                        depth -= 1
                    elif ch == ':' and depth == 0 and head[i:i + 2] != ':=':
                        cut = i
                concl = head[cut + 1:] if cut >= 0 else head
                own = k == 'SIDE-explicit-formula' and f in OWN
                if own:
                    cls = 'OWN'
                elif STRICT_NEG.search(concl):
                    cls = 'NEGATES'
                elif STRICT_POS.search(concl):
                    cls = 'CONCLUDES'
                elif NEG_RX.search(concl) or CLAUSE_RX.search(concl):
                    cls = 'READ'
                else:
                    cls = 'OTHER'
                rows.append(dict(kernel=k, file=f, line=ln, name=name, cls=cls, conclusion=concl[:300],
                                 reading=HAND.get((f, name)) if cls == 'READ' else None))
    return rows, kernels, files


# ================================================================================ COMPONENTS 3-4: THE NODE LISTS AND THE PAGES
NODE_HEAD = ['# b596 -- THE ζ NODE LIST AT v0.17, (R206)(4)(b): b592`s 25 records (relay data/b592_nodes.txt, every record line',
             '# unchanged) with the five declarations of SIDEExplicitFormula/Simplicity.lean appended, the pin moved to v0.17. Every cell is',
             '# elaborated by the generator`s probe at the pin, never typed here.', '#']
NODE_ADD = [NS + 'allSimple | kernel | added: (R206)(4)(b), the title`s clause over a configuration of the schema',
            NS + 'simplicity | kernel | added: (R206)(4)(b), the title`s clause over the genuine configuration',
            NS + 'simplicity_iff | kernel | added: (R206)(4)(b), the clause read as every nontrivial zero of multiplicity one',
            NS + 'SimpleProportion | kernel | added: (R206)(4)(b), the proportion as a named premise',
            NS + 'exceptional_mass_le_third | kernel | added: (R206)(4)(b), the proportion`s consequence at INTERFACES']
CHI_HEAD = ['# b596 -- THE χ NODE LIST AT v0.17, (R206)(4)(b): b592`s records (relay data/b592_nodes_chi.txt, every record line unchanged),',
            '# the pin moved to v0.17; the χ-leg gains no node. Every cell is elaborated by the generator`s probe at the pin.', '#']


def faces_line_text():
    return io.open(os.path.join(SP, 'faces_line.txt'), encoding='utf-8').read().strip()


def node_lists(*a):
    """### data/b596_nodes.txt and data/b596_nodes_chi.txt (Component 3); with `faces`, data/b596_nodes_faces.txt (Component 4):
    ### b596_nodes.txt with one `# backmatter:` record, the faces' line, appended."""
    if a and a[0] == 'faces':
        src = rd('b596_nodes.txt').rstrip(NL).split(NL)
        line = faces_line_text()
        out = ['# b596 -- COMPONENT 4, (R206)(4)(c): relay data/b596_nodes.txt, every line unchanged, with the faces` line as one',
               '# backmatter record (the generator`s channel, the author`s answer before b596`s seal).', '#'] + src + ['# backmatter: ' + line]
        put_txt('b596_nodes_faces.txt', out)
        return
    z = rd('b592_nodes.txt').rstrip(NL).split(NL)
    if z.count('# pin: v0.16') != 1:
        sys.exit('### b592`s ζ list does not carry its pin once -- NOTHING WRITTEN')
    put_txt('b596_nodes.txt', NODE_HEAD + [('# pin: v0.17' if l == '# pin: v0.16' else l) for l in z] + NODE_ADD)
    c = rd('b592_nodes_chi.txt').rstrip(NL).split(NL)
    if c.count('# pin: v0.16') != 1:
        sys.exit('### b592`s χ list does not carry its pin once -- NOTHING WRITTEN')
    put_txt('b596_nodes_chi.txt', CHI_HEAD + [('# pin: v0.17' if l == '# pin: v0.16' else l) for l in c])


def faces_line():
    """### (R206)(4)(c): the one line printed with its three citations, each read at its pin, before it is written."""
    line = faces_line_text()
    cites = [('SIDEExplicitFormula.B321.h2_sign_iff_rh', 'SIDEExplicitFormula/Seam.lean', 'v0.2'),
             ('SIDEExplicitFormula.LiCriterionBridge.li_nonneg_iff_rh', 'SIDEExplicitFormula/LiCriterionBridge.lean', 'v0.9'),
             ('SIDEExplicitFormula.LiCriterionBridge.arith_limit_nonneg_iff_rh', 'SIDEExplicitFormula/LiCriterionBridge.lean', 'v0.9')]
    L = ['b596 -- COMPONENT 4: THE FACES` LINE, (R206)(4)(c), PRINTED WITH ITS THREE CITATIONS BEFORE IT IS WRITTEN (UTC %s)' % utc(), '',
         '### the line:', '    ' + line, '', '### its three citations, each read at its pin (git grep of the declaration line):']
    ok = True
    for full, rel, tag in cites:
        short = full.split('.')[-1]
        pin = g(EFK, 'rev-parse', '--short=7', tag + '^{commit}').strip()
        hit = [l for l in g(EFK, 'grep', '-n', '-E', r'^theorem %s\b' % re.escape(short), tag, '--', rel).split(NL) if l.strip()]
        inline = ('`%s`' % short) in line and pin in line
        ok = ok and bool(hit) and inline
        L.append('    %s at %s = %s : %s ; named in the line with its pin: %s' % (short, tag, pin, hit, inline))
    L += ['', '### ### **%s**' % ('THE THREE CITATIONS READ AT THEIR PINS AND NAMED IN THE LINE' if ok else '### A CITATION NOT READ OR NOT NAMED')]
    put_txt('b596_faces_line.txt', L)
    put_json('b596_faces_line.json', dict(line=line, ok=ok, sha256=sha(line)))
    for l in L:
        print(l[:240])


def pages(stage):
    """### the pages re-emitted by relay tools/chain_page.py. `c3`: both at v0.17 from data/b596_nodes.txt and data/b596_nodes_chi.txt,
    ### full runs (the probe banked: data/b596_probe_out.txt, data/b596_chi_probe_out.txt, and their .lean.txt); `c4`: the ζ page from
    ### data/b596_nodes_faces.txt, re-emitted from the banked ζ probe. Writes the PLACE-papers pages and data/b596_pages_<stage>.json."""
    import shutil
    import chain_page as C
    res = {}
    plan = [('zeta', 'b596_nodes.txt', PAGE, None), ('chi', 'b596_nodes_chi.txt', DIR_PAGE, None)] if stage == 'c3' else \
        [('zeta', 'b596_nodes_faces.txt', PAGE, os.path.join(D, 'b596_probe_out.txt'))]
    for k, nodes, page, frm in plan:
        pdir = os.path.join(SP, '_b596_%s_%s' % (stage, k))
        rc, pg, meta, log = C.build(os.path.join(D, nodes), pdir, frm)
        res[k] = dict(rc=rc, log=log, nodes=nodes)
        if rc == 0:
            b = pg.encode('utf-8')
            out = os.path.join(PP, page)
            open(out + '.tmp', 'wb').write(b)
            os.replace(out + '.tmp', out)
            res[k].update(bytes=len(b), sha256=sha(b), order=meta['order'],
                          new=[dict(name=n, grade=meta['cells'][n]['grade'], tier=meta['cells'][n].get('tier'), premises=meta['cells'][n].get('premises'),
                                    axioms=meta['cells'][n].get('axioms'), entry=meta['cells'][n].get('entry'))
                               for n in NEW_NODES if n in meta['cells']])
            if frm is None:
                po = 'b596_probe_out.txt' if k == 'zeta' else 'b596_chi_probe_out.txt'
                shutil.copyfile(os.path.join(pdir, 'chain_page_probe_out.txt'), os.path.join(D, po))
                shutil.copyfile(os.path.join(pdir, 'chain_page_probe.lean'), os.path.join(D, po.replace('_out.txt', '.lean.txt')))
        for l in log:
            print('  %s: %s' % (k, l))
        print('  %s: exit %d %s' % (k, rc, res[k].get('bytes', '')))
        for x in res[k].get('new', []):
            print('    NEW NODE %s -- %s ; tier %s ; premises %s' % (x['name'], x['grade'], x['tier'], x['premises']))
    put_json('b596_pages_%s.json' % stage, res)


def page_arms(stage):
    """### both page arms at PLACE-papers HEAD from this act's lists and probes, and b592's lists against the pre-act page blobs."""
    import g_chain_page as GCP
    zl = 'b596_nodes_faces.txt' if stage == 'c4' else 'b596_nodes.txt'
    L = ['b596 -- THE PAGE ARMS AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), stage)]
    n = 0
    for arm, nodes, probe, com in (('G-CHAIN-PAGE', zl, 'b596_probe_out.txt', None), ('G-CHAIN-PAGE-CHI', 'b596_nodes_chi.txt', 'b596_chi_probe_out.txt', None),
                                   ('G-B592-LISTS-CONTROL (ζ)', 'b592_nodes.txt', 'b592_probe_out.txt', PAGE),
                                   ('G-B592-LISTS-CONTROL (χ)', 'b592_nodes_chi.txt', 'b592_chi_probe_out.txt', DIR_PAGE)):
        committed = None if com is None else subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (PRE_PP, com)], capture_output=True).stdout
        r = GCP.arm(os.path.join(D, nodes), os.path.join(SP, '_b596_gcp'), os.path.join(D, probe), committed=committed)
        ok = r.get('ok') is True
        n += ok
        L.append('  %s : %s' % (arm, 'PASS' if ok else 'FAIL %s' % {k: v for k, v in r.items() if k != 'ok'}))
    L.append('### PAGE ARMS PASSING : %d of 4' % n)
    put_txt('b596_page_arms_%s.txt' % stage, L)
    for l in L:
        print(l[:220])


# ================================================================================ COMPONENT 5: THE READING
def reading():
    """### SIMPLICITY's tier block and work-list read line by line against (a)-(c); the marked sentences from SP/reading.json
    ### (the seat's line-by-line reading, each row: line, sentence, mover (a)/(b)/(c), the citation), each row checked against the
    ### document at its pin (the quoted sentence must sit on the cited line); data/b596_simplicity_reading.txt / .json; H29c."""
    R = json.load(io.open(os.path.join(SP, 'reading.json'), encoding='utf-8'))
    doc = g(PP, 'show', '%s:%s' % (PRE_PP, SIMP)).split(NL)
    tb0 = [i for i, l in enumerate(doc, 1) if l.startswith('#### THE CASCADE, ACT EIGHT')]
    tb = (tb0[0], len(doc)) if len(tb0) == 1 else (0, 0)
    L = ['b596 -- COMPONENT 5: SIMPLICITY_OF_RIEMANN_ZEROS READ AGAINST (a)-(c), (R206)(4)(d) -- THE EDITION`S WORK-LIST ADDENDUM, NOT AN EDITION',
         '### the document: PLACE-papers %s @ %s (%d lines), the current version, unedited; its tier block :%d-:%d; its work-list relay '
         'data/b558_editions/SIMPLICITY_OF_RIEMANN_ZEROS.txt (5 sentence-rows, 4 lines). The movers: (a) the proportion -- Zeta23.thmB₀_mult at '
         'the upstream pin (FinalMult.lean :350), not vendored, premised at v0.17 as SimpleProportion (relay data/b596_lemmas.txt); (b) the '
         'Prop -- simplicity at v0.17, salt-checked (data/b596_h29b.txt); (c) the faces` silence -- the line of data/b596_faces_line.txt.'
         % (SIMP, PRE_PP, len(doc), tb[0], tb[1]), '']
    ok_rows, rows = 0, []
    for r in R['rows']:
        ln = r['line']
        here = doc[ln - 1] if 0 < ln <= len(doc) else ''
        found = r['quote'] in here
        intb = tb[0] <= ln <= tb[1]
        ok_rows += found
        rows.append(dict(r, found=found, in_tier_block=intb))
        L += [':%d -- MOVED-IN-MEANING by %s%s' % (ln, r['mover'], ' (in the tier block)' if intb else ''),
              '    the sentence: "%s"%s' % (r['quote'], '' if found else '   ### NOT ON THE CITED LINE'),
              '    what moves: %s' % r['why'], '    it will cite: %s' % r['cite'], '']
    L += ['### THE TIER BLOCK, READ LINE BY LINE (:%d-:%d): %s' % (tb[0], tb[1], R['tier_block_note']), '',
          '### THE WORK-LIST, READ LINE BY LINE: %s' % R['worklist_note'], '']
    by = {}
    for r in rows:
        by[r['mover']] = by.get(r['mover'], 0) + 1
    tb_a = [r for r in rows if r['in_tier_block'] and '(a)' in r['mover']]
    h29c = 'HOLDS' if tb_a else 'REFUTED'
    L += ['### marked %d (%s) ; on their cited lines %d ; in the tier block %d, by the proportion %d' % (
        len(rows), ', '.join('%s %d' % kv for kv in sorted(by.items())), ok_rows, sum(r['in_tier_block'] for r in rows), len(tb_a)),
          '### ### **H29c %s** -- the tier block carries %s sentence the proportion makes MOVED-IN-MEANING.' % (h29c, 'a' if tb_a else 'no')]
    put_txt('b596_simplicity_reading.txt', L)
    put_json('b596_simplicity_reading.json', dict(rows=rows, tier_block=tb, H29c=h29c, by=by, all_found=ok_rows == len(rows),
                                                  tier_block_note=R['tier_block_note'], worklist_note=R['worklist_note']))
    print('  marked %d ; found %d ; H29c %s' % (len(rows), ok_rows, h29c))


def held_line():
    """### PLACE-papers OPEN_TRAILS: the HELD mark at the edition order (:12026) lifted if H29b holds, kept with the cause otherwise."""
    Q = _Q()
    p = Q.line_of(Q.OT, HELD_LINE)
    if p != 12026:
        sys.exit('### THE ADDRESSED LINE MOVED: %s -- NOTHING WRITTEN' % p)
    hb = jl('b596_h29b.json')['H29b']
    head = ('*Appended 2026-10-02 by b596 to SIMPLICITY’s HELD mark (:%d), under `(R206)`(5) -- %s:*' % (
        p, 'THE HOLD LIFTED' if hb == 'HOLDS' else 'THE HOLD KEPT'))
    Q.guard_absent(Q.OT, head)
    if hb == 'HOLDS':
        text = ('\n%s `W-ORD-SIMPLICITY-FACE` (:12012) has landed at b596 and H29b holds (relay data/b596_h29b.txt): SIMPLICITY_OF_RIEMANN_ZEROS’ '
                'edition is released from HELD and is b597’s, by the form, from its tier block, its work-list and the b596 addendum '
                '(relay data/b596_simplicity_reading.txt).\n' % head)
    else:
        text = ('\n%s H29b is refuted (relay data/b596_h29b.txt); SIMPLICITY_OF_RIEMANN_ZEROS’ edition stays HELD, the cause printed '
                'there.\n' % head)
    r = Q.append_to(Q.OT, text)
    put_json('b596_held_line.json', dict(line=Q.line_of(Q.OT, head), head=head, append=r, H29b=hb))
    print('  held line :%s' % Q.line_of(Q.OT, head))


# ================================================================================ THE SCORES AND THE RECORD
SCORE_KEYS = ('H29a', 'H29b', 'H29c', 'N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')


def scores():
    """### every hypothesis and expectation scored on its bank, by its letter; data/b596_scores.json."""
    W, Hb, Rd = jl('b596_lemmas.json'), jl('b596_h29b.json'), jl('b596_simplicity_reading.json')
    E1, E2 = jl('b596_e0_simp.json'), jl('b596_e0_salt.json')
    P3, P4 = jl('b596_pages_c3.json'), jl('b596_pages_c4.json')
    pa3, pa4 = rd('b596_page_arms_c3.txt'), rd('b596_page_arms_c4.txt')
    em = E1['rows'].get(NS + 'exceptional_mass_le_third', {})
    si = E1['rows'].get(NS + 'simplicity_iff', {})
    S = {}
    S['H29a'] = (W['H29a'], 'relay data/b596_lemmas.txt (7): the vendored set holds the simple-on-the-line statement only as the Prop '
                            'ThmB_statement at 1/2; the theorem at 2/3 is Zeta23.thmB₀_mult, upstream at FinalMult.lean :350')
    S['H29b'] = (Hb['H29b'], 'relay data/b596_h29b.txt: the salt-check`s two theorems at the standard three; %d federation headers '
                             'naming the clause`s constants, CONCLUDES or NEGATES %d' % (len(Hb['rows']), len(Hb['bad'])))
    S['H29c'] = (Rd['H29c'], 'relay data/b596_simplicity_reading.txt: in the tier block, rows marked by the proportion %d' % sum(
        1 for r in Rd['rows'] if r['in_tier_block'] and '(a)' in r['mover']))
    S['N1'] = ('HELD' if W['H29a'] == 'HOLDS' else 'REFUTED', 'H29a %s; the vendored statement`s bound for simple zeros on the line is 1/2, '
                                                            'the work-order`s 2/3 is upstream`s (data/b596_lemmas.txt (8))' % W['H29a'])
    n2 = Hb['H29b'] == 'HOLDS' and not jl('b596_prints.json').get('sorry')
    S['N2'] = ('HELD' if n2 else 'REFUTED', 'the salt-check compiled at the standard three, no sorryAx, the walk`s CONCLUDES/NEGATES %d' % len(Hb['bad']))
    zeta_new = {x['name']: x['grade'] for x in P3.get('zeta', {}).get('new', [])}
    n3 = em.get('grade') == 'INTERFACES' and zeta_new.get(NS + 'exceptional_mass_le_third') == 'INTERFACES'
    S['N3'] = ('HELD' if n3 else 'REFUTED', 'the node carrying the proportion, exceptional_mass_le_third, E0 %s at the branch tip and %s on '
                                            'the page; the clause`s own nodes DEF (allSimple, simplicity, SimpleProportion) and the check '
                                            'simplicity_iff %s' % (em.get('grade'), zeta_new.get(NS + 'exceptional_mass_le_third'), si.get('grade')))
    n4 = len(Rd['rows']) >= 3 and any('(c)' in r['mover'] for r in Rd['rows'])
    S['N4'] = ('HELD' if n4 else 'REFUTED', 'marked %d, by the faces` silence %d' % (len(Rd['rows']), sum('(c)' in r['mover'] for r in Rd['rows'])))
    S['N5'] = ('REFUTED', 'in its letter: the generator edit (relay tools/chain_page.py and its test) is a file beyond its list, by the '
                          'author`s answer before the seal (the cause the navigator`s); the salt-check and axiom-check files are the house '
                          'form`s; nothing deposits, no main kernel file edited outside the merge, no current version edited')
    S['S1'] = ('HELD' if W['H29a'] == 'REFUTED' else 'REFUTED', 'H29a %s' % W['H29a'])
    s2 = E1.get('gate') and E2.get('gate') and em.get('grade') == 'INTERFACES' and si.get('grade') == 'DERIVES' and not jl('b596_prints.json').get('sorry')
    S['S2'] = ('HELD' if s2 else 'REFUTED', 'gates %s/%s; exceptional_mass_le_third %s; simplicity_iff %s' % (E1.get('gate'), E2.get('gate'), em.get('grade'), si.get('grade')))
    S['S3'] = ('HELD' if Hb['H29b'] == 'HOLDS' else 'REFUTED', 'H29b %s' % Hb['H29b'])
    S['S4'] = ('HELD' if Rd['H29c'] == 'REFUTED' and any(r['line'] == 24 and '(a)' in r['mover'] for r in Rd['rows']) else 'REFUTED',
               'H29c %s; the Abstract`s :24 marked by the proportion: %s' % (Rd['H29c'], any(r['line'] == 24 and '(a)' in r['mover'] for r in Rd['rows'])))
    s5 = len(P3.get('zeta', {}).get('new', [])) == 5 and P3.get('zeta', {}).get('rc') == 0 and P3.get('chi', {}).get('rc') == 0 \
        and P4.get('zeta', {}).get('rc') == 0 and 'PAGE ARMS PASSING : 4 of 4' in pa3 and 'PAGE ARMS PASSING : 4 of 4' in pa4
    S['S5'] = ('HELD' if s5 else 'REFUTED', 'ζ new nodes %d; exits c3 %s/%s, c4 %s; page arms c3 %s, c4 %s' % (
        len(P3.get('zeta', {}).get('new', [])), P3.get('zeta', {}).get('rc'), P3.get('chi', {}).get('rc'), P4.get('zeta', {}).get('rc'),
        'PAGE ARMS PASSING : 4 of 4' in pa3, 'PAGE ARMS PASSING : 4 of 4' in pa4))
    put_json('b596_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %-8s %s' % (k, S[k][0], S[k][1][:200]))


TITLE = ('## W-ORD-SIMPLICITY-FACE: the proportion of simple zeros walked in the vendored set and found upstream; the simplicity '
         'clause as a salt-checked Prop at v0.17; the three faces’ silence on multiplicity on the page; SIMPLICITY’s sentences marked '
         'for its edition')
TRAIL_HEAD = ('### b596 — lane three, act twenty-three under (R206): W-ORD-SIMPLICITY-FACE -- the proportion walked, the clause as a '
              'salt-checked Prop at v0.17, the faces’ silence on the page, SIMPLICITY read for its edition')


def _pp_commits():
    return [l.split(' ', 1) for l in g(PP, 'log', '--reverse', '--format=%h %s', PRE_PP + '..HEAD').split(NL) if l.strip()]


def findings():
    Q = _Q()
    S, wl, rl, Hb, Rd = jl('b596_scores.json'), jl('b596_weight_line.json'), jl('b596_rule_lines.json'), jl('b596_h29b.json'), jl('b596_simplicity_reading.json')
    hl = jl('b596_held_line.json')
    Q.guard_absent(Q.FIND, TITLE[:90])
    tag = g(EFK, 'rev-parse', '--short=7', TAG + '^{commit}').strip()
    e = ['', TITLE, '',
         '*Filed at b596 on the author’s ruling `(R206)`. Banks: relay `data/b596_lemmas.txt`, `data/b596_h29b.txt`, `data/b596_prints.txt`, '
         '`data/b596_faces_line.txt`, `data/b596_simplicity_reading.txt`, `data/b596_author_answers.txt`. Nothing deposits.*', '',
         '**The walk** (`(R206)`(4)(a)): the vendored Zeta23 set (57 modules at `3635e748`) holds the proportion of simple zeros on the line '
         'only as the Prop `Zeta23.ThmB_statement`, at the bound 1/2; the theorem at 2/3 -- `(2/3 − ε)·N(T,2T) ≤ N₀ˢ(T,2T)` for all large '
         'T, counted with multiplicity -- is `Zeta23.thmB₀_mult`, upstream at `Zeta23/FinalMult.lean` :350, outside the vendored set. '
         'H29a %s. The work-order’s words are corrected in the bank, not the module.' % S['H29a'][0], '',
         '**The Prop** (`(R206)`(4)(b)): SIDE-explicit-formula `SIDEExplicitFormula/Simplicity.lean`, %s = `%s`: `simplicity`, every '
         'nontrivial zero of `riemannZeta` of multiplicity one over the genuine configuration (`zetaWeilConfig`), `simplicity_iff` its '
         'check; the proportion beside it as the named premise `SimpleProportion` and `exceptional_mass_le_third` at INTERFACES on it. '
         'The salt-check (`SaltCheckSimplicity.lean`): a configuration of the schema with its target held and Weil-positive holds the '
         'clause, and another with a point of multiplicity two does not. The federation walk found %d headers naming the clause’s '
         'constants, none concluding the clause or its negation. H29b %s.' % (TAG, tag, len(Hb['rows']), S['H29b'][0]), '',
         '**The faces’ line** (`(R206)`(4)(c)): on the ζ page after its Correspondence table, through the generator’s node list (relay '
         'tools/chain_page.py, the `# backmatter:` channel, the author’s answer before the seal).', '',
         '**The reading** (`(R206)`(4)(d)): %d sentences of SIMPLICITY_OF_RIEMANN_ZEROS marked MOVED-IN-MEANING; H29c %s. The edition’s '
         'HELD mark: OPEN_TRAILS :%d.' % (len(Rd['rows']), S['H29c'][0], hl['line']), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the walk re-reads b468’s reading of the paper (relay '
         'data/b468r_closing.txt :39-:41) against the vendored modules; the Prop re-reads FINDINGS :5778 (the title’s reduction '
         'compiled in neither direction) and is stated over the schema of :6356, salt-checked in the form of :6740; the faces’ line '
         're-reads the equivalences of :4595 and :6194 for what they carry; the reading re-reads b554’s tier block (:5788) and '
         'b558’s work-list (:5990), and is re-read by b597’s edition. It strengthens one of the programme’s offerings: the compiled '
         'separation of what the faces state from what they are silent on.', '',
         '**The record lines.** b595’s weight at FINDINGS :%d; the seat’s items and the batch-refresh standing line at OPEN_TRAILS :%d, '
         ':%d; W-ORD-QUANTIFIER-COLUMN at :%d.' % (wl['line'], rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][2]['line']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Next.** Per `(R206)`(5): b597, SIMPLICITY’s edition by the form, %s; then one CP-1b act over SILENCE_STAGES and '
         'REPARAMETERIZATION; then the research sequence of `(R204)`(3)(i) from REMAINDER 5. The author rules on the closing.' % (
             'released from HELD' if S['H29b'][0] == 'HOLDS' else 'held with the cause printed'), '',
         '*Nothing deposits; README, REGISTRY and ERRATA unwritten; no current version edited; nothing here is a statement about RH or any '
         'zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b596_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE[:90]), title=TITLE, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, TITLE[:90]))


def trail():
    Q = _Q()
    S, fj, wl, rl, hl = jl('b596_scores.json'), jl('b596_findings.json'), jl('b596_weight_line.json'), jl('b596_rule_lines.json'), jl('b596_held_line.json')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    tag = g(EFK, 'rev-parse', '--short=7', TAG + '^{commit}').strip()
    rows_ = ['', TRAIL_HEAD, '',
             '**(R206) ratified.** (1) b595 at its weight. (2) The seat’s three items. (3) W-ORD-QUANTIFIER-COLUMN. (4) W-ORD-SIMPLICITY-FACE, '
             'items (a)-(d), H29a-H29c. (5) The acts after: b597.', '',
             '**Entered:** FINDINGS.md:%d (b595’s weight), :%d (the entry); OPEN_TRAILS.md:%d (the seat’s items), :%d (the batch refresh, '
             'standing), :%d (W-ORD-QUANTIFIER-COLUMN), :%d (SIMPLICITY’s HELD mark), this record; the two pages re-emitted at %s, the ζ '
             'page again with the faces’ line, each alone; SIDE-explicit-formula %s = `%s` (Simplicity.lean, SaltCheckSimplicity.lean, '
             'AxiomCheckSimplicity.lean); relay tools/chain_page.py (the backmatter channel) with its test; TECHNE-Core '
             'DELIBERATION_TREE.md, one sentence in section (v), alone, not pushed.' % (
                 wl['line'], fj['entry_line'], rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][2]['line'], hl['line'], TAG, TAG, tag), '',
             '**Answered before the seal, by the author** (relay data/b596_author_answers.txt): the faces’ line through a minimal generator '
             'edit, a `# backmatter:` record emitted after the Correspondence table, a list without one regenerating byte for byte; the seat '
             'waits at the 2,560 MB hold before every Lean call. **Answered after the pages’ first re-emission** (prompt 3): a '
             'structure’s entry tag added to the generator commit (entry_tag’s own pattern; DECL untouched), so the page prints '
             'SimpleProportion at v0.17; G-GEN-EDIT and G-ANSWERS-BANKED refuted in their letter by it, the cause the navigator’s -- '
             'the write list priced the generator edit as the back-matter channel alone without reading that the named premise would '
             'enter the page as a structure. **Recorded as the navigator’s:** (R206)(4)(c)’s entry “through the '
             'generator’s node list” without reading that chain_page.py carried no back-matter channel, the write list omitting the '
             'generator; the work-order’s “Alpöge–Furman, at least 2/3 … simple and on the line” as the vendored set’s (a fact correction, '
             'relay data/b596_lemmas.txt (8)).', '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R206)`(5), b597, SIMPLICITY_OF_RIEMANN_ZEROS’ edition by the form from its tier block, its work-list and the '
             'b596 addendum; then one CP-1b act over SILENCE_STAGES and REPARAMETERIZATION; then the research sequence from REMAINDER 5; the '
             'author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; ERRATA untouched; FACES_LEDGER untouched; row U1 unedited; `h2` where the '
             'deposit left it; the four lists stay OPEN.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b596_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b596_trail.json')['line'])


def desk():
    S = jl('b596_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    HK = ('H29a', 'H29b', 'H29c')
    L = ['=' * 104, 'b596 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H29a-H29c.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HK]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)),
          '### ### **' + ' ; '.join('%s %s' % (k, S[k][0]) for k in HK) + '.**', '']
    L += rd('b596_defects.txt').rstrip(NL).split(NL)
    put_txt('b596_desk_notes.txt', L)


def components():
    S, fj, tj, wl, rl, hl = (jl('b596_scores.json'), jl('b596_findings.json'), jl('b596_trail.json'), jl('b596_weight_line.json'),
                             jl('b596_rule_lines.json'), jl('b596_held_line.json'))
    tag = g(EFK, 'rev-parse', '--short=7', TAG + '^{commit}').strip()
    L = ['b596 -- THE COMPONENTS, BANKED UNDER (R206).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b595`s closing push-out relay %s ; push-b595* branches deleted by name '
         '(data/b596_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b596_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b595`s weight FINDINGS :%d ; the seat`s items OPEN_TRAILS :%d ; the batch refresh :%d ; W-ORD-QUANTIFIER-COLUMN '
         ':%d ; the tree`s sentence (TECHNE-Core, alone, not pushed)' % (wl['line'], rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][2]['line']),
         '### COMPONENT 2 : the walk (data/b596_lemmas.txt) ; H29a %s' % S['H29a'][0],
         '### COMPONENT 3 : SIDE-explicit-formula %s = %s ; the salt-check and the prints ; the pages re-emitted ; H29b %s' % (TAG, tag, S['H29b'][0]),
         '### COMPONENT 4 : the faces` line on the ζ page through the generator`s backmatter channel (data/b596_faces_line.txt)',
         '### COMPONENT 5 : the reading (data/b596_simplicity_reading.txt) ; the HELD mark OPEN_TRAILS :%d ; H29c %s' % (hl['line'], S['H29c'][0]),
         '### COMPONENT 6 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b597 SIMPLICITY`s edition ; N1 %s, N2 %s, N3 %s, '
         'N4 %s, N5 %s' % (fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b596_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b596_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
