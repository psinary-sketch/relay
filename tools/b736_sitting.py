# -*- coding: utf-8 -*-
"""b736_sitting.py -- (R346)(4), AS THE AUTHOR AMENDED IT (data/b736_author_words.txt): THE SECOND SITTING over data/b732_phase2_frontdoors.txt.

  check            every README draft planned over the kernel's main in memory, every removal row found or printed; nothing written.
  show N           the one item as it is put: current words, drafted words, file, line, grade, what falls with it, the pin against main.
  pass N           the author's number passed: CURRENT read and compared; README.md alone, or the gh description, one commit; Zenodo banked only.
  strike N WORDS   the row in the sitting's bank with the author's words.
  follow           the rows of PART A take their draft's state, [19] struck unread.
  bank             rewrites data/b736_sitting.txt from data/b736_sitting.json.

One run writes at most one commit and no file but README.md on the kernel the item names. Controls before figures: `check`.
"""
import difflib
import json
import os
import re
import shutil
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
AGENDA = os.path.join(D, 'b732_phase2_frontdoors.txt')
DOORS = os.path.join(D, 'b732_phase2_doors.txt')
ROWS = os.path.join(D, 'b736_sitting.json')
TEXT = os.path.join(D, 'b736_sitting.txt')
BASES = os.path.join(D, 'b736_kernel_bases.json')
DIFFS = os.path.join(D, 'b736_sitting_diffs')
SKIP_CI = ('SIDE-cosmo', 'SIDE-effects', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-trivium')   # ### a workflow on push at main: the commit carries [skip ci] so that no runner is dispatched (N1)
STRUCK_UNREAD = {19: 'the author`s word: [19], the private kernel, is struck unread'}
LEAN = r'(?:noncomputable |private |protected )*(?:theorem|lemma|def|abbrev|structure|class|inductive|instance|axiom)\b'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def items():
    L = open(AGENDA, encoding='utf-8').read().split(NL)
    out, cur, part = {}, None, None
    for i, l in enumerate(L, 1):
        if l.startswith('## PART'):
            part = l[8:9]
        m = re.match(r'  \[(\d+)\] (.*)$', l)
        if m:
            cur = out.setdefault(int(m.group(1)), {'title': m.group(2), 'at': i, 'part': part})
            continue
        m = re.match(r'    (FILE|LINE|CURRENT|DRAFT|WHY):\s+(.*)$', l)
        if m and cur is not None:
            cur[m.group(1).lower()] = m.group(2)
    return out


def doors(kernel):
    """the rows of a kernel's section that fall with its paragraph: [(line, id, text, class)]; the private kernel's rows are never read here."""
    out, on = [], False
    for l in open(DOORS, encoding='utf-8').read().split(NL):
        if l.startswith('## '):
            on = l.startswith('## %s at ' % kernel)
            continue
        m = re.match(r'  (\d+)\.(\d+)\s+([A-Z-]+)\s+\| (.*)$', l) if on else None
        if not m:
            continue
        rest = m.group(4)
        if rest.endswith(' | SILENT'):
            out.append((int(m.group(1)), m.group(1) + '.' + m.group(2), rest[:-len(' | SILENT')], 'SILENT'))
        elif ' | LOAD-BEARING' in rest:
            out.append((int(m.group(1)), m.group(1) + '.' + m.group(2), rest.split(' | LOAD-BEARING')[0], 'LOAD-BEARING'))
    return out


def read(p):
    raw = open(p, 'rb').read()
    crlf = raw.count(b'\r\n') > 0
    t = raw.decode('utf-8')
    return (t.replace('\r\n', NL) if crlf else t), crlf


def write(p, t, crlf):
    b = (t.replace(NL, '\r\n') if crlf else t).encode('utf-8')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo, *a], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def gh(*a):
    r = subprocess.run(['gh', *a], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def flat(s):
    return ' '.join(s.split())


def layout(draft):
    """the draft's one line as prose, statement lines indented four, statement and path kept as the bank carries them; the words equal, the control below."""
    m = re.search(r'Statements at (\S+): ', draft)
    if not m:
        return draft
    pre, tail = draft[:m.end()].rstrip(), draft[m.end():]
    q, at = [], 0
    pat = re.compile(r'(%s.*?\(\S+\.lean :\d+\)) ?' % LEAN)
    while True:
        k = pat.match(tail, at)
        if not k:
            break
        q.append('    ' + k.group(1))
        at = k.end()
    post = tail[at:].strip()
    out = (NL + NL).join(x for x in (pre, NL.join(q), post) if x)
    if flat(out) != flat(draft):
        sys.exit('### THE LAYOUT MOVED THE WORDS -- NOTHING WRITTEN')
    return out


FALLS = {72: ('Each numerical fact it encodes is also proved in at least one sibling kernel.',),   # ### the author's words at the sitting: a line beside the rows
         78: ('This is the **first radial-trace kernel** in the federation.', 'Traces 1 and 6 remain corpus-side; Trace 4', 'Four substrate classes (A, B, C, D) with their specific arithmetic:'),
         80: ('It sits between the foundational', 'It comes with three rank classifications:', '`structuralRank` — count', '`splitRank` — count', '`continuousRank` — count', 'typed κ = 0 in `MetaKernel.lean`.', 'cited κ = 0 in published synthesis.'),
         82: ('No wildcard.',),
         92: ('Given:', 'This kernel proves:', '1. Sum of three weight-1 contributions = 14', '2. Sum of three weight-2 contributions = 16/3'),
         96: ('Contrast with the standard per-component model from SIDE-steane-arithmetic where d = 3 (Steane [[7, 1, 3]]).',)}
ABBR = ('e.g.', 'i.e.', 'cf.', 'vs.', 'etc.', 'al.', 'Thm.', 'Prop.', 'Lem.', 'Sec.', 'No.', 'Dr.', 'St.')
MARK = chr(0xE000)


def blocks(L):
    """the file's sentence-bearing blocks, each a list of line numbers (0-based): a blank, a list item, a head, a table row, a quote line or a fence opens a new one; a fence's insides and table rows carry no sentences."""
    out, cur, fence = [], [], False
    for i, l in enumerate(L):
        x = l.strip()
        if x.startswith('```'):
            fence = not fence
            cur = []
            continue
        if fence or not x or x.startswith(('#', '|')):
            cur = []
            continue
        if re.match(r'\s*(?:[-*+] |\d+\. |> ?)', l) or not cur:
            cur = [i]
            out.append(cur)
        else:
            cur.append(i)
    return out


def spread(L, fallen):
    """a row is a line's part of a sentence, and the sentence falls whole: any sentence of a block that a fallen character touches falls, and a list item falls whole with its first sentence."""
    for bl in blocks(L):
        where, chars = [], []
        for i in bl:
            for c, ch in enumerate(L[i]):
                where.append((i, c))
                chars.append(ch)
            where.append(None)
            chars.append(' ')
        t = ''.join(chars)
        cuts, at = [], 0
        for m in re.finditer(r'[.!?](?:\*\*|\*|`|\)|"|”)*(?=\s)', t):
            if any(t[:m.end()].endswith(x) for x in ABBR) or re.search(r'(?:^|[\s*])[A-Z]\.$', t[:m.end()]):
                continue
            cuts.append((at, m.end()))
            at = m.end()
        if at < len(t):
            cuts.append((at, len(t)))
        hit = [any(where[k] is not None and where[k][1] in fallen.get(where[k][0], ()) and not t[k].isspace() for k in range(u, v)) for u, v in cuts]
        if re.match(r'\s*(?:[-*+] |\d+\. )', L[bl[0]]) and hit and hit[0]:
            hit = [True] * len(hit)
        if re.fullmatch(r'\s*\*[^*].*[^*]\*\s*', t) and any(hit):   # ### a line in italics is one line: it does not stand in part
            hit = [True] * len(hit)
        for (u, v), h in zip(cuts, hit):
            if h:
                for k in range(u, v):
                    if where[k] is not None:
                        fallen.setdefault(where[k][0], set()).add(where[k][1])


def fences(L, fallen, rows):
    """a fence is not cut in part: a citation or a command fence stands, its row with it; a list of declarations loses its lines; any other fence with a fallen row falls whole."""
    i = 0
    while i < len(L):
        if not L[i].strip().startswith('```'):
            i += 1
            continue
        j = i + 1
        while j < len(L) and not L[j].strip().startswith('```'):
            j += 1
        body = [x for x in range(i + 1, min(j, len(L))) if L[x].strip()]
        if any(fallen.get(x) for x in body):
            if L[i].strip()[3:]:
                for x in body:
                    fallen.pop(x, None)
                    rows[:] = [r for r in rows if int(r[0].split('.')[0]) != x + 1]
            elif not all(re.match(LEAN, L[x].strip()) for x in body):
                for x in range(i, min(j + 1, len(L))):
                    fallen.setdefault(x, set()).update(range(len(L[x])))
        i = j + 1


def tables(t2):
    """a table whose every row fell falls with its head and rule."""
    K = t2.split(NL)
    out, i = [], 0
    while i < len(K):
        if i + 1 < len(K) and K[i].lstrip().startswith('|') and re.fullmatch(r'\s*\|[\s:|-]+\|?\s*', K[i + 1]) and not (i + 2 < len(K) and K[i + 2].lstrip().startswith('|')):
            i += 2
            continue
        out.append(K[i])
        i += 1
    return NL.join(out)


def heads(t2, text):
    """a head whose whole section fell falls with it; a head empty at main stands."""
    def empties(t):
        K = t.split(NL)
        e = []
        for i, l in enumerate(K):
            h = re.match(r'(#+) ', l)
            if not h:
                continue
            j = i + 1
            while j < len(K) and not K[j].strip():
                j += 1
            if j == len(K) or (re.match(r'(#+) ', K[j]) and len(re.match(r'(#+) ', K[j]).group(1)) <= len(h.group(1))):
                e.append(i)
        return e
    was = set(text.split(NL)[i] for i in empties(text))
    while True:
        K = t2.split(NL)
        gone = [i for i in empties(t2) if K[i] not in was]
        if not gone:
            return t2
        t2 = NL.join(l for i, l in enumerate(K) if i not in gone)


def plan(n, it, base=None):
    """(new text, the rows taken, the rows missed, crlf): in memory, nothing written; `base` a text to plan over in place of the working file, a repair's."""
    kernel = it['file'].split()[0]
    p = 'D:/%s/README.md' % kernel
    text, crlf = read(p)
    if base is not None:
        text = base
    L = text.split(NL)
    title = re.match(r':(\d+)\.(\d+)', it['line'])
    tl = int(title.group(1))
    if it['current'] not in L[tl - 1]:
        return None, [], [('title', it['current'])], crlf
    keep = 'graded SCOPE' in it.get('why', '')   # ### a SCOPE title row is the kernel's own banner, not a door: it stands and the paragraph follows it
    rows, miss, fallen = [], [], {}
    for ln, rid, t, cls in doors(kernel):
        if ln == tl and t in it['current']:
            continue
        if ln > len(L) or t not in L[ln - 1]:
            miss.append((rid, t))
            continue
        c = L[ln - 1].find(t)
        have = fallen.setdefault(ln - 1, set())
        while c >= 0 and c in have:
            c = L[ln - 1].find(t, c + 1)
        c = c if c >= 0 else L[ln - 1].find(t)
        have.update(range(c, c + len(t)))
        rows.append((rid, cls, t))
    for t in FALLS.get(n, ()):
        at = [i for i, l in enumerate(L) if t in l]
        if len(at) != 1:
            sys.exit('### THE AUTHOR`S LINE DOES NOT MEET THE FILE ONCE -- NOTHING WRITTEN')
        c = L[at[0]].find(t)
        fallen.setdefault(at[0], set()).update(range(c, c + len(t)))
    head = L[tl - 1].find(it['current'])
    if not keep:
        fallen.setdefault(tl - 1, set()).update(range(head, head + len(it['current'])))
    spread(L, fallen)
    fences(L, fallen, rows)
    if not keep and flat(' '.join(L[tl - 1:tl + 1 if L[tl:tl + 1] and L[tl].strip() else tl])).endswith(':'):   # ### a title that opens a list takes its list
        j = tl + (1 if L[tl].strip() else 0)
        while j < len(L) and not L[j].strip():
            j += 1
        while j < len(L) and re.match(r'\s*[-*+] ', L[j]):
            fallen.setdefault(j, set()).update(range(len(L[j])))
            j += 1
    if keep:
        end = tl - 1
        while end + 1 < len(L) and L[end + 1].strip():
            end += 1
        L[end] = L[end] + NL + NL + MARK
    else:
        fallen[tl - 1].discard(head)
        L[tl - 1] = L[tl - 1][:head] + MARK + L[tl - 1][head + 1:]
    out = []
    for i, l in enumerate(L):
        if i in fallen and fallen[i]:
            l = ''.join(ch for c, ch in enumerate(l) if c not in fallen[i])
            if not l.strip(' \t-*>|#:;,.`_()') or re.fullmatch(r'\s*\d+\.\s*', l):
                continue
            item = L[i].lstrip().startswith(('- ', '* ')) or re.match(r'\s*\d+\. ', L[i])
            l = (re.match(r' *', L[i]).group(0) if item else '') + re.sub(r'  +', ' ', l.strip())
        out.append(l)
    t2 = NL.join(out)
    m = re.search(MARK + r'[ \t]*(\S?)', t2)
    t2 = t2.replace(MARK, layout(it['draft']) + (NL + NL if m and m.group(1) else ''), 1)
    t2 = heads(tables(t2), text)
    while NL + NL + NL in t2:
        t2 = t2.replace(NL + NL + NL, NL + NL)
    return t2, rows, miss, crlf


def at_main(it):
    """the statements quoted at the pin, read at main: how many stand in the named file with their words; the lines may move."""
    out = []
    k = it['file'].split()[0]
    for s, f, ln in re.findall(r'(%s.*?) \((\S+\.lean) :(\d+)\)' % LEAN, it['draft'].split('Statements at ', 1)[-1].split(': ', 1)[-1]):
        rc, t, _e = git('D:/' + k, 'show', 'main:' + f)
        out.append((f, ln, rc == 0 and flat(s)[:60] in flat(t)))
    return out


def rows():
    return json.load(open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else {}


def bank(R):
    with open(ROWS + '.tmp', 'wb') as fh:
        fh.write((json.dumps(R, ensure_ascii=False, indent=1) + NL).encode('utf-8'))
    os.replace(ROWS + '.tmp', ROWS)
    I = items()
    L = ['b736 -- (R346)(4) AS AMENDED: THE RECORD OF THE SECOND SITTING, one row per item of data/b732_phase2_frontdoors.txt and the three at its head (%s)' % now(), '',
         '### By tools/b736_sitting.py. The author`s words: data/b736_author_words.txt. CURRENT: read at the file, or by gh, before the write and compared to the agenda. A README row`s removals: data/b736_sitting_diffs/.', '']
    key = lambda k: (0, k) if not k.isdigit() else (1, '%04d' % int(k))
    for k in sorted(R, key=key):
        r = R[k]
        it = I.get(int(k), {}) if k.isdigit() else {}
        L += ['[%s] %s' % (k, r['state']), '  FILE: ' + r.get('file', it.get('file', '')), '  LINE: ' + r.get('line', it.get('line', '')), '  CURRENT READ: ' + r['read'], '  COMPARED TO THE AGENDA: ' + r['compared'],
              '  DRAFT WRITTEN: ' + r['draft'], '  CONFIRMATION: ' + r['confirm'], '  THE AUTHOR`S WORD: ' + r.get('word', ''), '  AT: ' + r['at'], '']
    c = {}
    for r in R.values():
        k = r['state'].split()[0].strip(',')
        c[k] = c.get(k, 0) + 1
    L.append('### ### **THE SITTING: %d ROWS ; %s.**' % (len(R), ' ; '.join('%s %d' % (k, c[k]) for k in sorted(c))))
    with open(TEXT + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(TEXT + '.tmp', TEXT)


def scan():
    r = subprocess.run([sys.executable, '-X', 'utf8', '-u', os.path.join(ROOT, 'tools', 'b736_address_scan.py'), 'scan'], capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=ROOT)
    tail = [l for l in r.stdout.split(NL) if l.startswith('### ### **')]
    print('  SCAN:', tail[-1] if tail else r.stdout[-300:])
    if not tail or not re.search(r'ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ', tail[-1]):
        sys.exit('### THE SCAN IS NOT ZERO -- NOT COMMITTED; the write stands in the working tree')
    return 'scan 0 ; 0 ; 0 ; 0'


def check():
    I = items()
    print('### THE CONTROLS: the layout keeps the words at every draft, and a planted absent title refuses')
    n_ok = bad = 0
    for n, it in sorted(I.items()):
        if it['title'] != 'README PARAGRAPH':
            continue
        layout(it['draft'])
        n_ok += 1
        fake = dict(it, current='a sentence planted, in no README')
        if plan(n, fake)[0] is not None:
            bad += 1
    print('  layouts %d ; a planted title accepted %d -- %s' % (n_ok, bad, 'AS WANTED' if n_ok == 22 and not bad else 'NOT AS WANTED'))
    print('### THE PLANS, OVER MAIN IN MEMORY')
    for n, it in sorted(I.items()):
        if it['title'] != 'README PARAGRAPH':
            continue
        t2, r, m, _c = plan(n, it)
        k = it['file'].split()[0]
        cur = read('D:/%s/README.md' % k)[0]
        am = at_main(it)
        print('[%d] %-36s lines %4d -> %4s ; rows taken %3d (SILENT %d) ; missed %d ; statements at main %d of %d %s' % (
            n, k, cur.count(NL) + 1, (t2.count(NL) + 1) if t2 else '--', len(r), sum(1 for x in r if x[1] == 'SILENT'), len(m), sum(1 for x in am if x[2]), len(am), [x[:2] for x in am if not x[2]] or ''))
        for rid, t in m[:3]:
            print('      MISSED %s: %s' % (rid, t[:90]))


def show(n):
    it = items()[n]
    print('[%d] %s' % (n, it['title']))
    for k in ('file', 'line', 'current', 'draft', 'why'):
        print('  %s: %s' % (k.upper(), it.get(k, '')))
    if it['title'] == 'README PARAGRAPH':
        t2, r, m, _c = plan(n, it)
        print('  FALLS WITH IT: %d rows (%d SILENT), missed %d' % (len(r), sum(1 for x in r if x[1] == 'SILENT'), len(m)))
        print('  AT MAIN: %s' % at_main(it))
    if it['title'] == 'GITHUB DESCRIPTION':
        rc, out, err = gh('repo', 'view', 'psinary-sketch/' + it['file'].split()[0], '--json', 'description', '-q', '.description')
        print('  CURRENT AT GITHUB: %s ; equal to the agenda %s' % (out or err, out == it.get('current')))


def put_row(n, row):
    R = rows()
    if str(n) in R:
        sys.exit('### [%s] HAS ITS ROW ALREADY -- NOTHING DONE' % n)
    row.setdefault('at', now())
    R[str(n)] = row
    bank(R)


AMEND = {68: ('At this pin the xi statements close by native_decide.', 'At this pin the xi statements close by native_decide; at main they close by decide.'),
         92: ('no statement carries a bridge from 1/12.', 'no statement carries a bridge from 1/12: at main two statements each compute a 1/12, and the file has them coincide by construction.'),
         98: ('No statement names (ℤ/2)³ \\ {0} as a group or says any labeling realizes it.', 'At this pin no statement names (ℤ/2)³ \\ {0} as a group or says any labeling realizes it; main adds a list of 168 invertible Boolean matrices acting on Bool triples, tied to no labeling.')}   # ### the author's words at the sitting


PP_ITEMS = {109: [("brought to Science-Statement Standard parity (A_METHODOLOGY §VI.3.1) as the Ω_b exemplar — the excluded-class σ-distances quantified in the Selection table (B 351σ, C 18.6σ, D 304σ, computed against Planck 2018), and the kernel-verified final step the `xi_*` cluster (`xi_visible = 4`, `xi_total = 81`, `xi_wall_sq`; 4/81 = visible/total; `SIDE-cosmo/SIDECosmo/FormationPhaseSpace.lean`, `{propext, Quot.sound}`) — *citation corrected 2026-07-28: the earlier `SIDEOmegaB.omega_b_equals_4_over_81` name does not exist on disk* cited in the status table.",
                   "brought to Science-Statement Standard parity (A_METHODOLOGY §VI.3.1) -- the excluded-class σ-distances quantified in the Selection table (B 351σ, C 18.6σ, D 304σ, computed against Planck 2018), and the `xi_*` cluster cited in the status table: `xi_visible : visible_slots xi = 4`, `xi_total : total_slots xi = 81`, `xi_wall_sq : total_slots xi = (stormer_wall xi) ^ 2` (SIDE-cosmo at 95d2540, `SIDECosmo/FormationPhaseSpace.lean`, closing by `native_decide` at that pin) — *citation corrected 2026-07-28: the earlier `SIDEOmegaB.omega_b_equals_4_over_81` name does not exist on disk* — note 2026-11-02: the name omega_b_equals_4_over_81 exists at SIDE-omega-b 9c80279, Theorem.lean :130 ([88] of this sitting); the 07-28 correction stands as written for its date. Those statements compute two natural numbers; the fraction 4/81 and its reading as Ω_b are this paper's.")],
            110: [(" are this paper's. No claim changed; the derived 4/81 and its 0.13σ match stand.*", " are this paper's.*")]}
BACK_110 = '> *Removed from the v1.0.1 head note: "No claim changed; the derived 4/81 and its 0.13σ match stand." No compiled statement derives 4/81 as a physical fraction or carries a match; the comparison stands in the paper\'s body with its own error bar.*'


def apply(n, word):
    it = items()[n]
    if n in AMEND:
        if it['draft'].count(AMEND[n][0]) != 1:
            sys.exit('### THE AMENDMENT DOES NOT MEET ITS DRAFT -- NOTHING WRITTEN')
        it = dict(it, draft=it['draft'].replace(*AMEND[n]))
    k = it['file'].split()[0]
    if str(n) in rows():
        sys.exit('### [%d] HAS ITS ROW ALREADY -- NOTHING DONE' % n)
    if it['title'] == 'README PARAGRAPH':
        if git('D:/' + k, 'status', '--porcelain', '--', 'README.md')[1] or git('D:/' + k, 'rev-parse', '--abbrev-ref', 'HEAD')[1] != 'main':
            sys.exit('### %s NOT CLEAN ON main -- NOTHING WRITTEN' % k)
        t2, r, m, crlf = plan(n, it)
        if t2 is None:
            print('### [%d] THE CURRENT DIFFERS FROM THE AGENDA: nothing written' % n)
            put_row(n, dict(state='NOT APPLIED (the CURRENT differs from the agenda)', read=read('D:/%s/README.md' % k)[0][:300], compared='MISMATCH', draft='none', confirm='none', word=word))
            return
        old = read('D:/%s/README.md' % k)[0]
        os.makedirs(DIFFS, exist_ok=True)
        with open(os.path.join(DIFFS, '%s.diff' % k), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(NL.join(difflib.unified_diff(old.split(NL), t2.split(NL), 'main README.md', 'b736 [%d]' % n, lineterm='', n=0)) + NL)
        write('D:/%s/README.md' % k, t2, crlf)
        sc = scan()
        msg = 'b736 [%d]: README.md, the README paragraph, by (R346)(4) as the author amended it (relay data/b732_phase2_frontdoors.txt :%d)%s' % (n, it['at'], ' [skip ci]' if k in SKIP_CI else '')
        rc, out, err = git('D:/' + k, 'commit', '-m', msg, '--', 'README.md')
        if rc:
            sys.exit('### THE COMMIT REFUSED AT [%d]: %s %s' % (n, out, err))
        h = git('D:/' + k, 'rev-parse', '--short=8', 'HEAD')[1]
        files = git('D:/' + k, 'show', '--format=', '--name-only', 'HEAD')[1]
        if files != 'README.md':
            sys.exit('### THE COMMIT TOUCHED %s' % files)
        print('  COMMIT %s %s -- %s ; rows taken %d ; missed %d' % (k, h, files, len(r), len(m)))
        put_row(n, dict(state='PASS', read=it['current'], compared='EQUAL', draft='the agenda`s paragraph; rows taken %d, missed %s (relay data/b736_sitting_diffs/%s.diff)' % (len(r), [x[0] for x in m] or 'none', k),
                        confirm='%s %s (%s)' % (k, h, sc), word=word))
        return
    if it['title'] == 'GITHUB DESCRIPTION':
        rc, cur, err = gh('repo', 'view', 'psinary-sketch/' + k, '--json', 'description', '-q', '.description')
        if rc or cur != it['current']:
            print('### [%d] THE CURRENT DIFFERS: %s -- nothing written' % (n, cur or err))
            put_row(n, dict(state='NOT APPLIED (the CURRENT differs from the agenda)', read=cur or err, compared='MISMATCH', draft='none', confirm='none', word=word))
            return
        rc, out, err = gh('repo', 'edit', 'psinary-sketch/' + k, '--description', it['draft'])
        if rc:
            sys.exit('### gh REFUSED [%d]: %s %s' % (n, out, err))
        rc, back, err = gh('repo', 'view', 'psinary-sketch/' + k, '--json', 'description', '-q', '.description')
        if back != it['draft']:
            sys.exit('### THE READ-BACK DIFFERS AT [%d]: %s' % (n, back))
        print('  READ BACK BY gh, EQUAL:', back)
        put_row(n, dict(state='PASS', read=cur, compared='EQUAL', draft=it['draft'], confirm='gh read back %s, equal' % now(), word=word))
        return
    if it['title'] == 'ZENODO NOTE':
        put_row(n, dict(state='PASS, BANKED ONLY, carried to a Tier 3 act on the author`s number', read='not read: nothing is written', compared='not compared', draft=it['draft'], confirm='no write', word=word))
        print('  BANKED ONLY')
        return
    if n in PP_ITEMS:
        rel = 'phase2/physics/STORMER.md'
        p = 'D:/MY-DOwnloads/PLACE-papers/' + rel
        text, crlf = read(p)
        for a, b in PP_ITEMS[n]:
            if text.count(a) != 1:
                sys.exit('### [%d]: THE WORDS DO NOT MEET THE FILE ONCE -- NOTHING WRITTEN' % n)
            text = text.replace(a, b)
        if n == 110:
            text = text.rstrip(NL) + NL + NL + BACK_110 + NL
        write(p, text, crlf)
        sc = scan()
        msg = 'b736 [%d]: %s, by (R346)(4) on the author`s number (relay data/b732_phase2_frontdoors.txt :%d)' % (n, rel, it['at'])
        rc, out, err = git('D:/MY-DOwnloads/PLACE-papers', 'commit', '-m', msg, '--', rel)
        if rc:
            sys.exit('### THE COMMIT REFUSED AT [%d]: %s %s' % (n, out, err))
        h = git('D:/MY-DOwnloads/PLACE-papers', 'rev-parse', '--short=8', 'HEAD')[1]
        print('  COMMIT PLACE-papers %s -- %s' % (h, git('D:/MY-DOwnloads/PLACE-papers', 'show', '--format=', '--name-only', 'HEAD')[1]))
        put_row(n, dict(state='PASS', read=it['current'], compared='EQUAL', draft='as the author`s word', confirm='PLACE-papers %s (%s)' % (h, sc), word=word))
        return
    sys.exit('### [%d] %s: a PLACE-papers item, not this route' % (n, it['title']))


def repair(n, word):
    """`repair N WORD`: an item written by the plan before it took whole sentences: the plan over the file below the item's own commit, one further commit, none amended; the row `NR`."""
    it = items()[n]
    k = it['file'].split()[0]
    key = '%dR' % n
    if key in rows():
        sys.exit('### [%s] HAS ITS ROW ALREADY -- NOTHING DONE' % key)
    h0 = rows()[str(n)]['confirm'].split()[1]
    base = git('D:/' + k, 'show', h0 + '~1:README.md')[1].replace('\r\n', NL) + NL
    t2, r, m, crlf = plan(n, it, base)
    if t2 is None or m:
        sys.exit('### THE PLAN DOES NOT STAND OVER THE BASE -- NOTHING WRITTEN')
    old = read('D:/%s/README.md' % k)[0]
    with open(os.path.join(DIFFS, '%s_repair.diff' % k), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(NL.join(difflib.unified_diff(old.split(NL), t2.split(NL), 'b736 [%d] README.md' % n, 'b736 [%s]' % key, lineterm='', n=0)) + NL)
    write('D:/%s/README.md' % k, t2, crlf)
    sc = scan()
    msg = 'b736 [%s]: README.md, the fragments [%d] left, removed by the author`s number; [%d] stands' % (key, n, n)
    rc, out, err = git('D:/' + k, 'commit', '-m', msg, '--', 'README.md')
    if rc:
        sys.exit('### THE COMMIT REFUSED AT [%s]: %s %s' % (key, out, err))
    h = git('D:/' + k, 'rev-parse', '--short=8', 'HEAD')[1]
    files = git('D:/' + k, 'show', '--format=', '--name-only', 'HEAD')[1]
    if files != 'README.md':
        sys.exit('### THE COMMIT TOUCHED %s' % files)
    print('  COMMIT %s %s -- %s' % (k, h, files))
    put_row(key, dict(state='PASS', read='the file at %s' % h0, compared='the plan`s fragments', draft='the sentences and list items the fragments belonged to fall whole (relay data/b736_sitting_diffs/%s_repair.diff)' % k, confirm='%s %s (%s)' % (k, h, sc), word=word))


def follow():
    R = rows()
    I = items()
    S = {}
    for n, it in I.items():
        if it['title'] in ('README PARAGRAPH', 'ZENODO NOTE'):
            S.setdefault(it['file'].split()[0], []).append(n)
    done = 0
    for n, it in sorted(I.items()):
        if it['part'] != 'A' or str(n) in R:
            continue
        if n in STRUCK_UNREAD:
            R[str(n)] = dict(state='STRUCK ' + STRUCK_UNREAD[n], read='not read', compared='not compared', draft='none', confirm='left as it stands', word='see data/b736_author_words.txt', at=now())
            done += 1
            continue
        k = it['file'].split()[0]
        note = 'note' in it['draft']
        tgt = [x for x in S.get(k, []) if (I[x]['title'] == 'ZENODO NOTE') == note]
        t = tgt[0] if tgt else None
        if t is None or str(t) not in R:
            print('### [%d]: its draft has no row yet' % n)
            continue
        st = R[str(t)]['state']
        R[str(n)] = dict(state=('%s, as [%d]' % (st.split(',')[0].split(' (')[0].split()[0], t)), read='as [%d]' % t, compared='as [%d]' % t, draft='as [%d]' % t, confirm='as [%d]' % t, word='as [%d]' % t, at=now())
        done += 1
    bank(R)
    print('rows followed %d' % done)


def main(a):
    if not a:
        sys.exit(__doc__)
    c = a[0]
    if c == 'check':
        check()
    elif c == 'show':
        show(int(a[1]))
    elif c == 'pass':
        apply(int(a[1]), ' '.join(a[2:]) or 'Pass [%s]' % a[1])
    elif c == 'repair':
        repair(int(a[1]), ' '.join(a[2:]) or 'Pass [%sR]' % a[1])
    elif c == 'push':
        k = a[1]
        b0 = json.load(open(BASES, encoding='utf-8'))[k]
        if git('D:/' + k, 'diff', '--name-only', b0, 'main')[1] != 'README.md' or git('D:/' + k, 'rev-parse', '--abbrev-ref', 'HEAD')[1] != 'main':
            sys.exit('### %s: NOT README.md ALONE ON main -- NOTHING PUSHED' % k)
        rc, out, err = git('D:/' + k, 'branch', 'push-b736-sitting', 'main')
        if rc:
            sys.exit('### THE BRANCH REFUSED: %s %s' % (out, err))
        r = subprocess.run([shutil.which('bash'), ROOT.replace(os.sep, '/') + '/tools/push_gated.sh', '/' + 'd/' + k, 'push-b736-sitting'], capture_output=True, text=True, encoding='utf-8', errors='replace')
        print(r.stdout[-900:], r.stderr[-300:], 'EXIT', r.returncode)
    elif c == 'same':
        put_row(a[1], dict(state='PASS, no write: the draft equals the current line', read=items()[int(a[1])]['current'], compared='EQUAL', draft='as the current line', confirm='no write', word=' '.join(a[2:])))
    elif c == 'superseded':
        put_row(a[1], dict(state='SUPERSEDED, by (A1) on the author`s word: no write', read='the agenda`s words, overtaken at b733 and b735', compared='phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md :624 stands', draft='none', confirm='no write', word=' '.join(a[2:])))
    elif c == 'carry':
        put_row(a[1], dict(state='CARRIED, by the author`s number', read='not read for a write', compared='not compared', draft='none', confirm='left as it stands', word=' '.join(a[2:])))
    elif c == 'strike':
        n = a[1]
        put_row(n, dict(state='STRUCK', read='not read for a write', compared='not compared', draft='none', confirm='left as it stands', word=' '.join(a[2:])))
    elif c == 'follow':
        follow()
    elif c == 'bases':
        ks = sorted({it['file'].split()[0] for it in items().values() if it.get('file', '').startswith('SIDE-') and it['file'].split()[1] == 'README.md' and it['file'].split()[0] != 'SIDE-constants'})
        if os.path.exists(BASES):
            sys.exit('### THE BASES STAND')
        with open(BASES, 'w', encoding='utf-8', newline='\n') as fh:
            json.dump({k: git('D:/' + k, 'rev-parse', 'main')[1] for k in ks}, fh, indent=1)
            fh.write(NL)
        print('bases', len(ks))
    elif c == 'bank':
        bank(rows())
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
