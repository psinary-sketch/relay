# -*- coding: utf-8 -*-
"""module_header.py -- THE ARM G-MODULE-HEADER, a standalone tool under (R259)(2)(c), an arm of every suite from b649.

### Every module header -- the `/-! -/` block at a file's head, before its first declaration -- of every .lean file on every kernel's main
### (the kernels of tools/no_sorry_main.py) is read as a document through the licensed-statement table's generated rule extended to headers
### (tools/licensed_table.py `attached_claims`, the clause window it reads for the docstring and module rules), its hard-wrapped lines
### first joined into sentences (a blank line, a bullet and a numbered item kept). A header's claims are:
###   PROVED -- a proof word attached to a named declaration (proved, proves, PROVED, DERIVES, derives, establishes, holds unconditionally,
###             unconditionally, outright), the name its subject or its object in the clause ("`X` is proved", "`X` (proved)", "proves `X`");
###   THEOREM -- a declaration the header names as a theorem or lemma ("theorem `X`", "Theorem: `X`", "lemmas `X`, `Y`").
### Each claimed name is resolved among the file's own declarations (its qualified name, or its last component). A row OVERREACHES when the
### header names a theorem the file does not declare, or describes as proved a declaration the file declares as a def, abbrev, structure,
### class, inductive, opaque or axiom (a Prop given by definition and not proved among them), a theorem whose proof is `sorry` (a Prop
### without proof), or a declaration b648 RESTATED (relay data/b648_sorry_classification.json). A claimed name the file does not declare is a
### REFERENCE, not a row, where another file of the kernel declares it, where it is a module of the kernel, or where its clause places it
### elsewhere -- naming a .lean file, Mathlib, or "in", "from", "of" or "via" another module's backticked name. A header with no row is MATCHES. Any OVERREACHES fails the arm, printed with file, line and the declaration; the
### per-file verdicts are banked.
###
### Usage:  python tools/module_header.py [--bank data/<name>.txt] [kernel ...]
### Library: header_of(text), rows_of(kernel, path, text, restated), run(kernels)
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import no_sorry_main as NSM   # noqa: E402
import axiom_claim as AC      # noqa: E402
import licensed_table as LT   # noqa: E402

NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROOF = re.compile(r'\b(?:PROVED|proved|proves|DERIVES|derives|establish(?:es|ed)?|holds unconditionally|unconditionally|outright)\b')
THEOREM = re.compile(r'\b(?:[Tt]heorems?|[Ll]emmas?)\b[:\s]*\(?\s*((?:`[\w.\'’!?₀-₉]+`(?:\s*(?:,|and)\s*)?)+)')
ELSEWHERE = re.compile(r'\.lean\b|\bMathlib\b|\b(?:in|from|of|via|imported from)\s+`?[A-Z][\w]*(?:\.[A-Z][\w]*)+`?')
DEFLIKE = ('def', 'abbrev', 'structure', 'class', 'inductive', 'opaque', 'axiom')
RESTATED_BANK = os.path.join(ROOT, 'data', 'b648_sorry_classification.json')


def restated():
    """{kernel: {declaration}} b648 RESTATED, from relay data/b648_sorry_classification.json."""
    try:
        rows = json.load(io.open(RESTATED_BANK, encoding='utf-8')).get('rows') or []
    except Exception:
        return {}
    out = {}
    for r in rows:
        if r.get('proposed') == 'RESTATED' and r.get('decl'):
            out.setdefault(r['kernel'], set()).add(r['decl'].split('.')[-1])
    return out


def header_of(text):
    """(line, body) of the `/-!` block at the file's head, before its first declaration; None where the file has none."""
    ds = AC.decls(text)
    first = ds[0][0] if ds else len(text)
    for op, s, e, body in AC.doc_blocks(text):
        if op == '/-!' and s < first:
            return text.count(NL, 0, s) + 1, body
        if s >= first:
            break
    return None


def _decl_index(text):
    """{last component: [(qualified, kind, sorry-closed)]} of the file's declarations."""
    ds = AC.decls(text)
    hits = set(ln for ln, _t in NSM.sorry_hits(text))
    lines = [text.count(NL, 0, off) + 1 for off, _k, _q in ds] + [text.count(NL) + 2]
    out = {}
    for i, (off, kind, q) in enumerate(ds):
        if not q:
            continue
        closed = any(lines[i] <= h < lines[i + 1] for h in hits)
        out.setdefault(q.split('.')[-1], []).append((q, kind, closed))
    return out


SUBJ = re.compile(r'^(?:\s*(?:,|and)\s*`[^`]+`)*\s*\)?\s*,?\s*(?:(?:is|are|was|were|has been|have been|stands|now|both|all)\s+)*'
                  r'(?:(?!(?:and|or|but|by)\b)\w+\s+){0,2}?(?:proved|PROVED|proven|established)\b|^\s*\(\s*(?:proved|PROVED)\b|^\s*proves\b')
OBJ = re.compile(r'(?:\b[Pp]roves?|\bPROVED:?|\bproved:|\b[Ee]stablish(?:es)?)\s+(?:that\s+)?(?:\w+\s+){0,3}?\(?\s*`?$'
                 r'|\b(?:proved|PROVED|proves)\b[^.;]{0,40}:\s[^.;]{0,160}$')


def unwrap(body):
    """a header's hard-wrapped lines joined into its sentences: a single line break becomes a space; a blank line, a bullet and a numbered
    item keep theirs; markdown emphasis (`*`, `**`) dropped so that "is *proved*" reads as "is proved"."""
    body = re.sub(r'(?<!\n)\n(?![ \t]*\n|[ \t]*(?:[-*•]|\d+[.)])\s)', ' ', body)
    parts = re.split(r'(`[^`]*`)', body)   # ### emphasis dropped outside code spans only: `stormer_*.length` keeps its star
    return ''.join(p if p.startswith('`') else re.sub(r'(?<=\S)\*+|\*+(?=\S)', '', p) for p in parts)


def as_proved(body, name):
    """True where the clause holding `name` makes it the subject or the object of a proof word (the attachment the generated rule finds,
    read narrowly: "`X` is proved", "`X` (proved)", "`X` proves", "proves `X`")."""
    for m in re.finditer(r'`%s`' % re.escape(name), body):
        after = re.split(r'[;\n]|\. ', body[m.end():m.end() + 90])[0]
        before = re.split(r'[;\n]|\. ', body[max(0, m.start() - 60):m.start()])[-1]
        if SUBJ.search(after) or OBJ.search(before):
            return True
    return False


def rows_of(kernel, path, text, restated_names=(), kernel_names=()):
    """(header line or None, [row]) for one file; a row dict(kernel, file, line, name, claim, words, verdict, why). `kernel_names`: the last
    components of every declaration of the kernel's other files -- a claimed name found there is a REFERENCE to another file."""
    h = header_of(text)
    if not h:
        return None, []
    line, body = h
    body = unwrap(body)
    idx = _decl_index(text)
    claims = []
    for name, grade, words, side in LT.attached_claims(body, plain=False):
        if grade == 'DERIVES' and PROOF.search(words) and as_proved(body, name):
            claims.append((name, 'PROVED', words))
    for m in re.finditer(r'\b[Pp]roves\s+(?:that\s+)?`([\w.\'’!?₀-₉]+)`', body):   # ### "Proves `X`": the rule's words are lower-case
        claims.append((m.group(1), 'PROVED', m.group(0)[:60]))
    for m in THEOREM.finditer(body):
        for n in re.findall(r'`([\w.\'’!?₀-₉]+)`', m.group(1)):
            claims.append((n, 'THEOREM', m.group(0)[:60]))
    rows, seen = [], set()
    tally = dict(proved=0, theorem=0, in_file=0, reference=0)
    for name, claim, words in claims:
        if (name, claim) in seen:
            continue
        seen.add((name, claim))
        tally['proved' if claim == 'PROVED' else 'theorem'] += 1
        CLAIMS.append((kernel, path, line, claim, name))
        short = name.split('.')[-1]
        cand = [x for x in idx.get(short, []) if x[0] == name or x[0].endswith('.' + name) or name.endswith('.' + x[0]) or '.' not in name]
        pos = body.find('`%s`' % name)
        pos = body.find(name) if pos < 0 else pos
        clause = re.split(r'[;\n]|\. ', body[max(0, pos - 90):pos + len(name) + 90])
        clause = next((c for c in clause if name in c), '')
        why = None
        if not cand:
            if ELSEWHERE.search(clause) or short in kernel_names:
                tally['reference'] += 1
                continue
            why = 'the header names `%s` as %s; the file declares no such name' % (name, 'proved' if claim == 'PROVED' else 'a theorem')
        else:
            tally['in_file'] += 1
            q, kind, closed = cand[0]
            if short in restated_names:
                why = '`%s` is described as %s; b648 RESTATED it' % (q, claim.lower())
            elif kind in DEFLIKE and claim == 'PROVED':
                why = '`%s` is described as proved; the file declares it a %s' % (q, kind)
            elif kind in ('theorem', 'lemma') and closed:
                why = '`%s` is described as %s; its proof in the file is `sorry`' % (q, 'proved' if claim == 'PROVED' else 'a theorem')
        if why:
            rows.append(dict(kernel=kernel, file=path, line=line, name=name, claim=claim, words=words, verdict='OVERREACHES', why=why))
    TALLY.append(tally)
    return line, rows


TALLY = []   # ### the claims each header read: proved, theorem, resolved in its file, placed elsewhere (the matcher's yield, printed)
CLAIMS = []  # ### every claim read, (kernel, file, line, PROVED or THEOREM, name), printed whole


def run(names):
    rs = restated()
    per, rows = {}, []
    for k in names:
        p = 'D:/' + k
        main, fs = AC.lean_files(p)
        nh = nm = 0
        texts = {}
        for f in fs:
            rc, t = AC._git(p, 'show', '%s:%s' % (main, f))
            if not rc:
                texts[f] = t
        owners = {}
        for f, t in texts.items():
            for _o, _kd, q in AC.decls(t):
                if q:
                    owners.setdefault(q.split('.')[-1], set()).add(f)
        mods = set(os.path.basename(f)[:-5] for f in texts)   # ### a module of the kernel named in a header is a reference to that file
        for f, t in texts.items():
            others = set(n for n, fl in owners.items() if fl - {f}) | (mods - {os.path.basename(f)[:-5]})
            line, rr = rows_of(k, f, t, rs.get(k, set()), others)
            if line is None:
                continue
            nh += 1
            nm += not rr
            rows += rr
        per[k] = dict(main=main[:12], files=len(fs), headers=nh, matches=nm, overreaches=nh - nm)
    return per, rows


def report(per, rows):
    L = ['module_header.py -- THE ARM G-MODULE-HEADER ((R259)(2)(c)): every module header of every kernel`s main read through the '
         'licensed-statement table`s generated rule extended to headers (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### kernel | main | .lean files | headers | MATCHES | OVERREACHES (headers with a row)']
    L += ['  %-34s %s %4d %4d %4d %4d' % (k, v['main'], v['files'], v['headers'], v['matches'], v['overreaches']) for k, v in per.items()]
    L += ['', '### EVERY OVERREACHES ROW (kernel file:line -- the declaration -- why):']
    L += ['  %s %s:%d -- %s -- %s' % (r['kernel'], r['file'], r['line'], r['name'], r['why']) for r in rows] or ['  NONE']
    files = sorted(set((r['kernel'], r['file']) for r in rows))
    ty = dict((k, sum(t[k] for t in TALLY)) for k in ('proved', 'theorem', 'in_file', 'reference'))
    L += ['', '### THE MATCHER`S YIELD over the headers read: claims of a name as proved %d ; names given as theorems %d ; resolved among the '
              'file`s own declarations %d ; placed elsewhere by their clause (REFERENCE) %d' % (ty['proved'], ty['theorem'], ty['in_file'],
                                                                                              ty['reference'])]
    L += ['### EVERY CLAIM READ (kernel file:line, the claim, the name):'] + ['  %s %s:%d %s `%s`' % c for c in CLAIMS]
    ok = not rows
    L += ['', '### ### **HEADERS %d ; MATCHES %d ; OVERREACHES %d HEADERS, %d ROWS ; VERDICT : %s**' % (
        sum(v['headers'] for v in per.values()), sum(v['matches'] for v in per.values()), len(files), len(rows), 'PASS' if ok else 'FAIL')]
    return ok, L


def main(argv):
    bank = argv[argv.index('--bank') + 1] if '--bank' in argv else None
    names = [a for a in argv if not a.startswith('--') and a != bank] or NSM.kernels()
    per, rows = run(names)
    ok, L = report(per, rows)
    if bank:
        for p, b in ((bank, (NL.join(L) + NL).encode('utf-8')),
                     (os.path.splitext(bank)[0] + '.json', (json.dumps(dict(ok=ok, per=per, rows=rows), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
            open(p + '.tmp', 'wb').write(b)
            os.replace(p + '.tmp', p)
    print(L[-1])
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
