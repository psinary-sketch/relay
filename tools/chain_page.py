# -*- coding: utf-8 -*-
"""chain_page.py -- THE PAGE WITHOUT NARRATIVE, GENERATED. ### (R178)(4)-(5), written at b568 (CP-4, lane three, act one).

### ### **WHAT IT DOES.** Reads a node list (relay data/b568_nodes.txt), refuses unless the kernel checkout is at the pin
### with no tracked change, writes ONE probe file into a given directory, elaborates it by ONE `lake env lean` call from the
### kernel checkout, parses Lean's own output, and emits the page: the head, one line per node in dependency order, the
### open-node line, the last derived line (README :121's bytes at PLACE-papers HEAD), and two tables (Placement,
### Correspondence). Every cell of a node line comes from the probe or from a committed blob, never from the node list:
###   module:line      -- Lean's declaration range and module index (`findDeclarationRanges?`, `getModuleIdxFor?`)
###   entry tag = SHA  -- the first kernel tag (by creation date) whose tree declares the name in that file (git)
###   statement        -- `#print` for a definition, `#print sig` for a theorem (#print's own header, no proof term);
###                       whitespace runs collapsed to one space, the cell's one transformation
###   premises, E0     -- relay tools/e0_rule.py on the declaration's SOURCE header at the pin (`#print sig` renders an
###                       unnamed hypothesis as an arrow, so the binder rule reads the source, as b566/b567 did)
###   tier             -- a tier written in the name's record grade cell (relay data/terminal_table.json at relay HEAD)
###                       when one is, else the tier law (b539 ferry :20-:31; FINDINGS :4819, :5812) on the grade and print
###   axioms           -- `#print axioms`
###   consumes         -- the node-list constants reached from the node's type and value, following every constant of
###                       the kernel's, Zeta23's and Bulka's modules that is not a node, stopping at nodes; Mathlib not followed
### ### **IT CONFERS NO GRADE.** The E0 grade is the shared rule's reading; the record grade is carried from the table.
### ### **DETERMINISTIC BY CONSTRUCTION:** no time, path or run-dependent text enters the page; a second run from the same
### node list at the same pins writes the same bytes (H20c).

### Usage:
###   python tools/chain_page.py --nodes <nodes.txt> --probe-dir <dir> --out <page.md> [--cells <cells.json>]
###   python tools/chain_page.py --nodes <nodes.txt> --probe-dir <dir> --out <page.md> --from-output <probe_out.txt>
###     (re-emit from a banked probe output without elaborating: the parser and emitter only)
### Exit: 0 written; 2 usage; 3 the checkout refused; 4 free memory below the hold; 5 the probe failed; 6 a node unresolved;
### 7 (R179)(4) a node's tier computed from its printed facts disagrees with the table's tier cell -- a CONFLICT, no page.
### ### (R179)(4), b569: a node list carrying `# pin: <tag>` is generated at that tag, with the tier key on the head and the
### table's tier printed beside every node's computed tier (`tier_of_node`); a list without one is generated as at b568.
### (R232)(4), b622: a node list carrying `# column: quantifier` takes the shape cell after each node's statement and the key's head
### line (`node_column`, `shape_of`); a list without it is generated exactly as before.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import e0_rule as E0   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NL = chr(10)
KER = 'D:/SIDE-explicit-formula'
PP = 'D:/MY-DOwnloads/PLACE-papers'
PIN_TAG = 'v0.10'
PIN = '6baed63ae664a22db1f325177b81253e270de6e3'
MATHLIB = 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11'
ZETA23 = '3635e748'
BULKA = '35df682f'
TOOLCHAIN = 'leanprover/lean4:v4.34.0-rc1'
STD3 = ['propext', 'Classical.choice', 'Quot.sound']
HOLD_MB = 2560
PAGE_NAME = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
OPEN_LINE = ('h2_sign — open; by the compiled equivalences above, the same open statement as Li positivity and as '
             'arithmetic-limit positivity.')
# ### (R183)(5), b573: THE DIRICHLET VARIANT. A node list carrying `# page: dirichlet` is the χ-leg's: its page is written
# ### under its own name and title, with the ruled open line, its last derived line the (R183)(3) successor sentence as the
# ### author wrote it (read from README's placed line at PLACE-papers HEAD), the ζ page as a Placement row, and the graded
# ### χ-side names as its Correspondence rows; its probe also imports the χ and schema modules at the pin. A list without
# ### `# page:` is generated exactly as before (b568's and b569's lists still regenerate their page byte for byte).
DIR_PAGE_NAME = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
DIR_TITLE = '# THE CLAUSE AT THE DIRICHLET INSTANCE'
DIR_OPEN_LINE = ('GRH_chi — open, for each primitive χ ≠ 1; by the compiled equivalence the same open statement as Weil positivity '
                 'on classK for χ')
DIR_CEIL_MARK = "*(Appended under the author's ruling `(R183)`(3)"
DIR_CEIL_OPEN = "Supportable, the author's sentence: *"
SCHEMA_PREFIX = 'SIDEExplicitFormula.Schema.'
VARIANT = None
BULKA_ROOTS = ('Lc', 'Hadamard', 'FunctionsOfOneComplexVariable')
LEDGERS = ['FINDINGS.md', 'OPEN_TRAILS.md', 'ERRATA.md', 'FACES_LEDGER.md']
CHI_PREFIX = 'SIDEExplicitFormula.GRHWeil.'


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


# ================================================================================ the node list
def node_pin(path):
    """### (R179)(4), b569: the node list names the kernel tag the page is generated at by one line `# pin: <tag>`; a list
    ### without one is generated at v0.10 (b568's list, unchanged). The tag is resolved by git; None when it does not resolve."""
    tag = PIN_TAG
    for raw in io.open(path, encoding='utf-8'):
        m = re.match(r'^# pin: (\S+)\s*$', raw.rstrip('\r\n'))
        if m:
            tag = m.group(1)
    rc, sha = git(KER, 'rev-parse', '--verify', '-q', tag + '^{commit}')
    return tag, (sha.strip() if rc == 0 and len(sha.strip()) == 40 else None)


def node_variant(path):
    """### (R183)(5): the page variant a node list names by one line `# page: <name>`; None for a list without one."""
    v = None
    for raw in io.open(path, encoding='utf-8'):
        m = re.match(r'^# page: (\S+)\s*$', raw.rstrip('\r\n'))
        if m:
            v = m.group(1)
    return v


def page_name_of(path):
    """### the page file a node list generates: the Dirichlet page for `# page: dirichlet`, else the ζ page."""
    return DIR_PAGE_NAME if node_variant(path) == 'dirichlet' else PAGE_NAME


def read_nodes(path):
    nodes, drops, corr, marks = [], [], [], []
    for raw in io.open(path, encoding='utf-8'):
        line = raw.rstrip('\n').rstrip('\r')
        if line.startswith('# DROP '):
            name, why = line[len('# DROP '):].split(' : ', 1)
            drops.append(dict(name=name.strip(), why=why.strip()))
        elif not line.strip() or line.startswith('#'):
            continue
        elif line.startswith('@corr '):
            f = [x.strip() for x in line[len('@corr '):].split(' | ')]
            corr.append(dict(repo=f[0], name=f[1], grade=f[2], tier=f[3], note=f[4] if len(f) > 4 else ''))
        elif line.startswith('@mark '):
            marks.append(line[len('@mark '):].strip())
        else:
            f = [x.strip() for x in line.split(' | ')]
            nodes.append(dict(name=f[0], source=f[1], role=f[2]))
    return nodes, drops, corr, marks


def backmatter_of(path):
    """### b596, the author's answer before its seal: a node list's `# backmatter: <line>` records, in list order; the page
    ### carries them as one paragraph after the Correspondence table. A list without one emits exactly as before."""
    return [raw.rstrip('\n').rstrip('\r')[len('# backmatter: '):] for raw in io.open(path, encoding='utf-8') if raw.startswith('# backmatter: ')]


# ================================================================================ the record grades (relay HEAD's table)
def record_rows():
    rc, out = git(ROOT, 'show', 'HEAD:data/terminal_table.json')
    if rc:
        return {}
    rows = json.loads(out).get('rows', [])
    return {r['name']: r for r in rows if r.get('repo') == 'SIDE-explicit-formula'}


def record_tier(row):
    for c in (row or {}).get('grade_cells') or []:
        m = re.search(r'\btier (T[0-4](?:-[A-Za-z]+)?)\b', c.get('quote') or '')
        if m:
            return m.group(1), '%s:%s' % (c.get('ledger'), c.get('line'))
    return None, None


# ================================================================================ the probe
PROBE_HEAD = r'''@@IMPORTS@@
import Lean

/-! relay tools/chain_page.py's probe (b568, (R178)(5)). Written by the generator; not a kernel file. -/

open Lean Elab Command

namespace ChainPageProbe

def bulkaRoots : List Name := [`Lc, `Hadamard, `FunctionsOfOneComplexVariable]

def followed (m : Name) : Bool :=
  let r := m.getRoot
  r == `SIDEExplicitFormula || r == `Zeta23 || bulkaRoots.contains r

def modOf (env : Environment) (c : Name) : Name :=
  match env.getModuleIdxFor? c with
  | some i => env.header.moduleNames[i.toNat]!
  | none => Name.anonymous

/-- the node-list constants reached from `start`'s type and value, following non-node constants of the kernel's,
Zeta23's and Bulka's modules; also every followed constant under a watched prefix. -/
def consumes (env : Environment) (nodes : NameSet) (watch : List Name) (start : Name) : Array Name × Array Name := Id.run do
  let some ci := env.find? start | return (#[], #[])
  let mut stack : Array Name := ci.getUsedConstantsAsSet.toArray
  let mut seen : NameSet := {}
  let mut found : Array Name := #[]
  let mut watched : Array Name := #[]
  while stack.size > 0 do
    let c := stack.back!
    stack := stack.pop
    if seen.contains c then continue
    seen := seen.insert c
    if c == start then continue
    if watch.any (fun p => p.isPrefixOf c) then watched := watched.push c
    if nodes.contains c then
      found := found.push c
      continue
    if followed (modOf env c) then
      if let some cj := env.find? c then
        for d in cj.getUsedConstantsAsSet.toArray do
          unless seen.contains d do stack := stack.push d
  return (found, watched)

def kindOf (env : Environment) (n : Name) : String :=
  match env.find? n with
  | some (.thmInfo _) => "theorem"
  | some (.defnInfo _) => "def"
  | some (.axiomInfo _) => "axiom"
  | some (.opaqueInfo _) => "opaque"
  | some (.inductInfo _) => "inductive"
  | some _ => "other"
  | none => "MISSING"

end ChainPageProbe

open ChainPageProbe in
elab "#chain_cell " id:ident " [" ns:ident,* "]" " [" ws:ident,* "]" : command => do
  let env ← getEnv
  let n := id.getId
  let nodes : NameSet := ns.getElems.foldl (fun s i => s.insert i.getId) {}
  let watch := ws.getElems.toList.map (·.getId)
  let k := kindOf env n
  logInfo m!"@@BEGIN {n}"
  if k == "MISSING" then
    logInfo m!"@@MISSING {n}"
  else
    let r? ← findDeclarationRanges? n
    let line : Nat := match r? with | some r => r.selectionRange.pos.line | none => 0
    let (found, watched) := consumes env nodes watch n
    logInfo m!"@@CELL @@KIND {k} @@MODULE {modOf env n} @@LINE {line} @@CONSUMES {found.toList} @@WATCHED {watched.toList}"
    logInfo m!"@@STMT"
    if k == "theorem" then
      elabCommand (← `(command| #print sig $(mkIdent n):ident))
    else
      elabCommand (← `(command| #print $(mkIdent n):ident))
    logInfo m!"@@AXIOMS"
    elabCommand (← `(command| #print axioms $(mkIdent n):ident))
  logInfo m!"@@END {n}"
'''


def probe_imports():
    """### every top-level kernel module at the pin but the chi-leg's (GRHWeil.lean; Chi/ is a subdirectory and not listed):
    ### the root module SIDEExplicitFormula.lean imports only Zeta23.WeilEF.Main, so it cannot stand for the kernel."""
    rc, out = git(KER, 'ls-tree', '--name-only', PIN, 'SIDEExplicitFormula/')
    mods = sorted(x[:-5].replace('/', '.') for x in out.split(NL) if x.endswith('.lean') and not x.endswith('/GRHWeil.lean'))
    if VARIANT == 'dirichlet':
        # ### (R183)(5): the χ-leg's page also imports GRHWeil and every module of Chi/ and Schema/ at the pin
        rc2, out2 = git(KER, 'ls-tree', '-r', '--name-only', PIN, 'SIDEExplicitFormula/Chi/', 'SIDEExplicitFormula/Schema/')
        mods += ['SIDEExplicitFormula.GRHWeil'] + sorted(x[:-5].replace('/', '.') for x in out2.split(NL) if x.endswith('.lean'))
    return NL.join('import %s' % m for m in mods)


def probe_text(names, all_nodes, watch):
    ids = ', '.join(all_nodes)
    w = ', '.join(watch)
    return (PROBE_HEAD.replace('@@IMPORTS@@', probe_imports()) + NL
            + NL.join('#chain_cell %s [%s] [%s]' % (n, ids, w) for n in names) + NL)


def free_mb():
    try:
        out = subprocess.run(['powershell', '-NoProfile', '-Command',
                              '(Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory'], capture_output=True, text=True).stdout
        return int(out.strip()) // 1024
    except Exception:
        return -1


def run_probe(probe_dir, text):
    os.makedirs(probe_dir, exist_ok=True)
    p = os.path.join(probe_dir, 'chain_page_probe.lean')
    io.open(p, 'w', encoding='utf-8', newline=NL).write(text)
    out = os.path.join(probe_dir, 'chain_page_probe_out.txt')
    with open(out, 'wb') as fh:
        r = subprocess.run(['lake', 'env', 'lean', p], cwd=KER, stdout=fh, stderr=subprocess.STDOUT)
    return r.returncode, io.open(out, encoding='utf-8', errors='replace').read().replace(chr(13), '')


# ================================================================================ the parser
def parse(out):
    """### blocks between `@@BEGIN n` and `@@END n`; inside, the CELL line, the #print text after @@STMT, the axioms line."""
    cells = {}
    errors = [l for l in out.split(NL) if re.search(r':\d+:\d+: error', l)]
    for m in re.finditer(r'^@@BEGIN (\S+)\n(.*?)^@@END \1$', out, re.M | re.S):
        n, body = m.group(1), m.group(2)
        if '@@MISSING ' in body:
            cells[n] = dict(missing=True)
            continue
        # ### Lean's formatter wraps a long list across lines: the CELL message is read with its line breaks collapsed.
        cm = re.search(r'^@@CELL (.*?)(?=^@@STMT$)', body, re.M | re.S)
        cl = ' '.join(cm.group(1).split()) if cm else ''
        c = re.match(r'^@@KIND (\S+) @@MODULE (\S+) @@LINE (\d+) @@CONSUMES \[(.*?)\] @@WATCHED \[(.*?)\]$', cl)
        st = re.search(r'^@@STMT\n(.*?)^@@AXIOMS\n(.*)\Z', body, re.M | re.S)
        if not c or not st:
            cells[n] = dict(missing=True, raw=body[:400])
            continue
        stmt = ' '.join(st.group(1).split())
        ax_text = ' '.join(st.group(2).split())
        am = re.match(r"^'(.+?)' depends on axioms: \[(.*)\]$", ax_text)
        axioms = [x.strip() for x in am.group(2).split(',')] if am else ([] if 'does not depend on any axioms' in ax_text else None)
        split = lambda s: [x.strip() for x in s.split(',') if x.strip()]
        cells[n] = dict(kind=c.group(1), module=c.group(2), line=int(c.group(3)), consumes=split(c.group(4)),
                        watched=split(c.group(5)), statement=stmt, axioms=axioms, axioms_text=ax_text)
    return cells, errors


# ================================================================================ the source reads at the pin
def module_path(mod):
    parts = mod.split('.')
    rel = '/'.join(parts) + '.lean'
    if parts[0] in BULKA_ROOTS:
        return 'Vendored/Bulka/' + rel
    return rel


def source_at(rev, rel, cache={}):
    k = (rev, rel)
    if k not in cache:
        rc, out = git(KER, 'show', '%s:%s' % (rev, rel))
        cache[k] = None if rc else out
    return cache[k]


DECL = r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev|irreducible_def)\s+'


def source_header(src, short, line):
    """### the text between the declared name and its `:=`, from the declaration at `line` (1-based)."""
    if src is None:
        return None
    rest = NL.join(src.split(NL)[line - 1:])
    m = re.match(DECL + r'(?:[A-Za-z_][\w]*\.)*' + re.escape(short) + r'(?![\w\'₀-₉])(.*?):=', rest, re.S)
    return ' '.join(m.group(1).split()) if m else None


def entry_tag(rel, short):
    rc, out = git(KER, 'tag', '--sort=creatordate')
    pat = re.compile(DECL + r'(?:[A-Za-z_][\w]*\.)*' + re.escape(short) + r'(?![\w\'₀-₉])', re.M)
    pat = re.compile(DECL.replace('irreducible_def)', 'irreducible_def|structure)') + r'(?:[A-Za-z_][\w]*\.)*' + re.escape(short) + r'(?![\w\'₀-₉])', re.M)  # b596, the author's answer: a structure node's entry tag
    for t in [x for x in out.split(NL) if x.strip()]:
        src = source_at(t, rel)
        if src and pat.search(src):
            rc2, sha = git(KER, 'rev-parse', '--short=7', t + '^{commit}')
            return t, sha.strip()
    return None, None


# ================================================================================ grades and tiers
def premise_heads(prem_text):
    return re.findall(r'^\s*([A-Za-z_][\w.]*)', prem_text or '')


def tier_of(kind, grade_e0, why, axioms, rec_row, nodeset):
    """### RETURN (tier, source). A definition carries no tier. A tier written in the record cell wins."""
    if kind != 'theorem':
        return '—', 'a definition; the law tiers terminals'
    std3 = axioms is not None and set(axioms) <= set(STD3)
    if not std3:   # ### the print is read FIRST: no record cell lifts a print beyond the three
        return 'NOT T0', 'axioms beyond the standard three'
    t, src = record_tier(rec_row)
    if t:
        return t, 'the record cell ' + src
    rec_g = (rec_row or {}).get('grade')
    if rec_g in ('ENCODES-CONCLUSION', 'ENCODES', 'SHELL'):
        return 'T2', 'the tier law on the record grade %s' % rec_g
    if rec_g == 'CONFLICT':
        return 'CONFLICT', 'the record grade CONFLICT'
    g = rec_g if rec_g in ('DERIVES', 'INTERFACES') else grade_e0
    if g == 'DERIVES':
        return 'T0', 'the tier law: compiled, the standard three, no premise'
    heads = [h for part in (why or '').split(', ') for h in premise_heads(part.split(' : ', 1)[-1])]
    if any(h.split('.')[-1] == 'h2_sign' for h in heads):
        return 'T1-open', 'the tier law: INTERFACES on h2_sign'
    return 'T2-INTERFACES', 'the tier law`s programme-premise clause (FINDINGS :5812): INTERFACES on %s' % (', '.join(heads) or '?')


# ### ### **(R179)(4), b569: THE TIER CELL OF A NODE, DEFINED WHERE THE PAGE IS READ.** *A node's tier cell is computed from
# ### three printed facts -- grade DERIVES, the standard three, no premise -- and reads T0 when all three hold, with the law's
# ### "compiled against a Mathlib statement" clause witnessed by the consumes column and not separately tested. The terminal
# ### table's tier cell, where one exists, is printed beside it and any disagreement is a CONFLICT the regeneration refuses.*
# ### The table has no tier column; its tier cell is read as a tier WRITTEN in the name's record ledger cell (`record_tier`).
# ### Where the three facts do not all hold, the tier law's other clauses apply to the printed facts as before (NOT T0 for a
# ### print beyond the three; T1-open for INTERFACES on h2_sign; T2-INTERFACES otherwise); a record GRADE no longer lifts or
# ### lowers a node's tier. The Correspondence table's rows (not nodes) keep `tier_of`.
TIER_KEY = ('A node\'s tier cell is computed from three printed facts — E0 grade DERIVES, the axioms the standard three '
            '[propext, Classical.choice, Quot.sound], no premise — and reads T0 when all three hold, the tier law\'s clause '
            '"compiled against a Mathlib statement" being witnessed by the consumes column (Mathlib\'s `RiemannHypothesis` or '
            '`riemannZeta` among the constants the anchor nodes consume) and not separately tested; the terminal table\'s '
            'tier cell for the node, where one exists, is printed beside it as `table:`, and a disagreement refuses the page.')


def tier_of_node(kind, grade_e0, why, axioms, rec_row):
    """### RETURN (tier, source, table tier or None, conflict: bool) -- (R179)(4)."""
    t_rec, src = record_tier(rec_row)
    if kind != 'theorem':
        return '—', 'a definition; the law tiers terminals', t_rec, bool(t_rec)
    std3 = axioms is not None and set(axioms) <= set(STD3)
    if not std3:
        t, s = 'NOT T0', 'axioms beyond the standard three'
    elif grade_e0 == 'DERIVES':
        t, s = 'T0', 'the three printed facts: E0 DERIVES, the standard three, no premise'
    else:
        heads = [h for part in (why or '').split(', ') for h in premise_heads(part.split(' : ', 1)[-1])]
        if any(h.split('.')[-1] == 'h2_sign' for h in heads):
            t, s = 'T1-open', 'the tier law: INTERFACES on h2_sign'
        else:
            t, s = 'T2-INTERFACES', 'the tier law`s programme-premise clause (FINDINGS :5812): INTERFACES on %s' % (', '.join(heads) or '?')
    return t, s + ('; the table`s tier %s at %s' % (t_rec, src) if t_rec else ''), t_rec, bool(t_rec) and t_rec != t


# ================================================================================ the order
def dep_order(names, consumes):
    idx = {n: i for i, n in enumerate(names)}
    pending = {n: set(c for c in consumes.get(n, []) if c in idx) for n in names}
    out = []
    while pending:
        ready = sorted((n for n, d in pending.items() if not d), key=lambda n: idx[n])
        if not ready:
            return None
        n = ready[0]
        out.append(n)
        del pending[n]
        for d in pending.values():
            d.discard(n)
    return out


# ================================================================================ the quantifier column (b622, (R232)(4))
# ### W-ORD-QUANTIFIER-COLUMN (OPEN_TRAILS :12266, DENSITY :12296): each node's shape read from its statement as the probe printed it.
# ### The proposition read: a theorem's type; a Prop-valued definition's body after its `fun` parameters; a Prop structure's fields,
# ### joined as a conjunction; any other definition is an object and reads '—'. At each step: `¬` is passed through; an iff, a
# ### conjunction or a disjunction reads the higher of its sides in the order of SHAPES; a premise (`A → B`) is passed over to B; a
# ### leading binder group is read by its domains (a configuration, a character, a type or a family of them FAMILY; ℕ, ℤ, ℚ, ℝ, ℂ and
# ### functions among them UNIVERSAL, FINITE when a numeral bounds them above; a proof binder passed over; `x ∈ S` by S) and its body
# ### read on; the eventual form `∀ ε > 0, ∃ T₀, ∀ T ≥ T₀, X` reads LIMIT, DENSITY when X compares counting functions; an atom is a
# ### comparison (FINITE), a `Filter.Tendsto` (LIMIT), a Prop of the page read through its own statement, or unread. A node with nothing
# ### read reads UNCLASSIFIED, for the author's ruling.
# ### b627, (R237)(3): BOUNDED, between FINITE and UNIVERSAL -- a number-typed binder whose body carries a premise bounding the
# ### variable's height (`|x.im|`), norm (`‖x‖`, `|x|`, `Complex.abs x`) or, for ℕ and ℤ, its index (`x`) above by a term free of x
# ### (`_measure_bounded`); FINITE as it read before, for Finset and finite-range forms.
SHAPES = ('FINITE', 'BOUNDED', 'UNIVERSAL', 'LIMIT', 'DENSITY', 'FAMILY')
COLUMN_MARK = '# column: quantifier'
SHAPE_KEY = ('The shape cell after each statement is read by the generator from the statement\'s leading binders as the probe printed '
             'it: FINITE for a closed statement or a finite range (a cell, a window, a Finset, a count up to T), BOUNDED for a quantifier '
             'over the zeros, the primes, the integers or the reals whose body bounds the variable\'s height, norm or index by an explicit '
             'term, UNIVERSAL for one with no bound, LIMIT for a Filter.Tendsto or an eventual ε–T₀ form, DENSITY for that '
             'form over a proportion of counts, FAMILY for a quantifier over a class of objects (every character, every configuration); an '
             'iff or a conjunction reads the higher of its sides in that order, a premise is passed over, a Prop on the page is read through '
             'its own statement, a node with nothing the reader can read is printed UNCLASSIFIED for the author\'s ruling, and a definition '
             'of an object, not a Prop, reads —.')
_FAMILY_TY = r'\b(WeilConfig|ZeroConfig|DirichletCharacter)\b'
_COUNT_FNS = r'\b(Ncount|N0simple|Nat\.count|Finset\.card|Set\.ncard|Nat\.card)\b'
_NUMBER_TY = r'^[\s()ℕℤℚℝℂ→]+$'
_RELS = (' = ', ' ≠ ', ' < ', ' ≤ ', ' > ', ' ≥ ')
_OPEN, _CLOSE = '([{⟨', ')]}⟩'


def node_column(path):
    """### b622, (R232)(4): a node list carrying `# column: quantifier` is emitted with the shape column and the key's head line; a list
    ### without it emits exactly as before."""
    return any(raw.rstrip('\r\n') == COLUMN_MARK for raw in io.open(path, encoding='utf-8'))


# ### b638, (R248)(4), THE READER'S CLAUSE: a node list carrying the one line `# glossary` is emitted with the glossary block beneath the
# ### page's head line -- every internal name the two pages and the keystone census use, defined in the programme's own words, printed
# ### from relay data/glossary.txt, the one shared source the census prints through this same renderer, so the block reads byte for byte
# ### alike in all three. A list without the line emits exactly as before.
GLOSSARY_MARK = '# glossary'
GLOSSARY_FILE = os.path.join(ROOT, 'data', 'glossary.txt')
GLOSSARY_HEAD = '## Glossary'
GLOSSARY_INTRO = ('*The internal names this document uses, each defined in the programme’s own words with where the programme states it. '
                  'The block is printed by relay `tools/chain_page.py` from relay `data/glossary.txt`, one source shared by the two generated '
                  'pages and the keystone census, so it reads the same in all three.*')


def node_glossary(path):
    """### b638, (R248)(4): True for a node list carrying the line `# glossary`."""
    return any(raw.rstrip('\r\n') == GLOSSARY_MARK for raw in io.open(path, encoding='utf-8'))


def glossary_entries(path=None):
    """### b638: the glossary's entries in its file's order, (name, definition, source); a line beginning # is a comment."""
    out = []
    for raw in io.open(path or GLOSSARY_FILE, encoding='utf-8'):
        line = raw.rstrip('\n').rstrip('\r')
        if not line.strip() or line.startswith('#'):
            continue
        f = line.split('\t')
        if len(f) != 3 or not all(x.strip() for x in f):
            raise ValueError('a glossary line is not name, definition and source: %r' % line[:80])
        out.append(tuple(x.strip() for x in f))
    return out


def glossary_block(path=None):
    """### b638: the glossary block's lines -- its heading, its one-line introduction, one line per entry."""
    return [GLOSSARY_HEAD, '', GLOSSARY_INTRO, ''] + ['- **%s** — %s *(%s)*' % e for e in glossary_entries(path)]


def _wraps(s):
    d = 0
    for i, ch in enumerate(s):
        if ch in _OPEN:
            d += 1
        elif ch in _CLOSE:
            d -= 1
            if d == 0 and i != len(s) - 1:
                return False
    return True


def _strip(s):
    s = s.strip()
    while len(s) > 1 and s[0] == '(' and s[-1] == ')' and _wraps(s):
        s = s[1:-1].strip()
    return s


def _split(s, op):
    """### s split at its FIRST top-level `op`; None when there is none before a binder (whose body runs to the end)."""
    d = 0
    for i, ch in enumerate(s):
        if ch in _OPEN:
            d += 1
        elif ch in _CLOSE:
            d -= 1
        elif d == 0 and s.startswith(op, i):
            return s[:i].strip(), s[i + len(op):].strip()
        elif d == 0 and (ch in '∀∃' or (s.startswith('fun ', i) and (i == 0 or s[i - 1] == ' '))):
            return None
    return None


def _group(s):
    """### s opens with ∀ or ∃: (the binder text, the body)."""
    d = 0
    for i in range(1, len(s)):
        ch = s[i]
        if ch in _OPEN:
            d += 1
        elif ch in _CLOSE:
            d -= 1
        elif ch == ',' and d == 0:
            return s[1:i].strip(), s[i + 1:].strip()
    return s[1:].strip(), ''


def _binders(text):
    """### [(name, type or set or bound, relation or None)]: `(x y : T)`, `{N : ℕ}`, `x ∈ S`, `x ≤ c`, bare names; instance binders dropped."""
    out = []
    for m in re.finditer(r'\(([^():]+?) : ((?:[^()]|\((?:[^()]|\([^()]*\))*\))+)\)|\{([^{}:]+?) : ([^{}]+)\}|\[[^\[\]]*\]', text):
        if m.group(1) is None and m.group(3) is None:
            continue
        for nm in (m.group(1) or m.group(3)).split():
            out.append((nm, (m.group(2) or m.group(4)).strip(), None))
    rest = re.sub(r'\((?:[^()]|\((?:[^()]|\([^()]*\))*\))*\)|\{[^{}]*\}|\[[^\[\]]*\]', ' ', text).strip()
    if rest:
        m = re.match(r'^(.+?)\s+(∈|≤|<|≥|>)\s+(.+)$', rest)
        t = re.match(r'^([^:∈≤<≥>]+?) : (.+)$', rest)   # ### `x y : T` unparenthesized, as a source file writes it
        if t:
            out += [(nm, t.group(2).strip(), None) for nm in t.group(1).split()]
        elif m:
            out += [(nm, m.group(3).strip(), m.group(2)) for nm in m.group(1).split()]
        else:
            out += [(nm, None, None) for nm in rest.split()]
    return out


def _bounded(nm, body):
    s = body
    while True:
        sp = _split(s, ' → ')
        if not sp:
            return False
        if re.fullmatch(re.escape(nm) + r' (≤|<) \d+', _strip(sp[0])):
            return True
        s = sp[1]


def _measure_bounded(nm, ty, body):
    """### b627, (R237)(3): a premise of the body bounding the variable's height (`|x.im|`), norm (`‖x‖`, `|x|`, `Complex.abs x`) or,
    ### for ℕ and ℤ, its index (`x` itself) above by a term that does not mention it."""
    v = re.escape(nm)
    meas = [r'\|%s\.im\|' % v, r'‖%s‖' % v, r'\|%s\|' % v, r'Complex\.abs %s' % v] + ([v] if ty.strip() in ('ℕ', 'ℤ') else [])
    s = body
    while True:
        sp = _split(s, ' → ')
        if not sp:
            return False
        m = re.fullmatch(r'(%s) (≤|<) (.+)' % '|'.join(meas), _strip(sp[0]))
        if m and not re.search(r'(?<![\w.\'])%s(?![\w\'₀-₉])' % v, m.group(3)):
            return True
        s = sp[1]


def _domain(nm, ty, rel, body, env, tys):
    if rel in ('≤', '<'):
        return 'FINITE' if re.fullmatch(r'\d+', ty) else 'UNIVERSAL'
    if rel in ('≥', '>'):
        return 'UNIVERSAL'
    if rel == '∈':
        h = ty.split()[0]
        if h in env:
            return 'FAMILY' if re.search(_FAMILY_TY, env[h]) or re.search(r'Finset (ι|\(?Type)', env[h]) or env[h].split()[-1] in env else 'FINITE'
        return 'FAMILY' if re.search(_FAMILY_TY, tys.get(h, '')) else 'UNIVERSAL'
    if ty is None:
        return None
    if re.search(_FAMILY_TY, ty) or re.match(r'^(Type|Sort)\b', ty) or any(re.search(r'\b%s\b' % re.escape(v), ty) for v, t in env.items()
                                                                          if re.match(r'^(Type|Sort)\b', t)):
        return 'FAMILY'
    if re.match(_NUMBER_TY, ty):
        if ty.strip() in ('ℕ', 'ℤ') and _bounded(nm, body):
            return 'FINITE'
        return 'BOUNDED' if _measure_bounded(nm, ty, body) else 'UNIVERSAL'
    return None   # ### a proof binder: a premise, passed over


def _top(parts):
    known = [p for p in parts if p in SHAPES]
    return max(known, key=SHAPES.index) if known else None


def _read(s, cells, tys, env, seen, depth):
    s = _strip(s)
    if depth > 40 or not s:
        return None
    if s.startswith('¬'):
        return _read(s[1:], cells, tys, env, seen, depth + 1)
    for op in (' ↔ ', ' ∧ ', ' ∨ '):
        sp = _split(s, op)
        if sp:
            return _top([_read(x, cells, tys, env, seen, depth + 1) for x in sp])
    sp = _split(s, ' → ')
    if sp:
        return _read(sp[1], cells, tys, env, seen, depth + 1)
    if s[0] in '∀∃':
        m = re.match(r'^∀ \S+ > 0, ∃ (\S+), ∀ \S+ ≥ \1, (.*)$', s)
        if m:
            return 'DENSITY' if re.search(_COUNT_FNS, m.group(2)) else 'LIMIT'
        bt, body = _group(s)
        env = dict(env)
        bs = _binders(bt)
        for nm, ty, rel in bs:
            if rel is None and ty is not None:
                env[nm] = ty
        return _top([_domain(nm, ty, rel, body, env, tys) for nm, ty, rel in bs] + [_read(body, cells, tys, env, seen, depth + 1)])
    head = s.split()[0].lstrip('@')
    if head == 'Filter.Tendsto':
        return 'LIMIT'
    if head in ('Filter.liminf', 'Filter.limsup'):
        return 'DENSITY' if re.search(_COUNT_FNS, s) else 'LIMIT'
    if any(_split(s, r) for r in _RELS):
        return 'FINITE'
    if head in cells and head not in seen:
        return _shape(head, cells, tys, seen | {head}, depth + 1)
    return None


def _prop(c):
    """### ('prop', text) | ('fields', [texts]) | ('object', None) | (None, None)"""
    st = re.sub(r'^@\[[^\]]*\]\s*', '', c.get('statement') or '')
    if c.get('kind') == 'theorem':
        m = re.match(r'^theorem \S+ : (.*)$', st)
        return ('prop', m.group(1)) if m else (None, None)
    if c.get('kind') == 'inductive':
        m = re.match(r'^(?:inductive )?structure (\S+).*? : Prop number of parameters: \d+ fields: (.*?) constructor: ', st)
        if not m:
            return ('object', None)
        fs = re.split(r' (?=%s\.[^\s.]+ : )' % re.escape(m.group(1)), m.group(2))
        return ('fields', [f.split(' : ', 1)[1] for f in fs if ' : ' in f])
    m = re.match(r'^def \S+ : (.*?) := (.*)$', st)
    if not m:
        return (None, None)
    if not (m.group(1) == 'Prop' or m.group(1).endswith('→ Prop')):
        return ('object', None)
    return ('prop', re.sub(r'^fun .*? => ', '', m.group(2), count=1))


def _shape(n, cells, tys, seen, depth):
    k, p = _prop(cells[n])
    if k == 'object':
        return '—'
    if k == 'fields':
        return _top([_read(f, cells, tys, {}, seen, depth + 1) for f in p])
    return _read(p, cells, tys, {}, seen, depth + 1) if k == 'prop' else None


def shape_of(n, cells):
    """### the node's shape: one of SHAPES, '—' for an object, or 'UNCLASSIFIED'. `cells` is the parser's, every cell of the probe."""
    live = {k: v for k, v in cells.items() if not v.get('missing')}
    tys = {}
    for k, v in live.items():
        m = re.match(r'^(?:@\[[^\]]*\]\s*)?(?:def|theorem) \S+ : (.*?)(?: := .*)?$', v.get('statement') or '')
        tys[k] = m.group(1) if m else ''
    r = _shape(n, live, tys, {n}, 0)
    return r if r in SHAPES or r == '—' else 'UNCLASSIFIED'


# ================================================================================ the page
def ceiling_line():
    rc, out = git(PP, 'show', 'HEAD:README.md')
    lines = out.split(NL)
    return lines[120] if len(lines) > 120 else ''


def dir_ceiling():
    """### (R183)(5): the successor sentence of (R183)(3), as the author wrote it, read from README's placed line at PLACE-papers
    ### HEAD (between `Supportable, the author's sentence: *` and the closing `*`); with the line numbers at README and REGISTRY."""
    rc, out = git(PP, 'show', 'HEAD:README.md')
    rc2, out2 = git(PP, 'show', 'HEAD:REGISTRY.md')
    rl = [i for i, l in enumerate(out.split(NL), 1) if l.startswith(DIR_CEIL_MARK)]
    gl = [i for i, l in enumerate(out2.split(NL), 1) if l.startswith(DIR_CEIL_MARK)]
    if len(rl) != 1:
        return '', rl, gl
    line = out.split(NL)[rl[0] - 1]
    a = line.find(DIR_CEIL_OPEN)
    b = line.find('*', a + len(DIR_CEIL_OPEN)) if a >= 0 else -1
    return (line[a + len(DIR_CEIL_OPEN):b] if a >= 0 and b > 0 else ''), rl, gl


def keystones(short_names):
    # ### b592, the author's answer before its seal (relay data/b592_author_answers.txt, prompt 7): a node whose short name is a
    # ### plain lower-case word (`detector`) names a keystone only by its qualified name or in backticks, so that a file using
    # ### the English word is not read as naming the node. A list with no such name builds the pattern exactly as before.
    # ### b629, the author's answer after its seal (relay data/b629_author_answers.txt, prompt 3): the guard extended in the same
    # ### terms to a short name of upper-case letters alone (`NB`, `BD`), so that an acronym in prose ('NB:', '(BD)') is not read
    # ### as naming the node. A list with no such name still builds the pattern exactly as before.
    plain = sorted(s for s in short_names if re.fullmatch(r'[a-z]+|[A-Z]+', s))
    rest = sorted(s for s in short_names if s not in plain)
    alts = [r'\b(' + '|'.join(re.escape(s) for s in rest) + r')\b'] if rest else []
    alts += [r'(`' + re.escape(s) + r'`|[A-Za-z0-9_]\.' + re.escape(s) + r'\b)' for s in plain]
    rc, out = git(PP, 'grep', '-l', '-E', '|'.join(alts), 'HEAD', '--', '*.md')
    files = sorted(set(x.split(':', 1)[1] for x in out.split(NL) if ':' in x))
    root = set(LEDGERS + ['README.md', 'REGISTRY.md', PAGE_NAME, DIR_PAGE_NAME])   # ### both generated pages, never keystones
    return [f for f in files if f not in root and not f.startswith('archive/')]


def short(n):
    return n.split('.')[-1]


def emit(nodes, cells, order, corr_rows, keystone_files, ceiling, nodes_name='b568_nodes.txt', key=False, column=False, glossary=False):
    head = ('This page is generated by relay `tools/chain_page.py` from the node list relay `data/%s`: the compiled chain '
            'from Mathlib\'s `RiemannHypothesis` to the ceiling sentence, one declaration per line, in dependency order. '
            'It is generated at SIDE-explicit-formula %s = `%s` (Lean %s; Mathlib `%s`; Zeta23 vendored at `%s`; Bulka vendored '
            'at `%s`). Each line reads: name — module:line — entry tag = SHA — the statement as `#print` gives it (a theorem by '
            '`#print sig`; whitespace runs collapsed) — premises — E0 grade — tier — axioms — the nodes it consumes.'
            % (nodes_name, PIN_TAG, PIN[:7], TOOLCHAIN.split(':')[1], MATHLIB[:8], ZETA23, BULKA))
    L = ['# THE CLAUSE AND ITS COMPILED FACES', '', head + ((' ' + TIER_KEY) if key else ''), '']
    if glossary:
        L += glossary_block() + ['']   # ### b638, (R248)(4): the glossary block beneath the head line
    if column:
        L += [SHAPE_KEY, '']   # ### b622, (R232)(4): the column's one head line
    for i, n in enumerate(order, 1):
        c = cells[n]
        ax = '[' + ', '.join(c['axioms']) + ']' if c['axioms'] is not None else c['axioms_text']
        cons = ', '.join('`%s`' % short(x) for x in c['consumes']) or 'none'
        tier = c['tier'] + ((' (table: %s)' % (c.get('table_tier') or 'none')) if key else '')
        sh = (' — shape: %s' % c.get('shape')) if column else ''   # ### b622, (R232)(4): the shape cell, after the statement
        L.append('%d. `%s` — %s:%d — %s — `%s`%s — premises: %s — E0: %s — tier: %s — axioms: %s — consumes: %s'
                 % (i, n, c['path'], c['line'], c['entry'], c['statement'], sh, c['premises'], c['grade'], tier, ax, cons))
    L += ['', OPEN_LINE, '', ceiling, '', '## Placement', '', '| object | path |', '|:--|:--|',
          '| this page | `%s` |' % PAGE_NAME]
    L += ['| ledger | `%s` |' % f for f in LEDGERS]
    L += ['| the ceiling sentence | `README.md:121`, `REGISTRY.md:956` |']
    L += ['| keystone naming a node | `%s` |' % f for f in keystone_files]
    L += ['| the χ-leg | its own page when `EF_lit_chi`\'s proof lands (SIDE-explicit-formula `SIDEExplicitFormula/Chi/Statement.lean`) |']
    L += ['', '## Correspondence', '', '| declaration | repository | grade | tier |', '|:--|:--|:--|:--|']
    for r in corr_rows:
        L.append('| `%s` | %s | %s | %s |' % (r['name'], r['repo'], r['grade'], r['tier']))
    return NL.join(L) + NL


def emit_dirichlet(nodes, cells, order, corr_rows, keystone_files, ceiling, ceil_lines, nodes_name, key=True, column=False, glossary=False):
    """### (R183)(5): the χ-leg's page -- the same head key and node-line form as the ζ page; its own title, open line, last
    ### derived line (the successor sentence) and Placement rows."""
    head = ('This page is generated by relay `tools/chain_page.py` from the node list relay `data/%s`: the compiled chain '
            'from `GRH_chi` to the ceiling\'s successor sentence, one declaration per line, in dependency order. '
            'It is generated at SIDE-explicit-formula %s = `%s` (Lean %s; Mathlib `%s`; Zeta23 vendored at `%s`; Bulka vendored '
            'at `%s`). Each line reads: name — module:line — entry tag = SHA — the statement as `#print` gives it (a theorem by '
            '`#print sig`; whitespace runs collapsed) — premises — E0 grade — tier — axioms — the nodes it consumes.'
            % (nodes_name, PIN_TAG, PIN[:7], TOOLCHAIN.split(':')[1], MATHLIB[:8], ZETA23, BULKA))
    L = [DIR_TITLE, '', head + ((' ' + TIER_KEY) if key else ''), '']
    if glossary:
        L += glossary_block() + ['']   # ### b638, (R248)(4): the glossary block beneath the head line
    if column:
        L += [SHAPE_KEY, '']   # ### b622, (R232)(4): the column's one head line
    for i, n in enumerate(order, 1):
        c = cells[n]
        ax = '[' + ', '.join(c['axioms']) + ']' if c['axioms'] is not None else c['axioms_text']
        cons = ', '.join('`%s`' % short(x) for x in c['consumes']) or 'none'
        tier = c['tier'] + ((' (table: %s)' % (c.get('table_tier') or 'none')) if key else '')
        sh = (' — shape: %s' % c.get('shape')) if column else ''   # ### b622, (R232)(4): the shape cell, after the statement
        L.append('%d. `%s` — %s:%d — %s — `%s`%s — premises: %s — E0: %s — tier: %s — axioms: %s — consumes: %s'
                 % (i, n, c['path'], c['line'], c['entry'], c['statement'], sh, c['premises'], c['grade'], tier, ax, cons))
    rl, gl = ceil_lines
    L += ['', DIR_OPEN_LINE, '', ceiling, '', '## Placement', '', '| object | path |', '|:--|:--|',
          '| this page | `%s` |' % DIR_PAGE_NAME]
    L += ['| ledger | `%s` |' % f for f in LEDGERS]
    L += ['| the successor sentence | %s |' % ', '.join(['`README.md:%d`' % x for x in rl] + ['`REGISTRY.md:%d`' % x for x in gl])]
    L += ['| keystone naming a node | `%s` |' % f for f in keystone_files]
    L += ['| the ζ-leg | `%s` |' % PAGE_NAME]
    L += ['', '## Correspondence', '', '| declaration | repository | grade | tier |', '|:--|:--|:--|:--|']
    for r in corr_rows:
        L.append('| `%s` | %s | %s | %s |' % (r['name'], r['repo'], r['grade'], r['tier']))
    return NL.join(L) + NL


def corr_select(rec, names, marks, variant):
    """### The Correspondence rows' names: the graded names of the table that are not nodes, and the list's marks.
    ### ζ page: kernel and Zeta23 names outside the χ side and -- (R184)(2), b573's finding -- outside the schema
    ### (`SIDEExplicitFormula.Schema.`), so that a schema name graded at a close never joins the ζ page.
    ### Dirichlet page ((R183)(5)): the χ-side and schema names."""
    if variant == 'dirichlet':
        pick = lambda n: n.startswith(CHI_PREFIX) or n.startswith(SCHEMA_PREFIX)
    else:
        pick = lambda n: ((n.startswith('SIDEExplicitFormula.') or n.startswith('Zeta23.')) and not n.startswith(CHI_PREFIX)
                          and not n.startswith(SCHEMA_PREFIX))
    return sorted(set(n for n, r in rec.items() if pick(n) and n not in names and r.get('grade') != 'UNGRADED')
                  | set(m for m in marks if m not in names))


# ================================================================================ the run
def build(nodes_path, probe_dir, from_output=None):
    # ### (R179)(4): the pin and the tier key come with the node list. A list carrying `# pin: <tag>` is generated at that
    # ### tag with the tier key on its head and the table's tier beside every node's; a list without one (b568's) at v0.10
    # ### as b568 generated it, so b568's page still regenerates byte for byte from b568's list.
    global PIN_TAG, PIN, VARIANT
    VARIANT = node_variant(nodes_path)
    if VARIANT not in (None, 'dirichlet'):
        return 2, None, None, ['unknown page variant %r' % VARIANT]
    keyed = any(re.match(r'^# pin: \S+\s*$', raw.rstrip('\r\n')) for raw in io.open(nodes_path, encoding='utf-8'))
    PIN_TAG, PIN = ('v0.10', '6baed63ae664a22db1f325177b81253e270de6e3')
    if keyed:
        PIN_TAG, PIN = node_pin(nodes_path)
        if PIN is None:
            return 3, None, None, ['the node list`s pin %s does not resolve in the kernel' % PIN_TAG]
    nodes, drops, corr_extra, marks = read_nodes(nodes_path)
    column = node_column(nodes_path)   # ### b622, (R232)(4): the shape column, by the list's one line
    gloss = node_glossary(nodes_path)  # ### b638, (R248)(4): the glossary block, by the list's one line
    names = [x['name'] for x in nodes]
    rec = record_rows()
    corr_names = corr_select(rec, names, marks, VARIANT)
    watch = ['SIDEExplicitFormula.RegisterDepth']
    log = []
    if from_output is None:
        rc, head = git(KER, 'rev-parse', 'HEAD')
        rc2, tag = git(KER, 'rev-parse', PIN_TAG + '^{commit}')
        rc3, dirty = git(KER, 'status', '--porcelain', '--untracked-files=no')
        log.append('checkout HEAD %s ; %s %s ; tracked changes %d' % (head.strip()[:12], PIN_TAG, tag.strip()[:12], len(dirty.split(NL)) - 1))
        if head.strip() != PIN or tag.strip() != PIN or dirty.strip():
            return 3, None, None, log
        fm = free_mb()
        log.append('free memory before the lean call: %d MB (hold %d)' % (fm, HOLD_MB))
        # ### b630, (R240)(5), W-ORD-PROBE-HOLD: the reading (in force since b568) printed on the generator's own output at every
        # ### start, refused or not, so no caller has to print the log for the reading to be seen.
        print('chain_page: free memory before the lean call: %d MB (hold %d) -- %s' % (
            fm, HOLD_MB, 'REFUSED, beneath the hold' if 0 <= fm < HOLD_MB else 'started'))
        if 0 <= fm < HOLD_MB:
            return 4, None, None, log
        rc, out = run_probe(probe_dir, probe_text(names + corr_names, names, watch))
        log.append('lake env lean exit %d' % rc)
        if rc != 0:
            return 5, None, None, log
    else:
        out = io.open(from_output, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    cells, errors = parse(out)
    missing = [n for n in names + corr_names if n not in cells or cells[n].get('missing')]
    if missing:
        log.append('unresolved: %s' % missing)
        return 6, None, dict(cells=cells, errors=errors), log
    nodeset = set(names)
    for n in names + corr_names:
        c = cells[n]
        rel = module_path(c['module'])
        src = None if c['module'].startswith('Mathlib') else source_at(PIN, rel)
        head = source_header(src, short(n), c['line']) if src is not None else None
        if c['kind'] == 'theorem' and head is None:
            # ### a theorem whose source header cannot be read is NOT graded: an empty header would read DERIVES.
            log.append('source header unread: %s at %s:%d' % (n, rel, c['line']))
            return 6, None, dict(cells=cells), log
        grade, why, _b = E0.grade(head or '', 'theorem' if c['kind'] == 'theorem' else 'def')
        c['path'], c['source_header'] = rel, head
        c['grade'] = grade if c['kind'] == 'theorem' else 'DEF'
        c['premises'] = why if grade == 'INTERFACES' else 'none'
        if keyed and n in nodeset:
            c['tier'], c['tier_source'], c['table_tier'], c['tier_conflict'] = tier_of_node(c['kind'], grade, why, c['axioms'], rec.get(n))
        else:
            c['tier'], c['tier_source'] = tier_of(c['kind'], grade, why, c['axioms'], rec.get(n), nodeset)
        c['record_grade'] = (rec.get(n) or {}).get('grade')
        c['std3'] = c['axioms'] is not None and set(c['axioms']) <= set(STD3)
        if c['module'].startswith('Mathlib'):
            c['entry'] = 'Mathlib = %s' % MATHLIB[:8]
            c['entry_tag'] = None
        else:
            t, sha = entry_tag(rel, short(n))
            c['entry_tag'] = t
            pre = '%s = %s' % (t, sha) if t else 'NO TAG'
            if c['module'].startswith('Zeta23'):
                pre += ' (Zeta23 vendored at %s)' % ZETA23
            elif c['module'].split('.')[0] in BULKA_ROOTS:
                pre += ' (Bulka vendored at %s)' % BULKA
            c['entry'] = pre
            if t:
                old = source_at(t, rel)
                m0 = re.search(DECL + r'(?:[A-Za-z_][\w]*\.)*' + re.escape(short(n)) + r'(?![\w\'₀-₉])(.*?):=', old or '', re.M | re.S)
                c['header_at_entry_equal'] = bool(m0) and ' '.join(m0.group(1).split()) == (head or '')
    conflicts = [n for n in names if cells[n].get('tier_conflict')]
    for n in names:
        if keyed:
            log.append('tier %-72s computed %-14s table %s%s' % (n, cells[n]['tier'], cells[n].get('table_tier') or 'none',
                                                                  '   ### CONFLICT' if cells[n].get('tier_conflict') else ''))
    if conflicts:
        log.append('### CONFLICT -- the table`s tier differs from the computed tier at %s; NO PAGE (R179)(4)' % conflicts)
        return 7, None, dict(cells=cells, conflicts=conflicts), log
    if column:
        for n in names:
            cells[n]['shape'] = shape_of(n, cells)
    order = dep_order(names, {n: cells[n]['consumes'] for n in names})
    if order is None:
        log.append('the consumption relation has a cycle')
        return 6, None, dict(cells=cells), log
    corr_rows = []
    for n in corr_names:
        c = cells[n]
        g = c['record_grade'] or 'UNGRADED'
        # ### b592, the author's answer before its seal (prompt 6): a row graded INTERFACES names its premises in its tier cell,
        # ### read by the shared E0 rule from the source header at the pin; a DERIVES row is written exactly as before.
        prem = ('; premises: ' + c['premises'].replace('|', '¦')) if g == 'INTERFACES' and c.get('premises') not in (None, 'none') else ''
        # ### b632, (R242)(3) and the author's answer before b632's seal (prompt 2): a row the table grades by the shared E0 rule says so
        # ### in its tier cell, the same mark the table carries; a row graded by ledger cells is written exactly as before.
        # ### b635, the author's answer after b635's seal (the page-mark prompt): any provenance but the ledger cells' (and 'none', no grade)
        # ### prints as itself -- "rule-elab" as "rule-elab" -- rather than being matched by name.
        pv = (rec.get(n) or {}).get('provenance')
        prov = ('; provenance: ' + pv) if pv not in (None, 'cell', 'none') else ''
        corr_rows.append(dict(name=n, repo='SIDE-explicit-formula', grade=g, tier=c['tier'] + prem + prov))
    for x in corr_extra:
        corr_rows.append(dict(name=x['name'], repo=x['repo'], grade=x['grade'], tier=x['tier'] + ('; ' + x['note'] if x['note'] else '')))
    kfiles = keystones([short(n) for n in names if not cells[n]['module'].startswith('Mathlib')])
    if VARIANT == 'dirichlet':
        sent, rl, gl = dir_ceiling()
        if not sent:
            log.append('the successor sentence is not found once at README (lines %s)' % rl)
            return 6, None, dict(cells=cells), log
        page = emit_dirichlet(nodes, cells, order, corr_rows, kfiles, sent, (rl, gl), os.path.basename(nodes_path), keyed, column, gloss)
    else:
        page = emit(nodes, cells, order, corr_rows, kfiles, ceiling_line(), os.path.basename(nodes_path), keyed, column, gloss)
    # ### b596: the backmatter channel -- the list's `# backmatter:` records as one paragraph after the Correspondence table
    bm = backmatter_of(nodes_path)
    if bm:
        page = page + NL + ' '.join(bm) + NL
    for d in drops:   # ### each DROP checked here, not typed: a declaration of that exact name at the pin, and the watch
        ere = (r'^[[:space:]]*(@\[[^]]*\][[:space:]]*)?((private|protected|noncomputable)[[:space:]]+)*'
               r'(theorem|lemma|def|abbrev|structure|inductive|irreducible_def)[[:space:]]+([A-Za-z_][A-Za-z0-9_]*\.)*'
               + d['name'] + r'([[:space:]]|:|\(|\{|\[|$)')
        rc, out = git(KER, 'grep', '-n', '-E', ere, PIN, '--', '*.lean')
        d['declarations_at_pin'] = [x for x in out.split(NL) if x.strip()]
        d['watched_by_nodes'] = sorted(set(w for n in names for w in cells[n]['watched'] if d['name'] in w.split('.')))
    meta = dict(order=order, cells=cells, drops=drops, corr=corr_rows, keystones=kfiles, errors=errors, nodes=nodes)
    return 0, page, meta, log


def main(argv):
    def arg(k, default=None):
        return argv[argv.index(k) + 1] if k in argv else default
    nodes, probe_dir, out = arg('--nodes'), arg('--probe-dir'), arg('--out')
    if not (nodes and probe_dir and out):
        print(__doc__.split('### Usage:')[1])
        return 2
    rc, page, meta, log = build(nodes, probe_dir, arg('--from-output'))
    for l in log:
        print('chain_page: ' + l)
    if rc:
        print('chain_page: REFUSED / FAILED, exit %d' % rc)
        if meta and arg('--cells'):
            io.open(arg('--cells'), 'w', encoding='utf-8', newline=NL).write(json.dumps(meta, indent=1, ensure_ascii=False, default=str) + NL)
        return rc
    b = page.encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    print('chain_page: written %s (%d bytes, %d nodes)' % (out, len(b), len(meta['order'])))
    if arg('--cells'):
        c = (json.dumps(meta, indent=1, ensure_ascii=False, default=str) + NL).encode('utf-8')
        open(arg('--cells') + '.tmp', 'wb').write(c)
        os.replace(arg('--cells') + '.tmp', arg('--cells'))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
