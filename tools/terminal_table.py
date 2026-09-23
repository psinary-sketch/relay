# -*- coding: utf-8 -*-
"""terminal_table.py -- (R107) K0. ### **THE TERMINAL TABLE, GENERATED.**

### ### **AN INSTRUMENT OUTPUT, NOT A TRACKING DOCUMENT.** ### (R107): regenerated at every close
### by the closing suite, filed under `relay/data`, cited by keystones as a bank, ### **AND NO PROSE
### LIVES IN IT.**
###
### ### **IT CONFERS NO GRADE AND MOVES NONE.** ### Every grade is READ from a ledger cell and
### carried with the act and line that wrote it. ### Where two cells grade one name differently the
### row records `CONFLICT` and quotes BOTH ### **WITHOUT CHOOSING** -- a table that resolves a
### disagreement has conferred a grade.
###
### ### **EVERY REPOSITORY IS READ AS COMMITTED BLOBS THROUGH `git show`, NEVER THROUGH THE WORKING
### ### TREE.** ### A dirty working file is not what a pin cites.
###
### This module is SHARED and not act-stemmed, because (R107) has the closing suite re-run it.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D = os.path.join(ROOT, 'data')
DRIVE = os.path.join('D:', os.sep)
PP = os.path.join(DRIVE, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join(DRIVE, 'SIDE-global-section')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### ### **THE MATCHER IS b378's, IMPORTED AND NOT COPIED.** ### b435: a cure in one tool is not a
# ### guard; a matcher COPIED is a matcher that drifts from the fixtures that prove it.
import b378_terminals as B378          # noqa: E402

GRADES = ('DERIVES', 'INTERFACES', 'SHELL', 'ENCODES-CONCLUSION', 'ENCODES')
# ### **THE LONGER NAME FIRST**, or `ENCODES` swallows every `ENCODES-CONCLUSION`.
GRADE_RE = re.compile(r'\b(DERIVES|INTERFACES|SHELL|ENCODES-CONCLUSION|ENCODES)\b')
NAME_RE = re.compile(r'`([A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*)`')
PRINT_SRC = re.compile(r'^[ \t]*#print[ \t]+axioms[ \t]+([A-Za-z_][A-Za-z0-9_.\u2019\']*)',
                       re.M)
# ### the captured-stdout dialect: `'Name' does not depend on any axioms`
# ###                          or `'Name' depends on axioms: [propext, ...]`
PRINT_OUT = re.compile(r"^'([A-Za-z_][A-Za-z0-9_.]*)'[ \t]+(does not depend on any axioms"
                       r"|depends on axioms:.*)$", re.M)
ARTEFACT = re.compile(r'(?:^|/)(AxiomCheck[^/]*\.lean|PrintAxioms[^/]*\.lean|'
                      r'[^/]*AxiomCheck[^/]*\.lean|AXIOM_PRINTS[^/]*\.txt)$')
ACT_RE = re.compile(r'\bb(\d{2,4})\b')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True,
                          text=True, encoding='utf-8', errors='replace')


def gs(repo, *a):
    return git(repo, *a).stdout.replace(chr(13), '').strip()


# ### ### **THE TREE IS FETCHED ONCE PER (repo, ref) AND HELD.** ### The first version called
# ### `git show` per file per name: 44 repositories x ~700 ledger names x hundreds of files is
# ### hundreds of thousands of processes, and it did not finish. ### **A CORRECT INSTRUMENT THAT
# ### ### CANNOT COMPLETE IS NOT AN INSTRUMENT**, so the whole tree comes back in ONE `git archive`
# ### and every later read is a dictionary lookup. ### The bytes are still THE COMMITTED BYTES --
# ### the working tree is never consulted.
_TREE = {}


def tree(repo, ref):
    key = (repo, ref)
    if key in _TREE:
        return _TREE[key]
    import tarfile
    import io as _io
    out = {}
    r = subprocess.run(['git', '-C', repo, 'archive', '--format=tar', ref],
                       capture_output=True)
    if r.returncode == 0:
        try:
            with tarfile.open(fileobj=_io.BytesIO(r.stdout)) as tf:
                for m in tf.getmembers():
                    if not m.isfile():
                        continue
                    if not (m.name.endswith('.lean') or m.name.endswith('.txt')
                            or m.name.endswith('.md')):
                        continue
                    if m.size > 4000000:
                        continue
                    f = tf.extractfile(m)
                    if f is not None:
                        out[m.name] = f.read().decode('utf-8', 'replace').replace(chr(13), '')
        except Exception:
            out = {}
    _TREE[key] = out
    return out


def blob(repo, ref, path):
    """### ### **THE FILE AS COMMITTED AT A REF.** ### Never the working tree."""
    return tree(repo, ref).get(path)


def kernels():
    """### ### **THE ROSTER, ON DISK.** ### b378's predicate, and BOTH figures printed."""
    named = sorted(n for n in os.listdir(DRIVE) if n.startswith('SIDE-'))
    withgit = [(n, os.path.join(DRIVE, n)) for n in named
               if os.path.isdir(os.path.join(DRIVE, n, '.git'))]
    return named, withgit


# =====================================================================================================
# ### THE LEDGERS
# =====================================================================================================
def ledger_files():
    """### ### **EVERY LEDGER, INCLUDING THE ARCHIVE'S SPLIT LOOMS.** ### b494 found the 2026-07-26
    ### census in the archive, not the live loom: ### **A SPLIT MOVES A LEDGER, IT DOES NOT RETIRE
    ### IT**, and a reader that lists only the live files reads a truncated record."""
    out = []
    for n in ('REGISTRY.md', 'FINDINGS.md', 'VERIFICATION_LOOM.md', 'OPEN_TRAILS.md',
              'CASCADE_ANCHORS_CORRECTED.md', 'FACES_LEDGER.md'):
        p = os.path.join(PP, n)
        if os.path.exists(p):
            out.append(('PLACE-papers/' + n, p))
    out.append(('SIDE-global-section/CORRESPONDENCE.md', os.path.join(SIDE, 'CORRESPONDENCE.md')))
    arch = os.path.join(PP, 'archive')
    for dirpath, _, files in os.walk(arch):
        for f in sorted(files):
            if f.endswith('.md'):
                p = os.path.join(dirpath, f)
                out.append(('PLACE-papers/' + os.path.relpath(p, PP).replace(os.sep, '/'), p))
    return out


# ### ### **A MENTION IS NOT A GRADE CELL, AND THE FIRST MATCHER COULD NOT TELL THEM APART.**
# ### Version 1 took ANY LINE carrying a grade word and EVERY backticked name on it. ### These
# ### ledgers carry 2,000-character re-grade paragraphs that name a dozen keystones and use three
# ### grade words about DIFFERENT ones; version 1 paired every name with every grade on the line
# ### and reported ### **67 CONFLICTS**, of which the two read by hand were both artefacts --
# ### `identity_formation_bijection` "conflicting" because a paragraph mentioning it elsewhere
# ### says DERIVES about `CLASS_NUMBER_ANOMALY`.
# ### ### **BOTH YIELDS ARE PRINTED** (b381's lineage rule: never replace a matcher silently).
WINDOW = 120


def _names_on(ln):
    out = []
    for m in NAME_RE.finditer(ln):
        nm = m.group(1)
        if '.' not in nm and not re.search(r'[a-z]_[a-z]', nm) and len(nm) < 6:
            continue              # ### a bare short token is a word, not a terminal name
        if nm.endswith(('.md', '.json', '.lean', '.toml', '.txt', '.py')):
            continue
        out.append((m.start(), m.end(), nm))
    return out


def _segments(ln):
    """### ### **A TABLE ROW IS A ROW OF CELLS, AND A CELL IS THE UNIT THE ORDER NAMES.**
    ### Splitting on `|` keeps a grade in column 5 from reaching a name in column 2."""
    if ln.lstrip().startswith('|'):
        off, out = 0, []
        for part in ln.split('|'):
            out.append((off, part))
            off += len(part) + 1
        return out
    return [(0, ln)]


def grade_cells_v3():
    """### ### **VERSION 3, KEPT SO ITS YIELD CAN BE RE-RUN.** ### Nearest-name attachment, but
    ### BLIND TO COMPOUND VERDICTS: it read `ENCODES-CONCLUSION \ SHELL` as two cells."""
    cells = []
    for label, path in ledger_files():
        text = read(path)
        for i, ln in enumerate(text.split(NL), 1):
            if not GRADE_RE.search(ln):
                continue
            for off, seg in _segments(ln):
                gs_ = [(m.start(), m.end(), m.group(1)) for m in GRADE_RE.finditer(seg)]
                names = _names_on(seg)
                if not gs_ or not names:
                    continue
                for g0, g1, gr in gs_:
                    best, bd = None, None
                    for a0, b0, nm in names:
                        d = abs((g0 - b0) if g0 >= b0 else (a0 - g1))
                        if d <= WINDOW and (bd is None or d < bd):
                            best, bd = nm, d
                    if best is not None:
                        cells.append(dict(name=best, grade=gr, ledger=label, line=i))
    return cells


def grade_cells_v2():
    """### ### **VERSION 2, KEPT SO ITS YIELD CAN BE RE-RUN AND NOT MERELY RECALLED.**
    ### Every name within `WINDOW` of a grade takes that grade. ### Discarded: proximity is not
    ### attachment, and this made the relation a CROSS PRODUCT inside a crowded line."""
    cells = []
    for label, path in ledger_files():
        text = read(path)
        for i, ln in enumerate(text.split(NL), 1):
            if not GRADE_RE.search(ln):
                continue
            for off, seg in _segments(ln):
                gs_ = [(m.start(), m.group(1)) for m in GRADE_RE.finditer(seg)]
                if not gs_:
                    continue
                for a0, b0, nm in _names_on(seg):
                    near = sorted((abs(gp - (a0 if gp < a0 else b0)), gr) for gp, gr in gs_
                                  if abs(gp - (a0 if gp < a0 else b0)) <= WINDOW)
                    if near:
                        cells.append(dict(name=nm, grade=near[0][1], ledger=label, line=i))
    return cells


def grade_cells(loose=False):
    """### ### **EVERY GRADE CELL: `(name, grade, ledger, line, quote)`.**

    ### ### **TIGHT (the one used):** ### the name and the grade word lie in the SAME table cell
    ### (or the same non-table line) and ### **WITHIN 120 CHARACTERS OF EACH OTHER**, so the pairing
    ### is a local one a reader can see. ### **LOOSE (printed for its yield only):** ### version 1.
    ### ### **THE QUOTE IS THE PAIRING'S OWN NEIGHBOURHOOD**, so a disagreement can be READ.
    """
    cells = []
    for label, path in ledger_files():
        text = read(path)
        if not text:
            continue
        for i, ln in enumerate(text.split(NL), 1):
            if not GRADE_RE.search(ln):
                continue
            act = ACT_RE.search(ln)
            act = ('b' + act.group(1)) if act else None
            if loose:
                grades = sorted(set(GRADE_RE.findall(ln)), key=lambda x: -len(x))
                for _, _, nm in _names_on(ln):
                    cells.append(dict(name=nm, grade=grades[0], ledger=label, line=i,
                                      act=act, quote=ln.strip()[:400]))
                continue
            for off, seg in _segments(ln):
                gs_ = [(m.start(), m.end(), m.group(1)) for m in GRADE_RE.finditer(seg)]
                if not gs_:
                    continue
                names = _names_on(seg)
                if not names:
                    continue
                # ### ### **v3: A GRADE ATTACHES TO THE NEAREST NAME, NOT TO EVERY NAME NEAR IT.**
                # ### v2 gave each NAME every grade within the window, so a line reading
                # ### *"`bright_access_required` -- ENCODES-CONCLUSION \ SHELL. ... inherits
                # ### `sieve_ceiling`'s status"* graded BOTH names twice and reported a conflict
                # ### on `sieve_ceiling`, which that line does not grade at all.
                # ### ### **THE RELATION IS MANY-GRADES-TO-ONE-NAME, NOT A CROSS PRODUCT.**
                # ### ### **A COMPOUND GRADE IS ONE CELL, NOT TWO CELLS DISAGREEING.**
                # ### The order defines CONFLICT as *"two ledger cells grade one name
                # ### differently"*. ### These ledgers routinely write ONE verdict as
                # ### `ENCODES-CONCLUSION \ SHELL`, `SHELL / hypothesis-assumed`,
                # ### `SHELL/ENCODES until wired`, or recite the vocabulary
                # ### `DERIVES/INTERFACES/SHELL Correspondence`. ### v3 read every one of those as
                # ### a disagreement and reported 12 conflicts, of which hand-reading found ONE
                # ### genuine. ### **ADJACENT GRADE WORDS JOINED BY A SEPARATOR ARE A SINGLE
                # ### ### COMPOUND VERDICT**, recorded as such and never as a conflict.
                merged = []
                for g0, g1, gr in gs_:
                    if merged:
                        p0, p1, pg = merged[-1]
                        # ### ### **THE SEPARATOR CLASS MUST CONTAIN A LITERAL BACKSLASH.**
                        # ### These ledgers write the compound as `ENCODES-CONCLUSION \ SHELL`.
                        # ### The first version of this class lost its backslash to a heredoc
                        # ### (b483's and b490's trap, a third time), so the commonest compound
                        # ### in the corpus did not merge and the count moved by one.
                        # ### Emphasis markers count as separators too: the ledgers also write
                        # ### `**DERIVES** / **INTERFACES**`, which is 7 characters of join.
                        # ### ### **NO REGEX HERE AT ALL.** ### Two attempts to write this as a
                        # ### character class lost the literal backslash -- once to the heredoc
                        # ### that wrote the file, once to the class itself, where a leading
                        # ### `\` escaped the `*` beside it instead of standing for itself.
                        # ### **A SEPARATOR TEST THAT CANNOT SEE ITS COMMONEST SEPARATOR IS A
                        # ### ### TEST THAT PASSES BY NOT FIRING**, so this strips the separator
                        # ### characters by value and asks whether anything is left.
                        between = seg[p1:g0]
                        SEP = chr(92) + '*/,-— \t()[]' + chr(39) + '"'
                        rest = (between or '').strip(SEP).strip().lower()
                        if len(between) <= 16 and rest in ('', 'or', 'and', 'vs', 'then'):
                            merged[-1] = (p0, g1, pg + ' \ ' + gr)
                            continue
                    merged.append((g0, g1, gr))
                gs_ = merged
                for g0, g1, gr in gs_:
                    best, bd = None, None
                    for a0, b0, nm in names:
                        d = (g0 - b0) if g0 >= b0 else (a0 - g1)
                        d = abs(d)
                        if d <= WINDOW and (bd is None or d < bd):
                            best, bd = (a0, b0, nm), d
                    if best is None:
                        continue
                    a0, b0, nm = best
                    lo = max(0, min(a0, g0) - 60)
                    cells.append(dict(name=nm, grade=gr, ledger=label, line=i, act=act,
                                      distance=bd,
                                      quote=seg[lo:max(b0, g1) + 60].strip()[:400]))
    return cells


# =====================================================================================================
# ### THE PRINTS
# =====================================================================================================
def prints_at(repo, ref):
    """### ### **BOTH SHAPES.** ### `#print axioms NAME` SOURCE lines in an `AxiomCheck*.lean`, and
    ### CAPTURED STDOUT in an `AXIOM_PRINTS*.txt`. ### **A READER THAT KNOWS ONE SHAPE SEES HALF THE
    ### POPULATION AND REPORTS A CLEAN NUMBER** -- which is why both are read and both are counted."""
    files = [f for f in sorted(tree(repo, ref)) if ARTEFACT.search(f)]
    src, out = {}, {}
    for f in files:
        t = blob(repo, ref, f)
        if t is None:
            continue
        if f.endswith('.lean'):
            for m in PRINT_SRC.finditer(t):
                src.setdefault(m.group(1), []).append(f)
        else:
            for m in PRINT_OUT.finditer(t):
                out[m.group(1)] = dict(profile=m.group(2).strip(), file=f)
    return files, src, out


def statement(repo, ref, name):
    """### ### **THE STATEMENT AS THE SOURCE FILE PRINTS IT, FROM THE DECLARATION LINE UP TO `:=`.**

    ### Taken from the FILE AT THE REF and ### **NEVER FROM A README** -- a README paraphrases, and
    ### a paraphrase in a column headed STATEMENT is a claim this table is not entitled to make.
    ### ### **AN UNRESOLVED STATEMENT IS A CELL, NOT A DROPPED ROW** -- (S1).
    """
    ns, last = B378.split(name)
    pat = B378.decl_re(last)
    T = tree(repo, ref)
    for f in sorted(T):
        if not f.endswith('.lean'):
            continue
        t = T[f]
        # ### ### **THE CHEAP TEST FIRST.** ### `declares()` runs two regexes; a plain substring
        # ### test on the last segment rejects the overwhelming majority of files for free.
        if last not in t:
            continue
        if not B378.declares(t, name, f):
            continue
        m = pat.search(t)
        if not m:
            continue
        rest = t[m.start():]
        # ### up to the FIRST `:=` at depth 0, or to the declaration's end if it has none
        cut, depth = None, 0
        i = 0
        while i < len(rest) - 1:
            c = rest[i]
            if c in '([{':
                depth += 1
            elif c in ')]}':
                depth -= 1
            elif c == ':' and rest[i + 1] == '=' and depth <= 0:
                cut = i
                break
            elif c == NL and rest[i + 1] not in ' \t' and i > 0:
                nxt = rest[i + 1:i + 40]
                if re.match(r'^(?:@\[|theorem|lemma|def|abbrev|instance|end|namespace|/-)', nxt):
                    cut = i
                    break
            i += 1
        body = rest[:cut] if cut is not None else rest[:600]
        return dict(text=NL.join(x.rstrip() for x in body.strip().split(NL)), file=f)
    return None


# =====================================================================================================
def pins_from_registry():
    """### ### **THE PIN REGISTRY'S KERNEL TABLE CITES, PER REPOSITORY -- OR NONE.**
    ### (S3): the table names a pin for a HANDFUL, not for the roster, and ### **AN EMPTY PIN IS A
    ### FINDING ABOUT THE REGISTRY, SAID AND NOT SILENTLY DOUBLED.**"""
    text = read(os.path.join(PP, 'REGISTRY.md'))
    head = text.find('## DEPOSIT-PIN / WORKING-HEAD')
    if head < 0:
        return {}, None
    # ### ### **`str.find` RETURNS A CHARACTER OFFSET, NOT A LINE NUMBER.** ### The first run
    # ### printed `REGISTRY kernel table at line 143979` for a file of 938 lines -- a figure
    # ### absurd enough to catch, which is luck. ### A plausible wrong offset would have stood.
    line_no = text.count(NL, 0, head) + 1
    seg = text[head:]
    end = seg.find(NL + '## ', 10)
    seg = seg[:end] if end > 0 else seg
    pins = {}
    for ln in seg.split(NL):
        if not ln.startswith('|'):
            continue
        cells = [c.strip() for c in ln.split('|')]
        if len(cells) < 3:
            continue
        rm = re.search(r'`(SIDE-[A-Za-z0-9-]+)`', cells[1])
        if not rm:
            continue
        pm = re.search(r'`(v[0-9][A-Za-z0-9._-]*|[0-9a-f]{7,40}|NONE)`', cells[2])
        pins[rm.group(1)] = dict(pin=(pm.group(1) if pm else None), cell=cells[2][:300])
    return pins, line_no


def resolve(repo, pin):
    if not pin or pin == 'NONE':
        return None
    r = git(repo, 'rev-parse', '%s^{commit}' % pin)
    return r.stdout.strip() if r.returncode == 0 else None


def build():
    named, repos = kernels()
    pins, pin_line = pins_from_registry()
    cells = grade_cells()
    loose = grade_cells(loose=True)
    v2 = grade_cells_v2()
    v3 = grade_cells_v3()
    by_name = {}
    for c in cells:
        by_name.setdefault(c['name'], []).append(c)
        _, last = B378.split(c['name'])
        by_name.setdefault('~' + last, []).append(c)

    rec('=' * 104)
    rec('(R107) K0 -- THE TERMINAL TABLE. ### **GENERATED; NO GRADE CONFERRED, NONE MOVED.**')
    rec('=' * 104)
    rec('  `SIDE-*` directories on D:\\      : ### **%d**' % len(named))
    rec('  of those, carrying a `.git`      : ### **%d**  (b378`s own predicate)' % len(repos))
    rec('  ### **BOTH FIGURES ARE PRINTED** -- a roster counted one way is a roster with a')
    rec('  ### convention hidden in it.')
    # ### ### **NEVER DEFER A FORMAT PAST THE `rec()` THAT PRINTS IT.** ### The shape
    # ### `rec('... %d'); L[-1] = L[-1] % n` printed a RAW `%d` to the terminal and to the bank,
    # ### and it has now bitten three times (b494's closing, b495's push, here). ### The value is
    # ### formatted AT THE CALL or it is not formatted at all.
    rec('  ledgers read : ### **%d**  (including the archive`s split looms -- b494 found the'
        % len(ledger_files()))
    rec('  ### 2026-07-26 census there, and ### **A SPLIT MOVES A LEDGER, IT DOES NOT RETIRE IT**)')
    rec('  ### THE GRADE-CELL MATCHER, BOTH VERSIONS, YIELD PRINTED.')
    rec('    v1 LOOSE (any name on any line carrying a grade word) : %d cells, %d names'
        % (len(loose), len(set(c['name'] for c in loose))))
    rec('    v2 WINDOWED (every name within %d chars of a grade)  : %d cells, %d names'
        % (WINDOW, len(v2), len(set(c['name'] for c in v2))))
    rec('    v3 NEAREST (each grade attaches to its NEAREST name)   : %d cells, %d names'
        % (len(v3), len(set(c['name'] for c in v3))))
    rec('    ### **v4 COMPOUND-AWARE (adjacent grades = ONE verdict)    : %d cells, %d names**'
        % (len(cells), len(set(c['name'] for c in cells))))
    rec('    ### ### **v1 AND v2 ARE DISCARDED AND THEIR YIELDS ARE PRINTED ANYWAY** -- b381`s')
    rec('    ### rule, that a matcher is never replaced silently. ### These ledgers carry')
    rec('    ### 2,000-character re-grade paragraphs naming a dozen keystones and using three')
    rec('    ### grade words about DIFFERENT ones. ### **v1 PAIRED EVERY NAME WITH EVERY GRADE ON')
    rec('    ### THE LINE** and reported 67 CONFLICTS; two read by hand were both artefacts.')
    rec('    ### **v2 BOUNDED IT TO A TABLE CELL AND A %d-CHARACTER WINDOW** and reported 17;' % WINDOW)
    rec('    ### hand-reading all 17 found the residue still crossed -- a line grading')
    rec('    ### `bright_access_required` ENCODES-CONCLUSION and mentioning `sieve_ceiling`')
    rec('    ### graded BOTH. ### **v3 MAKES THE RELATION MANY-GRADES-TO-ONE-NAME**: each grade')
    rec('    ### goes to its NEAREST name and to no other. ### **A MENTION IS NOT A GRADE CELL,')
    rec('    ### AND PROXIMITY IS NOT ATTACHMENT.**')
    rec('    ### ### **v3 REPORTED 12 CONFLICTS AND HAND-READING ALL 12 FOUND ONE GENUINE.**')
    rec('    ### The other eleven were ONE CELL writing a COMPOUND verdict --')
    rec('    ### `ENCODES-CONCLUSION \ SHELL`, `SHELL / hypothesis-assumed`, `SHELL/ENCODES`')
    rec('    ### -- or reciting the vocabulary `DERIVES/INTERFACES/SHELL Correspondence`.')
    rec('    ### ### **THE ORDER DEFINES CONFLICT AS TWO CELLS GRADING ONE NAME DIFFERENTLY**, and')
    rec('    ### a compound verdict is ONE cell. ### v4 joins adjacent grade words into a single')
    rec('    ### verdict and the residue is hand-read in the components bank, row by row.')
    rec('  REGISTRY kernel table at line %s ; repositories it names a pin for : ### **%d of %d**'
        % (pin_line, len(pins), len(repos)))
    rec('')

    # ### the matcher, fixtured BEFORE it is used -- b378's own discipline, carried not copied
    # ### ### **IT RETURNS `(ok, cases)`.** ### Unpacking it as a bare list made `c['got']`
    # ### subscript a bool and crash. ### **A CRASH IS THE KIND OUTCOME**: had it returned a
    # ### truthy object the arm would have reported ALL PASS having checked nothing.
    ok, fx = B378.fixtures(verbose=False)
    ok = bool(ok) and all(c['got'] is c['want'] for c in fx)
    rec('  ### THE MATCHER IS `b378_terminals.py`S, ### **IMPORTED AND NOT COPIED.**')
    rec('    fixtures, both dialects, both polarities : ### **%s** (%d cases)'
        % ('ALL PASS' if ok else '### FAILED', len(fx)))
    if not ok:
        rec('    ### ### **HALT. ### A MATCHER THAT FAILS ITS OWN FIXTURES MEASURES NOTHING.**')
        return None
    rec('')

    rows, unresolved_names, seen = [], [], set()
    for name, path in repos:
        head = gs(path, 'rev-parse', 'HEAD')
        pinrec = pins.get(name) or {}
        pin = pinrec.get('pin')
        pin_sha = resolve(path, pin)
        refs = [('HEAD', head)]
        if pin_sha and pin_sha != head:
            refs.insert(0, (pin, pin_sha))

        # ### the population at each ref
        pop = {}
        art_by_ref = {}
        for label, ref in refs:
            files, src, out = prints_at(path, ref)
            art_by_ref[label] = files
            for n in src:
                pop.setdefault(n, {})[label] = dict(kind='source', file=src[n][0], profile=None)
            for n, v in out.items():
                pop.setdefault(n, {})[label] = dict(kind='stdout', file=v['file'],
                                                    profile=v['profile'])
        # ### names a LEDGER cites that this repository declares
        for c in cells:
            n = c['name']
            if n in pop:
                continue
            for label, ref in refs:
                st = statement(path, ref, n)
                if st:
                    pop.setdefault(n, {})[label] = dict(kind='ledger-only', file=st['file'],
                                                        profile=None)
                    break

        for n in sorted(pop):
            key = (name, n)
            if key in seen:
                continue
            seen.add(key)
            at = pop[n]
            ref_label, ref_sha = (refs[0][0], refs[0][1])
            src_ref = refs[0][0] if refs[0][0] in at else (refs[-1][0] if refs[-1][0] in at else None)
            st = statement(path, dict(refs).get(src_ref, head), n) if src_ref else None
            profile = next((at[l]['profile'] for l, _ in refs if l in at and at[l]['profile']), None)
            _, last = B378.split(n)
            mine = [c for c in by_name.get(n, []) + by_name.get('~' + last, [])]
            uniq, seencell = [], set()
            for c in mine:
                k = (c['ledger'], c['line'], c['grade'])
                if k not in seencell:
                    seencell.add(k)
                    uniq.append(c)
            distinct = sorted(set(c['grade'] for c in uniq))
            rows.append(dict(
                repo=name, name=n, head=head[:12],
                pin=(pin or None), pin_sha=(pin_sha[:12] if pin_sha else None),
                pin_cell=(pinrec.get('cell') if pinrec else None),
                refs=[l for l, _ in refs],
                present_at=sorted(at),
                statement=(st['text'] if st else None),
                statement_file=(st['file'] if st else None),
                statement_state=('RESOLVED' if st else 'UNRESOLVED'),
                profile=(profile or 'NOT PROFILED'),
                profile_state=('PROFILED' if profile else 'NOT PROFILED'),
                grade=(distinct[0] if len(distinct) == 1 else
                       ('CONFLICT' if len(distinct) > 1 else 'UNGRADED')),
                grade_cells=[dict(grade=c['grade'], ledger=c['ledger'], line=c['line'],
                                  act=c['act'], quote=c['quote']) for c in uniq],
                conflict=(sorted(distinct) if len(distinct) > 1 else None)))

    # ### names a ledger cites that resolve in NO repository at ANY ref
    declared = set(r['name'] for r in rows) | set(B378.split(r['name'])[1] for r in rows)
    for n in sorted(set(c['name'] for c in cells)):
        if n in declared or B378.split(n)[1] in declared:
            continue
        unresolved_names.append(n)

    return dict(named=len(named), repos=len(repos), rows=rows, loose_cells=len(loose),
                v2_cells=len(v2), v3_cells=len(v3),
                unresolved_names=unresolved_names, ledgers=len(ledger_files()),
                cells=len(cells), pins_named=len(pins), pin_line=pin_line)


def emit(R):
    rows = R['rows']
    npro = [r for r in rows if r['profile_state'] == 'NOT PROFILED']
    ungr = [r for r in rows if r['grade'] == 'UNGRADED']
    conf = [r for r in rows if r['grade'] == 'CONFLICT']
    enc = [r for r in rows if r['grade'].startswith('ENCODES')]
    unst = [r for r in rows if r['statement_state'] == 'UNRESOLVED']

    rec('  ### THE COUNTS.')
    rec('  ' + '-' * 100)
    rec('    rows (repo, name)                                  : ### **%d**' % len(rows))
    rec('    NOT PROFILED                                       : ### **%d**' % len(npro))
    rec('    UNGRADED                                           : ### **%d**' % len(ungr))
    rec('    CONFLICT                                           : ### **%d**' % len(conf))
    rec('    ENCODES-graded (ENCODES or ENCODES-CONCLUSION)     : ### **%d**' % len(enc))
    rec('    names a ledger cites resolving in NO repo, any ref : ### **%d**'
        % len(R['unresolved_names']))
    rec('    (and, not asked for but owed by (S1)) STATEMENT UNRESOLVED : ### **%d**' % len(unst))
    rec('')

    # ---- the JSON and the MD
    prior_path = os.path.join(D, 'terminal_table.json')
    prior = None
    if os.path.exists(prior_path):
        try:
            prior = json.loads(read(prior_path))
        except Exception:
            prior = None
    if prior is not None:
        io.open(os.path.join(D, 'terminal_table_prior.json'), 'w', encoding='utf-8',
                newline=NL).write(json.dumps(prior, indent=1, ensure_ascii=False))

    payload = dict(generated_by='tools/terminal_table.py', ruling='(R107) K0',
                   repos_named=R['named'], repos_with_git=R['repos'],
                   ledgers=R['ledgers'], grade_cells=R['cells'],
                   grade_cells_loose_v1=R['loose_cells'], grade_cells_v2=R['v2_cells'],
                   grade_cells_v3=R['v3_cells'], grade_window=120,
                   grade_matcher='v4 nearest-name, compound-aware',
                   pins_named=R['pins_named'], registry_table_line=R['pin_line'],
                   counts=dict(rows=len(rows), not_profiled=len(npro), ungraded=len(ungr),
                               conflict=len(conf), encodes=len(enc),
                               ledger_names_unresolved=len(R['unresolved_names']),
                               statement_unresolved=len(unst)),
                   unresolved_names=R['unresolved_names'], rows=rows)
    io.open(os.path.join(D, 'terminal_table.json'), 'w', encoding='utf-8',
            newline=NL).write(json.dumps(payload, indent=1, ensure_ascii=False))

    M = ['# TERMINAL TABLE', '',
         '*(R107) K0. Generated by `tools/terminal_table.py`; regenerated at every close.*',
         '*INSTRUMENT OUTPUT. No prose lives here. No grade is conferred or moved: every grade '
         'is read from a ledger cell and carried with the act and line that wrote it.*', '',
         '| repo | name | pin | HEAD | statement | profile | grade | act:line | conflict |',
         '|:--|:--|:--|:--|:--|:--|:--|:--|:--|']
    for r in sorted(rows, key=lambda x: (x['repo'], x['name'])):
        st = (r['statement'] or 'UNRESOLVED').replace('|', '\\|').replace(NL, ' ')
        st = (st[:160] + '…') if len(st) > 160 else st
        gc = r['grade_cells'][0] if r['grade_cells'] else None
        where = ('%s:%d' % (gc['ledger'], gc['line'])) if gc else ''
        act = (gc['act'] or '') if gc else ''
        cf = ' / '.join(r['conflict']) if r['conflict'] else ''
        M.append('| `%s` | `%s` | %s | `%s` | `%s` | %s | **%s** | %s %s | %s |'
                 % (r['repo'], r['name'], ('`%s`' % r['pin']) if r['pin'] else '*none cited*',
                    r['head'], st, r['profile'][:60], r['grade'], act, where, cf))
    M += ['', '## CONFLICTS, BOTH CELLS QUOTED', '']
    if not conf:
        M.append('*none*')
    for r in conf:
        M.append('**`%s` / `%s`** — %s' % (r['repo'], r['name'], ' vs '.join(r['conflict'])))
        for c in r['grade_cells']:
            M.append('- **%s** — `%s:%d`%s — %s'
                     % (c['grade'], c['ledger'], c['line'],
                        (' (%s)' % c['act']) if c['act'] else '', c['quote'][:300]))
        M.append('')
    M += ['## NAMES A LEDGER CITES THAT RESOLVE IN NO REPOSITORY AT ANY REF', '']
    M.append(', '.join('`%s`' % n for n in R['unresolved_names']) or '*none*')
    M.append('')
    io.open(os.path.join(D, 'terminal_table.md'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(M) + NL)

    # ---- the diff against the prior run
    rec('  ### THE DIFF AGAINST THE PRIOR RUN.')
    rec('  ' + '-' * 100)
    if prior is None:
        rec('    ### ### **NO PRIOR RUN. ### THIS IS THE FIRST.**')
        rec('    ### The diff is a cell of this instrument from the next close onward; saying')
        rec('    ### "no change" on a first run would be a reassuring line about nothing.')
        diff = dict(first_run=True)
    else:
        was = {(x['repo'], x['name']): x for x in prior.get('rows', [])}
        now = {(r['repo'], r['name']): r for r in rows}
        added = sorted(set(now) - set(was))
        gone = sorted(set(was) - set(now))
        moved = [k for k in sorted(set(now) & set(was))
                 if (now[k]['grade'], now[k]['profile_state']) != (was[k]['grade'],
                                                                   was[k]['profile_state'])]
        rec('    rows added : %d ; rows gone : %d ; grade-or-profile changed : %d'
            % (len(added), len(gone), len(moved)))
        for k in moved[:20]:
            rec('      %s / %s : %s|%s -> %s|%s' % (k[0], k[1], was[k]['grade'],
                                                    was[k]['profile_state'], now[k]['grade'],
                                                    now[k]['profile_state']))
        diff = dict(first_run=False, added=added, gone=gone, changed=moved)
    rec('')
    rec('  written: data/terminal_table.json, data/terminal_table.md')
    rec('=' * 104)
    return payload, diff


def main():
    R = build()
    if R is None:
        return 2
    payload, diff = emit(R)
    io.open(os.path.join(D, 'terminal_table_run.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(diff, io.open(os.path.join(D, 'terminal_table_diff.json'), 'w',
                            encoding='utf-8', newline=NL), indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
