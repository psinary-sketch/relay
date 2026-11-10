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
    ol, nl_ = old.split(NL), new.split(NL)
    diff = udiff(ol, nl_, src_rel, dst_rel)
    changed = sum(1 for l in diff if l.startswith('+') and not l.startswith('+++'))
    L = ['%s -- THE CARRY BY DIFF (tools/standing/carry.py): %s -> %s (%s)' % (act, src_rel, dst_rel, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### the substitution alone (%s); %d lines, %d changed' % (', '.join('%s -> %s' % s for s in subs), len(nl_), changed),
         '### SHIFTED PAST WHAT EXISTS: %s' % ('; '.join(':%d %s' % s for s in shifted) if shifted else 'NONE'), '',
         '### THE DIFF OF THE SUBSTITUTION, FROM autojunk=False OPCODES:'] + ['  ' + l for l in diff]
    L += ['', '### ### **CARRIED %s ; LINES %d ; CHANGED %d ; SHIFTED %d%s**' % (dst_rel, len(nl_), changed, len(shifted),
                                                                          ' (WRITTEN BY --shifted)' if shifted else '')]
    p = os.path.join(D, '%s_carry_%s.txt' % (act, name))
    import act_membrane as MEM
    MEM.guard_path(act, p, None)
    for path, body in ((dst, new), (p, NL.join(L) + NL)):
        with open(path + '.tmp', 'wb') as fh:
            fh.write(body.encode('utf-8'))
        os.replace(path + '.tmp', path)
    print(NL.join(L[:4] + L[-1:]))


def check(src_rel, dst_rel):
    shifted = RP.shifted_missing(rd(_path(src_rel)), rd(_path(dst_rel)), T)
    for s in shifted:
        print('  :%d %s' % s)
    print('### SHIFTED PAST WHAT EXISTS: %d' % len(shifted))
    return 1 if shifted else 0


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
    n = 0
    for key, s, e in AM.blocks(act_text):
        if key not in pb or not same(act_text[s:e], substitute(pb[key], subs)):
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
        if key[:2] != ('SECTION', 'citation') or key not in pb or not same(act_text[s:e], substitute(pb[key], subs)):
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
        if key not in pb or not same(body, substitute(pb[key], subs)):
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
        for ln_, who, word in ordinal_mentions(act_text):
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
