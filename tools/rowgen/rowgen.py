#!/usr/bin/env python3
"""
rowgen — Correspondence row generator + differ.

PUBLIC tool. Emits from KERNELS (Lean declarations), never from papers.

Mode GENERATE: for each terminal {name, repo, pin, module, file}, produce a record:
  - check   : the `#check @name` statement, verbatim (from `lake env lean`)
  - axioms  : the `#print axioms name` line, verbatim
  - doc     : the declaration's docstring first paragraph, verbatim (from source at pin)
  - body1   : the proof body's first line
  - defenc  : DEFINITION-ENCODED flag — true if any definition named in the conclusion has a
              body that is a literal constant (:= 0, := true, := 1, …) or `True`.

Mode DIFF: given a paper's Correspondence table (markdown) and the generated records, flag each row whose
  - Status contradicts the docstring (e.g. row says DERIVES, doc says stand-in/encoded/placeholder),
  - profile is rounded (row omits an axiom the record has, e.g. [propext] written as axiom-free),
  - pin is stale (row's commit != record's pin),
  - cited terminal no longer exists (check/axioms failed to resolve).

Usage:
  python rowgen.py generate terminals.json            -> writes records.json, prints a table
  python rowgen.py diff terminals.json <table.md>     -> prints the row-by-row diff
"""
import sys, os, re, json, subprocess, tempfile
try: sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception: pass

def sh(cmd, cwd=None, timeout=600):
    try:
        p = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True,
                           timeout=timeout, encoding='utf-8', errors='replace')
        return p.returncode, p.stdout or '', p.stderr or ''
    except subprocess.TimeoutExpired:
        return 124, '', 'TIMEOUT'

def git_show(repo, pin, path):
    rc, out, err = sh(f'git show {pin}:{path}', cwd=repo)
    return out if rc == 0 else ''

def lean_check_axioms(repo, module, name):
    """Run #check @name and #print axioms name via lake env lean. Returns (check, axioms, ok)."""
    body = f"import {module}\n#check @{name}\n#print axioms {name}\n"
    fd, tmp = tempfile.mkstemp(suffix='.lean', dir=repo); os.close(fd)
    open(tmp, 'w', encoding='utf-8').write(body)
    try:
        rc, out, err = sh(f'lake env lean "{os.path.basename(tmp)}"', cwd=repo, timeout=600)
    finally:
        try: os.remove(tmp)
        except OSError: pass
    text = (out + '\n' + err).strip()
    if 'unknownIdentifier' in text or 'unknown' in text.lower() and name in text:
        return '', '', False
    lines = [l for l in text.splitlines() if l.strip()]
    chk = next((l for l in lines if l.strip().startswith(name) or f'{name} :' in l or l.strip().startswith(name.split('.')[-1])), '')
    ax = next((l for l in lines if 'depend' in l and 'axiom' in l), '')
    ok = bool(chk) or bool(ax)
    return chk.strip(), ax.strip(), ok

def extract_doc_body(src, name):
    """From source text, find `theorem/def name`, return (docstring-first-para, proof-body-first-line)."""
    short = name.split('.')[-1]
    lines = src.split('\n')
    doc, body1 = '', ''
    for i, ln in enumerate(lines):
        if re.match(rf'^\s*(?:@\[[^\]]*\]\s*)?(theorem|lemma|def)\s+{re.escape(short)}\b', ln):
            # docstring: walk up for /-- ... -/
            j = i - 1
            while j >= 0 and lines[j].strip() == '': j -= 1
            if j >= 0 and lines[j].rstrip().endswith('-/'):
                k = j
                while k >= 0 and '/--' not in lines[k]: k -= 1
                if k >= 0:
                    block = ' '.join(x.strip() for x in lines[k:j+1])
                    block = block.replace('/--', '').replace('-/', '').strip()
                    doc = re.split(r'\.\s|\n\n', block)[0].strip()
                    doc = re.sub(r'\s+', ' ', doc)[:400]
            # proof body first line: from ':=' onward
            buf = ln; m = i
            while ':=' not in buf and m + 1 < len(lines):
                m += 1; buf += ' ' + lines[m]
            if ':=' in buf:
                after = buf.split(':=', 1)[1].strip()
                if after: body1 = after.splitlines()[0][:120]
                elif m + 1 < len(lines): body1 = lines[m+1].strip()[:120]
            break
    return doc, body1

LIT = re.compile(r':=\s*(0|1|true|false|True|False)\s*$')
def definition_encoded(src, conclusion):
    """Flag if any identifier in `conclusion` has a `def <id> ... := <literal|True>` in src."""
    idents = set(re.findall(r'[A-Za-z_][A-Za-z0-9_\.]*', conclusion))
    for ident in idents:
        short = ident.split('.')[-1]
        for ln in src.split('\n'):
            md = re.match(rf'^\s*def\s+{re.escape(short)}\b.*:=\s*(.+)$', ln)
            if md:
                rhs = md.group(1).strip()
                if rhs in ('0', '1', 'true', 'false', 'True', 'False') or re.match(r'^(True|False|0|1)\b', rhs):
                    return True, f'{short} := {rhs}'
    return False, ''

def generate(terminals):
    records = []
    for t in terminals:
        repo = t['repo']; pin = t.get('pin', 'HEAD'); mod = t['module']; name = t['name']; f = t.get('file', '')
        src = git_show(repo, pin, f) if f else ''
        chk, ax, ok = lean_check_axioms(repo, mod, name)
        doc, body1 = extract_doc_body(src, name) if src else ('', '')
        concl = chk.split(':', 1)[1] if ':' in chk else chk
        defenc, why = definition_encoded(src, concl) if src else (False, '')
        records.append({'name': name, 'repo': os.path.basename(repo), 'pin': pin, 'exists': ok,
                        'check': chk, 'axioms': ax, 'doc': doc, 'body1': body1,
                        'defenc': defenc, 'defenc_why': why})
    return records

# ---- Mode DIFF -------------------------------------------------------------
ROUND = {'propext', 'Classical.choice', 'Quot.sound'}
def parse_table(md):
    rows = []
    for ln in md.split('\n'):
        if ln.strip().startswith('|') and '`' in ln:
            cells = [c.strip() for c in ln.strip().strip('|').split('|')]
            rows.append(cells)
    return rows

def diff(records, table_md):
    recmap = {}
    for r in records:
        recmap[r['name']] = r
        recmap[r['name'].split('.')[-1]] = r
    out = []
    for cells in parse_table(table_md):
        joined = ' '.join(cells)
        cited = re.findall(r'`([A-Za-z_][A-Za-z0-9_\.]*)`', joined)
        rec = None
        for c in cited:
            if c in recmap: rec = recmap[c]; break
        if not rec: continue
        flags = []
        if not rec['exists']:
            flags.append('MISSING: cited terminal did not resolve at pin')
        # profile rounding: row says axiom-free but record has axioms, or omits [propext]
        low = joined.lower()
        recax = rec['axioms']
        if 'propext' in recax and ('axiom-free' in low or 'no axiom' in low) and 'propext' not in low:
            flags.append(f"PROFILE-ROUNDED: record shows {recax!r}, row reads axiom-free")
        # status vs docstring: row DERIVES but doc says encoded/stand-in/placeholder
        docl = rec['doc'].lower()
        if ('derives' in low) and any(w in docl for w in ('stand-in', 'encoded', 'placeholder', 'deprecated', 'assigns')):
            flags.append(f"STATUS-vs-DOC: row DERIVES but docstring says '{rec['doc'][:60]}'")
        if rec['defenc'] and 'derives' in low and 'encodes' not in low:
            flags.append(f"DEFINITION-ENCODED: {rec['defenc_why']} — row reads DERIVES")
        # stale pin: any 7-40 hex in the row that isn't the record pin
        pins = re.findall(r'\b([0-9a-f]{7,40})\b', joined)
        if pins and rec['pin'] not in ('HEAD',) and not any(rec['pin'].startswith(p) or p.startswith(rec['pin']) for p in pins):
            flags.append(f"PIN: row cites {pins} but record pin is {rec['pin']}")
        out.append((rec['name'], flags if flags else ['ok']))
    return out

# ---- Mode CONSTELLATION ----------------------------------------------------
# A corpus cross-reference consistency checker. Operates on paths passed in; embeds no corpus content.
def build_corpus_index(root):
    """{basename.md: {title, version, path}} from the filesystem, and REGISTRY {id: {...}}."""
    files, reg = {}, {}
    for dp, dn, fn in os.walk(root):
        if '.git' in dp.split(os.sep): continue
        for f in fn:
            if not f.endswith('.md'): continue
            p = os.path.join(dp, f)
            try: txt = open(p, encoding='utf-8', errors='replace').read()
            except OSError: continue
            head = '\n'.join(txt.split('\n')[:15])
            title = ''
            m = re.search(r'^#\s+(.+)$', head, re.M)
            if m: title = m.group(1).strip()
            vm = re.search(r'\bv(\d+\.\d+(?:\.\d+)?)\b', head)
            files[f] = {'title': title, 'version': vm.group(1) if vm else '', 'path': p}
            if f == 'REGISTRY.md':
                for ln in txt.split('\n'):
                    rm = re.match(r'^\|\s*([A-Za-z0-9.]+-?\d*[a-z]?-?\d*)\s*\|\s*([^|]+?)\s*\|\s*`?([^|`]+\.md)`?\s*\|\s*(v?[\d.]+)?\s*\|[^|]*\|\s*([A-Z\-]+)?', ln)
                    if rm and re.match(r'^(d1|p1|p2|m5|1\.5|\d)', rm.group(1)):
                        reg[rm.group(1).strip()] = {'title': rm.group(2).strip(),
                                                    'file': os.path.basename(rm.group(3).strip()),
                                                    'version': (rm.group(4) or '').lstrip('v'),
                                                    'status': (rm.group(5) or '').strip()}
    return files, reg

CLOSED = ('READY', 'RATIFIED', 'LANDED', 'ENSHRINED', 'CLOSED', 'COMPLETE')
PENDING_WORD = re.compile(r'\b(pending|awaiting|not yet|to be|forthcoming|will be|held for|being drafted|in progress)\b', re.I)

# Historical-section exclusion (2026-07-31): dated ledger entries are the historical record —
# they report separately and never flag actionable. A line is HISTORICAL when it sits under a
# history-class heading (a heading carrying a date token or a history word), or in a paragraph
# whose first line carries a date token — UNLESS the line is a live REGISTRY id-row (the version
# table is live state regardless of dated notes in its cells).
# Intentional-provenance marker: a backticked `FILE.md` preceded nearby by "was"/"formerly"/
# "moved ... from" is a rename/move provenance annotation — classified PROVENANCE, never actionable.
DATE_TOK  = re.compile(r'\b20\d\d-\d\d(?:-\d\d)?\b')
HIST_HEAD = re.compile(r'history|heritage|row update|deposit|version history|version log|change ?log|addendum', re.I)
ID_ROW    = re.compile(r'^\|\s*(?:d1|p1|p2|m5|1\.5[a-z]?)-')
DATED_ROW = re.compile(r'^\|\s*20\d\d-\d\d-\d\d\s*\|')   # date-first table row = dated ledger entry
PROV_NEAR = re.compile(r'(\bwas\b|\bformerly\b|\bmoved\b[^`]{0,40}\bfrom\b|\bfrom\b[^`]{0,12}$)', re.I)
# External-location references: a backticked .md whose nearby text names an off-corpus home
# (another repo, the download layer, a drive path, a generated export artifact) is not a corpus
# target — classified EXTERNAL, reported separately, never actionable.
EXT_NEAR  = re.compile(r'(SIDE-[a-z0-9-]+|\bkernel\b|\brelay\b|D:\\|download[- ]layer|download to|sibling repo)', re.I)

def constellation(paper_path, files, reg):
    txt = open(paper_path, encoding='utf-8', errors='replace').read()
    lines = txt.split('\n')
    self_base = os.path.basename(paper_path)
    flags = []
    head_hist = False   # nearest preceding heading is history-class
    para_hist = False   # current paragraph's first line carries a date token
    prev_blank = True
    for i, ln in enumerate(lines, 1):
        hm = re.match(r'^#{1,6}\s+(.*)$', ln)
        if hm:
            head_hist = bool(HIST_HEAD.search(hm.group(1)) or DATE_TOK.search(hm.group(1)))
            para_hist = False
            prev_blank = True
            continue
        if not ln.strip():
            prev_blank = True
            para_hist = para_hist  # paragraph ends; reset happens at next para start
            continue
        if prev_blank:
            para_hist = bool(DATE_TOK.search(ln))
            prev_blank = False
        historical = ((head_hist or para_hist) and not ID_ROW.match(ln)) or bool(DATED_ROW.match(ln))
        def add(tgt, kind, klass):
            flags.append((i, tgt, kind, ln.strip()[:140], klass))
        # backticked filename refs
        for m in re.finditer(r'`([A-Za-z0-9_./-]+\.md)`', ln):
            fn = m.group(1)
            base = os.path.basename(fn)
            if base == self_base: continue
            prov = bool(PROV_NEAR.search(ln[max(0, m.start()-28):m.start()]))
            ext  = bool(EXT_NEAR.search(ln[max(0, m.start()-32):m.start()]) or
                        EXT_NEAR.search(ln[m.end():m.end()+32]))
            if base not in files:
                add(base, 'NONEXISTENT-TARGET',
                    'PROVENANCE' if prov else ('EXTERNAL' if ext else ('HISTORICAL' if historical else 'ACTIONABLE')))
                continue
            cur = files[base]['version']
            near = ln[max(0, ln.find(fn)-40):ln.find(fn)+len(fn)+40]
            vm = re.search(rf'{re.escape(base)}[^)]*?\bv(\d+\.\d+(?:\.\d+)?)\b|\bv(\d+\.\d+(?:\.\d+)?)\b[^)]*?{re.escape(base)}', near)
            cited_v = (vm.group(1) or vm.group(2)) if vm else ''
            if cur and cited_v and cited_v != cur and not (cur.startswith(cited_v) or cited_v.startswith(cur)):
                add(base, f'STALE-VERSION cited v{cited_v}, current v{cur}',
                    'PROVENANCE' if prov else ('HISTORICAL' if historical else 'ACTIONABLE'))
        # REGISTRY-ID refs with pending-language or stale title/status
        for rid in re.findall(r'\b((?:p2|m5|d1|1\.5[a-z]?)-\d+|1\.5[a-z]-\d+)\b', ln):
            if rid in reg:
                st = reg[rid]['status'].upper()
                if PENDING_WORD.search(ln) and any(c in st for c in CLOSED):
                    add(rid, f'STALE-STATUS: "pending" language, but {rid} is {reg[rid]["status"]}',
                        'HISTORICAL' if historical else 'ACTIONABLE')
    return flags

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    if mode == 'constellation':
        root = sys.argv[2]; papers = sys.argv[3:]
        files, reg = build_corpus_index(root)
        print(f"index: {len(files)} md files, {len(reg)} REGISTRY rows")
        for pp in papers:
            fl = constellation(pp, files, reg)
            act = [f for f in fl if f[4] == 'ACTIONABLE']
            hist = [f for f in fl if f[4] == 'HISTORICAL']
            prov = [f for f in fl if f[4] == 'PROVENANCE']
            extn = [f for f in fl if f[4] == 'EXTERNAL']
            print(f"\n=== {os.path.basename(pp)} : {len(act)} actionable, {len(prov)} provenance, {len(extn)} external, {len(hist)} historical ===")
            for label, group in (('ACTIONABLE', act), ('PROVENANCE', prov), ('EXTERNAL', extn), ('HISTORICAL', hist)):
                for i, tgt, kind, ctx, _ in group:
                    print(f"  [{label}] L{i}  [{tgt}]  {kind}\n       {ctx}")
        sys.exit(0)
    cfg = json.load(open(sys.argv[2], encoding='utf-8')) if len(sys.argv) > 2 else []
    recs = generate(cfg)
    if mode == 'generate':
        json.dump(recs, open('records.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
        for r in recs:
            print(f"\n=== {r['name']}  [{r['repo']} @ {r['pin']}]  exists={r['exists']} defenc={r['defenc']}")
            print(f"  check:  {r['check']}")
            print(f"  axioms: {r['axioms']}")
            print(f"  doc:    {r['doc']}")
            print(f"  body1:  {r['body1']}")
            if r['defenc']: print(f"  DEFINITION-ENCODED: {r['defenc_why']}")
    elif mode == 'diff':
        table = open(sys.argv[3], encoding='utf-8').read()
        for name, flags in diff(recs, table):
            print(f"{name}: {'; '.join(flags)}")
