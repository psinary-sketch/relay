# -*- coding: utf-8 -*-
"""b373_pins.py -- COMPONENT 1: `(R9)`, PRICED AND THEN EXECUTED.

### ### **THE PIN IS SOURCED ONLY FROM THE ACT THAT WROTE THE ROW, LOCATED IN ITS OWN BANK.**
### ### **NEVER FROM A CURRENT HEAD** -- that would date the claim to today rather than to when it was
### made, and `(R9)` forbids it in its own words.
### ### **THE CHAIN, DECLARED BEFORE IT IS RUN:** ### row re-anchored BY ITS OWN CONTENT -> the commit
### that INTRODUCED that content -> the ACT that commit's subject names -> ### **THAT ACT'S OWN BANKED
### ### PINS RECORD**, read for the kernel the row names.
### ### **AND EVERY LINK CAN FAIL, AND EACH FAILURE KEEPS ITS OWN NAME** -- a row nobody can date and a
### row whose kernel was never on the roster are not the same problem and will not have the same cure.
### ### ### **AND THE SCOPE OF THE EDIT IS NOT THE SCOPE OF THE CLASSIFICATION.** ### Every row is
### classified; ### **A DEPOSITED COMPANION, AN ARCHIVED SNAPSHOT AND AN APPEND-ONLY LEDGER ENTRY ARE
### ### NOT EDITED**, and each excluded row is listed with its reason and counted.
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
import run_clock                 # noqa: E402
import anchor_from_file as AF    # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### ### **THE KERNEL NAMES ARE DISCOVERED, NOT TYPED.** ### The first version of this file carried a
# ### hand-written list, and it reported rows naming `SIDE-carrier-spec` and `SIDE-li-map` as ### **NAMING
# ### ### NO KERNEL** -- because the list did not know them. ### That is `PREDICATE_ONE_SHAPE` committed
# ### by this act's own tool, in an act whose whole subject is a predicate that knew one shape. ### The
# ### list is now every `D:\SIDE-*` directory that is a git repository.
def _discover_kernels():
    root = 'D:' + os.sep
    names = []
    try:
        for n in sorted(os.listdir(root)):
            if not n.startswith('SIDE-'):
                continue
            if os.path.isdir(os.path.join(root, n, '.git')):
                names.append(n)
    except OSError:
        pass
    return names


KERNEL_NAMES = _discover_kernels()

# ### **THE SURFACES `(R9)` DOES NOT REACH.** ### Decided on the registration's face, before any edit.
FROZEN_PREFIX = ('outputs/DEPOSITED-', 'archive/')
LEDGERS = ('FINDINGS.md', 'ERRATA.md', 'OPEN_TRAILS.md', 'FACES_LEDGER.md')

ACT_RE = re.compile(r'\bb(\d{3})\b')
HEAD_BLOCK = re.compile(r'^--- (\S+)\s', re.M)

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(*a):
    return subprocess.run(['git', '-C', PP] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def parse_pins(path):
    """### **READ A BANKED PINS RECORD.** ### `--- <name>   (<path>)` then `local HEAD   : <sha>`."""
    out = {}
    name = None
    for ln in io.open(path, encoding='utf-8', errors='replace').read().split(chr(10)):
        m = HEAD_BLOCK.match(ln)
        if m:
            name = m.group(1)
            continue
        if name and ln.strip().startswith('local HEAD'):
            sha = ln.split(':', 1)[1].strip()
            if re.fullmatch(r'[0-9a-f]{40}', sha):
                out[name] = sha
            name = None
    return out


def act_pins_files(act):
    """### the act's own banked pins records, step-zero preferred over closing.
    ### ### **STEP ZERO IS THE STATE THE ACT STARTED FROM**, which is the state its prose was written
    ### against; the closing record is after the act's own pushes. ### Both are read and any
    ### disagreement for the kernel in question is REPORTED rather than silently resolved."""
    pats = [p for p in os.listdir(D)
            if p.startswith(act + '_pins') and p.endswith('.txt')]
    zero = [p for p in pats if 'step' in p]
    close = [p for p in pats if 'clos' in p or 'final' in p]
    other = [p for p in pats if p not in zero and p not in close]
    return sorted(zero), sorted(close), sorted(other)


# ### **AN EXTENSION THIS ACT DECLARES AND MARKS AS ITS OWN.** ### A row can name a kernel by a PATH
# ### INSIDE IT rather than by the repository's name -- `Core/FiniteSideSeal.lean` is
# ### `SIDE-global-section` and says so to a reader and not to a substring search. ### The first run of
# ### this tool reported those rows as ### **NAMING NO KERNEL**, which is `PREDICATE_ONE_SHAPE` again:
# ### a predicate that knows one shape finds one shape. ### The mapping is confirmed by asking the
# ### repository whether it actually tracks such a path, so it is evidence and not an assumption.
PATH_KERNEL = [('SIDEEffects/', 'SIDE-effects'),
               ('Core/', 'SIDE-global-section'),
               ('Interfaces/', 'SIDE-global-section'),
               ('AXIOM_PRINTS', 'SIDE-global-section'),
               ('Kernel/', 'SIDE-kernel'),
               ('Bridge/', 'SIDE-kernel'),
               ('MetaKernel', 'SIDE-kernel')]

_TRACKED = {}


def tracks(kernel, fragment):
    """### **ASK THE REPOSITORY, DO NOT ASSUME.** ### Does it track a path carrying this fragment?"""
    p = os.path.join('D:', os.sep, kernel)
    if kernel not in _TRACKED:
        r = subprocess.run(['git', '-C', p, 'ls-files'], capture_output=True, text=True,
                           encoding='utf-8', errors='replace')
        _TRACKED[kernel] = r.stdout if r.returncode == 0 else ''
    return fragment in _TRACKED[kernel]


def which_kernel(text):
    hits = [k for k in KERNEL_NAMES if k in text]
    # ### the longest name wins: `SIDE-bsd-formation-transfer` contains `SIDE-bsd`, and a shorter
    # ### name must not shadow it.
    hits.sort(key=len, reverse=True)
    if hits:
        return hits[0], 'by the repository name in the row'
    for frag, kern in PATH_KERNEL:
        if frag in text and tracks(kern, frag):
            return kern, ('by the path `%s`, which %s tracks' % (frag, kern))
    # ### **AND A BARE `X.lean` IS OFFERED TO EVERY KERNEL, AND PLACED ONLY IF EXACTLY ONE TRACKS IT.**
    # ### `b371`'s inventory counted a bare filename as naming a kernel; ### **A FILENAME IS NOT A
    # ### ### REPOSITORY**, and the difference is the whole of this link. ### Two kernels tracking the
    # ### same basename is ambiguous and is refused, the way an ambiguous anchor is refused.
    for base in sorted(set(re.findall(r'([A-Za-z0-9_]+\.lean)', text))):
        owners = [k for k in KERNEL_NAMES if tracks(k, '/' + base) or tracks(k, base)]
        if len(owners) == 1:
            return owners[0], ('by the file `%s`, which only %s tracks' % (base, owners[0]))
        if len(owners) > 1:
            return None, ('the file `%s` is tracked by %d kernels and the row names no repository'
                          % (base, len(owners)))
    return None, 'the row names neither a repository nor a path this record can place'


_BANKREF = {}
HEX = re.compile(r'(?<![0-9a-zA-Z])([0-9a-f]{7,40})(?![0-9a-zA-Z])')


def bank_refs(act, kernel):
    """### **THE SECOND WAY A REF CAN BE `LOCATED IN ITS OWN BANK`, AND `(R9)` ALLOWS IT IN WORDS.**
    ### Not every act banked a pins record -- the pins instrument begins at `b300` -- but an act's
    ### bank may still NAME a kernel commit in prose. ### Every hex-shaped token in the act's own
    ### files is offered to the kernel the row names, and only what ### **RESOLVES THERE** counts.
    ### ### **AND MORE THAN ONE RESOLVING TOKEN IS AMBIGUOUS AND IS REFUSED**, the way an ambiguous
    ### anchor is refused: a bank naming two refs for one kernel does not tell you which the row meant."""
    if (act, kernel) in _BANKREF:
        return _BANKREF[(act, kernel)]
    p = os.path.join('D:', os.sep, kernel)
    found = {}
    for f in sorted(os.listdir(D)):
        if not f.startswith(act + '_'):
            continue
        try:
            txt = io.open(os.path.join(D, f), encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        for m in HEX.finditer(txt):
            tok = m.group(1)
            if tok in found:
                continue
            r = subprocess.run(['git', '-C', p, 'rev-parse', '--verify', '--quiet',
                                tok + '^{commit}'], capture_output=True, text=True)
            if r.returncode == 0:
                found[tok] = dict(full=r.stdout.strip(), file=f)
    full = sorted(set(v['full'] for v in found.values()))
    _BANKREF[(act, kernel)] = (found, full)
    return found, full


def excluded_reason(rel):
    p = rel.replace(os.sep, '/')
    for pre in FROZEN_PREFIX:
        if p.startswith(pre):
            return ('DEPOSITED -- FROZEN' if pre.startswith('outputs') else 'ARCHIVED SNAPSHOT')
    if os.path.basename(p) in LEDGERS:
        return 'APPEND-ONLY LEDGER ENTRY'
    return None


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    write = ('--write' in argv)
    rec('=' * 100)
    rec('b373 -- COMPONENT 1: `(R9)`, THE PINS. ### **SOURCED FROM THE WRITING ACT, NEVER FROM A HEAD.**')
    rec('=' * 100)
    rec('  ### mode : %s' % ('WRITE' if write else 'READ ONLY -- NOTHING IS WRITTEN'))
    rec('')

    # ### **THE HEADS ARE READ ONCE, AND ONLY SO THAT NO PIN MAY EQUAL ONE.**
    heads = {}
    for name in KERNEL_NAMES + ['relay', 'PLACE-papers']:
        p = os.path.join('D:', os.sep, name)
        if name == 'PLACE-papers':
            p = PP
        elif name == 'relay':
            p = ROOT
        r = subprocess.run(['git', '-C', p, 'rev-parse', 'HEAD'], capture_output=True, text=True)
        if r.returncode == 0:
            heads[name] = r.stdout.strip()
    rec('  ### ### **TODAY`S HEADS, READ ONCE AND USED ONLY AS A PROHIBITION:** ### %d repositories.'
        % len(heads))
    rec('  ### ### **NO PIN THIS ACT WRITES MAY EQUAL ANY OF THEM** (`(R9)`), and the arm is below.')
    rec('')

    inv = json.load(io.open(os.path.join(D, 'b371_inventory.json'), encoding='utf-8'))
    rows = [r for r in inv['inventory'] if not r['has_pin']]
    rec('-' * 100)
    rec('  ### (1) THE SET. ### **THE PINLESS ROWS `b371` INVENTORIED, NOT RE-DERIVED HERE.**')
    rec('-' * 100)
    rec('    pinless rows : %d across %d files'
        % (len(rows), len(set(r['file'] for r in rows))))

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE CHAIN, RUN ROW BY ROW.')
    rec('-' * 100)
    t0 = time.time()
    out = []
    for r in rows:
        rel = r['file']
        path = os.path.join(PP, rel.replace('/', os.sep))
        rowrec = dict(file=rel, inventory_line=r['line'], text=r['text'],
                      kernels=r['kernels'], terminals=r['terminals'])
        # --- link 1: re-anchor BY CONTENT ------------------------------------------------------
        hint = r['text']
        try:
            n, line = AF.find(path, hint)
            rowrec['line'] = n
            rowrec['anchor'] = 'BY CONTENT'
            rowrec['line_text'] = line.rstrip()
        except AF.AnchorError as e:
            rowrec['anchor'] = 'REFUSED'
            rowrec['anchor_error'] = str(e).replace(chr(10), ' | ')[:140]
            rowrec['status'] = 'CITES-AT-AN-UNKNOWN-REF'
            rowrec['reason'] = 'ROW NOT RE-ANCHORABLE BY CONTENT'
            out.append(rowrec)
            continue
        # --- link 2: the commit that INTRODUCED it ----------------------------------------------
        # ### ### **THE SEARCH IS SCOPED TO THE ROW'S OWN FILE, AND THE WIDER SEARCH IS RUN TOO AND
        # ### ### REPORTED RATHER THAN SUBSTITUTED.** ### Dropping the pathspec looked like the safer
        # ### predicate -- a renamed file hides its row's introduction under the old path -- and it
        # ### made the located-act count FALL from 33 to 7. ### The reason is the record's own shape:
        # ### ### **THE SAME ROW TEXT LIVES IN THE LIVING PAPER, IN ITS DEPOSITED COPY AND IN ITS
        # ### ### ARCHIVED SNAPSHOT**, so a whole-repository search returns the oldest appearance
        # ### ANYWHERE, which is a different question from ### *which act wrote this row here.*
        g = git('log', '--format=%H%x1f%s', '-S', hint, '--', rel)
        commits = [x for x in g.stdout.split(chr(10)) if x.strip()]
        if not commits:
            rowrec['status'] = 'CITES-AT-AN-UNKNOWN-REF'
            rowrec['reason'] = 'INTRODUCING COMMIT NOT LOCATED'
            out.append(rowrec)
            continue
        sha, subject = commits[-1].split(chr(31), 1)
        rowrec['introducing_commit'] = sha
        rowrec['introducing_subject'] = subject[:150]
        rowrec['commits_touching'] = len(commits)
        gw = git('log', '--format=%H%x1f%s', '-S', hint)
        wide = [x for x in gw.stdout.split(chr(10)) if x.strip()]
        if wide and wide[-1].split(chr(31))[0] != sha:
            rowrec['earlier_elsewhere'] = wide[-1].split(chr(31), 1)[1][:120]
            rowrec['earlier_elsewhere_commit'] = wide[-1].split(chr(31))[0]
        # --- link 3: the ACT the subject names ---------------------------------------------------
        m = ACT_RE.search(subject)
        if not m:
            rowrec['status'] = 'CITES-AT-AN-UNKNOWN-REF'
            rowrec['reason'] = 'WRITING ACT NOT NAMED'
            out.append(rowrec)
            continue
        act = 'b' + m.group(1)
        rowrec['act'] = act
        # --- link 4: THAT ACT'S OWN BANKED PINS RECORD -------------------------------------------
        kern, how = which_kernel(rowrec['line_text'])
        if not kern:
            kern, how = which_kernel(hint)
        rowrec['kernel'] = kern
        rowrec['kernel_identified'] = how
        if not kern:
            rowrec['status'] = 'CITES-AT-AN-UNKNOWN-REF'
            rowrec['reason'] = 'ROW NAMES NO PLACEABLE KERNEL'
            out.append(rowrec)
            continue
        zero, close, other = act_pins_files(act)
        cands = zero + close + other
        rowrec['pins_files'] = cands
        readings = {}
        for f in cands:
            pins = parse_pins(os.path.join(D, f))
            if kern in pins:
                readings[f] = pins[kern]
        if readings:
            chosen_file = ([f for f in zero if f in readings]
                           + [f for f in close if f in readings]
                           + [f for f in other if f in readings])[0]
            pin = readings[chosen_file]
            rowrec['pin'] = pin
            rowrec['pin_from'] = chosen_file
            rowrec['pin_source'] = "THE ACT'S OWN PINS RECORD"
            rowrec['pin_readings'] = readings
            rowrec['pin_disagrees_within_act'] = (len(set(readings.values())) > 1)
            rowrec['status'] = 'PINNABLE'
        else:
            # ### the pins record is one way a ref is `located in its own bank`. ### It is not the
            # ### only way the ruling's words allow, and the acts that wrote most of these rows
            # ### predate the pins instrument entirely.
            found, full = bank_refs(act, kern)
            rowrec['bank_refs'] = {k: v['file'] for k, v in found.items()}
            if len(full) == 1:
                rowrec['pin'] = full[0]
                rowrec['pin_from'] = sorted(set(v['file'] for v in found.values()))[0]
                rowrec['pin_source'] = "A REF NAMED IN THE ACT'S OWN BANK"
                rowrec['status'] = 'PINNABLE'
                rowrec['equals_a_head'] = (rowrec['pin'] in set(heads.values()))
                rowrec['excluded'] = excluded_reason(rel)
                out.append(rowrec)
                continue
            elif len(full) > 1:
                rowrec['status'] = 'CITES-AT-AN-UNKNOWN-REF'
                rowrec['reason'] = "THE ACT'S BANK NAMES MORE THAN ONE REF FOR THAT KERNEL"
            elif not cands:
                rowrec['status'] = 'CITES-AT-AN-UNKNOWN-REF'
                rowrec['reason'] = "NO PINS RECORD AND NO REF IN THE ACT'S BANK"
            else:
                rowrec['status'] = 'CITES-AT-AN-UNKNOWN-REF'
                rowrec['reason'] = "KERNEL NOT ON THAT ACT'S ROSTER"
            out.append(rowrec)
            continue
        # ### **AND THE PROHIBITION IS CHECKED HERE, NOT ONLY IN THE GATE.**
        rowrec['equals_a_head'] = (pin in set(heads.values()))
        ex = excluded_reason(rel)
        rowrec['excluded'] = ex
        out.append(rowrec)
    elapsed = time.time() - t0
    rec('    rows walked : %d   ### elapsed : %.1fs   ### per row : %.2fs'
        % (len(rows), elapsed, elapsed / max(1, len(rows))))

    # ---------------------------------------------------------------- the classification
    def by(k):
        d2 = {}
        for x in out:
            d2[x.get(k)] = d2.get(x.get(k), 0) + 1
        return d2

    pinnable = [x for x in out if x['status'] == 'PINNABLE']
    unknown = [x for x in out if x['status'] == 'CITES-AT-AN-UNKNOWN-REF']
    located_act = [x for x in out if x.get('act')]
    rec('')
    rec('-' * 100)
    rec('  ### (3) THE CLASSIFICATION.')
    rec('-' * 100)
    rec('    ### ### **ROWS WITH A LOCATABLE WRITING ACT : %d of %d**' % (len(located_act), len(out)))
    rec('    ### ### **ROWS WHOSE ACT COULD NOT BE LOCATED : %d**'
        % (len(out) - len(located_act)))
    rec('    ### ### **PINNABLE : %d ### / ### CITES-AT-AN-UNKNOWN-REF : %d**'
        % (len(pinnable), len(unknown)))
    rec('')
    rec('    the reasons, kept apart because they will not have the same cure:')
    for reason, n in sorted(by('reason').items(), key=lambda x: -x[1]):
        if reason:
            rec('      %-44s %d' % (reason, n))
    rec('')
    rec('    the acts that wrote the pinnable rows:')
    acts = {}
    for x in pinnable:
        acts[x['act']] = acts.get(x['act'], 0) + 1
    rec('      %s' % dict(sorted(acts.items())))

    # ---------------------------------------------------------------- the scope of the edit
    rec('')
    rec('-' * 100)
    rec('  ### (4) THE SCOPE OF THE EDIT. ### **CLASSIFIED IS NOT THE SAME AS EDITED.**')
    rec('-' * 100)
    excl = [x for x in pinnable if x['excluded']]
    inscope = [x for x in pinnable if not x['excluded']]
    rec('    ### ### **PINNABLE AND IN SCOPE : %d ### / ### PINNABLE BUT ON A SURFACE NO ACT MAY '
        'REWRITE : %d**' % (len(inscope), len(excl)))
    for reason in sorted(set(x['excluded'] for x in excl)):
        fs = sorted(set(x['file'] for x in excl if x['excluded'] == reason))
        rec('      %-26s %d row(s) in %d file(s)'
            % (reason, sum(1 for x in excl if x['excluded'] == reason), len(fs)))
        for f in fs:
            rec('          %s' % f)
    rec('    ### ### **AND THE EXCLUSION IS ROUTED, NOT DECIDED:** ### whether a deposited or archived')
    rec('    ### ### surface should carry pins is the author`s question and not this seat`s.')

    # ---------------------------------------------------------------- the price
    rec('')
    rec('-' * 100)
    rec('  ### (5) THE PRICE, IN THREE PARTS, REPORTED WHETHER OR NOT IT FITS.')
    rec('-' * 100)
    rec('    ### **ONE ROW** : a content re-anchor, one history search of the papers repository, one')
    rec('      subject parse, and one read of a banked pins record. ### Measured here at ### **%.2f'
        % (elapsed / max(1, len(rows))))
    rec('      SECONDS PER ROW**, dominated entirely by the history search.')
    rec('    ### **THE WHOLE SET** : %d rows at that rate is ### **%.0f SECONDS**, which is why this act'
        % (len(rows), elapsed))
    rec('      executes rather than only prices. ### **THE PRICE FITS ONE ACT.**')
    rec('    ### **THE SPLIT** : ### **THE LOCATING IS ENTIRELY MECHANICAL.** ### What is NOT mechanical')
    rec('      is ### **WHICH SURFACES MAY BE EDITED AT ALL** -- decided on the registration`s face and')
    rec('      routed to the author -- and ### **WHETHER A ROW`S CLAIM IS TRUE AT THE PIN NOW BESIDE')
    rec('      ### IT**, which is a check this act does not run and cannot be bought with a search.')

    # ---------------------------------------------------------------- the write
    wrote = []
    if write:
        rec('')
        rec('-' * 100)
        rec('  ### (6) THE WRITE. ### **ORIGINAL BANKED VERBATIM; PIN APPENDED TO THE CELL THAT NAMES')
        rec('  ### ### THE KERNEL; NO COLUMN ADDED; EVERY EDIT RE-READ FROM DISK.**')
        rec('-' * 100)
        byfile = {}
        for x in inscope:
            byfile.setdefault(x['file'], []).append(x)
        for rel, xs in sorted(byfile.items()):
            path = os.path.join(PP, rel.replace('/', os.sep))
            body = io.open(path, encoding='utf-8', errors='replace').read()
            body = body.replace(chr(13) + chr(10), chr(10))
            lines = body.split(chr(10))
            before = body
            n_ok = 0
            for x in xs:
                i = x['line'] - 1
                orig = lines[i]
                if orig.rstrip() != x['line_text']:
                    x['write'] = 'REFUSED -- THE ANCHOR MOVED'
                    continue
                if not orig.lstrip().startswith('|'):
                    x['write'] = 'REFUSED -- NOT A TABLE ROW; THE SHAPE CANNOT CARRY A PIN'
                    continue
                cells = orig.split('|')
                idx = [j for j, c in enumerate(cells) if x['kernel'] in c]
                if not idx:
                    x['write'] = 'REFUSED -- NO CELL NAMES THE KERNEL'
                    continue
                j = idx[0]
                pin7 = x['pin'][:7]
                if ('`%s`' % pin7) in cells[j]:
                    x['write'] = 'ALREADY PRESENT'
                    continue
                cells[j] = cells[j].rstrip() + (' (`%s`)' % pin7) + ' '
                lines[i] = '|'.join(cells)
                x['write'] = 'WRITTEN'
                x['original'] = orig
                x['written'] = lines[i]
                n_ok += 1
            after = chr(10).join(lines)
            if n_ok:
                io.open(path, 'w', encoding='utf-8', newline=chr(10)).write(after)
                back = io.open(path, encoding='utf-8', errors='replace').read().replace(
                    chr(13) + chr(10), chr(10))
                same_count = (len(back.split(chr(10))) == len(before.split(chr(10))))
                moved = sum(1 for a, b in zip(before.split(chr(10)), back.split(chr(10))) if a != b)
                rec('    %-62s %d written ; line count unchanged : %s ; lines differing : %d'
                    % (rel, n_ok, same_count, moved))
                wrote.append(dict(file=rel, written=n_ok, linecount_unchanged=same_count,
                                  lines_differing=moved))
            else:
                rec('    %-62s 0 written' % rel)
        refused = [x for x in inscope if x.get('write', '').startswith('REFUSED')]
        rec('')
        rec('    ### ### **WRITTEN : %d ### / ### REFUSED BY SHAPE : %d ### / ### ALREADY PRESENT : %d**'
            % (sum(1 for x in inscope if x.get('write') == 'WRITTEN'), len(refused),
               sum(1 for x in inscope if x.get('write') == 'ALREADY PRESENT')))
        for x in refused:
            rec('        %s:%d  %s' % (x['file'], x['line'], x['write']))

    badhead = [x for x in out if x.get('equals_a_head')]
    rec('')
    rec('=' * 100)
    rec('  ### ### **PINS EQUAL TO A CURRENT HEAD : %d** ### -- `(R9)` forbids it and this is the'
        % len(badhead))
    rec('  ### measurement, not the assertion.')
    rec('  ### **NO ROW WAS CHECKED AT ITS NEW PIN. ### NO KERNEL WAS OPENED. ### NO GRADE WAS MOVED.**')
    rec('  ### **NO DEPOSITED FILE, NO ARCHIVED FILE AND NO LEDGER ENTRY WAS EDITED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b373_pins_notes', LINES)
    io.open(os.path.join(D, 'b373_pins.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(mode=('write' if write else 'read'), rows=len(out),
                        located_act=len(located_act), act_not_located=len(out) - len(located_act),
                        pinnable=len(pinnable), unknown=len(unknown),
                        reasons=by('reason'), acts=acts,
                        in_scope=len(inscope), excluded=len(excl),
                        excluded_reasons={k: sum(1 for x in excl if x['excluded'] == k)
                                          for k in sorted(set(x['excluded'] for x in excl))},
                        written=sum(1 for x in out if x.get('write') == 'WRITTEN'),
                        files_written=wrote, equals_a_head=len(badhead),
                        seconds=elapsed, per_row=elapsed / max(1, len(rows)),
                        heads=heads, detail=out,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
