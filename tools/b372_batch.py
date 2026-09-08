# -*- coding: utf-8 -*-
"""b372_batch.py -- COMPONENT 3: THE FIRST BATCH, UNDER `(R6)` AND `(R8)`.

### ### **NO ROW IS REPAIRED. ### THE CLASSIFICATION IS THE PRODUCT.**
### ### **EVERY ROW IS RE-ANCHORED BY ITS OWN CONTENT** before it is read, because a row cited by line
### number is a row that moves (`(R2)`).
### ### **THE PIN IS TAKEN FROM THE ROW, NOT FROM THIS SEAT**, with `b371`'s own PIN pattern IMPORTED --
### and ### **A PIN THAT DOES NOT RESOLVE IN THE KERNEL THE ROW NAMES IS NOT A PIN**, which turns some
### of `b371`'s pinned rows pinless. ### That is `PREDICATE_ONE_SHAPE` running the other way: a pattern
### that knows one shape ALSO matches things that are not that shape.
### ### **A PINLESS ROW IS OPENED AT THE KERNEL'S LIVE HEAD (R8)**, the head is recorded HERE and never
### written into the row, and the verdict is marked `CHECKED-AT-HEAD`.
### ### **KERNELS ARE READ THROUGH `git show <ref>:<path>`, NEVER THROUGH THE WORKING TREE** (`b309`).
### ### **`RETIRED` QUOTES THE KERNEL'S OWN RECORD.** ### An inference from absence is not a quotation,
### and the two are kept apart in the output.
### ### ### **AND THE LEDGER'S ABBREVIATIONS ARE EXPANDED, BECAUSE `b369` PAID FOR THAT LESSON:** ### a
### retirement written `a/b/c` names three declarations and a whole-word search finds one.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                 # noqa: E402
import anchor_from_file as AF    # noqa: E402
import b371_inventory as INV     # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERNELS = {'SIDE-effects': os.path.join('D:', os.sep, 'SIDE-effects'),
           'SIDE-kernel': os.path.join('D:', os.sep, 'SIDE-kernel')}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE TWELVE ROWS `b371` FLAGGED.** ### The file and the HINT are given; ### **THE LINE, THE PINS,
# ### THE KERNEL AND THE TERMINALS ARE ALL READ OFF THE ROW ITSELF.**
ROWS = [
    ('01', 'REGISTRY.md', '| p2-31 | The Yang-Mills Mass Gap via SIDE Exclusion |'),
    ('02', 'SPIRAL_MAP.md', '*(merged 2026-08-14)*'),
    ('03', 'VERIFICATION_LOOM.md', '| no-conspiracy twin primes |'),
    ('04', 'VERIFICATION_LOOM.md', '| no-conspiracy Goldbach |'),
    ('05', 'VERIFICATION_LOOM.md', '| no-conspiracy Sophie Germain |'),
    ('06', 'VERIFICATION_LOOM.md', '| `side_exclusion` | '),
    ('07', 'VERIFICATION_LOOM.md', '| Yang-Mills mass gap (form) |'),
    ('08', 'VERIFICATION_LOOM.md', '| GRH exclusion (form) |'),
    ('09', 'phase1.5/method/EXCLUSION_ENGINE.md', '| `mass_gap` / `Massless` |'),
    ('10', 'phase1.5/method/EXCLUSION_ENGINE.md',
     '| `bsd_full` / `RankMismatch` / `MismatchMechanism` |'),
    ('11', 'phase1.5/method/EXCLUSION_ENGINE.md', '| `no_conspiracy_twins` / `TwinFinite` |'),
    ('12', 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md', '| Per-conjecture instantiations |'),
]

# ### **`[ \t]*` AND NOT `\s*`:** ### `\s` matches a newline, so a blank line before the declaration
# ### lets the match start a line early and every reported line number is off by one. ### Caught by
# ### printing the located line back and finding it EMPTY.
DECL = r'^[ \t]*(?:@\[[^\]]*\][ \t]*)?(?:private |protected |noncomputable )?' \
       r'(theorem|lemma|def|abbrev|instance|structure|inductive|axiom)[ \t]+%s(?![A-Za-z0-9_])'

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True)


def gtext(repo, *a):
    return git(repo, *a).stdout.decode('utf-8', 'replace')


def resolves(repo, ref):
    r = git(repo, 'rev-parse', ref + '^{commit}')
    return r.stdout.decode().strip() if r.returncode == 0 else ''


def tree_lean(repo, ref):
    return [f for f in gtext(repo, 'ls-tree', '-r', '--name-only', ref).split(chr(10))
            if f.endswith('.lean')]


def declared(repo, ref, name):
    """### **A DECLARATION HEAD, NOT A MENTION.** ### Returns every file:line that declares it."""
    short = name.split('.')[-1]
    pat = re.compile(DECL % re.escape(short), re.M)
    hits = []
    for f in tree_lean(repo, ref):
        body = gtext(repo, 'show', '%s:%s' % (ref, f))
        for m in pat.finditer(body):
            ln = body[:m.start()].count(chr(10)) + 1
            hits.append(dict(file=f, line=ln, text=body.split(chr(10))[ln - 1].strip()[:120]))
    return hits


def expand_slashes(text):
    """### **`a/b/c` NAMES THREE DECLARATIONS.** ### b369's lesson, mechanised."""
    out = set()
    for m in re.finditer(r'`?([A-Za-z_][A-Za-z0-9_]*(?:/[A-Za-z0-9_]+)+)`?', text):
        parts = m.group(1).split('/')
        stem = parts[0]
        out.add(stem)
        pre = stem.rsplit('_', 1)[0] if '_' in stem else stem
        for p in parts[1:]:
            out.add(pre + '_' + p)
    return out


def retirement_record(repo, ref):
    """### **THE KERNEL'S OWN RECORD.** ### Every comment line under a heading that says RETIRE."""
    blocks = []
    for f in tree_lean(repo, ref):
        body = gtext(repo, 'show', '%s:%s' % (ref, f))
        rows = body.split(chr(10))
        for i, ln in enumerate(rows):
            if re.search(r'RETIRE', ln, re.I) and ln.lstrip().startswith('--'):
                blocks.append(dict(file=f, line=i + 1, text=ln.strip()))
        # ### the whole ledger region, so a quotation has context and is not one line torn out
    return blocks


def ledger_region(repo, ref):
    """### **THE LEDGER REGION, AND THE HEADING MUST BE A `--` COMMENT LINE.**
    ### ### The first version matched a DOCSTRING sentence saying `given in the retirement ledger
    ### ### below` and returned a two-line region, so every terminal came back `ABSENT`. ### **A
    ### ### PREDICATE THAT MATCHES THE MENTION INSTEAD OF THE THING REPORTS THE OPPOSITE OF THE
    ### ### TRUTH**, and it reports it confidently. ### The longest region wins, not the first."""
    best = None
    for f in tree_lean(repo, ref):
        body = gtext(repo, 'show', '%s:%s' % (ref, f))
        rows = body.split(chr(10))
        for i, ln in enumerate(rows):
            if not ln.lstrip().startswith('--'):
                continue
            if not re.search(r'RETIREMENT LEDGER', ln, re.I):
                continue
            end = i
            while end + 1 < len(rows) and (rows[end + 1].lstrip().startswith('--')
                                           or not rows[end + 1].strip()):
                end += 1
                if end - i > 400:
                    break
            cand = dict(file=f, start=i + 1, end=end + 1, rows=rows[i:end + 1])
            if best is None or len(cand['rows']) > len(best['rows']):
                best = cand
    return best


# ### **AN EXTENSION THIS ACT DECLARES AND MARKS AS ITS OWN.** ### `b371`'s imported TERMINAL pattern
# ### sees dotted and snake_case names only, so a row naming `RankMismatch` and `MismatchMechanism`
# ### hands the classifier ONE name out of three. ### **THE ROW'S OTHER NAMES ARE NOT SILENTLY
# ### DROPPED**; they are matched by this extension, classified, and REPORTED AS MATCHED BY IT.
# ### **AND IT REQUIRES A LOWERCASE LETTER**, or it matches the grading vocabulary -- `INTERFACES`,
# ### `DERIVES`, `SHELL` -- and reports a GRADE WORD as an absent declaration. ### It did, once.
CAMEL = re.compile(r'`([A-Z][A-Za-z0-9_]*[a-z][A-Za-z0-9_]*)`')
# ### **AND LEAN'S OWN VOCABULARY IS EXCLUDED BY NAME, NOT BY A CLEVERNESS.** ### `Prop` is a sort, not
# ### a terminal -- and it matched, and the string `opaque-Prop` in the kernel's ledger then made it
# ### come back RETIRED. ### **A FALSE TERMINAL WITH A CONFIDENT VERDICT IS WORSE THAN A MISS.**
# ### The list is written out so it can be disagreed with (`b369`'s three named exclusions).
BUILTIN = {'Prop', 'Type', 'Sort', 'Nat', 'Int', 'Bool', 'String', 'List', 'Option', 'Unit',
           'True', 'False', 'Set', 'Real', 'Complex', 'Fin', 'Char', 'Array', 'Subtype'}


def last_declared(repo, name, limit=40):
    """### **WHEN WAS IT LAST A DECLARATION?** ### Read-only history, so a row that is false at the
    head can be reported as ### **TRUE AT A REF IT DOES NOT NAME** -- which is the finding."""
    short = name.split('.')[-1]
    out = gtext(repo, 'log', '--format=%H', '-S', short).split()
    for c in out[:limit]:
        if declared(repo, c, name):
            return dict(commit=c, date=gtext(repo, 'show', '-s', '--format=%cI', c).strip()[:10])
    return None


def identify_kernel(txt):
    """### **THE KERNEL IS TAKEN FROM THE ROW, BY NAME IF THE ROW GIVES ONE.**
    ### ### And one row gives NONE -- it says the terminal is `not present on any live branch` and
    ### names only a `.lean` file. ### **A ROW THAT NAMES NO REPOSITORY IS NOT AN ERROR TO CRASH ON**,
    ### so the file it does name is looked for in each kernel and, if exactly one carries it, that is
    ### the kernel and ### **THE OUTPUT SAYS THE IDENTIFICATION WAS BY FILE AND NOT BY NAME.**"""
    for k in ('SIDE-kernel', 'SIDE-effects'):
        if k in txt:
            return k, 'by the repository name in the row'
    files = set(re.findall(r'([A-Za-z0-9_]+\.lean)', txt))
    if files:
        owners = []
        for k, p in KERNELS.items():
            tree = set(os.path.basename(f) for f in tree_lean(p, 'HEAD'))
            if files & tree:
                owners.append(k)
        if len(owners) == 1:
            return owners[0], ('by the file %s, because the row names no repository'
                               % sorted(files))
        return None, ('NOT IDENTIFIED -- the row names no repository and %s is carried by %s'
                      % (sorted(files), owners or 'no rostered kernel'))
    return None, 'NOT IDENTIFIED -- the row names neither a repository nor a file'


def profile_files(repo, ref):
    return [f for f in gtext(repo, 'ls-tree', '-r', '--name-only', ref).split(chr(10))
            if f.strip() and re.search(r'AXIOM_PRINT', f, re.I)]


def main(argv=None):
    rec('=' * 100)
    rec('b372 -- COMPONENT 3: THE FIRST BATCH. ### **CLASSIFIED, NOT REPAIRED.**')
    rec('=' * 100)
    rec('')
    rec('  ### the PIN pattern is IMPORTED from b371_inventory.py : %s' % INV.PIN.pattern)
    rec('  ### the TERMINAL pattern is IMPORTED too              : %s' % INV.TERMINAL.pattern)
    rec('')
    heads = {}
    for k, p in KERNELS.items():
        heads[k] = dict(head=gtext(p, 'rev-parse', 'HEAD').strip(),
                        branch=gtext(p, 'rev-parse', '--abbrev-ref', 'HEAD').strip(),
                        profiles=profile_files(p, 'HEAD'))
        rec('  ### ### **THE LIVE HEAD, RECORDED HERE AND NEVER IN A ROW (R8):**')
        rec('      %-14s `%s` = `%s`   ### shipped axiom profile : %s'
            % (k, heads[k]['branch'], heads[k]['head'], heads[k]['profiles'] or 'NONE'))
    rec('  ### ### **DATED 2026-09-08.** ### A check at a head is only as good as the date beside it.')

    # ### the kernel records, read ONCE per (kernel, ref) and quoted from
    ledgers = {}
    out = []
    rec('')
    for rid, rel, hint in ROWS:
        path = os.path.join(PP, rel.replace('/', os.sep))
        n, line = AF.find(path, hint)
        txt = line.rstrip()
        pins = [a or b for a, b in INV.PIN.findall(txt)]
        imported = sorted(set(t for t in INV.TERMINAL.findall(txt) if not t.endswith('.lean')))
        extra = sorted(set(CAMEL.findall(txt)) - set(imported) - BUILTIN)
        terms = imported + extra
        kern, how = identify_kernel(txt)
        repo = KERNELS.get(kern)
        rec('-' * 100)
        rec('  ROW %s -- %s:%d' % (rid, rel, n))
        rec('    | %s' % txt[:220])
        rec('    kernel : %s   ### identified %s' % (kern, how))
        rec('    pins matched in the row : %s' % (pins or 'NONE'))
        chosen, mode = None, None
        pinstate = []
        for p in pins:
            v = resolves(repo, p) if repo else ''
            pinstate.append(dict(pin=p, resolves=bool(v), commit=v))
            rec('      pin `%-24s` resolves in %s : %-5s %s'
                % (p, kern, bool(v), v[:12]))
        good = [x for x in pinstate if x['resolves']]
        if good:
            chosen, mode = good[0]['commit'], 'AT-PIN'
        elif repo:
            chosen, mode = heads[kern]['head'], 'CHECKED-AT-HEAD'
        rec('    ### ### **OPENED AT : `%s` -- %s**' % ((chosen or '')[:12], mode))
        if pins and not good:
            rec('    ### ### **AND THE ROW`S `PIN` DOES NOT RESOLVE IN THE KERNEL IT NAMES**, so the')
            rec('    ### ### row is PINLESS in fact and is opened at the head under `(R8)`.')

        key = (kern, chosen)
        if key not in ledgers:
            ledgers[key] = dict(region=ledger_region(repo, chosen),
                                marks=retirement_record(repo, chosen))
        reg = ledgers[key]['region']
        regtext = chr(10).join(reg['rows']) if reg else ''
        covered = expand_slashes(regtext) if regtext else set()

        verdicts = []
        for t in terms:
            short = t.split('.')[-1]
            hits = declared(repo, chosen, t) if repo else []
            named_outright = bool(re.search(r'(?<![A-Za-z0-9_])%s(?![A-Za-z0-9_])'
                                            % re.escape(short), regtext))
            named_abbrev = (short in covered)
            quote = None
            if named_outright or named_abbrev:
                for i, ln in enumerate(reg['rows']):
                    if short in ln or (named_abbrev and any(
                            s in ln for s in (short.rsplit('_', 1)[-1],))):
                        quote = dict(file=reg['file'], line=reg['start'] + i, text=ln.strip())
                        break
            if hits:
                v = 'PRESENT'
                prof = heads[kern]['profiles']
                note = ('profile read from %s' % prof) if prof else 'PROFILE NOT LOCATED'
            elif quote:
                v = 'RETIRED'
                note = 'named %s in the kernel`s own retirement ledger' % (
                    'outright' if named_outright else 'by the ledger`s `a/b/c` abbreviation')
            else:
                v = 'ABSENT'
                note = 'no declaration at this ref and no line of the kernel`s record names it'
            last = None if hits else last_declared(repo, t)
            verdicts.append(dict(terminal=t, verdict=v, note=note, declared=hits, quote=quote,
                                 named_outright=named_outright, named_abbrev=named_abbrev,
                                 pattern=('b371 imported' if t in imported
                                          else 'this act`s declared extension'),
                                 last_declared=last))
            rec('    %-42s ### ### **%s** -- %s' % ('`' + t + '`', v, note))
            if t in extra:
                rec('        ### matched by THIS ACT`S DECLARED EXTENSION, not by the imported pattern.')
            if hits:
                rec('        declared at : %s' % '; '.join(
                    '%s:%d' % (h['file'], h['line']) for h in hits[:3]))
                rec('        | %s' % hits[0]['text'])
            if quote:
                rec('        the kernel`s own words, %s:%d' % (quote['file'], quote['line']))
                rec('        | %s' % quote['text'])
            if last:
                rec('        ### ### **IT WAS A DECLARATION AS RECENTLY AS `%s` (%s)** -- a ref this'
                    % (last['commit'][:12], last['date']))
                rec('        ### ### row does not name.')
        # ### **THE ROW-LEVEL LINE IS A COMPOSITION, NOT A FIFTH WORD.** ### The order rules four
        # ### words for a TERMINAL; a row naming several terminals gets the tally of those four and
        # ### ### **NOT AN INVENTED WORD LIKE `MIXED`**, which is what this line said first.
        comp = {}
        for v in verdicts:
            comp[v['verdict']] = comp.get(v['verdict'], 0) + 1
        rowverdict = (list(comp)[0] if len(comp) == 1
                      else ', '.join('%s x%d' % (k, n) for k, n in sorted(comp.items())))
        rec('    ### ### ### **THE ROW`S TERMINALS : %s%s**'
            % (rowverdict, ('  (' + mode + ')') if mode == 'CHECKED-AT-HEAD' else ''))
        out.append(dict(row=rid, file=rel, line=n, text=txt, kernel=kern, pins=pinstate,
                        terminals=terms, ref=chosen, mode=mode, verdicts=verdicts,
                        row_verdict=rowverdict))

    rec('')
    rec('=' * 100)
    rec('  ### THE TALLY.')
    rec('=' * 100)
    tally = {}
    for r in out:
        tally[r['row_verdict']] = tally.get(r['row_verdict'], 0) + 1
    for k, v in sorted(tally.items()):
        rec('    rows classified %-10s : %d' % (k, v))
    modes = {}
    for r in out:
        modes[r['mode']] = modes.get(r['mode'], 0) + 1
    rec('    by mode : %s' % modes)
    tv = {}
    for r in out:
        for v in r['verdicts']:
            tv[v['verdict']] = tv.get(v['verdict'], 0) + 1
    rec('    terminals classified : %s' % tv)
    absent = [(r['row'], v['terminal']) for r in out for v in r['verdicts']
              if v['verdict'] == 'ABSENT']
    rec('')
    rec('    ### ### **THE NAMES THE KERNEL`S OWN RECORD DOES NOT MENTION AT ALL : %s**' % absent)
    rec('    ### these are the retirement ledger`s OWN LACUNAE, filed and not invented (`(R5)`).')
    rec('  ### **NO ROW WAS REPAIRED. ### NO PIN WAS ADDED. ### NO KERNEL FILE WAS WRITTEN.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b372_batch_notes', LINES)
    io.open(os.path.join(D, 'b372_batch.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(heads=heads, rows=out, tally=tally, modes=modes, terminal_tally=tv,
                        absent=absent, date='2026-09-08',
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
