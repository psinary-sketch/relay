"""correspondence_gen.py -- the Correspondence generator, under (R282)(4) (b672).

Reads each roster table (data/b672_roster_read.json: the roster's file, the heading line above the table, the header row's text) by its
anchor, and rewrites in it only the cells the ruling names, from the sources it names (the file's one-copy partner is written too, and
identically, where it carried an identical table before the run -- the navigator's answer on the REGISTRY):
  the kernel cell's leading clause(s) -- version and commit -- from each kernel's current tag (one `git ls-remote --tags` per repository,
      the highest v-tag, the commit it peels to);
  the profile cell's one profile token -- from the kernel's latest relay print bank that is AT THE TAG (built at the tag, or at an ancestor
      of it with no .lean, lean-toolchain or lake-manifest.json file differing); a print bank is either b<act>_runner_<kernel>[_run<id>].txt or
      b<act>_prints_<kernel>... carrying its own rows, or (b682, W-ORD-CORRESPONDENCE-RUNNER-BANKS) the runner print bank as b674, b676 and b678
      banked it: b<act>_axioms_<kernel>_<before|after>.txt, the raw #print axioms lines, its built commit read from the header of its companion
      b<act>_runner_<kernel>_<before|after>.txt ("the ref built (out/ref.txt): <40 hex>", else "the ref input <40 hex>"); a print bank at the
      tag takes precedence over NO PRINT BANK, its verdict for the row's declaration read in the shape below;
  the status cell's leading grade token -- from the grade bank (data/terminal_table.json), with " UNREFRESHED" where the kernel has no print
      bank at its tag.
Rows are neither added nor removed; names, prose and the table's position are untouched; a table already at its tag is byte-identical.

The cell words, each counted on its own: ABSENT AT <tag> (the row's declaration is not declared at the tag: the pin is kept);
NO PRINT BANK AT <tag> (no qualifying bank for the kernel); NOT PRINTED AT <tag> (a qualifying bank that did not print the declaration),
written as "NOT PRINTED AT <tag> (was <old profile> at <old version = commit>)", the old pin from the row's kernel cell before the rewrite.
Held and left as they stand, each counted: a table not in the generator's shape (no kernel, terminal or profile column) -- NOT IN THE
GENERATOR'S SHAPE; a kernel cell naming a DEPOSIT-PIN or a DOI, and the rows inheriting it -- HELD: DEPOSIT PIN; a profile cell with more than
one profile token -- MULTI; with none -- NO PROFILE TOKEN. The navigator's answers on readings (1)-(8) and the anchor (b672) fix these rules.

The row's declaration is the first backticked Lean identifier of its terminal cell; the profile cell is read as that declaration's profile.
The prose of each cell is carried unverified: the tool's claim is the tokens it writes, nothing else.

Usage:
    python -X utf8 tools/correspondence_gen.py dry [roster.json] [full]   the local clones' tags (no remote call), prints the run (`full`:
                                                                           the whole bank text, diff included), writes nothing
    python -X utf8 tools/correspondence_gen.py run [roster.json]   writes the changed files, data/b672_correspondence_diff.txt and .json
    ... --diff <stem>   (b682) the run's diff banks named data/<stem>.txt and .json in place of b672's (b672's own banks left as they stand)
"""
import collections, hashlib, io, json, os, re, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = 'D:/MY-DOwnloads/PLACE-papers'
KD = 'D:/'
NL = '\n'
ROSTER = os.path.join(D, 'b672_roster_read.json')
DIFF_TXT = os.path.join(D, 'b672_correspondence_diff.txt')
DIFF_JSON = os.path.join(D, 'b672_correspondence_diff.json')
GRADES = os.path.join(D, 'terminal_table.json')

VOCAB = ('ENCODES-CONCLUSION', 'ENCODES', 'DERIVES', 'INTERFACES', 'SHELL', 'DEF')
ORDER = ('propext', 'sorryAx', 'Classical.choice', 'Quot.sound')
WORDS = ('ABSENT', 'NO PRINT BANK', 'NOT PRINTED')

SEP_ROW = re.compile(r'^\s*\|[\s:|-]+\|\s*$')
KNAME = re.compile(r'`?(SIDE-[a-z0-9]+(?:-[a-z0-9]+)*)`?')
HEX = r'([0-9a-f]{7,40})(?![0-9a-zA-Z])'
VER = re.compile(r'(\s+)(`?)(v\d+(?:\.\d+)*)(`?)')
VTAIL = re.compile(r'(\s*=\s*|\s+\((?:pin\s+)?)(\*\*)?(`?)' + HEX + r'(`?)')
BRANCH = re.compile(r'(\s+)((?:branch\s+`[^`]+`|main)\s+(?:=|at))(\s+)(\*\*)?(`?)' + HEX + r'(`?)')
CONLY = re.compile(r'(\s+\((?:pin\s+)?|\s*=\s*)(\*\*)?(`?)' + HEX + r'(`?)|(\s+)(\*\*)?(`)' + HEX + r'(`)')
INHERIT = re.compile(r'^(`?)(v\d+(?:\.\d+)*)(`?)')
CLAUSE_JOIN = re.compile(r'\s*·\s*')
PTOK = re.compile(r'`\{[^`}]*\}`|`\[[^`\]]*\]`|axiom-free(?: \((?:none|both)\))?|(?:ABSENT|NO PRINT BANK|NOT PRINTED) AT [^\s;,)|*]+')
GTOK = re.compile(r'^((?:###\s*)?(?:\*\*)?)(' + '|'.join(VOCAB) + r')( UNREFRESHED)?(?![\w-])')
IDENT = re.compile(r"`([A-Za-z_][\w.'′″₀-₉]*)`")
HELD_PIN = re.compile(r'DEPOSIT-PIN|\bDOI\b')
# ### the navigator's answer on the NOT PRINTED cells (b672): the word keeps what was verified -- "NOT PRINTED AT <tag> (was <old profile> at
# ### <old version = commit>)", the old pin from the row's kernel cell before the rewrite, the commit bare (a backticked commit in a row is a
# ### pin to reading (ii)). The parenthetical is skipped when the cell's profile tokens are counted, so a re-run leaves the cell as it stands.
WAS = re.compile(r' \(was .*? at [^)]*\)| \(was .*?, no pin cited\)')


# ================================================================================ CELLS
def spans(line):
    """The (start, end) of each cell's interior: the segments between unescaped |, the outer pipes dropped."""
    cut = [i for i, ch in enumerate(line) if ch == '|' and (i == 0 or line[i - 1] != '\\')]
    return [(cut[n] + 1, cut[n + 1]) for n in range(len(cut) - 1)]


def cell(line, sp):
    return line[sp[0]:sp[1]].strip()


def put_cell(line, sp, new):
    seg = line[sp[0]:sp[1]]
    a = len(seg) - len(seg.lstrip())
    b = len(seg.rstrip())
    return line[:sp[0]] + seg[:a] + new + seg[b:] + line[sp[1]:]


def columns(header):
    """The kernel, terminal, profile and status columns by the header's words; None for a column the header does not name."""
    hs = [h.strip().lower() for h in header.strip().strip('|').split('|')]
    def first(pred, skip=()):
        for i, h in enumerate(hs):
            if i not in skip and pred(h):
                return i
        return None
    k = first(lambda h: 'kernel' in h)
    t = first(lambda h: 'theorem' in h or 'terminal' in h, (k,))
    p = first(lambda h: 'profile' in h or '#print axioms' in h, (k, t))
    s = first(lambda h: 'status' in h, (k, t, p))
    if s is None:
        s = first(lambda h: 'grade' in h, (k, t, p))
    return dict(kernel=k, terminal=t, profile=p, status=s, n=len(hs))


# ================================================================================ PROFILES AND GRADES
def fmt_set(axs, style):
    xs = sorted(set(axs), key=lambda a: (ORDER.index(a) if a in ORDER else len(ORDER), a))
    if not xs:
        return 'axiom-free (none)'
    return ('`[%s]`' if style == '[' else '`{%s}`') % ', '.join(xs)


def tok_set(tok):
    """A profile token's axiom set, or None for a cell word."""
    if tok.startswith('axiom-free'):
        return frozenset()
    if tok.startswith('`{') or tok.startswith('`['):
        return frozenset(x.strip() for x in tok[2:-2].split(',') if x.strip())
    return None


def lookup(names, t):
    """A table name against a bank's full names: exact, else the one full name ending with '.' + it; None when absent or not unique."""
    if t in names:
        return t
    hit = [n for n in names if n.endswith('.' + t)]
    return hit[0] if len(hit) == 1 else None


# ================================================================================ ONE TABLE
def _is(line, anchor, key, strip):
    """A line against an anchor part: its text, or (a withheld document's anchor, b670's rules row 5) the sha256 of its text."""
    s = line.strip() if strip else line.rstrip()
    if key in anchor:
        return s == (anchor[key].strip() if strip else anchor[key].rstrip())
    return hashlib.sha256(s.encode('utf-8')).hexdigest() == anchor[key + '_sha256']


def find_table(lines, anchor):
    """The table by its anchor: the one line equal to its heading, then the first line after it equal to its header row; the table runs from
    the header row to the first line that is not a table row. Returns (i_header, i_end) or a reason string."""
    hs = [i for i, l in enumerate(lines) if _is(l, anchor, 'heading', False)]
    if len(hs) != 1:
        return 'ANCHOR HEADING FOUND %d TIMES' % len(hs)
    j = next((i for i in range(hs[0] + 1, len(lines)) if _is(lines[i], anchor, 'header', True)), None)
    if j is None:
        return 'ANCHOR HEADER ROW NOT FOUND BENEATH ITS HEADING'
    e = j
    while e < len(lines) and lines[e].lstrip().startswith('|'):
        e += 1
    return j, e


def parse_kernel_cell(kc):
    """The kernel cell's leading clauses: [(kernel or None for an inheriting clause, [(start, end, kind, text)] of its version and commit
    tokens in the cell)]. kind is 'ver', 'hex' or 'branch' (the branch words, with the separator, replaced by the tag)."""
    pos = 0
    m0 = re.match(r'^(?:###\s*)?(?:\*\*)?', kc)
    pos = m0.end()
    out = []
    im = INHERIT.match(kc, pos)
    if im:
        toks = [(im.start(2), im.end(2), 'ver', im.group(2))]
        q = im.end()
        tm = VTAIL.match(kc, q)
        if tm:
            toks.append((tm.start(4), tm.end(4), 'hex', tm.group(4)))
        return [(None, toks)]
    while True:
        km = KNAME.match(kc, pos)
        if not km:
            break
        k, q, toks = km.group(1), km.end(), []
        bm = BRANCH.match(kc, q)
        vm = VER.match(kc, q)
        if bm:
            toks = [(bm.start(2), bm.end(2), 'branch', bm.group(2)), (bm.start(6), bm.end(6), 'hex', bm.group(6))]
            q = bm.end()
        elif vm:
            toks = [(vm.start(3), vm.end(3), 'ver', vm.group(3))]
            q = vm.end()
            tm = VTAIL.match(kc, q)
            if tm:
                toks.append((tm.start(4), tm.end(4), 'hex', tm.group(4)))
                q = tm.end()
        else:
            cm = CONLY.match(kc, q)
            if cm:
                g = 4 if cm.group(4) else 9      # ### the second alternative's commit is its group 9 (6 space, 7 bold, 8 and 10 backticks)
                toks = [(cm.start(g), cm.end(g), 'hex', cm.group(g))]
                q = cm.end()
        out.append((k, toks))
        jm = CLAUSE_JOIN.match(kc, q)
        if not jm or not KNAME.match(kc, jm.end()):
            break
        pos = jm.end()
    return out


def rewrite_clause_tokens(kc, toks, tag, commit):
    """The cell with one clause's tokens set to the tag: the version to the tag's name, the commit to the tag's commit at the cited length,
    the branch words to the tag's name and '='."""
    for s, e, kind, text in sorted(toks, reverse=True):
        if kind == 'ver':
            new = tag
        elif kind == 'hex':
            new = commit[:max(7, len(text))]
        else:
            new = tag + ' ='
        kc = kc[:s] + new + kc[e:]
    return kc


def old_pin(toks):
    """A clause's cited pin as the NOT PRINTED parenthetical names it: 'v0.4.0 = 0d2d74c', 'v0.4.0', '0d2d74c', or None."""
    ver = next((t for _s, _e, kind, t in toks if kind == 'ver'), None)
    hx = next((t for _s, _e, kind, t in toks if kind == 'hex'), None)
    return ' = '.join(x for x in (ver, hx) if x) or None


def was_note(old_tok, pin):
    return ' (was %s at %s)' % (old_tok, pin) if pin else ' (was %s, no pin cited)' % old_tok


def clause_at_tag(toks, tag, commit):
    for _s, _e, kind, text in toks:
        if kind == 'ver' and text != tag:
            return False
        if kind == 'hex' and not commit.startswith(text):
            return False
        if kind == 'branch':
            return False
    return True


def regen_lines(lines, anchor, ctx, doc=''):
    """One table regenerated. `lines` without their endings; `anchor` dict(heading, header); `ctx` the sources:
        tags      {kernel: (tag, commit40)} -- a kernel absent or None has no tag
        banks     {kernel: {'prints': {full name: [axioms]}, ...}} -- the qualifying bank; absent or None: no print bank at the tag
        grades    {kernel: {full name: grade}}
        present   function(kernel, commit40, name) -> bool, the declaration declared at the commit
    Returns (new lines, result dict)."""
    lines = list(lines)
    res = dict(doc=doc, changes=[], counts=collections.Counter(), by_kernel=collections.defaultdict(collections.Counter), rows=[])
    ft = find_table(lines, anchor)
    if isinstance(ft, str):
        res['status'] = ft
        return lines, res
    j, e = ft
    cols = columns(lines[j])
    res['columns'] = cols
    res['span'] = (j + 1, e)
    if cols['kernel'] is None or cols['terminal'] is None or cols['profile'] is None:
        res['status'] = 'NOT IN THE GENERATOR`S SHAPE'
        return lines, res
    res['status'] = 'SHAPED'
    prev_k, prev_held, prev_pins = [], False, {}
    for i in range(j + 1, e):
        line = lines[i]
        if SEP_ROW.match(line):
            continue
        sp = spans(line)
        if len(sp) < cols['n']:
            res['counts']['ROW WITH TOO FEW CELLS'] += 1
            res['rows'].append(dict(line=i + 1, kernels=[], reading='ROW WITH TOO FEW CELLS'))
            prev_k, prev_held = None, True      # ### a row beneath it that inherits ("same") inherits an unread row, and is held
            continue
        old_line = line
        kc = cell(line, sp[cols['kernel']])
        clauses = parse_kernel_cell(kc)
        held = bool(HELD_PIN.search(kc))
        if (kc.strip('`* ').lower() == 'same' or (clauses and clauses[0][0] is None)) and prev_k is None:
            res['rows'].append(dict(line=i + 1, kernels=[], reading='INHERITS AN UNREAD ROW'))
            res['counts']['INHERITS AN UNREAD ROW'] += 1
            continue
        if kc.strip('`* ').lower() == 'same' or (clauses and clauses[0][0] is None):
            ks, held = list(prev_k), held or prev_held
            if clauses and clauses[0][0] is None:
                clauses = [(prev_k[0] if prev_k else None, clauses[0][1])]
            pins = dict(prev_pins)
            pins.update((k, old_pin(t)) for k, t in clauses if k and old_pin(t))
        else:
            ks = [k for k, _t in clauses]
            pins = dict((k, old_pin(t)) for k, t in clauses)
            if ks:
                prev_k, prev_held, prev_pins = ks, held, pins
        row = dict(line=i + 1, kernels=ks)
        res['rows'].append(row)
        if not ks or not ks[0]:
            row['reading'] = 'NO KERNEL'
            res['counts']['NO KERNEL'] += 1
            continue
        if held:
            row['reading'] = 'HELD: DEPOSIT PIN'
            res['counts']['HELD: DEPOSIT PIN'] += 1
            continue
        tagged = [k for k in ks if (ctx['tags'].get(k) or None)]
        if not tagged:
            row['reading'] = 'NO TAG'
            res['counts']['NO TAG'] += 1
            continue
        decls = [n for n in IDENT.findall(cell(line, sp[cols['terminal']])) if not n.endswith('.lean') and n != 'sorry']
        if not decls:
            row['reading'] = 'NO DECLARATION'
            res['counts']['NO DECLARATION'] += 1
            continue
        d0 = decls[0]
        row['declaration'] = d0
        star = next((k for k in tagged if ctx['present'](k, ctx['tags'][k][1], d0)), None)
        pc = cell(line, sp[cols['profile']])
        ptoks = PTOK.findall(WAS.sub('', pc))
        if star is None:
            k0 = tagged[0]
            row['reading'] = 'ABSENT'
            res['counts']['ABSENT'] += 1
            res['by_kernel'][k0]['ABSENT'] += 1
            word = 'ABSENT AT %s' % ctx['tags'][k0][0]
            if len(ptoks) == 1 and ptoks[0] != word:
                line = put_cell(line, sp[cols['profile']], pc.replace(ptoks[0], word, 1))
            elif len(ptoks) != 1:
                res['counts']['MULTI' if ptoks else 'NO PROFILE TOKEN'] += 1
            lines[i] = line
            _record(res, doc, i, old_line, line, sp, cols, k0)
            continue
        tag, commit = ctx['tags'][star]
        # ### the kernel cell: every clause whose kernel has a tag and declares one of the row's declarations there
        new_kc = kc
        for k, toks in reversed(clauses):
            if not k or not ctx['tags'].get(k) or not toks:
                continue
            kt, kcm = ctx['tags'][k]
            if not any(ctx['present'](k, kcm, d) for d in decls):
                continue
            if not clause_at_tag(toks, kt, kcm):
                new_kc = rewrite_clause_tokens(new_kc, toks, kt, kcm)
        if new_kc != kc:
            line = put_cell(line, sp[cols['kernel']], new_kc)
            sp = spans(line)
        # ### the profile cell
        bank = (ctx['banks'].get(star) or None)
        if bank is None:
            word = 'NO PRINT BANK AT %s' % tag
            res['counts']['NO PRINT BANK'] += 1
            res['by_kernel'][star]['NO PRINT BANK'] += 1
            row['reading'] = 'NO PRINT BANK'
            new_tok = word
        else:
            full = lookup(list(bank['prints']), d0)
            if full is None:
                new_tok = 'NOT PRINTED AT %s' % tag
                res['counts']['NOT PRINTED'] += 1
                res['by_kernel'][star]['NOT PRINTED'] += 1
                row['reading'] = 'NOT PRINTED'
            else:
                new_tok = ('SET', frozenset(bank['prints'][full]))
                row['reading'] = 'PRINTED'
        pc = cell(line, sp[cols['profile']])
        ptoks = PTOK.findall(WAS.sub('', pc))
        if len(ptoks) == 1:
            t0 = ptoks[0]
            if isinstance(new_tok, tuple):
                if tok_set(t0) != new_tok[1]:
                    style = '[' if t0.startswith('`[') else '{'
                    pc = WAS.sub('', pc).replace(t0, fmt_set(new_tok[1], style), 1)
            elif t0 != new_tok:
                if new_tok.startswith('NOT PRINTED') and tok_set(t0) is not None:
                    new_tok = new_tok + was_note(t0, pins.get(star))     # ### the verified profile kept beside the word
                pc = pc.replace(t0, new_tok, 1)
            line = put_cell(line, sp[cols['profile']], pc)
            sp = spans(line)
        else:
            res['counts']['MULTI' if ptoks else 'NO PROFILE TOKEN'] += 1
        # ### the status cell's leading grade token
        if cols['status'] is not None:
            sc = cell(line, sp[cols['status']])
            gm = GTOK.match(sc)
            gb = ctx['grades'].get(star) or {}
            gfull = lookup(list(gb), d0)
            g = gb.get(gfull) if gfull else None
            if not gm:
                res['counts']['NO GRADE TOKEN'] += 1
            elif g not in VOCAB:
                res['counts']['GRADE NOT IN THE BANK'] += 1
            else:
                new_g = g + (' UNREFRESHED' if bank is None else '')
                if gm.group(2) + (gm.group(3) or '') != new_g:
                    sc = sc[:gm.start(2)] + new_g + sc[gm.end(3) if gm.group(3) else gm.end(2):]
                    line = put_cell(line, sp[cols['status']], sc)
        lines[i] = line
        _record(res, doc, i, old_line, line, spans(old_line), cols, star)
    return lines, res


def _record(res, doc, i, old_line, new_line, sp_old, cols, k):
    if old_line == new_line:
        return
    so, sn = spans(old_line), spans(new_line)
    names = ('kernel', 'profile', 'status')
    for nm in names:
        c = cols[nm]
        if c is None:
            continue
        a, b = cell(old_line, so[c]), cell(new_line, sn[c])
        if a != b:
            res['changes'].append(dict(doc=doc, line=i + 1, column=nm, kernel=k, old=a, new=b))
            res['counts']['CELLS CHANGED'] += 1


def regen_bytes(b, anchor, ctx, doc=''):
    """A whole file's bytes: its line endings kept (CRLF or LF, per the file), untouched when nothing changes."""
    t = b.decode('utf-8')
    crlf = '\r\n' in t
    body = t.replace('\r\n', '\n')
    lines = body.split('\n')
    new, res = regen_lines(lines, anchor, ctx, doc)
    if new == lines:
        return b, res
    out = '\n'.join(new)
    return (out.replace('\n', '\r\n') if crlf else out).encode('utf-8'), res


# ================================================================================ THE SOURCES (live runs only)
def git(kd, *a):
    r = subprocess.run(['git', '-C', kd] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout


def vkey(t):
    return tuple(int(x) for x in re.findall(r'\d+', t))


def read_tags(kernels, remote=True):
    """One `git ls-remote --tags origin` per repository: the highest v-tag and the commit it peels to; the local describe printed beside.
    remote=False (the dry run): the local clone's tags alone (`git show-ref --tags --dereference`), no remote call -- the ruling's one
    ls-remote per repository is the run's."""
    tags, log = {}, []
    for k in sorted(kernels):
        kd = KD + k
        if not os.path.isdir(os.path.join(kd, '.git')):
            tags[k] = None
            log.append((k, 'NO LOCAL CLONE', '', '', ''))
            continue
        if remote:
            rc, out = git(kd, 'ls-remote', '--tags', 'origin')
        else:
            rc, out = git(kd, 'show-ref', '--tags', '--dereference')
            out = NL.join(l.replace(' ', '\t', 1) for l in out.split(NL))
            rc = 0 if rc in (0, 1) else rc
        refs = dict((l.split('\t')[1], l.split('\t')[0]) for l in out.split(NL) if '\t' in l)
        vt = sorted({r[len('refs/tags/'):].replace('^{}', '') for r in refs if re.match(r'^refs/tags/v\d', r)}, key=vkey)
        if rc or not vt:
            tags[k] = None
            log.append((k, 'NO TAG %s (exit %d, %d refs)' % ('AT THE REMOTE' if remote else 'IN THE LOCAL CLONE', rc, len(refs)), '', '', ''))
            continue
        t = vt[-1]
        c = refs.get('refs/tags/%s^{}' % t) or refs.get('refs/tags/%s' % t)
        _r, loc = git(kd, 'describe', '--tags', '--abbrev=0', 'main')
        here = git(kd, 'cat-file', '-e', c + '^{commit}')[0] == 0
        if not here:
            tags[k] = None
            log.append((k, 'TAG COMMIT NOT IN THE LOCAL CLONE', t, c, loc.strip()))
            continue
        tags[k] = (t, c)
        log.append((k, 'READ' if remote else 'READ LOCALLY (DRY)', t, c, loc.strip()))
    return tags, log


BANK_NAME = re.compile(r'^b(\d+)_(?:runner|prints)_(SIDE-[a-z0-9-]+?)(?:_run\d+)?\.txt$')
BANK_ROW = re.compile(r"^  ([A-Za-z_][\w.'′″₀-₉]*)\s+(?:[A-Z][A-Z\\ -]*\s+)?(\[(?:'[^']*'(?:,\s*)?)*\])")
# ### b682, W-ORD-CORRESPONDENCE-RUNNER-BANKS: the runner print bank as b674, b676 and b678 banked it (relay data/b674_cut.txt :19-:20,
# ### data/b676_cut.txt :24-:27, data/b678_cut.txt :28-:31): the axioms bank beside its runner bank, one label each, before or after
AX_NAME = re.compile(r'^b(\d+)_axioms_(SIDE-[a-z0-9-]+?)_(before|after)\.txt$')
LEAN_ROW = re.compile(r"^'([A-Za-z_][\w.'′″₀-₉]*)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])\s*$")
REF_BUILT = re.compile(r'the ref built \(out/ref\.txt\): ([0-9a-f]{40})')


def parse_runner_bank(path):
    """a runner print bank of the b674 form: (built commit, {full name: [axioms]}). The prints are the axioms bank's raw #print axioms lines;
    the built commit is read from the companion runner bank's header (the ref built, else the ref input); None where that bank is absent."""
    d, f = os.path.split(path)
    m = AX_NAME.match(f)
    prints = {}
    for l in io.open(path, encoding='utf-8', errors='replace').read().split(NL):
        r = LEAN_ROW.match(l.rstrip('\r'))
        if r:
            prints.setdefault(r.group(1), [x.strip() for x in (r.group(2) or '').split(',') if x.strip()])
    built = None
    comp = os.path.join(d, 'b%s_runner_%s_%s.txt' % (m.group(1), m.group(2), m.group(3))) if m else ''
    if comp and os.path.exists(comp):
        h = io.open(comp, encoding='utf-8', errors='replace').read()
        b = REF_BUILT.search(h) or re.search(r'ref input ([0-9a-f]{40})', h)
        built = b.group(1) if b else None
    return built, prints


def parse_bank(path):
    if AX_NAME.match(os.path.basename(path)):
        return parse_runner_bank(path)
    t = io.open(path, encoding='utf-8', errors='replace').read()
    m = (re.search(r'#print axioms at ([0-9a-f]{7,40})', t) or re.search(r'ref input ([0-9a-f]{40})', t)
         or re.search(r'\bref ([0-9a-f]{40})', t))
    prints = {}
    for l in t.split(NL):
        r = BANK_ROW.match(l.rstrip('\r'))
        if r:
            prints.setdefault(r.group(1), re.findall(r"'([^']*)'", r.group(2)))
    return (m.group(1) if m else None), prints


def read_banks(tags):
    """Per kernel, the latest relay print bank AT THE TAG: built at the tag or an ancestor with no .lean, lean-toolchain or lake-manifest.json
    file differing; every bank read is printed with its reading."""
    found = collections.defaultdict(list)
    for f in sorted(os.listdir(D)):
        m = BANK_NAME.match(f) or AX_NAME.match(f)
        if m:
            found[m.group(2)].append((int(m.group(1)), f))
    banks, log = {}, []
    for k in sorted(tags):
        best = None
        for act, f in sorted(found.get(k, []), key=lambda x: (x[0], not x[1].endswith('_before.txt'), x[1]), reverse=True):   # ### an act's 'after' bank before its 'before'
            built, prints = parse_bank(os.path.join(D, f))
            if not tags[k]:
                log.append((k, f, built, 'KERNEL HAS NO TAG', None, len(prints)))
                continue
            t, c = tags[k]
            kd = KD + k
            if not built or not prints:
                log.append((k, f, built, 'NO BUILT COMMIT' if not built else 'NO PRINT ROWS', None, len(prints)))
                continue
            full = git(kd, 'rev-parse', '--verify', '-q', built + '^{commit}')[1].strip()
            if not full:
                log.append((k, f, built, 'BUILT COMMIT NOT IN THE LOCAL CLONE', None, len(prints)))
                continue
            anc = full == c or git(kd, 'merge-base', '--is-ancestor', full, c)[0] == 0
            nd = len([x for x in git(kd, 'diff', '--name-only', full, c, '--', '*.lean', 'lean-toolchain', 'lake-manifest.json')[1].split(NL) if x.strip()])
            ok = anc and nd == 0
            log.append((k, f, full[:7], ('AT THE TAG' if ok else ('NOT AN ANCESTOR' if not anc else 'FILES DIFFER')), nd, len(prints)))
            if ok and best is None:
                best = dict(file=f, built=full, prints=prints, diff=nd)
        banks[k] = best
    return banks, log


def read_grades():
    j = json.load(io.open(GRADES, encoding='utf-8'))
    g = collections.defaultdict(dict)
    for r in j['rows']:
        g[r['repo']][r['name']] = r['grade']
    return g


_PRES = {}


def present(k, commit, name):
    """The declaration declared at the commit: git grep bounded to *.lean -- a declaration keyword then the name's last component, or a
    structure field of that name."""
    last = name.split('.')[-1]
    key = (k, commit, last)
    if key not in _PRES:
        e = re.escape(last)
        p1 = (r"^[[:space:]]*(@\[[^]]*\][[:space:]]*)?((private|protected|noncomputable|nonrec|partial|unsafe)[[:space:]]+)*"
              r"(theorem|lemma|def|abbrev|structure|class|inductive|instance|axiom|opaque)[[:space:]]+([^[:space:]]*\.)?" + e + r"([[:space:]]|:|$)")
        p2 = r"^[[:space:]]+" + e + r"[[:space:]]*:"
        r = subprocess.run(['git', '-C', KD + k, 'grep', '-q', '-E', '-e', p1, '-e', p2, commit, '--', '*.lean'], capture_output=True)
        _PRES[key] = r.returncode == 0
    return _PRES[key]


# ================================================================================ THE RUN
def kernels_of(roster):
    ks = set()
    for t in roster['tables']:
        b = open(os.path.join(PP, t['path']), 'rb').read().decode('utf-8').replace('\r\n', '\n').split('\n')
        ft = find_table(b, t)
        if isinstance(ft, str):
            continue
        cols = columns(b[ft[0]])
        if cols['kernel'] is None:
            continue
        for l in b[ft[0] + 1:ft[1]]:
            sp = spans(l)
            if len(sp) > cols['kernel']:
                ks.update(KNAME.findall(cell(l, sp[cols['kernel']])))
    return ks


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


RANK = {'DERIVES': 3, 'INTERFACES': 2}


def grade_down(results):
    """Every status cell whose leading grade token moves downward (DERIVES to INTERFACES or lower; INTERFACES to lower), " UNREFRESHED"
    set aside for the rank."""
    out = []
    for r in results:
        for c in r['changes']:
            if c['column'] != 'status':
                continue
            a, b = GTOK.match(c['old']), GTOK.match(c['new'])
            if a and b and RANK.get(b.group(2), 1) < RANK.get(a.group(2), 1):
                out.append(dict(doc=c['doc'], line=c['line'], kernel=c['kernel'], old=a.group(2) + (a.group(3) or ''),
                                new=b.group(2) + (b.group(3) or ''), withheld=r['withheld']))
    return out


def main(mode, roster_path=ROSTER, full=False):
    roster = json.load(io.open(roster_path, encoding='utf-8'))
    ks = kernels_of(roster)
    tags, tlog = read_tags(ks, remote=(mode == 'run'))
    banks, blog = read_banks(tags)
    ctx = dict(tags=tags, banks=banks, grades=read_grades(), present=present)
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    results, writes = [], []
    pairs = []
    for t in roster['tables']:
        p = os.path.join(PP, t['path'])
        b = open(p, 'rb').read()
        nb, res = regen_bytes(b, t, ctx, t['doc'])
        res['path'] = t['path']
        res['withheld'] = bool(t.get('withheld'))
        results.append(res)
        if nb != b:
            writes.append((p, nb))
        # ### the navigator's answer on the REGISTRY: a one-copy partner carrying an identical table is written too, and identically
        if t.get('partner') and t.get('partner_identical'):
            q = os.path.join(PP, t['partner'])
            qb = open(q, 'rb').read()
            nq, rq = regen_bytes(qb, t, ctx, t['doc'] + ' (partner)')
            A = nb.decode('utf-8').replace('\r\n', '\n').split('\n')
            B = nq.decode('utf-8').replace('\r\n', '\n').split('\n')
            fa, fb = find_table(A, t), find_table(B, t)
            same = not isinstance(fa, str) and not isinstance(fb, str) and A[fa[0]:fa[1]] == B[fb[0]:fb[1]]
            if not same:
                sys.exit('### REFUSED: %s and its partner %s were identical before the run and differ after it -- NOTHING WRITTEN' % (t['path'], t['partner']))
            pairs.append(dict(doc=t['doc'], path=t['path'], partner=t['partner'], cells=rq['counts']['CELLS CHANGED'], written=nq != qb))
            if nq != qb:
                writes.append((q, nq))
        elif t.get('partner'):
            pairs.append(dict(doc=t['doc'], path=t['path'], partner=t['partner'], cells=0, written=False,
                              reason=('NOT WRITTEN: THE PARTNER`S TABLE DIFFERS IN %d LINES' % t.get('partner_lines_differing', -1))
                              if 'partner_identical' in t else 'NOT WRITTEN: %s' % t.get('partner_found')))
    tot = collections.Counter()
    byk = collections.defaultdict(collections.Counter)
    for r in results:
        tot.update(r['counts'])
        for k, c in r['by_kernel'].items():
            byk[k].update(c)
    L = ['b672 -- THE CORRESPONDENCE GENERATOR`S RUN, (R282)(4) (%s): tools/correspondence_gen.py %s' % (stamp, mode), '',
         '### the prose of every cell is carried unverified by the generator: its claim is the tokens it writes (the kernel clause`s version and',
         '### commit, the profile token, the leading grade token) and nothing else; a stale stipulation in prose is a cell-refresh item, not the',
         '### tool`s claim (the navigator`s answer on reading (1)). A withheld document`s cells print as sha256 and length, never as text.', '',
         '### THE TAGS: one `git ls-remote --tags origin` per repository (kernel ; reading ; tag ; the commit it peels to ; local describe on main)']
    L += ['    %-34s %-40s %-9s %s ; local %s' % (k, rd, tg, c[:12], loc or '-') for k, rd, tg, c, loc in tlog]
    L += ['', '### THE PRINT BANKS: every relay print bank of a tabled kernel (kernel ; bank ; built commit ; reading ; files differing to the tag ;',
          '### rows); the first AT THE TAG, newest act first, is the one read']
    L += ['    %-34s %-52s %-9s %-36s %-5s %s' % (k, f, (b or '-')[:7], rd, '-' if nd is None else nd, n) for k, f, b, rd, nd, n in blog]
    L += ['    %-34s ### NO PRINT BANK AT %s' % (k, tags[k][0]) for k in sorted(tags) if tags[k] and not banks.get(k)]
    L += ['', '### THE TABLES (document ; file ; status ; the table`s lines ; rows ; the cell words and holds)']
    for r in results:
        L.append('    %-36s %-62s %-30s %s ; rows %d ; %s' % (r['doc'], r['path'], r['status'], ':%d-:%d' % r['span'] if r.get('span') else '-',
                                                          len(r['rows']), dict(r['counts']) or '-'))
    L += ['', '### THE ONE-COPY PAIRS (the navigator`s answer on the REGISTRY): document ; the roster`s file ; its partner ; the partner`s reading']
    L += ['    %-36s %s ; %s ; %s' % (x['doc'], x['path'], x['partner'], ('WRITTEN IDENTICALLY (%d cells, as the roster`s file)' % x['cells'])
                                     if x['written'] else (x.get('reason') or 'IDENTICAL, NOTHING TO WRITE')) for x in pairs] or ['    none']
    down = grade_down(results)
    L += ['', '### THE GRADE TOKENS MOVED DOWNWARD (the navigator`s answer, b672: listed before the write, entered under W-ORD-GRADE-MOVED): '
              'document :line ; kernel ; old token -> new token']
    L += ['    %s :%d ; %s ; %s -> %s' % (d['doc'], d['line'], d['kernel'], d['old'], d['new']) for d in down] or ['    none']
    L += ['', '### THE DIFF: rows are cells changed (document :line ; column ; kernel ; old ; new)']
    for r in results:
        for c in r['changes']:
            if r['withheld']:
                L.append('    %s :%d | %s | %s | OLD sha256 %s length %d | NEW sha256 %s length %d' % (
                    c['doc'], c['line'], c['column'], c['kernel'], sha(c['old'])[:16], len(c['old']), sha(c['new'])[:16], len(c['new'])))
            else:
                L.append('    %s :%d | %s | %s | OLD %s | NEW %s' % (c['doc'], c['line'], c['column'], c['kernel'], c['old'], c['new']))
    L += ['', '### THE CELL WORDS BY KERNEL: ' + '; '.join('%s %s' % (k, dict(c)) for k, c in sorted(byk.items())) if byk else '### THE CELL WORDS BY KERNEL: none']
    shaped = sum(1 for r in results if r['status'] == 'SHAPED')
    L += ['### ### **TABLES %d ; SHAPED %d ; NOT IN THE GENERATOR`S SHAPE %d ; ANCHOR NOT FOUND %d ; KERNELS %d (WITH A TAG %d) ; CELLS CHANGED %d ; '
          'FILES CHANGED %d ; ABSENT %d ; NO PRINT BANK %d ; NOT PRINTED %d ; HELD: DEPOSIT PIN %d ; MULTI %d ; NO TAG %d.**' % (
              len(results), shaped, sum(1 for r in results if r['status'].startswith('NOT IN')),
              sum(1 for r in results if r['status'].startswith('ANCHOR')), len(tags), sum(1 for v in tags.values() if v), tot['CELLS CHANGED'],
              len(writes), tot['ABSENT'], tot['NO PRINT BANK'], tot['NOT PRINTED'], tot['HELD: DEPOSIT PIN'], tot['MULTI'], tot['NO TAG'])]
    tables_at = L.index('### THE TABLES (document ; file ; status ; the table`s lines ; rows ; the cell words and holds)')
    down_at = next(n for n, l in enumerate(L) if l.startswith('### THE GRADE TOKENS MOVED DOWNWARD'))
    pairs_at = next(n for n, l in enumerate(L) if l.startswith('### THE ONE-COPY PAIRS'))
    print(NL.join(l for n, l in enumerate(L) if not l.startswith('    ') or '### NO PRINT BANK AT' in l or tables_at < n <= tables_at + len(results)
                  or down_at < n <= down_at + max(1, len(down)) or pairs_at < n <= pairs_at + max(1, len(pairs))))
    if mode != 'run':
        if full:
            print(NL.join(L))
        print('### DRY: nothing written')
        return
    for p, nb in writes:
        if not os.path.abspath(p).replace('\\', '/').startswith(PP):
            sys.exit('### REFUSED: a write outside PLACE-papers: %s' % p)
        open(p + '.tmp', 'wb').write(nb)
        os.replace(p + '.tmp', p)
    open(DIFF_TXT + '.tmp', 'wb').write((NL.join(L) + NL).encode('utf-8'))
    os.replace(DIFF_TXT + '.tmp', DIFF_TXT)
    js = dict(at=stamp, tags={k: v for k, v in tags.items()}, banks={k: (dict(file=v['file'], built=v['built'], diff=v['diff']) if v else None)
                                                                   for k, v in banks.items()},
              tables=[dict(doc=r['doc'], path=r['path'], status=r['status'], span=r.get('span'), counts=dict(r['counts']),
                           rows=r['rows'], changes=(len(r['changes']) if r['withheld'] else r['changes'])) for r in results],
              counts=dict(tot), by_kernel={k: dict(c) for k, c in byk.items()}, files=[p for p, _b in writes], grade_down=down, pairs=pairs)
    open(DIFF_JSON + '.tmp', 'wb').write(json.dumps(js, ensure_ascii=False, indent=1).encode('utf-8'))
    os.replace(DIFF_JSON + '.tmp', DIFF_JSON)
    print('### WRITTEN: %d files ; %s ; %s' % (len(writes), DIFF_TXT, DIFF_JSON))


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ('dry', 'run'):
        print(__doc__)
        sys.exit(2)
    args = sys.argv[2:]
    if '--diff' in args:          # ### b682: the run's diff banks under another stem, b672's left as they stand
        i = args.index('--diff')
        stem = args[i + 1]
        if not re.match(r'^b\d+_[a-z_]+$', stem):
            sys.exit('### --diff takes a bank stem such as b682_correspondence_run -- NOTHING WRITTEN')
        DIFF_TXT, DIFF_JSON = os.path.join(D, stem + '.txt'), os.path.join(D, stem + '.json')
        args = args[:i] + args[i + 2:]
    rest = [x for x in args if x != 'full']
    main(sys.argv[1], *(rest[:1] or [ROSTER]), full='full' in args)
