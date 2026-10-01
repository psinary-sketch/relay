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
### Exit: 0 written; 2 usage; 3 the checkout refused; 4 free memory below the hold; 5 the probe failed; 6 a node unresolved.
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
BULKA_ROOTS = ('Lc', 'Hadamard', 'FunctionsOfOneComplexVariable')
LEDGERS = ['FINDINGS.md', 'OPEN_TRAILS.md', 'ERRATA.md', 'FACES_LEDGER.md']
CHI_PREFIX = 'SIDEExplicitFormula.GRHWeil.'


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


# ================================================================================ the node list
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


# ================================================================================ the page
def ceiling_line():
    rc, out = git(PP, 'show', 'HEAD:README.md')
    lines = out.split(NL)
    return lines[120] if len(lines) > 120 else ''


def keystones(short_names):
    pat = '|'.join(re.escape(s) for s in sorted(short_names))
    rc, out = git(PP, 'grep', '-l', '-E', r'\b(' + pat + r')\b', 'HEAD', '--', '*.md')
    files = sorted(set(x.split(':', 1)[1] for x in out.split(NL) if ':' in x))
    root = set(LEDGERS + ['README.md', 'REGISTRY.md', PAGE_NAME])
    return [f for f in files if f not in root and not f.startswith('archive/')]


def short(n):
    return n.split('.')[-1]


def emit(nodes, cells, order, corr_rows, keystone_files, ceiling):
    L = ['# THE CLAUSE AND ITS COMPILED FACES', '',
         'This page is generated by relay `tools/chain_page.py` from the node list relay `data/b568_nodes.txt`: the compiled chain '
         'from Mathlib\'s `RiemannHypothesis` to the ceiling sentence, one declaration per line, in dependency order. '
         'It is generated at SIDE-explicit-formula %s = `%s` (Lean %s; Mathlib `%s`; Zeta23 vendored at `%s`; Bulka vendored '
         'at `%s`). Each line reads: name — module:line — entry tag = SHA — the statement as `#print` gives it (a theorem by '
         '`#print sig`; whitespace runs collapsed) — premises — E0 grade — tier — axioms — the nodes it consumes.'
         % (PIN_TAG, PIN[:7], TOOLCHAIN.split(':')[1], MATHLIB[:8], ZETA23, BULKA), '']
    for i, n in enumerate(order, 1):
        c = cells[n]
        ax = '[' + ', '.join(c['axioms']) + ']' if c['axioms'] is not None else c['axioms_text']
        cons = ', '.join('`%s`' % short(x) for x in c['consumes']) or 'none'
        L.append('%d. `%s` — %s:%d — %s — `%s` — premises: %s — E0: %s — tier: %s — axioms: %s — consumes: %s'
                 % (i, n, c['path'], c['line'], c['entry'], c['statement'], c['premises'], c['grade'], c['tier'], ax, cons))
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


# ================================================================================ the run
def build(nodes_path, probe_dir, from_output=None):
    nodes, drops, corr_extra, marks = read_nodes(nodes_path)
    names = [x['name'] for x in nodes]
    rec = record_rows()
    corr_names = sorted(set(n for n, r in rec.items()
                            if (n.startswith('SIDEExplicitFormula.') or n.startswith('Zeta23.')) and not n.startswith(CHI_PREFIX)
                            and n not in names and r.get('grade') != 'UNGRADED') | set(m for m in marks if m not in names))
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
    order = dep_order(names, {n: cells[n]['consumes'] for n in names})
    if order is None:
        log.append('the consumption relation has a cycle')
        return 6, None, dict(cells=cells), log
    corr_rows = []
    for n in corr_names:
        c = cells[n]
        g = c['record_grade'] or 'UNGRADED'
        corr_rows.append(dict(name=n, repo='SIDE-explicit-formula', grade=g, tier=c['tier']))
    for x in corr_extra:
        corr_rows.append(dict(name=x['name'], repo=x['repo'], grade=x['grade'], tier=x['tier'] + ('; ' + x['note'] if x['note'] else '')))
    kfiles = keystones([short(n) for n in names if not cells[n]['module'].startswith('Mathlib')])
    page = emit(nodes, cells, order, corr_rows, kfiles, ceiling_line())
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
