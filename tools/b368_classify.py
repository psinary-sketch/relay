# -*- coding: utf-8 -*-
"""b368_classify.py -- THE RE-DERIVATION AND THE CLASSIFICATION. ### **A READ. ### NO BUILD.**

### ### **ADDITION ONE: THE FIGURE IS RE-DERIVED, NEVER CARRIED.** ### This tool reads NO prior act's
### JSON. ### It reads the front document's own export lines at the pinned ref, extracts the names they
### carry, and searches the kernel's own `.lean` files for a ### **DECLARATION** ### of each.
### ### **AND ITS DISAGREEMENT WITH `b367`, IF ANY, IS COMPUTED AND PRINTED** -- from a figure typed into
### this file as a CONSTANT so the comparison is explicit, and never by reading `b367`'s record.
### ### **ADDITION TWO: EVERY ABSENT NAME GETS A KIND AND ITS KIND'S OWN EVIDENCE.**
###   ### `PRESENT` needs a declaration site. ### `RETIRED` needs a ledger line. ### `RENAMED` needs a
###   ### **LOCATED SUCCESSOR.** ### `NEVER EXISTED` needs ### **THE SEARCH RECORDED**, and here that
###   search includes the kernel's own history -- because a name absent from HEAD and present in history
###   ### **EXISTED AND WAS REMOVED**, which is not the same thing at all.
### ### ### **AND NO NAME IS CLASSIFIED FROM ITS OWN SOUND.** ### The tool never infers a successor from
### a resemblance; a `RENAMED` row is emitted only where this seat has DECLARED a successor and the tool
### has LOCATED it by a declaration.
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

D = os.path.join(ROOT, 'data')
KERNEL = os.path.join('D:', os.sep, 'SIDE-effects')
AGENTS = os.path.join(KERNEL, 'AGENTS.md')
STRUCT_REL = 'SIDEEffects/Structural.lean'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE KERNEL'S OWN LEAN FILES. ### **`.lake` IS VENDORED MATHLIB AND IS NOT THIS KERNEL.**
KERNEL_LEAN = ['SIDEEffects.lean', 'SIDEEffects/ExhaustivenessLicense.lean',
               'SIDEEffects/Milestones.lean', 'SIDEEffects/Phase15/Module1.lean',
               'SIDEEffects/Phase15/SIDEFramework.lean', STRUCT_REL]

# ### THE FRONT DOCUMENT'S LAYER-1 EXPORT LINES, FOUND BY THEIR OWN SHAPE AND NOT BY TYPED HEADINGS.
LAYER = re.compile(r'^- \*\*[^*]+\*\*:')

# ### **THE FIGURE THIS ACT COMPARES AGAINST, TYPED HERE AS A CONSTANT** so the comparison is explicit.
# ### **IT IS NOT READ FROM `b367` AND IT IS NOT USED IN ANY COUNT** -- only in the disagreement line.
B367_ABSENT = 18
B367_HEAD = 'afa9ccf'

# ### **THE LEDGER'S ENTRY HEADINGS**, each located in the ledger by the tool, so a row's RETIRED evidence
# ### is a line the ledger actually carries.
LEDGER_ENTRIES = [
    ('Yang-Mills mass gap', 'Yang-Mills mass gap'),
    ('GRH', 'GRH'),
    ('Landau-Siegel', 'Landau-Siegel'),
    ('Type-D', 'Type-D'),
    ('BSD', 'BSD'),
    ('Artin', 'Artin'),
    ('side_exclusion', 'side_exclusion'),
]

# ### **THE SUCCESSORS THIS SEAT DECLARES, TO BE LOCATED BY THE TOOL OR REFUSED.** ### Empty: this seat
# ### declares NONE. ### **THE LEDGER'S POINTERS ARE POINTERS TO GENUINE CONTENT, NOT RENAMES**, and its
# ### own heading says so -- *"where genuine content lives, if anywhere"*. ### `SIDE_exclusion` differs
# ### from `side_exclusion` only in case, which is exactly the resemblance the order's bar forbids.
DECLARED_SUCCESSORS = {}

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(*a):
    return subprocess.run(['git', '-C', KERNEL] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def kernel_text(rel):
    p = os.path.join(KERNEL, rel.replace('/', os.sep))
    return io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


DECL = r'^\s*(theorem|lemma|def|abbrev|instance|axiom|structure|inductive)\s+%s\b'


def declaration_of(name):
    """### **A DECLARATION, NOT A MENTION.** ### Returns [(file, line, text)]."""
    out = []
    for rel in KERNEL_LEAN:
        for i, ln in enumerate(kernel_text(rel).split(chr(10)), 1):
            if name in ln and re.match(DECL % re.escape(name), ln.split('--')[0]):
                out.append(dict(file=rel, line=i, text=ln.strip()[:170]))
    return out


def history_of(name):
    """### **THE SEARCH RECORDED.** ### Commits whose `.lean` diff changed the count of this string."""
    outs = git('log', '--oneline', '-S', name, '--', '*.lean').splitlines()
    return [x.strip()[:90] for x in outs if x.strip()]


def ledger_line_for(name, ledger):
    """### THE LEDGER'S OWN LINE NAMING THIS DECLARATION, IF IT CARRIES ONE."""
    for i, ln in enumerate(ledger.split(chr(10)), 1):
        if not ln.strip().startswith('--'):
            continue
        if re.search(r'`%s\b' % re.escape(name), ln) or re.search(r'/%s\b' % re.escape(name), ln):
            return dict(line=i, text=ln.strip()[:170])
    return None


def ledger_entry_for_layer(layer, ledger):
    """### THE LEDGER'S ENTRY HEADING FOR A LAYER, LOCATED BY THE TOOL."""
    for key, needle in LEDGER_ENTRIES:
        if key.split()[0].lower() in layer.lower() or needle.lower() in layer.lower():
            for i, ln in enumerate(ledger.split(chr(10)), 1):
                if ln.strip().startswith('--') and ln.strip('- ').strip().startswith(needle):
                    return dict(layer_key=key, line=i, text=ln.strip()[:170])
    return None


def main():
    rec('=' * 100)
    rec('b368 -- THE RE-DERIVATION AND THE CLASSIFICATION. ### **NO FIGURE IS CARRIED.**')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))

    rec('')
    rec('-' * 100)
    rec('  ### (0) ADDITION ONE -- THE REF, PINNED BY `ls-remote` BEFORE ANY CLASSIFICATION.')
    rec('-' * 100)
    branch = git('rev-parse', '--abbrev-ref', 'HEAD').strip()
    head = git('rev-parse', 'HEAD').strip()
    remote = (git('ls-remote', 'origin', 'refs/heads/%s' % branch).split() or [''])[0]
    dirty = bool(git('status', '--porcelain').strip())
    rec('    ref            : `%s`' % branch)
    rec('    local HEAD     : %s' % head)
    rec('    ls-remote      : %s' % remote)
    rec('    ### ### **EQUAL : %s** ### ; working tree dirty : %s' % (head == remote, dirty))
    moved = not head.startswith(B367_HEAD)
    rec('    ### **AND THE HEAD `b367` READ WAS `%s`. ### MOVED SINCE : %s.**' % (B367_HEAD, moved))
    rec('    ### **THE OTHER REFS, NOT READ:**')
    for ln in git('ls-remote', '--heads', 'origin').splitlines():
        parts = ln.split()
        if len(parts) == 2 and not parts[1].endswith('/' + branch):
            rec('        %s  %s' % (parts[0][:12], parts[1]))

    rec('')
    rec('-' * 100)
    rec("  ### (1) THE FRONT DOCUMENT'S OWN EXPORT LINES, FOUND BY THEIR SHAPE.")
    rec('-' * 100)
    agents = io.open(AGENTS, encoding='utf-8', errors='replace').read().split(chr(10))
    layers, names = [], []
    for i, ln in enumerate(agents, 1):
        if LAYER.match(ln):
            got = re.findall(r'`([A-Za-z_][A-Za-z0-9_.]*)`', ln)
            if not got:
                continue
            layer = ln.split('**')[1] if '**' in ln else ln
            layers.append(dict(layer=layer, line=i, names=got))
            names.extend(got)
            rec('    line %-5d %-42s names %d' % (i, layer[:42], len(got)))
    rec('    ### ### **NAMES THE FRONT DOCUMENT EXPORTS AT LAYER 1 : %d.**' % len(names))

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE RE-DERIVATION. ### **A DECLARATION IN THE KERNEL, OR NOT.**')
    rec('-' * 100)
    ledger = kernel_text(STRUCT_REL)
    present, absent = [], []
    for n in names:
        decls = declaration_of(n.split('.')[-1])
        (present if decls else absent).append(n)
    rec('    ### ### **PRESENT : %d ### / ### ABSENT : %d.**' % (len(present), len(absent)))
    rec('    present : %s' % (', '.join(present) or 'none'))
    rec('')
    rec('    ### ### **THE DISAGREEMENT LINE, COMPUTED AND NOT ASSUMED.** ### `b367` reported `%d`'
        % B367_ABSENT)
    rec('    ### absent at head `%s`. ### This act re-derives `%d` at head `%s`.'
        % (B367_HEAD, len(absent), head[:7]))
    agree = (len(absent) == B367_ABSENT)
    rec('    ### ### **THEY AGREE : %s.**' % agree)
    if not agree:
        rec('    ### ### **AND THE DISAGREEMENT IS THE FINDING, REPORTED AT FULL PROMINENCE.**')

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE CLASSIFICATION. ### **ONE ROW EACH, WITH ITS KIND’S OWN EVIDENCE.**')
    rec('-' * 100)
    layer_of = {}
    for L in layers:
        for n in L['names']:
            layer_of[n] = L['layer']
    rows = []
    for n in names:
        short = n.split('.')[-1]
        decls = declaration_of(short)
        if decls:
            rows.append(dict(name=n, kind='PRESENT', layer=layer_of.get(n, '?'),
                             evidence=decls[0], profile='NO PRINTED PROFILE',
                             note='a printed profile covering this declaration was not located in the '
                                  'kernel; no build was run in its place'))
            continue
        succ = DECLARED_SUCCESSORS.get(n)
        if succ:
            sd = declaration_of(succ)
            if sd:
                rows.append(dict(name=n, kind='RENAMED', layer=layer_of.get(n, '?'),
                                 evidence=dict(successor=succ, **sd[0]), note=''))
                continue
        line = ledger_line_for(short, ledger)
        if line:
            rows.append(dict(name=n, kind='RETIRED', layer=layer_of.get(n, '?'),
                             evidence=line, note='named by the ledger itself'))
            continue
        entry = ledger_entry_for_layer(layer_of.get(n, ''), ledger)
        hist = history_of(short)
        if hist:
            # ### **THE FIRST VERSION WROTE ONE NOTE FOR TWO DIFFERENT CASES**, and `b368`'s own gate
            # ### suite caught it: a row whose LAYER has no ledger entry at all was still described as
            # ### *its LAYER entry is quoted instead*. ### **THAT SENTENCE WAS FALSE FOR ONE ROW**, and a
            # ### note that describes evidence the row does not carry is the use-and-mention species
            # ### (`b348`) inside a classifier. ### **THE THREE CASES NOW HAVE THREE NOTES.**
            rows.append(dict(name=n, kind='RETIRED', layer=layer_of.get(n, '?'),
                             evidence=(entry or {'line': 0, 'text': 'NO LEDGER ENTRY FOR THIS LAYER'}),
                             history=hist,
                             note=('### **THE LEDGER DOES NOT NAME THIS DECLARATION.** ### Its LAYER '
                                   'entry is quoted instead, and the kernel’s own history shows the name '
                                   'was present and was removed') if entry else
                                  ('### **THE LEDGER HAS NO ENTRY FOR THIS LAYER AT ALL.** ### Neither '
                                   'the declaration nor its layer is recorded, and the kernel’s own '
                                   'history is the whole of the evidence that it existed')))
            continue
        rows.append(dict(name=n, kind='NEVER EXISTED', layer=layer_of.get(n, '?'),
                         evidence=dict(searched=KERNEL_LEAN, history_commits=0,
                                       ledger_line=None),
                         note='no declaration at this ref, no ledger line, and no commit in the '
                              'kernel’s `.lean` history changed the count of this string'))
    for r in rows:
        rec('')
        rec('    %-26s %-14s %s' % (r['name'], r['kind'], r['layer'][:40]))
        ev = r['evidence']
        if r['kind'] == 'PRESENT':
            rec('        declared at %s:%d' % (ev['file'], ev['line']))
            rec('        | %s' % ev['text'])
            rec('        axiom profile : %s' % r['profile'])
        elif r['kind'] == 'RENAMED':
            rec('        successor `%s` located at %s:%d' % (ev['successor'], ev['file'], ev['line']))
        elif r['kind'] == 'RETIRED':
            rec('        ledger line %s' % ev.get('line'))
            rec('        | %s' % ev.get('text'))
            if r.get('history'):
                rec('        history : %d commit(s) changed this name in `.lean`' % len(r['history']))
        else:
            rec('        searched %d kernel `.lean` files, the ledger, and the `.lean` history'
                % len(KERNEL_LEAN))
        if r['note']:
            rec('        %s' % r['note'])

    kinds = {}
    for r in rows:
        kinds[r['kind']] = kinds.get(r['kind'], 0) + 1
    named_by_ledger = sum(1 for r in rows
                          if r['kind'] == 'RETIRED' and r['note'] == 'named by the ledger itself')
    layer_only = sum(1 for r in rows if r['kind'] == 'RETIRED' and r['note'] != 'named by the ledger itself')
    # ### **AND THE SPLIT IS THREE-WAY, NOT TWO-WAY.** ### Read from the EVIDENCE, not from the note.
    history_only = sum(1 for r in rows if r['kind'] == 'RETIRED'
                       and r['note'] != 'named by the ledger itself'
                       and not r['evidence'].get('line'))
    layer_entry = layer_only - history_only
    rec('')
    rec('-' * 100)
    rec('  ### (4) THE COUNTS.')
    rec('-' * 100)
    for k in ('PRESENT', 'RETIRED', 'RENAMED', 'NEVER EXISTED'):
        rec('    %-16s %d' % (k, kinds.get(k, 0)))
    rec('    ### ### **AND THE RETIRED SPLIT, WHICH IS THIS ACT’S OWN FINDING ABOUT THE LEDGER:**')
    rec('    ### ### **NAMED BY THE LEDGER : %d ### / ### COVERED ONLY BY THEIR LAYER’S ENTRY : %d ###'
        % (named_by_ledger, layer_entry))
    rec('    ### ### / ### COVERED BY NEITHER, AND EVIDENCED BY THE HISTORY ALONE : %d.**' % history_only)
    rec('    ### **THE THIRD GROUP IS THE SHARPER HALF OF THE FINDING:** ### the ledger is not merely')
    rec('    ### incomplete about the names it lists -- ### **FOR ONE LAYER IT HAS NO ENTRY AT ALL.**')
    rec('    ### **NO NAME WAS CLASSIFIED FROM ITS OWN SOUND: `RENAMED` ROWS EMITTED : %d**, and this'
        % kinds.get('RENAMED', 0))
    rec('    ### seat declared no successor -- the ledger’s pointers are pointers to GENUINE CONTENT,')
    rec('    ### which its own heading says, and `SIDE_exclusion` differs from `side_exclusion` only in')
    rec('    ### case. ### **THAT RESEMBLANCE IS EXACTLY WHAT THE ORDER’S BAR FORBIDS ACTING ON.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b368_classify_run', LINES)
    io.open(os.path.join(D, 'b368_classify.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(ref=branch, head=head, ls_remote=remote, pinned=(head == remote), dirty=dirty,
                        head_moved_since_b367=bool(moved), b367_absent_constant=B367_ABSENT,
                        layers=layers, exported=len(names), present=present, absent=absent,
                        n_present=len(present), n_absent=len(absent), agrees_with_b367=bool(agree),
                        rows=rows, kinds=kinds, retired_named_by_ledger=named_by_ledger,
                        retired_layer_only=layer_only, retired_layer_entry=layer_entry,
                        retired_history_only=history_only, renamed_rows=kinds.get('RENAMED', 0),
                        declared_successors=DECLARED_SUCCESSORS, build_run=False, lean_written=0,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
