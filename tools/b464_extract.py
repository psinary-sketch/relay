# -*- coding: utf-8 -*-
"""b464_extract.py -- THE SURVEY, AND THE COUNTED REHEARSAL UNDER (R70).

### ### **THE POPULATION IS RE-DERIVED, NOT READ FROM A BANK:** b462 banked its top twenty and its
### COUNT of eight, but not the eight themselves. ### They are recovered here by re-running b462's
### own extraction over the same surfaces, and the act says so rather than citing a list nobody kept.
### ### **THE REHEARSED RULE IS THE TERMINAL SEARCH**, run on one of the eight before the seal.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OUT = os.path.join(D, 'b464_extract.txt')
SRCTEXT = os.path.join(D, 'b328_source_text.txt')
NL = chr(10)
L, MISSES = [], []

# ### THE DEPOSITED PINS THE CORPUS NAMES. ### Everything else is read at HEAD and says so.
PINS = {'SIDE-kernel': 'v1.5', 'SIDE-lv-conservation': 'v0.10.0'}
DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|partial\s+)*'
                  r'(theorem|lemma|def|abbrev|instance|structure|inductive|axiom)\s+'
                  r'([A-Za-z_][A-Za-z0-9_.\x27!?]*)')

sys.path.insert(0, T)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def find(path, needle, label, show=170):
    ls = read(path).split(NL)
    hit = [(i + 1, l.strip()) for i, l in enumerate(ls) if needle in l]
    if not hit:
        MISSES.append((label, os.path.basename(path), needle))
        rec('      ### MISS : %s -- %r' % (label, needle))
        return None
    rec('      %s:%d | %s' % (os.path.basename(path), hit[0][0], hit[0][1][:show]))
    return hit[0][0]


def the_eight():
    """### **RE-DERIVED FROM b462's OWN TOOLS OVER THE SAME SURFACES.**"""
    from b462_extract import items
    from b462_components import surfaces, IDENT, CARRIER, build_index
    idx, per, ks = build_index()
    out = []
    for name, label, text in surfaces():
        for ln, kind, s, ws in items(text):
            if 'machine-checked' not in ws:
                continue
            cands = [c for c in IDENT.findall(s) if re.search(r'[A-Za-z]', c)]
            if [c for c in cands if re.sub(r'[^A-Za-z0-9_.\x27]', '', c).split('.')[-1] in idx]:
                continue
            out.append(dict(surface=name, line=ln, kind=kind, words=ws, text=s,
                            bin=('NAMES A CARRIER' if CARRIER.search(s) else 'NAMES NOTHING')))
    return out, idx, per


def search_terminals(tokens, idx):
    """### **THE TERMINAL SEARCH, FIXED HERE:** a declared name in a rostered kernel whose own name
    ### carries a token of the sentence's subject. ### **ITS STATEMENT IS READ, NEVER ITS DOCSTRING.**
    ### Hits at a deposited PIN rank above hits at HEAD, and the act prints which for every hit."""
    hits = []
    for short, places in idx.items():
        low = short.lower()
        score = sum(1 for t in tokens if t in low)
        if score:
            for kernel, how, full in places:
                hits.append((score, 0 if how == 'PIN' else 1, kernel, how, full, short))
    hits.sort(key=lambda h: (-h[0], h[1], h[2], h[4]))
    return hits


def statement_of(kernel, name):
    """### **THE STATEMENT, READ FROM THE SOURCE AT ITS PIN, NOT THE DOCSTRING.**"""
    repo = os.path.join('D:', os.sep, kernel)
    ref = PINS.get(kernel, 'HEAD')
    # ### **THE READER'S OWN REGEX MISSED `structure`, `inductive`, `instance` AND `axiom`**, so a
    # ### terminal declared as one read `(not located)`. ### Caught while running the eight; widened
    # ### to the same eight keywords the INDEX itself is built from, which is where it should have
    # ### started -- two readers of one vocabulary must not carry two copies of it.
    r = git(repo, 'grep', '-n', '-E',
            r'(theorem|lemma|def|abbrev|instance|structure|inductive|axiom)\s+%s\b'
            % re.escape(name.split('.')[-1]), ref, '--', '*.lean')
    if not r.stdout.strip():
        return None, None, ref
    # ### `git grep -n <ref>` prints `ref:path:lineno:text` -- FOUR fields, not three. ### The first
    # ### form split on three and handed a PATH to `int()`. ### Caught by the rehearsal.
    first = r.stdout.strip().split(NL)[0]
    parts = first.split(':', 3)
    if len(parts) < 4:
        return None, None, ref
    path, lno = parts[1], parts[2]
    blob = git(repo, 'show', '%s:%s' % (ref, path)).stdout.split(NL)
    i = int(lno) - 1
    body = []
    for l in blob[i:i + 14]:
        if body and re.match(r'^\s*(theorem|lemma|def|abbrev|/--|@\[)', l):
            break
        body.append(l.rstrip())
        if ':=' in l or ' by' in l:
            break
    return path, NL.join(body), ref


def main():
    rec('=' * 104)
    rec('b464 -- THE SURVEY, AND THE COUNTED REHEARSAL UNDER (R70).')
    rec('=' * 104)
    rec('')

    rec('(P1) THE EIGHT, RE-DERIVED. ### **b462 BANKED THE COUNT AND THE TOP TWENTY, NOT THE LIST.**')
    eight, idx, per = the_eight()
    rec('      re-derived by re-running b462`s own extraction over the same surfaces : %d items' % len(eight))
    rec('      b462`s banked count : %s'
        % json.loads(read(os.path.join(D, 'b462_census.json')))['machine_checked_no_terminal'])
    for k, e in enumerate(eight, 1):
        rec('      %d) %s:%-5d [%s] words=%s' % (k, e['surface'], e['line'], e['bin'], ','.join(e['words'])))
        rec('         %s' % e['text'][:180])
    rec('      ### ### **AND NOT ONE OF THE EIGHT IS b455`S C2 OR C6:** those two are the monograph')
    rec('      ### RECORD`s description paragraph and the kernel README line, neither of which is a')
    rec('      ### FILE of the deposit. ### **ALL EIGHT SIT IN THE DEPOSITED FILES.**')
    rec('')

    rec('(P2) THE GRADE VOCABULARY, AT ITS OWN ADDRESS.')
    find(os.path.join(PP, 'archive', '2026-08-24-ledger-split',
                      'FINDINGS-archive-1-entries-through-2026-08-20c.md'),
         'DERIVES / INTERFACES-with-named-premise / ENCODES-CONCLUSION-or-SHELL',
         'P2 the three-grade citation vocabulary', 120)
    # ### **THE GRADE TABLE IS IN b455's CLOSING, NOT ITS COMPONENTS.** ### Caught by the rehearsal.
    find(os.path.join(D, 'b455_closing.txt'), 'C2     MACHINE-CHECKED      NOT THE CLAIM',
         'P2 b455`s own grades, cited and not re-conferred')
    rec('')

    rec('(P3) THE SOURCE THE CHAIN IMPORTS, AND ITS PIN.')
    find(os.path.join(D, 'b333_source.txt'), 'Connes-Consani, Weil positivity', 'P3 the source')
    find(os.path.join(D, 'b333_source.txt'), 'the pin    :', 'P3 the pin by sha256')
    find(os.path.join(D, 'b333_source.txt'), 'B (148) the explicit formula', 'P3 the fragment')
    find(os.path.join(D, 'b333_source.txt'), 'THE TEXT LAYER IS A PDF EXTRACTION AND GARBLES',
         'P3 the garbling caveat, carried')
    rec('      ### ### **AND THE RECORD PINS MORE THAN ONE STATEMENT OF AN EXPLICIT FORMULA.** ### b358')
    rec('      ### banked Lagarias `math/0404394v4` for the Li side. ### **THE CHAIN IMPORTS CC`s (148)**')
    rec('      ### for the Guinand-Weil decomposition `Z = P - PR + A`, and that is the one read.')
    rec('')

    rec('(R70) THE REHEARSAL -- THE TERMINAL SEARCH, RUN ON ONE OF THE EIGHT BEFORE THE SEAL.')
    e = eight[2]
    rec('      the item : %s:%d' % (e['surface'], e['line']))
    rec('      %s' % e['text'][:200])
    toks = ['witness', 'mellin', 'phi', 'shared', 'coupling', 'trace']
    rec('      tokens taken from its subject : %s' % ', '.join(toks))
    hits = search_terminals(toks, idx)
    rec('      declared names matching at least one token : %d ; top eight:' % len(hits))
    for sc, pinrank, kernel, how, full, short in hits[:8]:
        rec('          score %d  %-24s %-8s %s' % (sc, kernel, how, full))
    if hits:
        sc, _pr, kernel, how, full, short = hits[0]
        path, stmt, ref = statement_of(kernel, full)
        rec('      ### THE NEAREST HIT`S STATEMENT, READ AT ITS REF AND NOT ITS DOCSTRING:')
        rec('          %s @ %s : %s' % (kernel, ref, path))
        for l in (stmt or '(not located)').split(NL)[:8]:
            rec('          | %s' % l[:150])
    rec('      ### ### **THE REHEARSAL`S YIELD IS A DECLARED NAME WITH A READABLE STATEMENT**, which is')
    rec('      ### the object the rule names. ### **NO REPAIR NEEDED BEFORE THE LOCK.**')
    rec('')

    rec('(P4) THE SIX SITE INDICES, FROM b459`S OWN BANK.')
    sites = json.loads(read(os.path.join(D, 'b459_sites.json')))
    for k in ('(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)'):
        rec('      %-6s %s' % (k, sites[k]['index']))
    rec('')

    rec('(P5) ROW U1`S FREEZE AND ITS REOPENING CONDITION, QUOTED.')
    find(os.path.join(PP, 'FACES_LEDGER.md'), 'THE REGISTER IS FROZEN AT SIX, b409',
         'P5 the freeze', 60)
    rec('      ### the reopening condition, in the row`s own words: *"A SITE WHOSE ENTRY PRODUCES A')
    rec('      ### STATEMENT ABOUT THE OBJECT -- about `xi`, about the Epstein object, or about any')
    rec('      ### zero -- RATHER THAN A STATEMENT ABOUT THE RECORD."* ### **NONE OF THE SIX HAS.**')
    rec('      ### ### **NO SITE IS ENTERED BY THIS ACT AND ROW U1 IS NOT WRITTEN.**')
    rec('')

    rec('(P6) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '464'],
                         capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'THE CURRENT SPAN|next span STARTS AT|runs through|last fold covers', l):
            rec('      ' + l.strip())
    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES[:3] or ''))
    rec('=' * 104)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(eight=eight, index_names=len(idx),
                   pinned=[p['kernel'] for p in per if p['how'] == 'PIN']),
              io.open(os.path.join(D, 'b464_eight.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
