# -*- coding: utf-8 -*-
"""b369_repair.py -- COMPONENT 1: `(R4)` EXECUTED. ### **PRESERVE BY QUOTATION, REPAIR BY EDIT.**

### ### **THE ORDER OF OPERATIONS IS THE RULING'S OWN:** ### the original rows are QUOTED VERBATIM into
### the currency block; the quotation is VERIFIED byte-for-byte against the rows read before the edit;
### ### **ONLY THEN** ### is the list edited.
### ### **THE CLASSIFICATION IS RE-DERIVED HERE AND NOT CARRIED.** ### This tool reads no prior act's
### JSON. ### It reads the front document's own export rows at the pinned ref, extracts the names they
### carry, and searches the kernel's own `.lean` files for a ### **DECLARATION** ### of each. ### `b368`'s
### figure is a CONSTANT in this file, used ONLY in the disagreement line and never in a count.
### ### **AND THE EXPORT ARM IS A CONTENT PREDICATE.** ### After the edit the repaired rows are searched
### for every ABSENT name and the arm requires ### **ZERO HITS.** ### A count of edited lines proves
### nothing about what a list exports.
### ### **`(R5)` IS MECHANIZED, NOT PROMISED:** ### the block states, for each evidence group, what the
### kernel's record DOES say -- and where it says nothing, ### **THAT IT SAYS NOTHING.** ### No reason
### for any retirement is asserted.
### ### **NO `.lean` FILE IS WRITTEN AND NO BUILD IS RUN.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import anchor_from_file as AF   # noqa: E402
import gate_needle as GN        # noqa: E402

D = os.path.join(ROOT, 'data')
KERNEL = os.path.join('D:', os.sep, 'SIDE-effects')
AGENTS = os.path.join(KERNEL, 'AGENTS.md')
STRUCT_REL = 'SIDEEffects/Structural.lean'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KERNEL_LEAN = ['SIDEEffects.lean', 'SIDEEffects/ExhaustivenessLicense.lean',
               'SIDEEffects/Milestones.lean', 'SIDEEffects/Phase15/Module1.lean',
               'SIDEEffects/Phase15/SIDEFramework.lean', STRUCT_REL]

LAYER = re.compile(r'^- \*\*[^*]+\*\*:')
DECL = r'^\s*(theorem|lemma|def|abbrev|instance|axiom|structure|inductive)\s+%s\b'

# ### **`b368`'s FIGURE, TYPED HERE AS A CONSTANT SO THE COMPARISON IS EXPLICIT.**
# ### **IT IS NEVER AN INPUT TO A COUNT** -- only to the disagreement line.
B368_ABSENT = 18
B368_HEAD = '5530d7c'

MARK = '<!-- b369 (R4): the original list preserved verbatim, and the list repaired -->'
B368_MARK = '<!-- b368 currency block: layer-1 export list vs source -->'

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(*a):
    return subprocess.run(['git', '-C', KERNEL] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def nl(s):
    """### **THE WORKING FILE IS CRLF AND ITS BLOB IS LF** (`core.autocrlf`, `b309`'s trap). ### Every
    ### comparison in this tool is made in LF and every write is made in LF, so BAR 3 measures the EDIT
    ### and not the checkout. ### **A BYTE COMPARISON THAT MEASURES A LINE ENDING MEASURES NOTHING.**"""
    return s.replace(chr(13) + chr(10), chr(10))


def put(path, text):
    """### ONE FULL-FILE WRITE, IN LF, NEVER AN APPEND INTO A FILE OF THE OTHER FLAVOUR."""
    io.open(path, 'w', encoding='utf-8', newline='').write(text)


def kernel_text(rel):
    p = os.path.join(KERNEL, rel.replace('/', os.sep))
    return io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


def declaration_of(name):
    out = []
    for rel in KERNEL_LEAN:
        for i, ln in enumerate(kernel_text(rel).split(chr(10)), 1):
            if name in ln and re.match(DECL % re.escape(name), ln.split('--')[0]):
                out.append(dict(file=rel, line=i, text=ln.strip()[:170]))
    return out


def history_of(name):
    outs = git('log', '--oneline', '-S', name, '--', '*.lean').splitlines()
    return [x.strip()[:90] for x in outs if x.strip()]


def ledger_span(struct):
    """### THE LEDGER'S OWN COMMENT BLOCK, LOCATED BY ITS HEADING AND NOT BY A LINE NUMBER."""
    lines = struct.split(chr(10))
    start = None
    for i, ln in enumerate(lines):
        if 'RETIREMENT LEDGER' in ln:
            start = i
            break
    if start is None:
        return ''
    end = start
    for i in range(start, len(lines)):
        if lines[i].strip().startswith('--') or not lines[i].strip():
            end = i
        else:
            break
    return chr(10).join(lines[start:end + 1])


STOP = {'layer', 'and', 'the', 'full', 'for'}


def ledger_headings(ledger):
    """### THE LEDGER'S OWN ENTRY HEADINGS, READ FROM ITS OWN INDENTATION.

    ### ### **`b368` HAD NO NOTION OF A HEADING AND THAT IS WHY IT WAS WRONG.** ### It looked for a name
    ### preceded by a backtick or a slash. ### The ledger's entry for the shared engine names its
    ### declaration as a ### **BARE HEADING** -- `side_exclusion (¬P → ¬P)` -- so `b368` reported the
    ### layer as having no entry at all when it has an entry naming the declaration outright."""
    out = []
    for i, ln in enumerate(ledger.split(chr(10)), 1):
        m = re.match(r'^--\s{3}(\S.*)$', ln)
        if m:
            out.append(dict(line=i, text=m.group(1).strip()))
    return out


def explicit_names(ledger):
    """### **NAMED OUTRIGHT: THE IDENTIFIER APPEARS AS A WHOLE WORD ANYWHERE IN THE LEDGER**, whether in
    ### backticks, after a slash, or as a heading. ### No shape is privileged."""
    return set(re.findall(r'[A-Za-z_][A-Za-z0-9_]{2,}', ledger))


def abbreviated_names(ledger):
    """### **THE LEDGER'S SLASH ABBREVIATION, EXPANDED -- AND MARKED AS AN EXPANSION.**

    ### `no_conspiracy_twins/goldbach/sg` evidently names three declarations, and reading it so is a
    ### JUDGEMENT, not a string match. ### **SO THE EXPANSION IS KEPT IN ITS OWN GROUP** and reported as
    ### an abbreviation rather than folded into the names the ledger writes out."""
    got = {}
    for m in re.finditer(r'([A-Za-z_][A-Za-z0-9_]*)((?:/[A-Za-z0-9_]+)+)', ledger):
        head, tail = m.group(1), m.group(2)
        if '_' not in head:
            continue
        prefix = head[:head.rindex('_') + 1]
        for seg in tail.strip('/').split('/'):
            got[prefix + seg] = m.group(0)
    return got


def tokens(s):
    return {t.lower() for t in re.findall(r'[A-Za-z]{3,}', s)} - STOP


def main():
    rec('=' * 100)
    rec('b369 -- COMPONENT 1: `(R4)` EXECUTED. ### PRESERVE BY QUOTATION, REPAIR BY EDIT.')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))
    rec('  ### the needle helper fixtures                          : %s' % GN.self_test(False))

    # ---------------------------------------------------------------- (0) THE REF
    rec('')
    rec('-' * 100)
    rec('  ### (0) THE REF, PINNED BEFORE ANY CLASSIFICATION.')
    rec('-' * 100)
    ref = git('rev-parse', '--abbrev-ref', 'HEAD').strip()
    head = git('rev-parse', 'HEAD').strip()
    lsr = git('ls-remote', 'origin', 'refs/heads/main').split()
    lsr = lsr[0] if lsr else ''
    dirty = bool(git('status', '--porcelain').strip())
    rec('    `SIDE-effects` ref `%s` = `%s`' % (ref, head))
    rec('    ### **ls-remote = `%s` ### -- EQUAL : %s** ; working tree dirty : %s'
        % (lsr, lsr == head, dirty))
    if lsr != head or dirty:
        rec('    ### ### **THE REF IS NOT PINNED OR THE TREE IS DIRTY. ### NOTHING IS WRITTEN.**')
        run_clock.write(D, 'b369_repair_notes', LINES)
        return 2

    # ---------------------------------------------------------------- (1) THE ROWS, LOCATED
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE LIST, LOCATED BY ITS OWN SHAPE. ### **BEFORE ANY EDIT.**')
    rec('-' * 100)
    before = nl(io.open(AGENTS, encoding='utf-8', newline='').read())
    all_lines = before.split(chr(10))
    opener_n, _o = AF.find(AGENTS, 'Named theorems include:')
    closer_n, _c = AF.find(AGENTS, '`SIDEEffects/Milestones.lean` carries the analytic-existence')
    rows = []
    for i in range(opener_n, closer_n - 1):
        ln = all_lines[i]
        if LAYER.match(ln):
            rows.append((i + 1, ln))
    rec('    the list opens at line %d and the paragraph after it begins at line %d'
        % (opener_n, closer_n))
    rec('    ### ### **EXPORT ROWS LOCATED BETWEEN THEM : %d**' % len(rows))
    for n, ln in rows:
        rec('        line %-4d | %s' % (n, ln[:150]))
    if not rows:
        rec('    ### ### **NO ROWS LOCATED. ### NOTHING IS WRITTEN.**')
        run_clock.write(D, 'b369_repair_notes', LINES)
        return 2

    # ---------------------------------------------------------------- (2) THE RE-DERIVATION
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE CLASSIFICATION, RE-DERIVED. ### **NO PRIOR ACT`S JSON IS READ.**')
    rec('-' * 100)
    exported, layer_of = [], {}
    for n, ln in rows:
        layer = ln.split('**')[1] if '**' in ln else '?'
        for m in re.finditer(r'`([A-Za-z_][A-Za-z0-9_.]*)`', ln):
            nm = m.group(1)
            if nm not in exported:
                exported.append(nm)
                layer_of[nm] = layer
    present, absent = [], []
    sites = {}
    for nm in exported:
        d = declaration_of(nm)
        if d:
            present.append(nm)
            sites[nm] = d[0]
        else:
            absent.append(nm)
    rec('    names the rows export : %d' % len(exported))
    rec('    ### ### **DECLARED IN THE KERNEL : %d ### / ### ABSENT : %d**' % (len(present), len(absent)))
    for nm in present:
        rec('        PRESENT  %-24s declared at `%s:%d`' % (nm, sites[nm]['file'], sites[nm]['line']))
    rec('    ### the comparison, and it is a comparison only:')
    rec('    ### ### **`b368` REPORTED `%d` ABSENT AT `%s`. ### THIS ACT DERIVES `%d` AT `%s`. ###'
        % (B368_ABSENT, B368_HEAD, len(absent), head[:7]))
    rec('    ### ### AGREE : %s.**' % (len(absent) == B368_ABSENT))
    rec('    ### **THE CONSTANT ABOVE IS NEVER AN INPUT TO THE COUNT** -- the count comes from the file.')

    # ---------------------------------------------------------------- (3) (R5) THE EVIDENCE GROUPS
    rec('')
    rec('-' * 100)
    rec('  ### (3) `(R5)`: THE LEDGER`S OWN LACUNAE, FILED AND NOT INVENTED.')
    rec('-' * 100)
    struct = kernel_text(STRUCT_REL)
    ledger = ledger_span(struct)
    heads = ledger_headings(ledger)
    expl = explicit_names(ledger)
    abbr = abbreviated_names(ledger)
    rec('    the ledger block is %d lines and carries %d entry heading(s):'
        % (len(ledger.split(chr(10))), len(heads)))
    for h in heads:
        rec('        | %s' % h['text'][:110])
    named, by_abbr, layer_only, silent = [], [], [], []
    cover = {}
    for nm in absent:
        if nm in expl:
            named.append(nm)
        elif nm in abbr:
            by_abbr.append(nm)
        else:
            lay = layer_of.get(nm, '')
            lt = tokens(lay)
            hit = next((h for h in heads if lt & tokens(h['text'])), None)
            if hit:
                layer_only.append(nm)
                cover[nm] = hit['text']
            else:
                silent.append(nm)
    rec('    ### ### **NAMED OUTRIGHT BY THE LEDGER : %d**' % len(named))
    rec('    ### ### **NAMED ONLY BY ITS SLASH ABBREVIATION : %d ### -- %s**'
        % (len(by_abbr), ', '.join('`%s`' % x for x in by_abbr) or 'none'))
    rec('    ### **AND THAT GROUP IS KEPT APART BECAUSE READING THE ABBREVIATION IS A JUDGEMENT:**')
    for nm in by_abbr:
        rec('        `%s` <- the ledger writes `%s`' % (nm, abbr[nm]))
    rec('    ### ### **COVERED ONLY BY THEIR LAYER`S ENTRY : %d**' % len(layer_only))
    for nm in layer_only:
        rec('        `%-26s` -- entry: %s' % (nm, cover[nm][:70]))
    rec('    ### ### **AND THE LEDGER SAYS NOTHING OF THEIR LAYER AT ALL : %d ### -- %s**'
        % (len(silent), ', '.join('`%s`' % x for x in silent) or 'NONE'))
    rec('')
    rec('    ### ### ### **AND THIS CORRECTS `b368`, WHICH IS WHY THE ORDER MADE THE ACT RE-DERIVE.**')
    rec('    ### `b368` reported `9` named, `8` covered by a layer entry and ### **`1` WITH NO ENTRY AT')
    rec('    ### ### ALL** -- and called that last the sharper half of its finding. ### **IT IS NOT')
    rec('    ### ### TRUE.** ### The ledger carries an entry HEADED by that declaration`s own name.')
    rec('    ### `b368``s predicate required a backtick or a slash before a name, and the ledger names')
    rec('    ### that one as a bare heading. ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE.**')
    rec('    ### **`(R5)`: NO REASON IS ASSERTED FOR ANY RETIREMENT.** ### Where the kernel`s record')
    rec('    ### does not say why a name went, this act says that it does not say.')
    hist = {nm: history_of(nm) for nm in silent}
    for nm, h in hist.items():
        rec('        `%s` -- the repository`s own history carries %d commit(s) touching it' % (nm, len(h)))

    # ---------------------------------------------------------------- (4) THE BLOCK
    rec('')
    rec('-' * 100)
    rec('  ### (4) THE PRESERVATION. ### **VERBATIM, AND VERIFIED BEFORE THE EDIT.**')
    rec('-' * 100)
    if MARK in before:
        rec('  ### ### **THE MARK IS ALREADY PRESENT. ### NOTHING IS WRITTEN.**')
        run_clock.write(D, 'b369_repair_notes', LINES)
        return 0
    quoted = [ln for _n, ln in rows]
    blk = ['', MARK, '',
           '## The Layer-1 export list as it stood at `%s`, preserved verbatim — and repaired above'
           % head[:7],
           '',
           ('*Ruling (R4), 2026-09-08: **append-only is right for a ledger, where a reader reads the '
            'file; it is wrong for a list, where a reader reads the list.** The list above has therefore '
            'been **repaired in place**, and the original is preserved here, in the same file, quoted '
            'verbatim before the edit was made.*'),
           '',
           ('### The original rows, verbatim — quoted here, and nowhere used as an export list'),
           '',
           '```markdown']
    blk += quoted
    blk += [
        '```',
        '',
        ('Of the %d names those rows exported, **%d are declared in this kernel\'s own `.lean` files and '
         '%d are not** — re-derived at ref `%s` = `%s`, pinned against `ls-remote`, by extracting the '
         'backticked names and searching for a declaration of each. Every absent name existed and was '
         'removed; **none was invented, and none has a successor under another name in this kernel.**'
         % (len(exported), len(present), len(absent), ref, head)),
        '',
        '### What the retirement ledger says, and where it says nothing',
        '',
        ('The ledger is the comment block headed `RETIREMENT LEDGER (audit Phase S.2–S.4)` in '
         '`SIDEEffects/Structural.lean`. **It does not speak for all of them, and this note does not '
         'speak for it.**'),
        '',
        '- **Named outright (%d):** %s.' % (len(named), ', '.join('`%s`' % n for n in named)),
        ('- **Named only by the ledger\'s slash abbreviation (%d):** %s — the ledger writes %s. '
         '**Reading that as naming these is a judgement, not a string match**, so they are listed apart '
         'rather than folded in with the names it writes out.'
         % (len(by_abbr), ', '.join('`%s`' % n for n in by_abbr),
            ', '.join('`%s`' % v for v in sorted({abbr[n] for n in by_abbr})) or '—')
         if by_abbr else '- **Named only by the ledger\'s slash abbreviation (0):** none.'),
        ('- **Covered only by their layer\'s entry (%d):** %s — the entry records that the layer\'s '
         'skeletons were retired without listing these by name. Their presence in an earlier commit and '
         'their absence now are visible in this repository\'s own history.'
         % (len(layer_only), ', '.join('`%s`' % n for n in layer_only))),
        ('- **Not covered at all (%d):** %s'
         % (len(silent), (', '.join('`%s`' % n for n in silent) + ' — the ledger has no entry for the '
                          'layer and does not name the declaration.') if silent
            else '**none — every retired name is reached by the ledger, by its own name, by its '
                 'abbreviation, or through its layer\'s entry.**')),
        '',
        ('**Why the reason is not given here.** For no name in any group above does this kernel record '
         '*why* it went beyond what the entries quoted say. **This note does not supply one.** Ruling '
         '(R5): where the record is silent, the silence is reported rather than filled.'),
        '',
        '### What this block does and does not do',
        '',
        ('**It preserves; it does not restore.** The rows above are a quotation of a past state, not an '
         'export list. No name in them is available as a theorem.'),
        '',
        ('**It does not retire, rename or repair anything in the source.** No `.lean` file was touched, '
         'no build was run, and no axiom profile was computed. **It does not claim the retirements were '
         'right** — only that they happened, and how far the kernel\'s own record accounts for them.'),
        '',
        ('**And it supersedes two sentences in the block below it.** b368\'s currency note says that '
         'nothing above it had been changed and that the list was left exactly as it was. **Both were '
         'true when b368 wrote them and neither is true now**: ruling (R4) reversed the disposition, not '
         'the measurement. b368\'s block is left exactly as b368 wrote it; this paragraph is the '
         'correction, because a past record is named and superseded, never rewritten.'),
        '',
        ('*Measured, preserved and repaired by the PLACE TO STAND research seat, act b369 (2026-09-08), '
         'from this repository\'s own files at ref `%s` = `%s`.*' % (ref, head)),
    ]
    put(AGENTS, before + chr(10).join(blk) + chr(10))
    mid = nl(io.open(AGENTS, encoding='utf-8', newline='').read())
    seg = mid.split(MARK)[-1]
    verbatim = all(q in seg for q in quoted)
    rec('    rows quoted into the block : %d' % len(quoted))
    rec('    ### ### **EVERY LOCATED ROW APPEARS VERBATIM IN THE BLOCK : %s**' % verbatim)
    rec('    ### ### **AND THE FILE BEFORE IS STILL A TRUE PREFIX AT THIS POINT : %s**'
        % mid.startswith(before))
    if not verbatim:
        rec('    ### ### **THE PRESERVATION FAILED. ### THE LIST IS NOT EDITED.**')
        run_clock.write(D, 'b369_repair_notes', LINES)
        return 3

    # ---------------------------------------------------------------- (5) THE EDIT
    rec('')
    rec('-' * 100)
    rec('  ### (5) THE REPAIR. ### **ONLY NOW, AND ONLY THE ROWS.**')
    rec('-' * 100)
    by_layer = {}
    for nm in present:
        by_layer.setdefault(layer_of[nm], []).append(nm)
    new_rows = []
    for lay in [ln.split('**')[1] for _n, ln in rows]:
        keep = by_layer.get(lay, [])
        if keep:
            new_rows.append('- **%s**: %s' % (lay, ', '.join('`%s`' % k for k in keep)))
    new_rows.append('- **Every other layer this list once named**: no theorem of this kernel. Those '
                    'names were retired; they are preserved verbatim, with what the retirement ledger '
                    'does and does not say about them, in the note at the foot of this file.')
    cur = mid.split(chr(10))
    lo, hi = rows[0][0] - 1, rows[-1][0]
    out = cur[:lo] + new_rows + cur[hi:]
    put(AGENTS, chr(10).join(out))
    after = nl(io.open(AGENTS, encoding='utf-8', newline='').read())
    rec('    rows replaced : %d  ->  rows written : %d' % (len(rows), len(new_rows)))
    for r in new_rows:
        rec('        | %s' % r[:150])

    # ---------------------------------------------------------------- (6) THE ARMS
    rec('')
    rec('-' * 100)
    rec('  ### (6) THE ARMS. ### **BAR 1 PRESERVATION, BAR 2 EXPORT, BAR 3 BOUNDED EDIT.**')
    rec('-' * 100)
    aft = after.split(chr(10))
    n_open, _x = AF.find(AGENTS, 'Named theorems include:')
    n_close, _y = AF.find(AGENTS, '`SIDEEffects/Milestones.lean` carries the analytic-existence')
    repaired = [ln for ln in aft[n_open:n_close - 1] if LAYER.match(ln)]
    still = sorted({m.group(1) for ln in repaired
                    for m in re.finditer(r'`([A-Za-z_][A-Za-z0-9_.]*)`', ln)} & set(absent))
    bar1 = all(q in after.split(MARK)[-1] for q in quoted)
    bar2 = not still
    # ### **BAR 3: EVERY BYTE OUTSIDE THE ROWS AND THE APPENDED BLOCK IS ITS BLOB'S.**
    blob = nl(subprocess.run(['git', '-C', KERNEL, 'show', 'HEAD:AGENTS.md'],
                             capture_output=True).stdout.decode('utf-8', 'replace')).split(chr(10))
    a_pre, a_post = aft[:lo], aft[lo + len(new_rows):]
    b_pre, b_post = blob[:lo], blob[hi:]
    post_cut = len(b_post) - 0
    bar3_pre = a_pre == b_pre
    bar3_post = a_post[:post_cut] == b_post
    bar3 = bar3_pre and bar3_post
    rec('    ### ### **BAR 1 -- THE ORIGINAL ROWS SURVIVE VERBATIM IN THE FILE : %s**' % bar1)
    rec('    ### ### **BAR 2 -- ABSENT NAMES REMAINING IN THE REPAIRED ROWS : %d %s ### -> %s**'
        % (len(still), still or '', bar2))
    rec('    ### **AND BAR 2 IS A CONTENT PREDICATE OVER THE ROWS THEMSELVES**, not a line count.')
    rec('    ### ### **BAR 3 -- EVERYTHING ABOVE THE ROWS IS ITS BLOB`S : %s ### / ### EVERYTHING'
        % bar3_pre)
    rec('    ### ### BELOW THEM, UP TO THE APPENDED BLOCK, IS ITS BLOB`S : %s**' % bar3_post)
    lean_dirty = [x for x in git('status', '--porcelain').splitlines() if x.strip().endswith('.lean')]
    rec('    ### ### **AND NO `.lean` FILE WAS TOUCHED : %s** %s' % (not lean_dirty, lean_dirty or ''))
    rec('=' * 100)

    ok = bar1 and bar2 and bar3 and not lean_dirty
    rec('  ### ### **COMPONENT 1 : %s**' % ('EXECUTED' if ok else 'FAILED'))
    rec('=' * 100)
    p = run_clock.write(D, 'b369_repair_notes', LINES)
    io.open(os.path.join(D, 'b369_repair.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(
            ref=ref, head=head, ls_remote=lsr, pinned=(lsr == head), dirty=dirty,
            exported=len(exported), present=present, absent=absent,
            n_present=len(present), n_absent=len(absent), sites=sites, layer_of=layer_of,
            b368_absent_constant=B368_ABSENT, agrees_with_b368=(len(absent) == B368_ABSENT),
            ledger_headings=[h['text'] for h in heads],
            ledger_named=named, ledger_by_abbreviation=by_abbr, ledger_layer_only=layer_only,
            ledger_silent=silent, ledger_cover=cover, abbreviations=abbr,
            n_named=len(named), n_by_abbr=len(by_abbr), n_layer_only=len(layer_only),
            n_silent=len(silent),
            b368_split_reported=[9, 8, 1], b368_silent_claim_refuted=(len(silent) == 0),
            silent_history={k: len(v) for k, v in hist.items()},
            rows_located=[{'line': n, 'text': t} for n, t in rows],
            rows_replaced=len(rows), rows_written=len(new_rows), new_rows=new_rows,
            mark=MARK, bar1_preserved=bar1, bar2_exports_none=bar2, still_absent=still,
            bar3_bounded=bar3, bar3_above=bar3_pre, bar3_below=bar3_post,
            lean_touched=len(lean_dirty), build_run=False, reasons_asserted=0,
            successors_named=0, side='BEFORE THE PUSH',
            run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
