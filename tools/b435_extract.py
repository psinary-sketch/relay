# -*- coding: utf-8 -*-
"""b435_extract.py -- THE SURVEY FOR b435: THE CURE SHARED, AND THE SKIPS THAT PRINT LIKE PASSES.
### **THE CORPUS'S OWN TOOLS ONLY. ### NOTHING IS FETCHED, NOTHING IS BUILT, AND THIS TOOL WRITES
### NO TOOL AND NO CORPUS FILE.** ### It reads: b314's handler at its own line; every `rmtree` call
### site with the evidence that decides whether its tree can hold files the process cannot unlink;
### the guard whose skip prints like a pass; and the census scope.
### ### **EVERY CLASSIFICATION BELOW IS MADE FROM THE ENCLOSING FUNCTION'S OWN SOURCE**, never from
### the seat's recollection of what a temp directory holds.
"""
import io
import os
import re
import sys
import tokenize

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
FERRY = os.path.join(D, 'b435_ferry.txt')
OUT = os.path.join(D, 'b435_extract.txt')
NL = chr(10)
L, MISS = [], []
READS = [0]

# ### THE GUARDS THEMSELVES, NAMED ON THE ORDER'S OWN INSTRUCTION TO REPORT THEM SEPARATELY.
GUARDS = ('b376_lockgate.py', 'b378_lockgate.py', 'gate_hash.py')


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


def read(p):
    READS[0] += 1
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception as exc:
        MISS.append('%s : %s' % (os.path.basename(p), exc))
        return ''


def code_of(src):
    """### BAR: COMMENTS AND STRING LITERALS STRIPPED BEFORE ANY SOURCE MATCH."""
    out = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type in (tokenize.COMMENT, tokenize.STRING):
                continue
            out.append(tok.string)
    except Exception:
        return ''
    # ### **TWO NEEDLES, TWO NORMALISATIONS, AND THE FIRST WRITING USED THE WRONG ONE.** ### This
    # ### helper closes dots so `a.b` matches, but leaves the spaces the tokenizer puts around `=`
    # ### -- so `ignore_errors=True` never matched and the census reported ZERO call sites while
    # ### ten stood in the tree. ### **A CENSUS THAT FINDS NOTHING LOOKS EXACTLY LIKE A CLEAN
    # ### ### CORPUS**, which is this sortie's own minted species in a new dress.
    return re.sub(r'\s+', '', ' '.join(out))


def code_keep_strings(src):
    """### COMMENTS STRIPPED, ### **STRING LITERALS KEPT.**

    ### ### **THE BAR SAYS STRIP BOTH, AND FOR AN ARM READING ITS OWN PROSE THAT IS RIGHT.** ### It
    ### is wrong here, and the first writing got it exactly backwards: the evidence that a directory
    ### holds git objects IS a string literal -- `'init'`, `'clone'`, `'-C'` -- so a stripper that
    ### removes strings removes the only evidence there is. ### **THE CLASSIFIER WAS BLIND BY
    ### ### CONSTRUCTION AND CALLED EVERY TREE PLAIN.** ### Comments still go: a comment mentioning
    ### git is not git being run.
    """
    out = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type == tokenize.COMMENT:
                continue
            out.append(tok.string)
    except Exception:
        return ''
    return re.sub(r'\s+', '', ' '.join(out))


def wrap(text, width=90, indent='        '):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(indent + line)
            line = w
        else:
            line = (line + ' ' + w).strip()
    if line:
        out.append(indent + line)
    return out


def enclosing(src, lineno, span=60):
    """### THE FUNCTION A LINE SITS IN, SO A SITE IS JUDGED ON ITS OWN CONTEXT.

    ### ### **AND THE FRAGMENT IS DEDENTED BEFORE IT IS TOKENIZED.** ### The first writing handed
    ### `tokenize` a fragment that begins with an INDENTED `def`; it raised `IndentationError`, the
    ### stripper returned the empty string, and ### **EVERY SITE CAME BACK WITH NO EVIDENCE AND WAS
    ### ### CLASSED PLAIN** -- including `b257_checks.py`, which runs `git init` in the very
    ### directory it then removes. ### A classifier whose evidence is always empty classifies
    ### everything the same way and looks decisive doing it.
    """
    import textwrap
    lines = src.splitlines()
    i = lineno - 1
    start = i
    while start > 0 and not re.match(r'^\s*(def |class )', lines[start]):
        start -= 1
    lo = max(0, start)
    end = min(len(lines), i + span)
    frag = NL.join(lines[lo:end])
    return textwrap.dedent(frag), lo + 1


def sites():
    """### EVERY `ignore_errors=True` CALL SITE, BY FILE AND LINE. ### **CALL SITES, NOT MENTIONS.**"""
    out = []
    for f in sorted(os.listdir(T)):
        if not f.endswith('.py'):
            continue
        src = read(os.path.join(T, f))
        if 'ignore_errors=True' not in code_of(src):
            continue
        for i, ln in enumerate(src.splitlines(), 1):
            if 'ignore_errors=True' in ln and 'rmtree' in ln:
                out.append((f, i, ln.strip()))
    return out


def main(argv):
    rule('=')
    say('b435_extract.py -- THE SURVEY. ### THE HANDLER, THE SITES, THE SKIP, AND THE CENSUS SCOPE.')
    rule('=')
    say('  ### NOTHING IS FETCHED. ### NOTHING IS BUILT. ### THIS TOOL WRITES NO TOOL.')
    say()

    # ### =========================================================================================
    rule()
    say('  (1) b314`S HANDLER, AT ITS OWN FILE AND LINE.')
    rule()
    src = read(os.path.join(T, 'b314_coldclone.py'))
    ln = next((i for i, x in enumerate(src.splitlines(), 1)
               if re.match(r'^def _force_rm', x)), None)
    say('    tools/b314_coldclone.py:%s' % ln)
    if ln:
        for x in src.splitlines()[ln - 1:ln + 3]:
            say('        %s' % x.rstrip())
    else:
        MISS.append('b314`s handler not located')
    use = [i for i, x in enumerate(src.splitlines(), 1) if 'onerror=_force_rm' in x]
    say('    and its one use, at line(s)   : %s' % use)
    say('    ### **IT HAS LIVED HERE SINCE b314 AND IN NO OTHER TOOL**, which is the whole of what')
    say('    ### `(R46)` is about. ### A second tool, `b314_coldrelay.py`, carries its own copy:')
    cr = read(os.path.join(T, 'b314_coldrelay.py'))
    say('      b314_coldrelay.py defines its own `_force_rm` : %s'
        % bool(re.search(r'^def _force_rm', cr, re.M)))
    say('    ### **SO THE CURE WAS ALREADY DUPLICATED ONCE INSIDE ITS OWN ACT**, which is the same')
    say('    ### defect one step earlier: a copy is not a share.')
    say()

    # ### =========================================================================================
    rule()
    say('  (2) EVERY CALL SITE, AND THE EVIDENCE THAT DECIDES IT.')
    rule()
    S = sites()
    say('    call sites found : %d in %d files' % (len(S), len(set(f for f, _i, _t in S))))
    say()
    say('    %-24s %-6s %s' % ('file', 'line', 'what its own source shows in that function'))
    for f, i, _t in S:
        fs = read(os.path.join(T, f))
        fn, _fl = enclosing(fs, i)
        ev = []
        for pat, lbl in ((r"'init'", "git init in it"), (r"'clone'", 'git clone into it'),
                         (r'checkout-index', 'checkout-index --prefix (blobs only, no .git)'),
                         (r"'\.git'", "a filter that excludes .git"),
                         (r'copytree', 'copytree'), (r'mkdtemp', 'mkdtemp')):
            if re.search(pat, fn):
                ev.append(lbl)
        say('    %-24s %-6d %s' % (f, i, '; '.join(ev) or '(nothing but the removal)'))
    say()
    say('    ### **THIS PRINTS EVIDENCE AND CLASSIFIES NOTHING.** ### Three successive mechanical')
    say('    ### rules were tried here and each mis-sorted a site: one matched `git` anywhere in the')
    say('    ### function and called a sandbox that FILTERS `.git` OUT git-bearing; the next excluded')
    say('    ### on any `.git` string and flipped a directory that really is `git init`-ed. ### **A')
    say('    ### ### DERIVATION THAT KEEPS CHANGING ITS ANSWER IS NOT A MEASUREMENT**, and dressing')
    say('    ### the seat`s judgement as one would hide where the judgement actually lies.')
    say('    ### **SO THE CALL IS THE SEAT`S, MADE ON THE EVIDENCE ABOVE, BY A RULE THE FACE STATES**')
    say('    ### and carried per site in the components tool with its reason -- which is how this')
    say('    ### corpus already chooses a keystone row when a marker matches three (b430`s `F5`).')
    say()
    say('    ### AND THE GUARDS AMONG THEM, NAMED SEPARATELY AS THE ORDER REQUIRES:')
    for g in GUARDS:
        hits = [(f, i) for f, i, _t in S if f == g]
        say('      %-24s %s' % (g, hits if hits else '(no call site)'))
    say('    ### **THESE ARE INSTRUMENTS THAT DECIDE WHETHER AN ACT MAY SEAL**, so a change to them')
    say('    ### is a change to the gate itself and is reported on its own line, not in a total.')
    say()

    # ### =========================================================================================
    rule()
    say('  (3) THE SKIP THAT PRINTS LIKE A PASS.')
    rule()
    h = read(os.path.join(T, 'b304_hooks.py'))
    for i, x in enumerate(h.splitlines(), 1):
        if 'SKIPPED' in x:
            say('    b304_hooks.py:%d' % i)
            for w in wrap(re.sub(r'\s+', ' ', x.strip())[:300], 88, '        '):
                say(w)
    m = re.search(r'(?m)^.*REPOS FAILING.*$', h)
    say('    the line that totals it :')
    say('        %s' % (m.group(0).strip()[:96] if m else '### NOT FOUND ###'))
    fails = re.findall(r'(?m)^\s*(\w+)\s*(?:\+=|=)\s*.*fail', h)
    say('    ### **THE SKIP IS COUNTED INTO THE SAME TOTAL AS A FAILURE**, which is why the number')
    say('    ### reads as a failure in one table and as a pass in another. ### The state exists in')
    say('    ### the per-repository row and is LOST in the total.')
    say()
    say('    ### THE THREE STATES THE REPORT MUST DISTINGUISH: ### **PASS** (the guard ran and')
    say('    ### refused what it should), ### **FAIL** (it ran and did not), ### **SKIPPED** (it')
    say('    ### could not run, with the reason).')
    say()

    # ### =========================================================================================
    rule()
    say('  (4) THE CENSUS SCOPE, AND ITS POSITIVE CONTROL.')
    rule()
    say('    ### **THE CENSUS IS BY DESCRIPTION, NOT BY A LIST THIS SEAT TYPES.** ### A handler for')
    say('    ### an environmental failure is a routine that catches or works around a condition of')
    say('    ### the MACHINE rather than of the corpus -- a read-only tree, a rate limit, an')
    say('    ### encoding, a lock, a timeout, a memory ceiling -- and that lives in ONE tool.')
    say('    ### **THE POSITIVE CONTROL IS b314`S OWN HANDLER**: a census that cannot find the one')
    say('    ### the order names is not a census, and its count means nothing.')
    say()
    pats = [('read-only tree', r'S_IWRITE|chmod.*0o?[67]00|onerror\s*=|onexc\s*='),
            ('rate limit / retry', r'RETRIES|BACKOFF|time\.sleep\(\s*\d|429|503'),
            ('encoding', r"errors\s*=\s*'replace'|BOM|utf-8-sig|reconfigure\("),
            ('lock / busy', r'WinError 32|PermissionError|being used by another'),
            ('timeout ceiling', r'TimeoutExpired|timeout=\d|INCOMPLETE'),
            ('memory ceiling', r'bad_alloc|MemoryError|out of memory')]
    say('    the descriptions the census will search, each a MACHINE condition:')
    for lbl, p in pats:
        n = 0
        for f in sorted(os.listdir(T)):
            if f.endswith('.py') and re.search(p, code_of(read(os.path.join(T, f))) or ''):
                n += 1
        say('      %-22s tools matching : %d' % (lbl, n))
    say('    ### **THESE ARE SCOPE COUNTS, NOT THE CENSUS.** ### The census is Component 3 and it')
    say('    ### narrows these to handlers that live in ONE tool and nowhere else.')
    say()

    rule('=')
    say('  ### READS ATTEMPTED : %d' % READS[0])
    say('  ### MISSES          : %d' % len(MISS))
    for m_ in MISS:
        say('      %s' % m_)
    say('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rule('=')
    txt = NL.join(L) + NL
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(txt)
    os.replace(OUT + '.tmp', OUT)
    print(txt)
    print('  written: %s' % os.path.basename(OUT))
    return 0 if os.path.exists(OUT) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
