# -*- coding: utf-8 -*-
"""tools/standing/carry.py -- THE CARRY BY DIFF as a standing route (v1.4.0, (R334)(2)(ix)): a tool or sections file carried from the
previous act by the act names' substitution alone, its diff banked, and THE SUBSTITUTION REFUSED WHERE IT SHIFTS A NAME PAST WHAT EXISTS --
a module or tool the carried text names that tools/ lacks, where the source line named one that exists (b721 (p), b723 (d), b724 (d):
tools/b724_address_scan.py's `import b723_llm_line`, carried from b722_llm_line, which no act wrote). The refusal is before the write.

### carry.py <src_rel> <dst_rel> <name> --subs a:b,c:d,... [--shifted] [--again]
###   the pairs applied in the order given (descending, so each name shifts once); the diff banked in data/<act>_carry_<name>.txt, <act> the
###   destination's act (the second name of the first pair); `--shifted` writes a refused carry, the shifted names printed in its bank
### carry.py check <src_rel> <dst_rel>
###   a print only: the shifted names between two files already written; exit 1 where there are any
### carry.py ruled <act> <prev> <ferry bank>
###   v1.27.0, (R357)(3)(viii): every carried figure and section printed beside the ruling; R1-R3 refused (exit 13), before the citation check
###   v1.29.0, (R359)(3)(v): R4, a citation section carried unchanged naming a commit the ruling does not name, each of its rows printed
###   v1.30.0, (R360)(3)(x): R5, a row of a carried citation section or of the carried c1 route citing a bank the ruling does not name
###   v1.31.0, (R361)(3)(vii), (viii): every carried row printed with its banks beside the ruling; R6, the ferry not banked by the citation
###   route (data/<act>_ferry_scan.txt absent); the one-call tool's usage, phases and word form printed at the foot
### carry.py shared <act> <entering relay head>
###   v1.30.0, (R360)(3)(x): act_current's shared_edits from this act's own commits (standing.act.shared_edits), never carried
### carry.py kept <act>
###   v1.29.0, (R359)(3)(v): the step-zero bank's "KEPT as banked:" row, written from the branch listing of the relay, PLACE-papers and
###   SIDE-explicit-formula (every branch but main and the act's own push branches, by name and tip)
"""
import difflib
import io
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
NL = chr(10)
if T not in sys.path:
    sys.path.insert(0, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import standing.repeat as RP  # noqa: E402


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


# ### v1.13.0, (R343)(2)(vii): a kept branch is a name the act does not move: b730 (m), b731 (b), b732 (c), each the shift of zq-b730 by one act. push-bNNN alone is the act's and shifts
KEPT_BRANCH = re.compile(r'(?<![\w-])(?:zq|detect|keiper|c2|rebuild|port|scratch|pin|recut|challenge|corrigendum)-b[0-9]{3}(?![0-9])')


def substitute(text, subs):
    """the pairs applied in order, every kept branch's name held out of them."""
    held = []

    def hold(m):
        held.append(m.group(0))
        return '\0%d\0' % (len(held) - 1)
    out = KEPT_BRANCH.sub(hold, text)
    for a, b in subs:
        out = out.replace(a, b)
    return re.sub('\0([0-9]+)\0', lambda m: held[int(m.group(1))], out)


def udiff(old, new, a_name, b_name):
    sm = difflib.SequenceMatcher(None, old, new, autojunk=False)
    L = ['--- ' + a_name, '+++ ' + b_name]
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        L.append('@@ -%d,%d +%d,%d @@' % (i1 + 1, i2 - i1, j1 + 1, j2 - j1))
        L += ['-' + l for l in old[i1:i2]] + ['+' + l for l in new[j1:j2]]
    return L


def _path(rel):
    return rel if os.path.isabs(rel) else os.path.join(ROOT, *rel.split('/'))


def carry(src_rel, dst_rel, name, subs, shifted_ok=False, again=False):
    old = rd(_path(src_rel))
    if not old:
        sys.exit('### %s IS NOT THERE -- NOTHING CARRIED' % src_rel)
    dst = _path(dst_rel)
    if os.path.exists(dst) and not again:
        sys.exit('### %s EXISTS -- NOTHING WRITTEN (give --again to rewrite the carried form)' % dst_rel)
    new = substitute(old, subs)
    shifted = RP.shifted_missing(old, new, T)
    if shifted and not shifted_ok:
        sys.exit(NL.join(['### THE SUBSTITUTION SHIFTS %d NAME(S) PAST WHAT EXISTS -- NOTHING WRITTEN ((R334)(2)(ix)):' % len(shifted)]
                         + ['  :%d %s (tools/%s.py absent; the source line named a module that exists)' % (i, n, n) for i, n in shifted]
                         + ['### repair the carried form by hand after `--shifted`, or carry the name unshifted']))
    act = subs[0][1]
    absent = shifted_absent(old, new, act, lambda p_: os.path.exists(_path(p_)))   # ### v1.35.1, (R366)(6), b755 (n)
    ol, nl_ = old.split(NL), new.split(NL)
    diff = udiff(ol, nl_, src_rel, dst_rel)
    changed = sum(1 for l in diff if l.startswith('+') and not l.startswith('+++'))
    L = ['%s -- THE CARRY BY DIFF (tools/standing/carry.py): %s -> %s (%s)' % (act, src_rel, dst_rel, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### the substitution alone (%s); %d lines, %d changed' % (', '.join('%s -> %s' % s for s in subs), len(nl_), changed),
         '### SHIFTED PAST WHAT EXISTS: %s' % ('; '.join(':%d %s' % s for s in shifted) if shifted else 'NONE'), '']
    L += absent_lines(absent) + ['', '### THE DIFF OF THE SUBSTITUTION, FROM autojunk=False OPCODES:'] + ['  ' + l for l in diff]
    L += ['', '### ### **CARRIED %s ; LINES %d ; CHANGED %d ; SHIFTED %d%s ; CITES OF AN ABSENT BANK %d**' % (
        dst_rel, len(nl_), changed, len(shifted), ' (WRITTEN BY --shifted)' if shifted else '', len(absent))]
    p = os.path.join(D, '%s_carry_%s.txt' % (act, name))
    import act_membrane as MEM
    MEM.guard_path(act, p, None)
    for path, body in ((dst, new), (p, NL.join(L) + NL)):
        with open(path + '.tmp', 'wb') as fh:
            fh.write(body.encode('utf-8'))
        os.replace(path + '.tmp', path)
    print(NL.join(L[:4] + absent_lines(absent) + L[-1:]))


def check(src_rel, dst_rel):
    shifted = RP.shifted_missing(rd(_path(src_rel)), rd(_path(dst_rel)), T)
    for s in shifted:
        print('  :%d %s' % s)
    print('### SHIFTED PAST WHAT EXISTS: %d' % len(shifted))
    m = re.search(r'b\d{3}', os.path.basename(dst_rel))
    if m:
        print(NL.join(absent_lines(shifted_absent(rd(_path(src_rel)), rd(_path(dst_rel)), m.group(0), lambda p_: os.path.exists(_path(p_))))))
    return 1 if shifted else 0


# ================================================================================ v1.35.1, (R366)(6): b755 (n), 19 acts by data/b756_faults.txt
# ### the carry shifts every cited act's name with the act's own, so a carried row citing an earlier act's bank comes to cite one act later:
# ### b755's closing line read "b754`s [P1] (relay data/b754_attribution_plan.txt)", a bank no act wrote, the plan passed at b752; and a row
# ### so shifted was read against its new act only when a probe or a reader reached it. Each such cite is printed at the carry, before any
# ### write of the act: a print and not a refusal, for a module cites absent banks by design (b756's check that b755 kept no post-seal bank).
def shifted_absent(src, dst, act, exists):
    """[(line, the carried cite, the source line's cites)]: on a line the substitution changed, a bank of an act before `act` that the carried
    text cites and the tree lacks. The act's own banks, still to be written, are not read."""
    out, pair = [], {}
    n = int(act[1:])
    sl, dl = (src or '').split(NL), (dst or '').split(NL)
    # ### the lines paired by the diff's opcodes and not by position: the module's carry stubs blocks, so its line counts move
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, sl, dl, autojunk=False).get_opcodes():
        if tag != 'equal':
            for k in range(j1, j2):
                pair[k] = sl[i1 + k - j1] if tag == 'replace' and i1 + k - j1 < i2 else ''
    for k in sorted(pair):
        for m in DATAP.finditer(dl[k]):
            p = m.group(0)
            if int(p[6:9]) < n and not exists(p):
                out.append((k + 1, p, sorted(set(DATAP.findall(pair[k])))))
    return out


def absent_lines(absent):
    return (['### CITES SHIFTED TO A BANK ABSENT FROM THE TREE (v1.35.1, b755 (n)), each read against the act before any write: %d' % len(absent)]
            + ['  :%d %s (the source line cited %s)' % (i, p, ', '.join(s) or 'none') for i, p, s in absent])


# ================================================================================ v1.27.0, (R357)(3)(viii): THE CARRY BESIDE THE RULING
# ### b746 defects (d) and (o): the carried worklist held b745's figures (PRE_PP at 5937961, b745's start) and checks sections 25-26 kept
# ### b745's six-dispatch form (a dispatch row, a read by run id) where (R356) ordered none. Here every carried figure and section is printed
# ### beside the ruling, and two kinds are REFUSED before the citation check:
# ###   R1 a worklist figure carried unchanged that names the previous act's own start (its PRE_PP or PRE_RELAY), the ruling not naming it
# ###   R2 a section carried unchanged (equal to the previous act's after the substitution) that reads a figure the ruling sets (RULED) whose
# ###      value moved between the two worklists, or that R3 refused: the section's form was written for the previous ruling's figure
# ###   R3 a ruled figure carried unchanged and non-empty with an element the ruling does not name
RULED = ('MAX_DISPATCHES', 'EF_RUNS')
HEXV = re.compile(r'\b(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}\b')
HEXC = re.compile(r'(?<![\w-])(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}(?![\w-])')   # ### v1.29.0 R4: a commit, not a branch name's tail (pin-b718-de5ce8a9)
KNAME = re.compile(r'\b(?:K|WL)\.([A-Z_][A-Z0-9_]*)\b')
DATAP = re.compile(r'\bdata/b\d{3}_[\w.\-]+?\.(?:txt|json)\b')   # ### v1.30.0 R5: a bank an act wrote, cited by a carried row
RNUM = re.compile(r'\bR\d{3}\b')


def same(a, b):
    """v1.30.0, (R360)(3)(x), b750 step-zero (d): a section carried unchanged reads equal with the ruling numbers set aside. The carry shifts
    the ruling's number with the act's (b750's table: R359 -> R360, R358 -> R359), and v1.29.0 compared after the act names alone, so every
    carried section read as written anew and b750's ruled printed REFUSED 0 over b749's citation sections and c1 route."""
    return RNUM.sub('R###', a) == RNUM.sub('R###', b)


def literals(text):
    """{name: value} for every top-level assignment of a literal in a worklist's text (ast; a non-literal skipped)."""
    import ast
    out = {}
    for node in ast.parse(text).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                out[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, SyntaxError, TypeError):
                pass
    return out


def _empty(v):
    return v is None or v == 0 or v == '' or (isinstance(v, (tuple, list, dict, set)) and not v)


ACT_LINE = re.compile(r'(?m)^ACT (b\d{3}) - LANE [A-Z]+, ACT ONE HUNDRED AND ([A-Z][A-Z-]*)')
ORDINAL = re.compile(r'\b(b\d{3})\b[^\n\'"]{0,80}?\b[Aa][Cc][Tt] [Oo][Nn][Ee] [Hh][Uu][Nn][Dd][Rr][Ee][Dd] [Aa][Nn][Dd] ([A-Za-z][A-Za-z-]*)')
NEEDLE_PATH = re.compile(r'(?:data|tools)/[\w.\-/]+\.(?:txt|json|py|md)|phase[\w.\-/]+\.md|day1/[\w.\-]+\.md|[A-Z][A-Z_]+\.md')


def act_name_of(ruling_text):
    m = ACT_LINE.search(ruling_text or '')
    return m.group(1) if m else None


def ordinal_of(ruling_text):
    """(act, ORDINAL) from a ferry's ACT line ("ACT b752 - LANE TWO, ACT ONE HUNDRED AND SEVENTY-NINE, ..."), or None."""
    m = ACT_LINE.search(ruling_text or '')
    return (m.group(1), m.group(2)) if m else None


def ordinal_mentions(text):
    """[(line, act, ordinal word)] for every "act one hundred and <n>" standing after an act's name on one line."""
    out = []
    for i, l in enumerate(text.split(NL), 1):
        for m in ORDINAL.finditer(l):
            out.append((i, m.group(1), m.group(2)))
    return out


def readfirst_needles(text):
    """the READFIRST_NEEDLES tuple, read by parsing its assignment line by line until it closes (a comment after it read as one)."""
    import ast
    ls = text.split(NL)
    i = next((k for k, l in enumerate(ls) if l.startswith('READFIRST_NEEDLES = ')), None)
    if i is None:
        return None
    for j in range(i + 1, min(i + 80, len(ls)) + 1):
        try:
            node = ast.parse(NL.join(ls[i:j])).body[0]
        except SyntaxError:
            continue
        try:
            return list(ast.literal_eval(node.value))
        except ValueError:
            return None
    return None


def ruled(act_text, prev_text, wl_text, prev_wl_text, ruling_text, subs, ferry_routed=None, ordinals=None, own_rows=None):
    """pure: (lines, refused) -- every carried figure and section printed beside the ruling; R1 and R2 refused."""
    import actmodule as AM
    W, P = literals(wl_text), literals(prev_wl_text)
    starts = [str(P.get(k) or '')[:7] for k in ('PRE_PP', 'PRE_RELAY') if P.get(k)]
    rl = ruling_text.replace('\r', '').split(NL)

    def named(tok):
        return next((i for i, l in enumerate(rl, 1) if tok in l), None)
    L, refused = ['## THE CARRIED FIGURES (worklist constants equal to the previous act`s after the substitution, non-empty), each beside the ruling'], []
    for k in sorted(set(W) & set(P)):
        v, pv = W[k], P[k]
        if _empty(v) or repr(v) != substitute(repr(pv), subs):
            continue
        hx = HEXV.findall(repr(v))
        at = [named(h[:7]) for h in hx]
        bad = [h for h in hx if h[:7] in starts and not named(h[:7])]
        L.append('  %-28s %-60s %s%s' % (k, repr(v)[:60], ('hex %s ; ' % ', '.join('%s %s' % (h[:8], (':%d' % a) if a else 'NOT NAMED') for h, a in zip(hx, at))) if hx else '',
                                         '### REFUSED (R1): names the previous act`s start %s' % ', '.join(bad) if bad else 'carried'))
        if bad:
            refused.append(('R1', k, 'the previous act`s start %s carried as this act`s figure, the ruling not naming it' % ', '.join(bad)))
    # ### R3: a ruled figure carried unchanged and non-empty, an element the ruling does not name: the previous ruling's figure as this act's
    for k in RULED:
        if k in W and k in P and not _empty(W[k]) and repr(W[k]) == repr(P[k]):
            el = list(W[k]) if isinstance(W[k], (tuple, list)) else [W[k]]
            un = [x for x in el if not named(str(x))]
            L.append('  %-28s %-60s %s' % (k, repr(W[k])[:60], ('### REFUSED (R3): a ruled figure carried unchanged, not named in the ruling: %s' % ', '.join(map(str, un))) if un else 'named in the ruling'))
            if un:
                refused.append(('R3', k, 'the previous act`s ruled figure carried unchanged, %d element(s) the ruling does not name' % len(un)))
    moved = [k for k in RULED if k in W and k in P and repr(W[k]) != repr(P[k])] + [r[1] for r in refused if r[0] == 'R3']
    L += ['', '## THE CARRIED SECTIONS (equal to the previous act`s after the substitution); the ruled figures %s, moved: %s' % (
        ', '.join('%s %r -> %r' % (k, P.get(k), W.get(k)) for k in RULED), ', '.join(moved) or 'NONE')]
    pb = dict((key, prev_text[s:e]) for key, s, e in AM.blocks(prev_text))

    def carried_(key, body):
        # ### v1.34.0, (R364)(3)(ii): carried by either substitution -- v1.33.0's over the whole text, or v1.34.0's over code alone
        return key in pb and (same(body, substitute(pb[key], subs)) or same(body, substitute_code(pb[key], subs)))
    n = 0
    for key, s, e in AM.blocks(act_text):
        if not carried_(key, act_text[s:e]):
            continue
        n += 1
        reads = sorted(set(KNAME.findall(act_text[s:e])) & set(moved))
        if reads:
            L.append('  %s ### REFUSED (R2): carried unchanged, reads %s, a ruled figure that moved' % (' '.join(map(str, key)), ', '.join(reads)))
            refused.append(('R2', ' '.join(map(str, key)), 'carried unchanged and reads %s, moved %s' % (
                ', '.join(reads), '; '.join('%r -> %r' % (P[r], W[r]) for r in reads))))
    L.append('  carried sections %d ; refused %d' % (n, sum(1 for r in refused if r[0] == 'R2')))
    # ### v1.29.0, (R359)(3)(v), b748 defect (c): R4, every row of a citation section carried unchanged printed beside the ruling: a
    # ### citation row carries the ferry's figures, so a carried row naming a commit the ruling does not name is the previous act's row
    # ### under this act's name (b748's sections 1 and 4 held b747's and b746's rows: b746's closing head 3f5a33bb, C1_STANDING f4c286c0)
    L += ['', '## THE CARRIED CITATION ROWS (a citation section equal to the previous act`s after the substitution), each commit beside the ruling']
    nr = 0
    for key, s, e in AM.blocks(act_text):
        if key[:2] != ('SECTION', 'citation') or not carried_(key, act_text[s:e]):
            continue
        rows_ = [l for l in act_text[s:e].split(NL) if l.strip().startswith('add(')]
        hx = sorted(set(HEXC.findall(act_text[s:e])), key=act_text[s:e].index)
        un = [h for h in hx if not named(h[:7])]
        nr += len(rows_)
        L.append('  %s: rows %d ; commits %s%s' % (' '.join(map(str, key)), len(rows_), ', '.join('%s %s' % (h[:8], (':%d' % named(h[:7])) if named(h[:7]) else 'NOT NAMED') for h in hx) or 'none',
                                                   ' ### REFUSED (R4): %d commit(s) the ruling does not name' % len(un) if un else ''))
        if un:
            refused.append(('R4', ' '.join(map(str, key)), 'a citation section carried unchanged naming %s, which the ruling does not name' % ', '.join(h[:8] for h in un)))
    L.append('  carried citation rows %d ; refused sections %d' % (nr, sum(1 for r in refused if r[0] == 'R4')))
    # ### v1.30.0, (R360)(3)(x), b749 defects (b), (d), (g), (k), b750 step-zero (d): R5, EVERY ROW THE CARRY BRINGS PRINTED BESIDE THE RULING AND
    # ### REFUSED WHERE THE RULING DOES NOT NAME IT. R4 reads commits alone, and a ruling names the previous act's commits (b750's names b749's),
    # ### so b749's sections 1 and 4 and its c1 route, carried under b750's names, passed it. Each row of a carried citation section, and each
    # ### line of the carried c1 route citing a bank, is read by the banks it cites: a bank the ruling does not name refuses the row.
    L += ['', '## THE CARRIED ROWS BY THEIR BANKS (a citation section or the c1 route equal to the previous act`s after the substitution), each bank beside the ruling']
    nr5 = 0
    for key, s, e in AM.blocks(act_text):
        body = act_text[s:e]
        if not carried_(key, body):
            continue
        if key[:2] == ('SECTION', 'citation'):
            rows_ = [l for l in body.split(NL) if l.strip().startswith('add(')]
        elif '_c1_' in body or 'def c1' in body:
            rows_ = [l for l in body.split(NL) if DATAP.search(l)]
        else:
            continue
        bad_rows, row_lines = [], []
        for l in rows_:
            nr5 += 1
            un = [p for p in sorted(set(DATAP.findall(l))) if not named(p)]
            if un:
                bad_rows.append((l.strip()[:70], un))
            # ### v1.31.0, (R361)(3)(vii): every row the carry brings printed beside the ruling, each bank it cites with the ruling's line or NOT NAMED
            row_lines.append('    %s | %s' % (l.strip()[:90], ', '.join('%s %s' % (p, (':%d' % named(p)) if named(p) else 'NOT NAMED') for p in sorted(set(DATAP.findall(l)))) or 'no bank'))
        L.append('  %s: rows %d ; rows citing a bank the ruling does not name %d%s' % (' '.join(map(str, key)), len(rows_), len(bad_rows),
                                                                                       (' ### REFUSED (R5): ' + ' | '.join('%s -> %s' % (r, ', '.join(u)) for r, u in bad_rows[:4])) if bad_rows else ''))
        L += row_lines
        if bad_rows:
            refused.append(('R5', ' '.join(map(str, key)), '%d carried row(s) citing banks the ruling does not name: %s' % (
                len(bad_rows), ', '.join(sorted(set(p for _r, u in bad_rows for p in u)))[:200])))
    L.append('  carried rows read by their banks %d ; refused sections %d' % (nr5, sum(1 for r in refused if r[0] == 'R5')))
    # ### v1.31.0, (R361)(3)(vii), b750 defect (s), REPEAT b749 (o): R6, the ferry banked by the citation tool's route (`fold.py citation ferry`,
    # ### which runs tools/ferry_scan.py and banks data/<act>_ferry_scan.txt) before the carry is read beside it; b750's ferry was banked by the
    # ### Write tool alone and the route found absent at Component 4. `ferry_routed` None: not read (a caller of v1.30.0's form).
    # ### v1.32.0, (R362)(7)(vi), b751 defects (b), (q), REPEAT: R7, THE ROWS R1-R6 DID NOT READ. Every act ordinal the module carries ("act one
    # ### hundred and <n>" after an act's name) beside the ordinal the ruling gives that act (this act's from the ruling's ACT line, the previous
    # ### act's from its own ferry): a different ordinal refused. Every read-first needle (READFIRST_NEEDLES) beside the ruling: a needle naming a
    # ### path the ruling does not name refused. b751's module carried b750's needles and numbered its trail head and the prior act's "seventy-seven".
    if ordinals is not None:
        n7 = len([r for r in refused if r[0] == 'R7'])
        L += ['', '## THE ACT ORDINALS THE MODULE CARRIES, each beside the ruling`s (read from each act`s ferry: %s)' % (
            ', '.join('%s %s' % kv for kv in ordinals.items()) or 'NONE READ')]
        unreached = stubbed_lines(act_text)   # ### v1.34.0, (R364)(3)(ii): a stub's kept code is unreached and read by no reader here
        for ln_, who, word in ordinal_mentions(act_text):
            if ln_ in unreached:
                continue
            want = ordinals.get(who)
            ok_ = want is None or word.upper() == want.upper()
            L.append('  :%-6d %s act one hundred and %-16s %s' % (ln_, who, word, 'the ruling`s' if want and ok_ else ('not an act the ruling numbers' if want is None else
                                                                                                             '### REFUSED (R7): the ruling numbers %s %s' % (who, want))))
            if not ok_:
                refused.append(('R7', 'ordinal :%d' % ln_, '%s numbered %s, the ruling`s %s' % (who, word, want)))
        nds = readfirst_needles(act_text)
        L += ['', '## THE READ-FIRST NEEDLES (READFIRST_NEEDLES), each path beside the ruling: %s' % (
            'NONE IN THE MODULE' if nds is None else '%d read' % len(nds))]
        if nds is not None and not nds:
            refused.append(('R7', 'needles', 'READFIRST_NEEDLES stands and none was read from it: a check that cannot fire'))
        for nd in nds or []:
            ps = NEEDLE_PATH.findall(nd)
            un = [p for p in ps if not named(p) and not named(os.path.splitext(os.path.basename(p))[0]) and p not in (own_rows or '')]
            L.append('  %-70s %s' % (nd[:70], ('### REFUSED (R7): not named in the ruling: ' + ', '.join(un)) if un else
                                     ', '.join('%s %s' % (p, (lambda k: ':%d' % k if k else 'the act`s own read-first row')(
                                         named(p) or named(os.path.splitext(os.path.basename(p))[0]))) for p in ps) or 'no path'))
            if un:
                refused.append(('R7', 'needle %s' % nd[:40], 'a read-first needle naming %s, which the ruling does not name' % ', '.join(un)))
        L.append('  ordinals and needles refused %d' % (len([r for r in refused if r[0] == 'R7']) - n7))
    wv = writes_without_version(ruling_text)
    L += ['', '## THE LISTS OF WRITES IN THE RULING NAMING A STANDING PATH WITHOUT VERSION (v1.34.0, (R364)(3)(vi)), printed before the citation '
              'check: %d' % len(wv)] + ['  :%-5d %s ; %s' % (ln_, ', '.join(ps_), ex_) for ln_, ps_, ex_ in wv]
    st = [(':%d' % i, l) for i, l in stubs_in(act_text)] + [('worklist :%d' % i, l) for i, l in stubs_in(wl_text)]
    L += ['', '## THE CARRIED STUBS (v1.34.0, (R364)(3)(ii)): %d, each refusing itself when used until written for the act; none refused here' % len(st)]
    L += ['  %-14s %s' % x for x in st]
    if ferry_routed is not None:
        L += ['', '## THE FERRY`S ROUTE: data/<act>_ferry_scan.txt %s' % ('PRESENT, the ferry banked by the citation route' if ferry_routed else
                                                                           'ABSENT ### REFUSED (R6): the ferry not banked by the citation route (`fold.py citation ferry --act <act>`)')]
        if not ferry_routed:
            refused.append(('R6', 'ferry', 'the ferry not banked by the citation tool`s route: data/<act>_ferry_scan.txt absent'))
    L += ['', '### ### **THE CARRY BESIDE THE RULING: REFUSED %d (R1 %d, R2 %d, R3 %d, R4 %d, R5 %d, R6 %d, R7 %d)%s.**' % (
        len(refused), sum(1 for r in refused if r[0] == 'R1'), sum(1 for r in refused if r[0] == 'R2'), sum(1 for r in refused if r[0] == 'R3'),
        sum(1 for r in refused if r[0] == 'R4'), sum(1 for r in refused if r[0] == 'R5'), sum(1 for r in refused if r[0] == 'R6'),
        sum(1 for r in refused if r[0] == 'R7'),
        ' -- ' + '; '.join('%s %s' % r[:2] for r in refused) if refused else ' ; NONE REFUSED')]
    return L, refused


# ================================================================================ v1.34.0, (R364)(3)(ii): THE CARRY'S STUBS
# ### b751 (b), b752 (b), b753 (b) with (t') and (y'): the carry copied the previous act's module under the new act's name and the seat
# ### rewrote what `ruled` refused (b754's first run REFUSED 28: R4 1, R5 2, R7 25). The half that lands at v1.34.0: the carry empties every
# ### section that reads a ruling or an act's banks -- the citation sections, the record route of Component 1, the act ordinals, the read-first
# ### needles, the worklist's stage-one values, the needles of the probes -- to a stub that refuses itself when used, until written for the
# ### act; and it leaves a cite standing inside a comment or a docstring as it is (y'): the substitution reads code, and the file's own head
# ### (its module docstring or its leading comment block) alone among the comments. The other half, a standing template with a per-act spec
# ### in place of the carry, is the seat's price put at [U4].
STUB_TAG = 'CARRIED STUB (tools/standing/carry.py v1.34.0)'
STAGE_ONE = ('PRE_PP', 'PRE_RELAY', 'PRE_PP_REMOTE_AT_START', 'PRE_RELAY_REMOTE_AT_START', 'B718_RELAY_HEAD', 'B718_PP_HEAD', 'DATE', 'SESSION_ID',
             'SP', 'SESSIONS_AFTER', 'PREV_SESSION', 'PREV_ANCHOR', 'B711_ENTRY', 'B711_WEIGHT', 'B711_CORRIGENDUM', 'B711_TRAIL', 'B711_FACE',
             'MIRROR_ZIP', 'TRAIL_ORDERS', 'TRAIL_RESOLVED', 'TRAIL_RETIRED', 'SECTION_BANK', 'STANDING_VERSION', 'STANDING_VERSION_ENTERING',
             'LEAN_TREES', 'B714_CLOSING', 'B714_RECORD', 'B714_ROOT', 'B723_ROOT_BANKS', 'ACT_CURRENT_COMMIT', 'STEPZERO', 'STEPZERO_PREVBUILD',
             'STEPZERO_BANKS', 'C1_STANDING', 'C1_RELAY', 'C1_PP', 'WEIGHT_LINE', 'CORR_LINE', 'C2_PLAN_FIRST', 'C2_RELAY_ALL', 'C2_RELAY',
             'C1_DEFECTS', 'SITTING_ITEMS', 'C3_RELAY', 'C4_LINE', 'NEXT', 'NEXT_ACT', 'COMPUTE_BANKS', 'COMPARATIVE_BANKS')
# ### the worklist's stage one: the per-act figures b754's step zero set by its script (each constant replaced whole by its name)


class Carried(object):
    """a value the carry emptied: every use refuses, naming it; its repr alone answers (so a print of the worklist reads it)."""
    __slots__ = ('_w',)

    def __init__(self, what):
        object.__setattr__(self, '_w', what)

    def _refuse(self, *a, **k):
        raise SystemExit('### %s IS A %s: written for the act before use -- NOTHING COMPOSED' % (object.__getattribute__(self, '_w'), STUB_TAG))
    __getattr__ = __call__ = __iter__ = __len__ = __bool__ = __str__ = __getitem__ = __contains__ = _refuse
    __add__ = __radd__ = __mod__ = __rmod__ = __format__ = __int__ = __index__ = __float__ = _refuse
    __lt__ = __le__ = __gt__ = __ge__ = __eq__ = __ne__ = __fspath__ = _refuse
    __hash__ = object.__hash__

    def __repr__(self):
        return 'Carried(%r)' % object.__getattribute__(self, '_w')


def _docstring_at(text, i):
    """True where the triple-quoted string at i opens a line and follows a line ending ':' or no code at all (a docstring)."""
    ls = text.rfind(NL, 0, i) + 1
    if text[ls:i].strip(' \t').lstrip('rRuU'):
        return False
    j = ls - 1
    while j > 0:
        ps = text.rfind(NL, 0, j) + 1
        line = text[ps:j]
        code = _code_of_line(line).rstrip()
        if code:
            return code.endswith(':')
        j = ps - 1
    return True


def _code_of_line(line):
    """the line up to a comment's '#' outside a one-line string."""
    q, k = None, 0
    while k < len(line):
        c = line[k]
        if q:
            if c == '\\':
                k += 2
                continue
            if c == q:
                q = None
        elif c in '\'"':
            q = c
        elif c == '#':
            return line[:k]
        k += 1
    return line


def held_spans(text):
    """[(start, end, kind)]: every comment (from '#' outside a string to the line's end) and every docstring of a Python-like text. The scan
    reads strings by their quotes alone (an act module is fragments, not one parseable file)."""
    out, i, n = [], 0, len(text)
    while i < n:
        c = text[i]
        if c == '#':
            j = text.find(NL, i)
            j = n if j < 0 else j
            out.append((i, j, 'comment'))
            i = j
            continue
        if c in '\'"':
            q3 = text[i:i + 3]
            if q3 in ('"""', "'''"):
                j = i + 3
                while True:
                    k = text.find(q3, j)
                    if k < 0:
                        k = n
                        break
                    b, m = 0, k - 1
                    while m >= i + 3 and text[m] == '\\':
                        b, m = b + 1, m - 1
                    if b % 2 == 0:
                        break
                    j = k + 1
                e = min(k + 3, n)
                if _docstring_at(text, i):
                    out.append((i, e, 'docstring'))
                i = e
                continue
            j = i + 1
            while j < n and text[j] != c and text[j] != NL:
                j += 2 if text[j] == '\\' else 1
            i = j + 1
            continue
        i += 1
    return out


def head_end(text):
    """the end of the file's own head: its module docstring, or its leading comment block up to the first block marker or code line."""
    sp = held_spans(text)
    k = 0
    for s, e, kind in sp:
        if text[k:s].strip():
            break
        if kind == 'comment' and text[s:].startswith('#⟪'):
            break
        k = e
        if kind == 'docstring':
            break
    return k


def substitute_code(text, subs):
    """the act names' substitution over code alone: every comment and docstring held as it stands but the file's own head (y'); a kept
    branch's name held as substitute() holds it."""
    he = head_end(text)
    held = []

    def hold(s, e):
        held.append(text[s:e])
        return '\x01%d\x01' % (len(held) - 1)
    parts, k = [], 0
    for s, e, _kind in held_spans(text):
        if e <= he:
            continue
        s = max(s, he)
        parts += [text[k:s], hold(s, e)]
        k = e
    parts.append(text[k:])
    out = substitute(''.join(parts), subs)
    return re.sub('\x01([0-9]+)\x01', lambda m: held[int(m.group(1))], out)


def _blank_held(text):
    """the text with every comment and docstring blanked (for a needle that reads code alone)."""
    out, k = [], 0
    for s, e, _kind in held_spans(text):
        out += [text[k:s], re.sub(r'[^\n]', ' ', text[s:e])]
        k = e
    out.append(text[k:])
    return ''.join(out)


def _stub_msg(act, what):
    return '### %s`s %s IS A %s: written for the act before use -- NOTHING COMPOSED' % (act, what, STUB_TAG)


def _stub_names(code):
    """[(kind, name)] of the top-level statements of parseable code: a def or class, each assigned name; None where it does not parse."""
    import ast
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return None
    out = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out.append(('def', node.name))
        elif isinstance(node, ast.ClassDef):
            out.append(('name', node.name))
        elif isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            tg = node.targets if isinstance(node, ast.Assign) else [node.target]
            for t in tg:
                for x in ast.walk(t):
                    if isinstance(x, ast.Name) and ('name', x.id) not in out:
                        out.append(('name', x.id))
    return out


def stub_forms(body, act, what):
    """the stub bodies to try for a block's body, in order: the comment lines kept, the code replaced by a form that refuses when reached."""
    ls = body.split(NL)
    keep = [l for l in ls if l.lstrip().startswith('#')]
    code = [l for l in ls if l.strip() and not l.lstrip().startswith('#')]
    head = ['# ### %s: %s; the body carried, %d code lines, stands in the carry`s diff bank' % (STUB_TAG, what, len(code))]
    msg = _stub_msg(act, what)
    if not code:
        return [NL.join(head + keep) + NL]
    ind = code[0][:len(code[0]) - len(code[0].lstrip())]
    cont = ' \\' if code[-1].rstrip().endswith('\\') else ''
    thr = '(_ for _ in ()).throw(SystemExit(%r))' % msg
    forms = []
    if not ind:
        nm = _stub_names(NL.join(code))
        if nm is not None:
            st = []
            for kind, name in nm:
                st += (['def %s(*a, **k):' % name, '    raise SystemExit(%r)' % msg] if kind == 'def' else
                       ['%s = __import__(%r, fromlist=[%r]).Carried(%r)' % (name, 'standing.carry', 'Carried', '%s`s %s' % (act, name))])
            forms.append(NL.join(head + keep + (st or ['pass'])) + NL)
    first = code[0].lstrip()
    # ### an indented block may continue its template's expression (a backslash before it), where no comment line may stand: its stub is
    # ### one line, its tag inside the refusal's message, a trailing comment only where no continuation follows; the body's comments dropped
    tail = '' if cont else '   # ### %s: the body carried, %d code lines, stands in the carry`s diff bank' % (STUB_TAG, len(code))
    # ### the emptied forms first: the code replaced whole by a refusal
    if first.startswith('and ') or first.startswith('or '):
        forms.append('%s%s %s%s%s' % (ind, first.split(' ', 1)[0], thr, cont, tail) + NL)
    forms.append('%sraise SystemExit(%r)%s' % (ind, msg, tail) + NL)
    forms.append('%s%s,%s%s' % (ind, thr, cont, tail) + NL)
    # ### where no emptied form compiles (the block shares an expression with its template's lines), the refusal stands before the carried
    # ### code, kept behind it unreached; the refusal's message says so
    kmsg = msg.replace(': written for the act', ', ITS CODE KEPT BEHIND THIS REFUSAL, UNREACHED: written for the act')
    kthr = '(_ for _ in ()).throw(SystemExit(%r))' % kmsg
    body_kept = body if body.endswith(NL) else body + NL
    if first.startswith('and ') or first.startswith('or '):
        forms.append('%s%s %s \\' % (ind, first.split(' ', 1)[0], kthr) + NL + body_kept)
    forms.append('%sraise SystemExit(%r)' % (ind, kmsg) + NL + body_kept)
    forms.append('%s%s,' % (ind, kthr) + NL + body_kept)
    return forms


def _why_whole(key, marker, body):
    if key[0] == 'SECTION' and key[1] == 'citation':
        return 'a citation section (%s %s %s)' % key
    if ' REPAIR (c1)' in marker or re.search(r'(?m)^def c1\(', body):
        return 'the record route of Component 1 (%s)' % marker.strip('#⟪⟫ ')
    if ' REPAIR (needle)' in marker:
        return 'a probe`s needle (%s)' % marker.strip('#⟪⟫ ')
    return None


def _reads_ruling(code):
    return bool(ORDINAL.search(code)) or bool(re.search(r'(?m)^\s*READFIRST_NEEDLES\s*=', code))


def carry_module(old, subs, act):
    """(text, stubs): the previous act's module carried by the code substitution, each block that reads a ruling or an act's banks stubbed.
    A block is stubbed whole where it is a citation section, the c1 route or a probe's needle, or where its code (comments and docstrings
    blanked) carries an act ordinal or the read-first needles and is not a top-level block; in a top-level block the statements carrying
    them alone are stubbed. Each stub's form is the first that compiles in its tool's render (stub_check)."""
    import actmodule as AM
    text = substitute_code(old, subs)
    out, stubs, k = [], [], 0
    for key, s, e in AM.blocks(text):
        ml = text.find(NL, s) + 1
        marker = text[s:ml].rstrip(NL)
        body = text[ml:e - len('#⟪END⟫\n')]
        why = _why_whole(key, marker, body)
        code = _blank_held(body)
        new_body = None
        if why is None and _reads_ruling(code):
            cl = [l for l in body.split(NL) if l.strip() and not l.lstrip().startswith('#')]
            top = bool(cl) and not cl[0][:1].isspace() and _stub_names(NL.join(cl)) is not None
            if not top:
                why = 'a block reading an act ordinal or the read-first needles (%s)' % marker.strip('#⟪⟫ ')
            else:
                new_body, part = _stub_statements(body, act)
                if part:
                    stubs.append((key, marker, 'statements %s' % ', '.join(part), None))
        if why:
            stubs.append((key, marker, why, stub_forms(body, act, why)))
            new_body = stub_forms(body, act, why)[0]
        out += [text[k:ml], new_body if new_body is not None else body]
        k = ml + len(body)
    out.append(text[k:])
    return ''.join(out), stubs


def _stub_statements(body, act):
    """(body, names): a top-level block with each statement carrying an act ordinal or the read-first needles replaced by its stub."""
    import ast
    tree = ast.parse(body)
    ls = body.split(NL)
    repl, names = [], []
    for node in tree.body:
        seg = NL.join(ls[node.lineno - 1:node.end_lineno])
        if not _reads_ruling(_blank_held(seg)):
            continue
        nm = _stub_names(seg) or []
        msg = _stub_msg(act, 'statement %s' % ', '.join(n for _k, n in nm))
        st = ['# ### %s: statement %s; it carried an act ordinal or the read-first needles' % (STUB_TAG, ', '.join(n for _k, n in nm))]
        for kind, name in nm:
            st += (['def %s(*a, **k):' % name, '    raise SystemExit(%r)' % msg] if kind == 'def' else
                   ['%s = __import__(%r, fromlist=[%r]).Carried(%r)' % (name, 'standing.carry', 'Carried', '%s`s %s' % (act, name))])
            names.append(name)
        repl.append((node.lineno - 1, node.end_lineno, st))
    for a, b, st in sorted(repl, reverse=True):
        ls[a:b] = st
    return NL.join(ls), names


def stub_check(act, text, stubs, tools=None, nm=None):
    """{tool: 'COMPILES' or the error}: each tool rendered from the carried module and compiled; where a whole-stubbed block's first form
    fails, its later forms tried in order, the text returned with the forms that compile. Returns (text, results). `nm`: the template's
    four names ({'⟪ACT⟫': .., '⟪PREV⟫': .., '⟪RUL⟫': .., '⟪PRUL⟫': ..}) where data/act_current.json does not yet name the act (the carry
    runs before it is written)."""
    import fold as F
    if nm is not None:
        _names = F.names
        F.names = lambda a: dict(nm) if a == act else _names(a)
    try:
        return _stub_check(F, act, text, stubs, tools)
    finally:
        if nm is not None:
            F.names = _names


def _stub_check(F, act, text, stubs, tools):
    res = {}
    for tool in tools or F.TOOLS:
        for _round in range(60):
            secs, ovs = F._parse(act, text)
            try:
                src = F.render(act, tool, secs, ovs)
                compile(src, '<%s_%s carried>' % (act, tool), 'exec')
                res[tool] = 'COMPILES'
                break
            except SyntaxError as ex:
                res[tool] = 'SyntaxError line %s: %s' % (ex.lineno, ex.msg)
                bad = _block_at(src, ex.lineno, text, stubs)
                if bad is None:
                    break
                text = bad
            except F.FoldRefused as ex:
                res[tool] = 'FoldRefused: %s' % ex
                break
    return text, res


def _block_at(src, lineno, text, stubs):
    """the module text with the next form of the nearest stub standing at or before the rendered error line (its head comment found by
    scanning back at most 80 lines), or None where no stub stands there or its forms are spent."""
    ls = src.split(NL)
    for k in range(lineno - 1, max(-1, lineno - 81), -1):
        l = ls[k] if k < len(ls) else ''
        if STUB_TAG not in l:
            continue
        for i, (key, marker, why, forms) in enumerate(stubs):
            if forms and len(forms) > 1 and why in l and forms[0] in text:
                stubs[i] = (key, marker, why, forms[1:])
                return text.replace(forms[0], forms[1], 1)
        return None
    return None


def carry_worklist(old, subs, act):
    """(text, names): the previous act's worklist carried by the code substitution, each stage-one value (STAGE_ONE) bound to a Carried stub
    that refuses on use, its line's comment replaced by the stub's; a line `from standing.carry import Carried as _Carried` after the imports."""
    import ast
    text = substitute_code(old, subs)
    tree = ast.parse(text)
    ls = text.split(NL)
    repl, names = [], []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        tg = [x.id for t in node.targets for x in ast.walk(t) if isinstance(x, ast.Name)]
        if not tg or not all(t in STAGE_ONE for t in tg):
            continue
        lhs = ls[node.lineno - 1].split('=', 1)[0].rstrip()
        rhs = ', '.join('_Carried(%r)' % ('%s`s %s' % (act, t)) for t in tg)
        repl.append((node.lineno - 1, node.end_lineno, '%s = %s   # ### %s: the stage-one value, written for the act at step zero' % (lhs, rhs, STUB_TAG)))
        names += tg
    for a, b, l in sorted(repl, reverse=True):
        ls[a:b] = [l]
    imp = max([n.end_lineno for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))] or [0])
    shift = sum(1 - (b - a) for a, b, _l in repl if a < imp)
    ls.insert(imp + shift, 'from standing.carry import Carried as _Carried   # ### %s: the stage-one values below refuse on use until written' % STUB_TAG)
    return NL.join(ls), names


STANDING_PATH = re.compile(r'tools/standing/[\w./-]*\w')
WRITES_LIST = re.compile(r"\(W\)|\bWRITES\b|\bTHE WRITES\b")


def writes_without_version(ruling_text):
    """v1.34.0, (R364)(3)(vi), b753 events (7)-(9): [(line, standing paths, excerpt)] for every paragraph (a ruling's line) holding a list of writes
    -- a (W) list or a heading of WRITES -- that names a path under tools/standing/ and does not name tools/standing/VERSION or VERSION."""
    out = []
    for i, l in enumerate((ruling_text or '').replace('\r', '').split(NL), 1):
        if not WRITES_LIST.search(l):
            continue
        ps = sorted(set(p.rstrip('.') for p in STANDING_PATH.findall(l) if not p.rstrip('.').endswith('VERSION')))
        if ps and 'VERSION' not in l:
            k = l.find(ps[0])
            out.append((i, ps, l[max(0, k - 90):k + 60].replace(NL, ' ')))
    return out


STUB_WHAT = re.compile(r"### b\d{3}`s (.+?)(?:, ITS CODE KEPT BEHIND THIS REFUSAL, UNREACHED)? IS A " + re.escape(STUB_TAG) + r"|^\s*# ### " + re.escape(STUB_TAG) + r": (.+?);")


def stubs_in(text):
    """[(line, what)]: every stub the carry left, once each -- a module block's or statement's (its head comment or its refusal's message,
    the first line naming it), a worklist's stage-one value (its `_Carried(` line)."""
    out, seen = [], set()
    for i, l in enumerate((text or '').split(NL), 1):
        if '= _Carried(' in l and STUB_TAG in l:
            out.append((i, 'the stage-one value ' + l.split('=', 1)[0].strip()))
            continue
        m = STUB_WHAT.search(l)
        if m:
            w = m.group(1) or m.group(2)
            if w not in seen:
                seen.add(w)
                out.append((i, w[:150]))
    return out


def stubbed_lines(text):
    """the line numbers of every module block a stub stands in (its body read by no ordinal or needle reader: unreached code)."""
    import actmodule as AM
    out = set()
    for _key, s, e in AM.blocks(text):
        if STUB_TAG in text[s:e]:
            a = text.count(NL, 0, s) + 1
            out.update(range(a, a + text.count(NL, s, e) + 1))
    return out


def kept_repos():
    """the relay, PLACE-papers and every D:/SIDE-* repository on disk."""
    out = [('relay', ROOT), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers')]
    try:
        out += [(n, 'D:/' + n) for n in sorted(os.listdir('D:/')) if n.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', n, '.git'))]
    except OSError:
        pass
    return out


def kept_row(act, repos=None, lister=None):
    """v1.29.0, (R359)(3)(v), b748 defect (o): the step-zero bank's "KEPT as banked:" row written from the branch listing, after the deletes:
    every kept branch (KEPT_BRANCH's families: zq, detect, keiper, c2, rebuild, port, scratch, pin, recut, challenge, corrigendum) of each
    repository by name and tip, the repository named; the act's own push branches and main never in it; the other branches counted."""
    import subprocess

    def lst(repo):
        r = subprocess.run(['git', '-C', repo, 'branch', '--list', '--format=%(refname:short) %(objectname:short=8)'], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return [l.split() for l in r.stdout.split(NL) if len(l.split()) == 2]
    parts, other = [], 0
    for name, repo in (repos or kept_repos()):
        bs = (lister or lst)(repo)
        kept = [(b, t) for b, t in bs if KEPT_BRANCH.match(b) and not b.startswith('push-%s-' % act)]
        other += sum(1 for b, _t in bs if b != 'main' and not KEPT_BRANCH.match(b))
        if kept:
            parts.append('%s: %s' % (name, ', '.join('%s (%s)' % (b, t) for b, t in kept)))
    return 'KEPT as banked (the tool`s row, tools/standing/carry.py kept %s, from each repository`s branch listing): %s ; other branches, none of the kept families, %d' % (
        act, ' ; '.join(parts) or 'none', other)


def main(argv):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    if argv[:1] in (['kept'], ['shared'], ['check'], ['ruled']) and len(argv) > 1:
        __import__('act').act_name(argv[1], 'carry.py %s' % argv[0], __doc__)   # ### v1.32.0, (R362)(7)(vii), b751 (t)
    if argv[:1] == ['kept'] and len(argv) == 2:
        print(kept_row(argv[1]))
        return 0
    if argv[:1] == ['shared'] and len(argv) == 3:
        # ### v1.30.0, (R360)(3)(x), b749 defect (k): act_current's shared_edits from this act's own list, never the previous act's
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import act as A_
        se = A_.shared_edits(argv[1], argv[2])
        print('THE SHARED EDITS OF %s (git diff %s..HEAD over tools/, less tools/%s_*, tools/acts/, tools/standing/): %s' % (argv[1], argv[2][:8], argv[1], se or '[]'))
        return 0
    if argv[:1] == ['check'] and len(argv) == 3:
        return check(argv[1], argv[2])
    if argv[:1] == ['ruled'] and len(argv) == 4:
        # ### carry.py ruled <act> <prev> <ferry bank>: the act's module and worklist beside the previous act's, at the working tree
        a, p, fb = argv[1], argv[2], argv[3]
        texts = [rd(_path(x)) for x in ('tools/acts/%s.py' % a, 'tools/acts/%s.py' % p, 'tools/%s_worklist.py' % a, 'tools/%s_worklist.py' % p, fb)]
        for x, t in zip(('tools/acts/%s.py' % a, 'tools/acts/%s.py' % p, 'tools/%s_worklist.py' % a, 'tools/%s_worklist.py' % p, fb), texts):
            if not t:
                sys.exit('### REFUSED: %s resolves to no file' % x)
        pn, an = int(p[1:]), int(a[1:])
        subs = (('b%d' % pn, 'b%d' % an), ('b%d' % (pn - 1), 'b%d' % (an - 1)))
        # ### v1.32.0, (R362)(7)(vi): R7 reads each act's ordinal from its own ferry's ACT line
        ords = dict(x for x in (ordinal_of(texts[4]), ordinal_of(rd(_path('data/%s_ferry.txt' % p)))) if x)
        L, refused = ruled(texts[0], texts[1], texts[2], texts[3], texts[4], subs, ferry_routed=os.path.isfile(_path('data/%s_ferry.txt' % a).replace('_ferry.txt', '_ferry_scan.txt')),
                           ordinals=ords, own_rows=NL.join(json.loads(rd(_path('data/%s_readfirst_rows.json' % a)) or '{}').get('own') or []))   # ### the act's own read-first rows, once written
        print(NL.join(L))
        # ### v1.31.0, (R361)(3)(viii): the one-call tool's usage, phases and word form, printed before the seat's opening call
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import commit as CM
        print(NL.join([''] + CM.usage_lines()))
        return 13 if refused else 0
    if len(argv) < 5 or '--subs' not in argv:
        sys.exit(__doc__)
    i = argv.index('--subs')
    subs = tuple(tuple(x.split(':', 1)) for x in argv[i + 1].split(','))
    carry(argv[0], argv[1], argv[2], subs, '--shifted' in argv, '--again' in argv)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
