# -*- coding: utf-8 -*-
"""b723_fold.py -- (R333)(2)(i) ON THE AUTHOR'S WORD (OPTION 2): THE SEVEN CLOSE TOOLS FOLDED INTO ONE STANDING MODULE TAKING THE ACT.
Written whole at b723 by the Write tool. It builds; tools/standing/fold.py loads.

  build [dry]   for each of the seven tools (checks, citation, closing, record, reg_gate, regspec, report): b721's tool shifted once by the act
                names (b721 -> b722, b720 -> b721, R331 -> R332, R330 -> R331, each name once, bounded) diffed line by line against b722's
                (difflib, autojunk off). The lines both share are the standing template, tools/standing/fold/<tool>.tpl, the act names in it
                written as tokens -- the act ⟪ACT⟫, the act before it ⟪PREV⟫, the act's ruling ⟪RUL⟫, the ruling before it ⟪PRUL⟫ -- so no
                substitution ever runs over a name that means one act; each hunk a line ⟪SLOT n⟫. Each act's side of each hunk is that act's
                section n of that tool: b722's in tools/acts/b722.py, b721's in tools/acts/b721.py (a directory of their own: no worklist's
                SEALED, os.listdir of tools/, takes them in), each section the act's own lines,
                verbatim. `dry` prints the counts and writes nothing.
  text          THE TEXT CONTROL: tools/standing/fold.py's render of each tool for b722 and for b721 equal to tools/b722_<tool>.py and
                tools/b721_<tool>.py byte for byte; a planted section (one line changed) differs, as wanted.
"""
import difflib
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(ROOT, 'tools')
FOLD_DIR = os.path.join(T, 'standing', 'fold')
NL = '\n'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TOOLS = ('checks', 'citation', 'closing', 'record', 'reg_gate', 'regspec', 'report')
A, P = 'b722', 'b721'
SHIFT = (('b721', 'b722'), ('b720', 'b721'), ('R331', 'R332'), ('R330', 'R331'))
TOKENS = (('b722', '⟪ACT⟫'), ('b721', '⟪PREV⟫'), ('R332', '⟪RUL⟫'), ('R331', '⟪PRUL⟫'))


def bounded(name):
    return re.compile(r'(?<![0-9A-Za-z])%s(?![0-9])' % re.escape(name))


def shift(t):
    for a, b in SHIFT:                          # ### each name once: a NUL marks a shifted name until every pair is done
        t = bounded(a).sub('\0' + b, t)
    return t.replace('\0', '')


def tokenize(t):
    for a, tok in TOKENS:
        t = bounded(a).sub(tok, t)
    return t


def rd(p):
    with open(p, 'rb') as f:
        return f.read().decode('utf-8')


def lines(t):
    """the text as lines, each keeping its own end, so a join is the text byte for byte."""
    return t.splitlines(keepends=True)


def build(mode):
    out = {}
    sec = {A: [], P: []}
    for tool in TOOLS:
        a_t, p_t = rd(os.path.join(T, '%s_%s.py' % (A, tool))), rd(os.path.join(T, '%s_%s.py' % (P, tool)))
        if '⟪' in a_t or '⟪' in p_t:
            sys.exit('### %s: A TOKEN MARK ALREADY IN THE SOURCE -- NOTHING WRITTEN' % tool)
        la, lp_shift, lp = lines(a_t), lines(shift(p_t)), lines(p_t)
        if len(lp_shift) != len(lp):
            sys.exit('### %s: THE SHIFT CHANGED THE LINE COUNT -- NOTHING WRITTEN' % tool)
        sm = difflib.SequenceMatcher(None, lp_shift, la, autojunk=False)
        tpl, n = [], 0
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                tpl += [tokenize(l) for l in la[j1:j2]]
                continue
            n += 1
            tpl.append('⟪SLOT %d⟫\n' % n)
            sec[A].append((tool, n, ''.join(la[j1:j2])))
            sec[P].append((tool, n, ''.join(lp[i1:i2])))
        out[tool] = (''.join(tpl), n, sum(1 for o in sm.get_opcodes() if o[0] == 'equal' for _ in [0]),
                     sum(o[2] - o[1] for o in sm.get_opcodes() if o[0] == 'equal'), len(la), len(lp))
    for tool in TOOLS:
        t, n, _ne, eq, na, np_ = out[tool]
        print('  %-9s template %5d lines (shared %5d) ; slots %3d ; b722 %5d lines ; b721 %5d lines' % (tool, t.count(NL), eq, n, na, np_))
    print('  sections: b722 %d ; b721 %d' % (len(sec[A]), len(sec[P])))
    if mode == 'dry':
        return
    os.makedirs(FOLD_DIR, exist_ok=True)
    for tool in TOOLS:
        with open(os.path.join(FOLD_DIR, tool + '.tpl'), 'wb') as f:
            f.write(out[tool][0].encode('utf-8'))
    sys.path.insert(0, T)
    sys.path.insert(0, os.path.join(T, 'standing'))
    import fold as F
    for act in (A, P):
        dd = {}
        for tool in TOOLS:
            alias, used, missing = F.missing_names(act, rd(os.path.join(T, '%s_%s.py' % (act, tool))))
            dd[tool] = sorted(missing)
            print('  %s %-9s worklist alias %-4s names read %3d ; its worklist lacks %2d (declared dead): %s' % (
                act, tool, alias or '-', len(used), len(missing), ', '.join(sorted(missing)) or 'NONE'))
        write_sections(act, sec[act], dd)
    print('written tools/standing/fold/<tool>.tpl (7), tools/acts/%s.py, tools/acts/%s.py' % (A, P))


def render_prov(F, act, tool, secs, ovs):
    """the render as [(line, provenance)]: ('T', template line) or ('S', slot n, line in the section) or ('O', first, line in the override)."""
    tpl = rd(os.path.join(FOLD_DIR, tool + '.tpl')).splitlines(keepends=True)
    nm = F.names(act)
    at = dict((first, (last, text)) for first, last, text in ovs.get(tool, []))
    out, i = [], 0
    while i < len(tpl):
        if i + 1 in at:
            last, text = at[i + 1]
            out += [(l, ('O', i + 1, k)) for k, l in enumerate(lines(text))]
            if last >= i + 1:
                i = last
                continue
        m = F.SLOT.match(tpl[i])
        if m:
            n = int(m.group(1))
            out += [(l, ('S', n, k)) for k, l in enumerate(lines(secs[(tool, n)]))]
        else:
            l = tpl[i]
            for tok, v in nm.items():
                l = l.replace(tok, v)
            out.append((l, ('T', i + 1)))
        i += 1
    return out


def adopt(tool):
    """THE ACT'S LANDED TOOL INTO ITS ARMS MODULE: each hunk between the render of tools/acts/<act>.py and the landed tools/<act>_<tool>.py
    mapped to its source -- inside one section, that section's lines changed; over template lines alone, an OVERRIDE of those lines -- and the
    module rewritten; the control the new render equal to the landed file byte for byte. A hunk across a section and the template is refused."""
    sys.path.insert(0, T)
    sys.path.insert(0, os.path.join(T, 'standing'))
    import fold as F
    act = F.act_current()['act']
    secs, ovs = F._parse(act)
    landed = rd(os.path.join(T, '%s_%s.py' % (act, tool)))
    R = render_prov(F, act, tool, secs, ovs)
    L = lines(landed)
    sm = difflib.SequenceMatcher(None, [l for l, _p in R], L, autojunk=False)
    sec_edits, new_ovs, refused = {}, [], []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            continue
        provs = [p for _l, p in R[i1:i2]]
        if not provs:                      # ### an insertion: into the section beside it, else before the template line it precedes
            before = R[i1 - 1][1] if i1 > 0 else None
            after = R[i1][1] if i1 < len(R) else None
            if before and before[0] == 'S':
                sec_edits.setdefault(before[1], []).append((before[2] + 1, before[2] + 1, L[j1:j2]))
            elif after and after[0] == 'S':
                sec_edits.setdefault(after[1], []).append((after[2], after[2], L[j1:j2]))
            elif after and after[0] == 'T':
                new_ovs.append((after[1], after[1] - 1, ''.join(L[j1:j2])))
            else:
                refused.append((i1, i2, 'insertion with no template or section beside it'))
            continue
        kinds = set(p[0] for p in provs)
        if kinds == {'S'} and len(set(p[1] for p in provs)) == 1:
            sec_edits.setdefault(provs[0][1], []).append((provs[0][2], provs[-1][2] + 1, L[j1:j2]))
        elif kinds == {'T'} and [p[1] for p in provs] == list(range(provs[0][1], provs[-1][1] + 1)):
            new_ovs.append((provs[0][1], provs[-1][1], ''.join(L[j1:j2])))
        elif kinds <= {'S', 'T'}:
            # ### a hunk across sources: split into runs of one source each, the landed lines to the first run and the others emptied; the
            # ### order of the runs is the render's, so the joined text is the landed text (the byte-for-byte control below reads it)
            runs = []
            for p in provs:
                key = ('S', p[1]) if p[0] == 'S' else ('T',)
                if runs and runs[-1][0] == key and (key[0] == 'S' or runs[-1][1][-1][1] + 1 == p[1]):
                    runs[-1][1].append(p)
                else:
                    runs.append((key, [p]))
            for k, (key, ps) in enumerate(runs):
                repl = L[j1:j2] if k == 0 else []
                if key[0] == 'S':
                    sec_edits.setdefault(key[1], []).append((ps[0][2], ps[-1][2] + 1, repl))
                else:
                    new_ovs.append((ps[0][1], ps[-1][1], ''.join(repl)))
        else:
            refused.append((i1, i2, 'a hunk across %s' % sorted(kinds)))
    if refused:
        sys.exit('### REFUSED, NOTHING WRITTEN: %s' % refused)
    for n, eds in sec_edits.items():
        sl = lines(secs[(tool, n)])
        for a, b, repl in sorted(eds, reverse=True):
            sl[a:b] = repl
        secs[(tool, n)] = ''.join(sl)
    ovs.setdefault(tool, [])
    ovs[tool] = sorted(ovs[tool] + new_ovs)
    got = F.render(act, tool, secs=secs, ovs=ovs)
    ok = got == landed
    print('  %s %-9s hunks %d: section edits in %d section(s) %s ; overrides %d %s ; the new render %s the landed file' % (
        act, tool, sum(len(e) for e in sec_edits.values()) + len(new_ovs), len(sec_edits), sorted(sec_edits),
        len(new_ovs), [(a, b) for a, b, _t in new_ovs], 'EQUAL BYTE FOR BYTE TO' if ok else 'DIFFERS FROM'))
    if not ok:
        sys.exit('### NOT EQUAL -- NOTHING WRITTEN')
    rows = [(t, n, text) for (t, n), text in sorted(secs.items())]
    write_sections(act, rows, dict((t, sorted(v)) for t, v in F.dead(act).items()), ovs,
                   pend=dict((t, sorted(v)) for t, v in F.pending(act).items()), reps=F.REPAIRS.get(act, {}))
    print('  written tools/acts/%s.py' % act)


def write_sections(act, rows, dd, ovs=None, pend=None, reps=None):
    """tools/acts/<act>.py: the act's sections, each a marker line and the given number of characters after it; read as text by the loader."""
    head = ('# -*- coding: utf-8 -*-\n'
            '# %s -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R333)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.\n'
            '# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)\n'
            '# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line\n'
            '# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline. Edited by the Edit tool. Built at b723 by\n'
            '# tools/b723_fold.py from tools/%s_<tool>.py.\n'
            '# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on\n'
            '# routes the act never ran (the tool as carried); the loader prints them and refuses any other missing name.\n' % (act, act)
            + ''.join('#⟪DEAD %s %s⟫\n' % (t, ','.join(dd.get(t, []))) for t in TOOLS)
            + ('# Each "#⟪PENDING <tool> <names>⟫" line: names the act`s tool reads on routes carried from the act before that the act has\n'
               '# still to write for itself; printed at every load; the act`s suite holds them empty at its seal.\n'
               + ''.join('#⟪PENDING %s %s⟫\n' % (t, ','.join(pend.get(t, []))) for t in TOOLS) if pend is not None else ''))
    def block(head, text, tag=None):
        noeol = bool(text) and not text.endswith('\n')
        return '#⟪%s%s%s⟫\n%s%s#⟪END⟫\n' % (head, ' NOEOL' if noeol else '', ' REPAIR ' + tag if tag else '', text, '\n' if noeol else '')
    reps = reps or {}
    body = ''.join(block('SECTION %s %d' % (tool, n), text) for tool, n, text in rows)
    body += ''.join(block('OVERRIDE %s %d %d' % (tool, a, b), text, reps.get((tool, a)))
                    for tool in TOOLS for a, b, text in sorted((ovs or {}).get(tool, [])))
    os.makedirs(os.path.join(T, 'acts'), exist_ok=True)
    with open(os.path.join(T, 'acts', '%s.py' % act), 'wb') as f:
        f.write((head + body).encode('utf-8'))


def text_control():
    sys.path.insert(0, os.path.join(T, 'standing'))
    import fold as F
    bad = 0
    for act in (A, P):
        for tool in TOOLS:
            want = rd(os.path.join(T, '%s_%s.py' % (act, tool)))
            got = F.render(act, tool)
            ok = got == want
            bad += not ok
            first = next((i for i, (x, y) in enumerate(zip(got, want)) if x != y), min(len(got), len(want)))
            print('  %s %-9s render %7d chars ; the file %7d ; %s' % (act, tool, len(got), len(want),
                                                                      'EQUAL BYTE FOR BYTE -- AS WANTED' if ok else 'DIFFERS at %d -- NOT AS WANTED' % first))
    import subprocess
    cur = F.act_current()['act']
    secs, ovs = F._parse(cur)
    reps = F.REPAIRS.get(cur, {})
    base = dict((t, [o for o in v if (t, o[0]) not in reps]) for t, v in ovs.items())
    n = 2 * len(TOOLS)
    import importlib
    sys.path.insert(0, T)
    landed_at = importlib.import_module('%s_worklist' % cur).STEPZERO_BANKS   # ### the commit that landed the carried tools (026335ad at b723)
    for tool in TOOLS:                      # ### the act's own: its base render (its named repairs left out) against each tool its step zero landed
        r = subprocess.run(['git', '-C', ROOT, 'show', '%s:tools/%s_%s.py' % (landed_at, cur, tool)], capture_output=True)
        if r.returncode != 0:
            continue
        n += 1
        ok = F.render(cur, tool, secs=secs, ovs=base) == r.stdout.decode('utf-8')
        bad += not ok
        print('  %s %-9s base render (repairs left out) against tools/%s_%s.py as landed at %s ; %s' % (
            cur, tool, cur, tool, landed_at[:8], 'EQUAL BYTE FOR BYTE -- AS WANTED' if ok else 'DIFFERS -- NOT AS WANTED'))
    for (tool, first), name in sorted(reps.items()):
        last = next(b for a, b, _t in ovs[tool] if a == first)
        print('  %s REPAIR %-6s %-8s the template`s lines %d-%d replaced in %s`s render alone' % (cur, name, tool, first, last, cur))
    # ### the plant: one section line changed, the render differs
    secs = F.sections(A)
    k = sorted(secs)[0]
    planted = dict(secs)
    planted[k] = planted[k].replace('\n', ' # planted\n', 1)
    got = F.render(A, k[0], secs=planted)
    want = rd(os.path.join(T, '%s_%s.py' % (A, k[0])))
    print('  PLANTED: %s section %s %d with one line changed -- the render %s' % (A, k[0], k[1], 'DIFFERS, AS WANTED' if got != want else 'EQUAL, NOT AS WANTED'))
    bad += got == want
    print('### ### **THE TEXT CONTROL: %d RENDERS ; %s.**' % (n,'ALL EQUAL BYTE FOR BYTE, THE PLANT DIFFERING' if not bad else '%d NOT AS WANTED' % bad))


IMP = re.compile(r'(?m)^\s*(?:import\s+([\w.]+(?:\s*,\s*[\w.]+)*)|from\s+([\w.]+)\s+import\s+([\w, ()]+))|'
                 r'import_module\(\s*[\'"]([\w.]+)[\'"]|__import__\(\s*[\'"]([\w.]+)[\'"]')
ACTNUM = re.compile(r'^b\d{3}_\w+$')


def imports_of(text):
    out = set()
    for m in IMP.finditer(text):
        if m.group(1):
            out |= {x.strip().split(' ')[0] for x in m.group(1).split(',')}
        if m.group(2):
            out.add(m.group(2))
            if m.group(2) == 'standing':
                out |= {'standing.' + x.strip() for x in m.group(3).replace('(', '').replace(')', '').split(',') if x.strip()}
        for g in (m.group(4), m.group(5)):
            if g:
                out.add(g)
    return out


def source_of(name):
    p = os.path.join(T, *name.split('.')) + '.py'
    return p if os.path.isfile(p) else None


def legacy(mode):
    """THE LEGACY LIST: every act-numbered module the folded tools reach by an import written in their source, followed through each
    reached module's own source (tools/ and tools/standing/), the folded tools themselves (an act with a sections file) left out."""
    sys.path.insert(0, os.path.join(T, 'standing'))
    import fold as F
    acts = [a for a in (A, P, F.act_current()['act']) if F.has_sections(a)]
    todo = [(a, F.render(a, t), '%s_%s' % (a, t)) for a in acts for t in TOOLS]
    seen, found, via = set(), set(), {}
    while todo:
        _a, text, who = todo.pop()
        for n in sorted(imports_of(text)):
            if n in seen:
                continue
            seen.add(n)
            if ACTNUM.match(n):
                if n[5:] in TOOLS and F.has_sections(n[:4]):
                    todo.append((n[:4], F.render(n[:4], n[5:]), n))
                    continue
                found.add(n)
                via[n] = who
            s = source_of(n)
            if s:
                todo.append((None, rd(s), n))
    names = sorted(found)
    print('  folded acts %s ; modules read %d ; act-numbered predecessors %d' % (', '.join(acts), len(seen), len(names)))
    for n in names:
        print('    %-28s first reached from %s%s' % (n, via[n], '' if source_of(n) else '   ### NO SOURCE IN tools/'))
    if mode == 'dry':
        return
    body = ('# -*- coding: utf-8 -*-\n'
            '"""standing/legacy.py -- THE ACT-NUMBERED PREDECESSOR MODULES THE FOLDED TOOLS IMPORT, BY NAME ((R333)(2)(i), the author`s word:\n'
            'Option 2). THE STATED EXCEPTION TO tools/standing/act.py`S RULE: tools/standing/fold.py`s import finder lets an act-numbered import\n'
            'through only where it is a folded tool or is named here. Written at b723 by tools/b723_fold.py legacy from the imports written in\n'
            'the folded tools and, followed, in the modules they reach; their flattening priced and carried to b724 (data/b723_fold.txt)."""\n'
            'NAMES = (\n' + ''.join("    '%s',\n" % n for n in names) + ')\n')
    with open(os.path.join(T, 'standing', 'legacy.py'), 'wb') as f:
        f.write(body.encode('utf-8'))
    print('written tools/standing/legacy.py (%d names)' % len(names))


def carry_act(mode):
    """b723'S ARMS MODULE, CARRIED: each of b722's sections shifted by tools/b723_carry.py's own substitute() (the pairs it ran over the whole
    tools at step zero), written to tools/acts/b723.py with its dead names read against tools/b723_worklist.py. The control: the render of each
    tool for b723 equal to substitute(tools/b722_<tool>.py), what the carry makes of the whole file, and, for the two the carry landed
    (b723_record.py, b723_citation.py), to the file as committed. b723's own changes are made after, by the Edit tool, as overrides."""
    sys.path.insert(0, T)
    sys.path.insert(0, os.path.join(T, 'standing'))
    import fold as F
    import b723_carry as C
    act = F.act_current()['act']
    rows = [(tool, n, C.substitute(text)) for (tool, n), text in sorted(F.sections(A).items())]
    p = os.path.join(T, 'acts', '%s.py' % act)
    if os.path.exists(p) and mode != 'again':
        sys.exit('### tools/acts/%s.py EXISTS: the act`s own module is edited by the Edit tool, not rebuilt -- NOTHING WRITTEN' % act)
    write_sections(act, rows, dict((t, []) for t in TOOLS))
    # ### the dead names carried are b722's declared dead alone: a name b723's worklist lacks beyond them is the act's work, and refuses its load
    dd, new = {}, {}
    d722 = F.dead(A)
    for tool in TOOLS:
        alias, used, missing = F.missing_names(act, F.render(act, tool))
        dd[tool] = sorted(missing & d722.get(tool, set()))
        new[tool] = sorted(missing - d722.get(tool, set()))
    write_sections(act, rows, dd, pend=new)
    for tool in TOOLS:
        print('  %s %-9s dead carried from %s %2d ; MISSING BEYOND THEM, PENDING (printed at every load; held empty at the seal) %2d %s' % (
            act, tool, A, len(dd[tool]), len(new[tool]), ', '.join(new[tool]) or 'NONE'))
    print('  written tools/acts/%s.py: %d sections carried from tools/acts/%s.py by the carry`s substitute()' % (act, len(rows), A))
    bad = 0
    for tool in TOOLS:
        got = F.render(act, tool)
        want = C.substitute(rd(os.path.join(T, '%s_%s.py' % (A, tool))))
        landed = os.path.join(T, '%s_%s.py' % (act, tool))
        lv = rd(landed) if os.path.isfile(landed) else None
        ok = got == want
        bad += not ok
        print('  %s %-9s render %7d chars ; the carry`s substitute of %s`s %7d ; %s%s' % (
            act, tool, len(got), A, len(want), 'EQUAL' if ok else 'DIFFERS at %d' % next(
                (i for i, (x, y) in enumerate(zip(got, want)) if x != y), min(len(got), len(want))),
            '' if lv is None else ' ; the landed tools/%s_%s.py %s' % (act, tool, 'EQUAL' if lv == got else 'DIFFERS')))
    print('### ### **b723`S ARMS MODULE: %s.**' % ('EVERY RENDER EQUAL TO THE CARRY`S SUBSTITUTE' if not bad else '%d RENDERS DIFFER' % bad))


def prevnames_control():
    """the author's word, Option 2: "the --prev names computed from the worklist". b723's _PrevWorklist.OWN (its slot, computed) beside the
    hand list b722 carried (b722's own OWN, the slot b723 carried before), each read from the rendered tool imported with --prev, nothing
    run: for every name both worklists carry the two give the same owner (a name the previous worklist lacks reads this act's under
    either; one this act's lacks reads the previous act's under either, the getattr falling through). The --prev READING itself is the
    pre-seal run's: its sources read the act's component commits, None until the components are made (the crash printed)."""
    import importlib
    sys.path[:0] = [T, os.path.join(T, 'standing')]
    import fold
    fold.install()
    sys.argv[1:] = ['--prev']
    k = {}
    for act in ('b722', 'b723'):
        m = importlib.import_module('%s_checks' % act)
        k[act] = (m._PrevWorklist.OWN, m.K._own, m.K._prev)
    hand, (own, K, K0) = set(k['b722'][0]), (set(k['b723'][0]), k['b723'][1], k['b723'][2])
    both = sorted(n for n in set(vars(K)) & set(vars(K0)) if not n.startswith('_'))
    differ = [n for n in both if (n in hand) != (n in own)]
    print('  the hand list (b722`s, carried): %d names ; computed for b723: %d: %s' % (len(hand), len(own), ' '.join(k['b723'][0])))
    print('  dropped by the computation: %s ; each absent from b722`s worklist or from b723`s, its owner unchanged' % (
        ' '.join('%s (%s)' % (n, 'b722 lacks' if not hasattr(K0, n) else 'b723 lacks, PENDING') for n in sorted(hand - own)) or 'NONE'))
    print('  added by the computation: %s' % (' '.join(sorted(own - hand)) or 'NONE'))
    print('  the names both worklists carry: %d ; their owner differing between the two lists: %d%s' % (len(both), len(differ),
          (' ' + ' '.join(differ)) if differ else ''))
    print('  ### the --prev READING on b722`s banks: CARRIED TO THE PRE-SEAL --prev RUN, NOT RUN NOW -- every part`s sources read the act`s '
          'component commits (b723_checks :503-:505, C3_RELAY ... C6_RELAY), None before the components; run 07:16:18Z and 07:17:11Z, '
          'TypeError at subprocess (a None argument), nothing banked')
    print('### PREVNAMES: %s' % ('ALL AS WANTED' if not differ else 'NOT AS WANTED'))
    return not differ


def names_control():
    """THE NAMES CONTROL ((R333)(2)(i)'s "a planted act missing one name fails as wanted"): every name each b722 tool reads through its
    worklist alias found in b722's worklist or declared dead (AS WANTED: loads); a copy of b722's worklist with one name the checks tool reads
    removed, in memory (AS WANTED: refused, naming it); the finder refusing an act-numbered import neither folded nor in the legacy list and
    letting a listed one through; and b723's own tools, each refused or not by the names its worklist lacks (the act's work, printed)."""
    sys.path.insert(0, T)
    sys.path.insert(0, os.path.join(T, 'standing'))
    import types
    import fold as F
    F.install()
    bad = 0
    for tool in TOOLS:
        try:
            used = F.check_names(A, tool, F.render(A, tool))
            print('  %s %-9s names read through its worklist %3d ; each defined or declared dead -- LOADS, AS WANTED' % (A, tool, len(used)))
        except F.FoldRefused as e:
            bad += 1
            print('  %s %-9s REFUSED, NOT AS WANTED: %s' % (A, tool, e))
    import importlib
    wl = importlib.import_module('%s_worklist' % A)
    text = F.render(A, 'checks')
    _alias, used, _m = F.missing_names(A, text)
    gone = sorted(used)[0]
    plant = types.ModuleType('planted')
    plant.__dict__.update(dict((k, v) for k, v in wl.__dict__.items() if k != gone))
    try:
        F.check_names(A, 'checks', text, plant)
        bad += 1
        print('  PLANTED: %s`s worklist without %s -- LOADED, NOT AS WANTED' % (A, gone))
    except F.FoldRefused as e:
        print('  PLANTED: %s`s worklist without %s (in memory) -- REFUSED, AS WANTED: %s' % (A, gone, e))
    for name, want in (('b999_nothing', 'refused'), ('b712_worklist', 'through')):
        try:
            F.FINDER.find_spec(name)
            got = 'through'
        except F.FoldRefused:
            got = 'refused'
        bad += got != want
        print('  THE FINDER on `import %s`: %s -- %s' % (name, got, 'AS WANTED' if got == want else 'NOT AS WANTED'))
    cur = F.act_current()['act']
    for tool in TOOLS:
        try:
            F.check_names(cur, tool, F.render(cur, tool))
            print('  %s %-9s loads' % (cur, tool))
        except F.FoldRefused as e:
            print('  %s %-9s refused (the act`s work, not a control): %s' % (cur, tool, e))
    print('### ### **THE NAMES CONTROL: %s.**' % ('ALL AS WANTED' if not bad else '%d NOT AS WANTED' % bad))


PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
ROW = re.compile(r'^  (G-[A-Z0-9-]+)\s+(PASS|FAIL|-+|\S+)\s+(PASS|FAIL|\S+)\s+(PASS|FAIL|\S+)\s+[\d.]+\s+(.*)$')


def arm_rows(p):
    """{arm: (LIVE, NEG, POS, verdict)} -- the arm table of one part bank, seconds left out."""
    if not os.path.isfile(p):
        return None
    out = {}
    for l in rd(p).replace('\r', '').split(NL):
        m = ROW.match(l)
        if m:
            out[m.group(1)] = (m.group(2), m.group(3), m.group(4), m.group(5).strip())
    return out


def bank():
    """data/b723_fold.txt: THE FOLD'S BUILD (each template's lines, slots and the acts' sections), THE LEGACY LIST PRINTED WHOLE (the stated
    exception to tools/standing/act.py's rule, the author's word), and THE FLATTENING PRICED for b724: the act-numbered predecessor modules the
    folded tools reach, their direct imports from the templates and the act modules, and the lines a flattening would read."""
    import hashlib
    import importlib
    sys.path.insert(0, T)
    sys.path.insert(0, os.path.join(T, 'standing'))
    import fold as F
    import legacy as LG
    act = F.act_current()['act']
    out = ['%s -- THE SEVEN CLOSE TOOLS FOLDED ((R333)(2)(i), the author`s word: Option 2), tools/standing/fold.py' % act, '']
    out.append('### THE BUILD (tools/%s_fold.py build): each tool`s template the lines b722`s and b721`s tools share after the shift, each hunk a slot' % act)
    for tool in TOOLS:
        tpl = rd(os.path.join(FOLD_DIR, tool + '.tpl'))
        out.append('  %-9s template %5d lines, slots %3d, sha256 %s' % (tool, tpl.count(NL), len(F.SLOT.findall(tpl)),
                                                                       hashlib.sha256(tpl.encode('utf-8')).hexdigest()[:16]))
    for a in (P, A, act):
        secs, ovs = F._parse(a)
        p = F.sections_path(a)
        out.append('  tools/acts/%s.py: sections %d, overrides %d (repairs %s), dead %s, pending %s ; sha256 %s' % (
            a, len(secs), sum(len(v) for v in ovs.values()), sorted(set(F.REPAIRS.get(a, {}).values())) or 'NONE',
            sum(len(v) for v in F.dead(a).values()), sum(len(v) for v in F.pending(a).values()),
            hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]))
    for a in (act,):
        for t, v in sorted(F.pending(a).items()):
            if v:
                out.append('  PENDING %s %-9s %s' % (a, t, ', '.join(sorted(v))))
    out += ['', '### THE LEGACY LIST, tools/standing/legacy.py, WHOLE: %d act-numbered predecessor modules the folded tools import, by name' % len(LG.NAMES)]
    for i in range(0, len(LG.NAMES), 6):
        out.append('  ' + ', '.join(LG.NAMES[i:i + 6]))
    direct = set()
    for a in (P, A, act):
        for tool in TOOLS:
            direct |= set(n for n in imports_of(F.render(a, tool)) if ACTNUM.match(n) and n in LG.NAMES)
    tot = sum(rd(source_of(n)).count(NL) for n in LG.NAMES if source_of(n))
    nosrc = [n for n in LG.NAMES if not source_of(n)]
    out += ['', '### THE FLATTENING, PRICED FOR b724 (carried, not done): the folded tools import %d of the %d directly; the other %d are reached' % (
        len(direct), len(LG.NAMES), len(LG.NAMES) - len(direct)),
        '  through them. A flattening reads the %d modules` %d lines (%d names have no source in tools/, a route importing one fails if called: %s), keeps' % (
            len(LG.NAMES) - len(nosrc), tot, len(nosrc), ', '.join(nosrc)),
        '  the functions the folded tools call, writes them into tools/standing/, and empties the list; the direct imports: %s' % ', '.join(sorted(direct))]
    p = os.path.join(ROOT, 'data', '%s_fold.txt' % act)
    with open(p + '.tmp', 'wb') as f:
        f.write((NL.join(out) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(NL.join(out))
    print('written data/%s_fold.txt' % act)


def run_compare(wt):
    """THE RUN CONTROL: in a worktree of the relay at b722's post-push state (wt), b722's suite run part by part by the tool as b722 left it
    (tools/b722_checks.py, banks *_rcorig_*) and by the fold (tools/standing/fold.py checks --act b722, banks *_rcfold_*); the two compared
    arm for arm (LIVE, NEG, POS, verdict), and each against b722's own post-push banks (data/b722_checks_postpush_<part>.txt)."""
    tot, twin_diff, bank_diff = 0, [], []
    for part in PARTS:
        o = arm_rows(os.path.join(wt, 'data', 'b722_checks_rcorig_%s.txt' % part))
        f = arm_rows(os.path.join(wt, 'data', 'b722_checks_rcfold_%s.txt' % part))
        b = arm_rows(os.path.join(ROOT, 'data', 'b722_checks_postpush_%s.txt' % part))
        if o is None or f is None or b is None:
            print('  %-13s ### A BANK ABSENT: original %s, fold %s, b722`s %s' % (part, o is not None, f is not None, b is not None))
            twin_diff.append((part, 'ABSENT'))
            continue
        tot += len(f)
        td = sorted(a for a in set(o) | set(f) if o.get(a) != f.get(a))
        bd = sorted(a for a in set(b) | set(f) if b.get(a) != f.get(a))
        twin_diff += [(part, a) for a in td]
        bank_diff += [(part, a, b.get(a), f.get(a)) for a in bd]
        print('  %-13s arms: original %3d, fold %3d, b722`s bank %3d ; original vs fold differ %d ; fold vs b722`s bank differ %d' % (
            part, len(o), len(f), len(b), len(td), len(bd)))
    print('  ### THE TWIN (the tool as b722 left it vs the fold, same worktree, same state): %d arm rows, %s' % (
        tot, 'EQUAL ARM FOR ARM -- AS WANTED' if not twin_diff else 'DIFFERING %s -- NOT AS WANTED' % twin_diff))
    print('  ### THE FOLD VS b722`S BANKED POST-PUSH READING: %d arm(s) differ%s' % (len(bank_diff), ':' if bank_diff else ''))
    for part, a, bv, fv in bank_diff:
        print('    %-13s %-30s b722`s bank %s ; this run %s ; %s' % (part, a, bv, fv, CAUSES.get(a, '### CAUSE NOT READ')))
    return twin_diff, bank_diff


# ### the causes of the arms the worktree reads differently from b722's bank, each read (scratchpad wtcause723.py; the transcript's lines named)
# ### and the same in the tool as b722 left it and in the fold
CAUSES = {
    'G-LOCAL-BANK-UNTRACKED': 'THE WORKTREE: b628`s local bank data/b628_intake_crank_v0_5.txt is untracked, present in the relay, absent from a worktree',
    'G-EXPORT-UNTRACKED': 'THE WORKTREE: the navigator`s export data/b647_navigator_memory.txt is untracked, present in the relay, absent from a worktree',
    'G-ACTROOT-LAST': 'THE WORKTREE: the arm reads each root bank`s write time against the root`s; a checkout writes every file at its own time',
    'G-RULE-POSTSEAL-READ': 'THE TRANSCRIPT READ LATER: the session transcript now carries the shell calls made after b722`s post-push reading '
                            '(two by a filter or a redirect, 03:05:11Z and 03:38:05Z)',
}


def run_bank(wt):
    """data/b723_fold_run.txt: the run control's comparison, with the worktree's commit and the fold's bytes the runs used."""
    import contextlib
    import hashlib
    import io as _io
    buf = _io.StringIO()
    with contextlib.redirect_stdout(buf):
        twin, bd = run_compare(wt)
    head = subprocess_out(['git', '-C', wt, 'rev-parse', 'HEAD']).strip()
    sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]
    hdr = ['b723 -- THE RUN CONTROL OF THE FOLD ON b722`S BANKS ((R333)(2)(i)): b722`s suite, part by part, by the tool as b722 left it',
           '(tools/b722_checks.py) and by the fold (tools/standing/fold.py checks --act b722), in a worktree of the relay at %s' % head,
           '(b722 record, its post-push reading`s HEAD); each part`s banks named *_rcorig_* and *_rcfold_* (--rerun-postpush), the fold`s files',
           'copied in untracked: fold.py %s, the worktree`s copy %s ; tools/acts/b722.py %s, the worktree`s %s' % (
               sha(os.path.join(T, 'standing', 'fold.py')), sha(os.path.join(wt, 'tools', 'standing', 'fold.py')),
               sha(os.path.join(T, 'acts', 'b722.py')), sha(os.path.join(wt, 'tools', 'acts', 'b722.py'))),
           '### A TRANSIENT, RECORDED: the original`s first standing-b2a run (its half banked 2026-10-29T06:42:52Z) read 17 of b624-b641 DISAGREE,',
           '### each "head SIDE-li-map b515e6b62c15 not on the remote main " with the remote main EMPTY (act_root.py :447-450: ls-remote returned',
           '### no refs), and its standing-b3 FAILED G-ACTROOT-VERIFY; the claim tested directly (ls-remote: main 9e02bc0010f1, b515e6b62c15 its',
           '### ancestor), the original`s standing-b2a and standing-b3 re-run alone (07:01:59Z, 07:10:14Z): AGREE 35, PASS. The first half`s JSON was',
           '### overwritten by the re-run, its words above from the session`s output. The runs compared below are the re-runs.', '']
    text = buf.getvalue().replace('\r', '')
    p = os.path.join(ROOT, 'data', 'b723_fold_run.txt')
    with open(p + '.tmp', 'wb') as f:
        f.write((NL.join(hdr) + NL + text).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(NL.join(hdr) + NL + text + 'written data/b723_fold_run.txt')


def subprocess_out(argv):
    import subprocess
    return subprocess.run(argv, capture_output=True).stdout.decode('utf-8', 'replace')


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r == 'run':
        run_bank(sys.argv[2]) if '--bank' in sys.argv else run_compare(sys.argv[2])
        sys.exit(0)
    if r == 'bank':
        bank()
        sys.exit(0)
    if r == 'build':
        build(sys.argv[2] if len(sys.argv) > 2 else 'write')
    elif r == 'text':
        text_control()
    elif r == 'names':
        names_control()
    elif r == 'prevnames':
        prevnames_control()
    elif r == 'adopt':
        adopt(sys.argv[2])
    elif r == 'carry':
        carry_act(sys.argv[2] if len(sys.argv) > 2 else '')
    elif r == 'legacy':
        legacy(sys.argv[2] if len(sys.argv) > 2 else 'write')
    else:
        sys.exit('usage: b723_fold.py build [dry] | text | legacy [dry]')
