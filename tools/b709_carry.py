# -*- coding: utf-8 -*-
"""b709_carry.py -- THE CARRY BY DIFF, data/b709_rules.txt row (1) ((R319)(2)): a tool carried from the previous act is produced from the
previous act's tool by the act names' substitution alone and its diff banked; the seat reads the carried tool through the previous act's
tool-repairs bank and the spans those diffs name, by offset and limit, and not whole.

### `carry <name>`: tools/b708_<name>.py -> tools/b709_<name>.py with b708 -> b709, b707 -> b708 (the previous act's names and baselines shift by one
### act), (R318) -> (R319), (R317) -> (R318); the diff banked in data/b709_carry_<name>.txt (built from autojunk=False opcodes, b697's trap) with
### the spans the previous act's tool-repairs bank names for the tool (its hunk headers), the spans the seat reads in the carried file by the Read
### tool; `spans`: every carried tool's spans summarised in data/b709_carry_spans.txt. The repairs of this act are then made by the Edit tool and
### banked in data/b709_tool_repairs.txt by the record tool. Written by the Write tool at b709; it writes only tools/b709_<name>.py and the
### banks named above.
"""
import difflib
import io
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PREV, ACT = 'b708', 'b709'
SUBS = (('b708', 'b709'), ('b707', 'b708'), ('(R318)', '(R319)'), ('(R317)', '(R318)'), ('R318', 'R319'), ('R317', 'R318'))


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def substitute(text):
    """the act names shifted by one act, longest names first so that (R318) is not read twice."""
    out = text
    for a, b in SUBS:
        out = out.replace(a, b)
    return out


def udiff(old, new, a_name, b_name):
    """a unified diff from autojunk=False opcodes (b697's trap: difflib's default autojunk drops long runs)."""
    sm = difflib.SequenceMatcher(None, old, new, autojunk=False)
    L = ['--- ' + a_name, '+++ ' + b_name]
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        L.append('@@ -%d,%d +%d,%d @@' % (i1 + 1, i2 - i1, j1 + 1, j2 - j1))
        for l in old[i1:i2]:
            L.append('-' + l)
        for l in new[j1:j2]:
            L.append('+' + l)
    return L


def repair_spans(name):
    """the hunk headers of the previous act's tool-repairs bank that name tools/<prev>_<name>.py: [(line of the row, hunk header)]."""
    L = rd(os.path.join(D, '%s_tool_repairs.txt' % PREV)).split(NL)
    out, cur = [], None
    for i, l in enumerate(L, 1):
        m = re.match(r'^  \((\d+)\) tools/(\S+)', l)
        if m:
            cur = (i, m.group(2))
        if l.strip().startswith('@@') and cur and cur[1] == '%s_%s.py' % (PREV, name):
            out.append((cur[0], i, l.strip()))
    return out


def carry(name, *a):
    src = os.path.join(T, '%s_%s.py' % (PREV, name))
    dst = os.path.join(T, '%s_%s.py' % (ACT, name))
    old = rd(src)
    if not old:
        sys.exit('### tools/%s_%s.py IS NOT THERE -- NOTHING CARRIED' % (PREV, name))
    if os.path.exists(dst) and 'again' not in a:
        sys.exit('### tools/%s_%s.py EXISTS -- NOTHING WRITTEN (give `again` to rewrite the carried form)' % (ACT, name))
    new = substitute(old)
    ol, nl_ = old.split(NL), new.split(NL)
    diff = udiff(ol, nl_, 'tools/%s_%s.py' % (PREV, name), 'tools/%s_%s.py' % (ACT, name))
    spans = repair_spans(name)
    with open(dst + '.tmp', 'wb') as fh:
        fh.write(new.encode('utf-8'))
    os.replace(dst + '.tmp', dst)
    changed = sum(1 for l in diff if l.startswith('+') and not l.startswith('+++'))
    L = ['%s -- THE CARRY BY DIFF (data/b709_rules.txt row (1)): tools/%s_%s.py -> tools/%s_%s.py (%s)' % (ACT, PREV, name, ACT, name, utc()), '',
         '### the previous act`s tool carried by the act names` substitution alone (%s); %d lines, %d lines changed by the substitution; the seat reads' % (
             ', '.join('%s -> %s' % s for s in SUBS), len(nl_), changed),
         '### the carried tool through the spans the previous act`s tool-repairs bank names for it (below) and this diff, by offset and limit, not whole.',
         '### THE SPANS data/%s_tool_repairs.txt NAMES FOR THIS TOOL (the row`s line ; the hunk`s line ; the hunk header, its line numbers in the carried file`s predecessor):' % PREV]
    L += ['  row :%d ; hunk :%d ; %s' % s for s in spans] or ['  NONE: no repair of this tool at %s; the seat reads this diff`s hunks alone' % PREV]
    L += ['', '### THE DIFF OF THE SUBSTITUTION, FROM autojunk=False OPCODES:'] + ['  ' + l for l in diff]
    L += ['', '### ### **CARRIED tools/%s_%s.py ; LINES %d ; CHANGED BY THE SUBSTITUTION %d ; REPAIR SPANS AT %s %d ; THE SEAT READS THE SPANS, NOT THE WHOLE.**' % (
        ACT, name, len(nl_), changed, PREV, len(spans))]
    p = os.path.join(D, '%s_carry_%s.txt' % (ACT, name))
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(NL.join(L[:6] + L[-1:]))


def prune(name, start, end, *a):
    """`prune <name> <start prefix> <end prefix>`: the lines of tools/b709_<name>.py from the one line starting with <start prefix> up to (not
    including) the one line starting with <end prefix> removed -- the previous act's routes over its own objects, not carried -- the removal
    banked as a hunk in data/b709_prune_<name>.txt (appended); a prefix that matches no line or more than one refuses."""
    dst = os.path.join(T, '%s_%s.py' % (ACT, name))
    L = rd(dst).split(NL)
    si = [i for i, l in enumerate(L) if l.startswith(start)]
    ei = [i for i, l in enumerate(L) if l.startswith(end)]
    if len(si) != 1 or len(ei) != 1 or ei[0] <= si[0]:
        sys.exit('### THE PRUNE MARKERS DO NOT NAME ONE SPAN (start %s, end %s) -- NOTHING WRITTEN' % (si, ei))
    s, e = si[0], ei[0]
    new = L[:s] + L[e:]
    with open(dst + '.tmp', 'wb') as fh:
        fh.write(NL.join(new).encode('utf-8'))
    os.replace(dst + '.tmp', dst)
    hunk = ['@@ -%d,%d +%d,0 @@ PRUNED (%s)' % (s + 1, e - s, s + 1, utc())] + ['-' + l for l in L[s:e]]
    p = os.path.join(D, '%s_prune_%s.txt' % (ACT, name))
    prev = rd(p)
    head = '' if prev else ('%s -- THE PRUNES OF THE CARRIED tools/%s_%s.py: the previous act`s routes over its own objects, removed at carry time (data/b709_rules.txt row (1)); rows are hunks.' % (ACT, ACT, name) + NL + NL)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((prev + head + NL.join(hunk) + NL + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print('  pruned tools/%s_%s.py :%d-:%d (%d lines, %r .. %r) ; banked in data/%s_prune_%s.txt' % (ACT, name, s + 1, e, e - s, start[:40], end[:40], ACT, name))


def repairdiff(name, *a):
    """`repairdiff <name>`: the carry-time repairs of tools/b709_<name>.py as a diff -- the substituted form of the previous act's tool (the carry)
    against the file as it stands now (after the prunes and the Edit tool's repairs); a pruned span printed as its hunk header with its line
    count, every other change in full; written to data/b709_repairdiff_<name>.txt."""
    old = substitute(rd(os.path.join(T, '%s_%s.py' % (PREV, name)))).split(NL)
    new = rd(os.path.join(T, '%s_%s.py' % (ACT, name))).split(NL)
    sm = difflib.SequenceMatcher(None, old, new, autojunk=False)
    L = ['%s -- THE CARRY-TIME REPAIRS OF tools/%s_%s.py AS A DIFF: the carried form (tools/%s_%s.py with the act names substituted) against the file now (%s)' % (ACT, ACT, name, PREV, name, utc()), '',
         '--- tools/%s_%s.py (the carried form)' % (ACT, name), '+++ tools/%s_%s.py (now)' % (ACT, name)]
    n_del, n_ins, n_hunks = 0, 0, 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        n_hunks += 1
        L.append('@@ -%d,%d +%d,%d @@' % (i1 + 1, i2 - i1, j1 + 1, j2 - j1))
        if tag == 'delete' and i2 - i1 > 12:
            L.append('-  ### %d lines pruned (data/%s_prune_%s.txt), the first: %s' % (i2 - i1, ACT, name, old[i1][:100]))
            n_del += i2 - i1
            continue
        for l in old[i1:i2]:
            L.append('-' + l)
        for l in new[j1:j2]:
            L.append('+' + l)
        n_del += i2 - i1
        n_ins += j2 - j1
    L += ['', '### ### **HUNKS %d ; LINES REMOVED %d ; LINES ADDED %d.**' % (n_hunks, n_del, n_ins)]
    p = os.path.join(D, '%s_repairdiff_%s.txt' % (ACT, name))
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(NL.join(L[-1:]))


def spans(*a):
    names = [f[len(ACT) + 1:-3] for f in sorted(os.listdir(T)) if f.startswith(ACT + '_') and f.endswith('.py') and os.path.exists(os.path.join(D, '%s_carry_%s.txt' % (ACT, f[len(ACT) + 1:-3])))]
    L = ['%s -- THE CARRIED TOOLS AND THEIR READ SPANS (N3; data/b709_rules.txt row (1)) (%s)' % (ACT, utc()), '',
         '### rows are carried tools: the tool | the spans the previous act`s tool-repairs bank names (hunk headers) | the substitution`s hunks (count) | the bank.']
    tot = 0
    for n in names:
        sp = repair_spans(n)
        bank = rd(os.path.join(D, '%s_carry_%s.txt' % (ACT, n)))
        hunks = sum(1 for l in bank.split(NL) if l.strip().startswith('@@'))
        tot += len(sp)
        L.append('  tools/%s_%s.py | repair spans %s | substitution hunks %d | data/%s_carry_%s.txt' % (ACT, n, [s[2] for s in sp] or 'NONE', hunks, ACT, n))
    L += ['', '### ### **CARRIED TOOLS %d ; REPAIR SPANS %d ; EACH CARRIED BY THE SUBSTITUTION AND BANKED BY ITS DIFF ; THE READS AS THE READ BANK AND THE DEFECTS BANK RECORD THEM (data/b709_read_calls.txt ; data/b709_defects.txt (b), (e)).**' % (len(names), tot)]
    p = os.path.join(D, '%s_carry_spans.txt' % ACT)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(NL.join(L))


if __name__ == '__main__':
    fn = {'carry': carry, 'spans': spans, 'prune': prune, 'repairdiff': repairdiff}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b709_carry.py carry <name> [again] | prune <name> <start prefix> <end prefix> | repairdiff <name> | spans')
        sys.exit(2)
    fn(*sys.argv[2:])
