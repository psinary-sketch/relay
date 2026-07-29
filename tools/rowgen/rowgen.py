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

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
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
