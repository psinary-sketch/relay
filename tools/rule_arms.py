# -*- coding: utf-8 -*-
"""rule_arms.py -- THE STANDING RULE ARMS, under (R293)(6) and the author's word on the sort (relay data/b683_author_answers.txt): one
standing VALUE arm per TRACEABLE rule of data/b680_rules_arms.txt's 24 NONE rows, as sorted at data/b683_arms_sort.txt -- the 15 LIVE and
the 5 DECLARATION-ONLY, twenty arms named G-RULE-<name>. The superseded rule (b677 row 1) is read through b678 row 1's arm
(G-RULE-SUITE-PARTS); the three PROSE rules stay where they are read (the step-zero citation check and the defects banks).

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE** (the suite's harness: LIVE, NEG on an unmutated copy, POS on a mutated copy):
### `sources(act, ...)` reads the trace once -- banks, the tree, the act's own session transcript -- and `ARMS` holds (name, reads,
### predicate, plant). `reading(name, R)` returns the arm's count beside its verdict: rows read, rows failing, and VACUOUS where the trace
### the rule reads holds no row yet (the five declaration-only arms until a declaration is written; the walk arm before its floor).
### A declaration, for the five declaration-only arms, is a line of a relay bank or ledger of the form `DECLARED: <state> MET`, the state
### one of PAIR OF READINGS, T1, T2, T3, T5 -- the form a reading act prints when it declares one.
### Written by the Write tool at b683; it reads and writes no bank of its own. Carried by later suites as a standing instrument.
### b691, (R301)(6): four arms added by the Edit tool for the rules data/b691_arms_sort.txt sorts TRACEABLE by b683's rule -- b680 row 1
### (G-RULE-BINARY-HASHES), b685 row 1 (G-RULE-SUITE-PART-CALLS), b690 rows (1) and (2) (G-RULE-POSTSEAL-READ, G-RULE-RECUT-QUOTE) -- each
### run at HEAD and counted before it is declared (data/b691_arms_added.txt); and CONTROLS, a positive control for an arm by a defect that arm
### caught (b690's (g) for G-RULE-METHOD-READINESS), the methods bank's reader factored as methods_rows for it.
### b696, (R306)(2): G-RULE-BINARY-HASHES repaired by the Edit tool to read a corrigendum for a frozen row -- a binary whose root-named text
### bank carries its sha256 on a row naming another path reads OK where the corrigenda bank (data/b675_corrigenda.txt) carries a row citing
### that bank and line with the corrected path and the equal sha256, the correction printed beside the frozen row; with no such row it fails
### as before (b694's (k) its positive control in CONTROLS, the corrigendum withheld). The diff banked in data/b696_tool_repairs.txt.
### b703, (R313)(2): G-RULE-RECUT-QUOTE branched on the kind of cut by the Edit tool -- a kernel cut read in b676's quote form
### (data/b<act>_quote_*.json, its merge on the kernel's main) and a paper cut in the b670 form (data/b<act>_quote.json, its document, the
### search before the cut's own PLACE-papers commit, its quoting lines entered in the cut bank's residues); the predicate unchanged. The diff
### banked in data/b703_tool_repairs.txt, the control on b702's paper cut bank and b697's kernel cut bank.
"""
import calendar
import glob
import io
import json
import os
import re
import subprocess
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = 'D:/MY-DOwnloads/PLACE-papers'
NL = chr(10)
TS = re.compile(r'(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)')
DECL = re.compile(r'(?m)^[#*\s]*DECLARED:\s*(PAIR OF READINGS|T1|T2|T3|T5) MET\b')
WALK_FLOOR = 684            # ### the author's word: walk banks from b684 onward; data/b679_zeta_walk.txt the breach before the floor (b680 (c))
PROGRESS_FLOOR = 672        # ### b671 row 7 was set mid-act at b671 after its run (b671 (h)); b671's progress bank is the table read after it
GIT_WRITE = re.compile(r'\bgit\s+(?:-C\s+\S+\s+)*(?:commit\b|push\b|merge(?![-\w])|rebase\b|reset\b|tag\s+(?!-l\b|--list\b|--points-at\b)\S|'
                       r'branch\s+-[dDmM]\b|branch\s+(?!-)[\w./-]+\s+[0-9a-f]{7,40}\b)|push_gated\.sh')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')


def _rd(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except OSError:
        return ''


def _iso(s):
    try:
        return calendar.timegm(time.strptime(s[:19] + 'Z', '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def _g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def _act_of(path):
    m = re.match(r'^b(\d{3})_', os.path.basename(path))
    return int(m.group(1)) if m else None


def _banks(pattern, floor=0, upto=None):
    out = []
    for p in sorted(glob.glob(os.path.join(D, pattern))):
        a = _act_of(p)
        if a is not None and a >= floor and (upto is None or a <= upto):
            out.append(p)
    return out


# ================================================================================ THE TRANSCRIPT: THE ACT'S TOOL CALLS, BY MESSAGE, WITH OUTPUTS
def transcript(jsonl, anchor):
    """every Bash and PowerShell call in the seat's session from its first user line carrying `anchor`: (message id, tool use id, time,
    command, output). Parallel calls in one assistant message share its message id. Read from the assistant lines alone (and the results
    from the user lines): the transcript's api-request-blob lines carry copies of earlier calls without ids and are not the act's calls."""
    rows, res, start = [], {}, None
    for ln in io.open(jsonl, encoding='utf-8', errors='replace'):
        try:
            j = json.loads(ln)
        except ValueError:
            continue
        if start is None:
            if anchor in ln and j.get('type') == 'user' and not j.get('isCompactSummary'):
                start = j.get('timestamp') or ''
            continue
        m = j.get('message') or {}
        for c in m.get('content') or [] if isinstance(m.get('content'), list) else []:
            if not isinstance(c, dict):
                continue
            if c.get('type') == 'tool_use' and c.get('name') in ('Bash', 'PowerShell') and j.get('type') == 'assistant':
                rows.append(dict(mid=m.get('id') or j.get('uuid'), tid=c.get('id'), ts=j.get('timestamp') or '',
                                 cmd=(c.get('input') or {}).get('command', '')))
            if c.get('type') == 'tool_result' and j.get('type') == 'user':
                t = c.get('content')
                res[c.get('tool_use_id')] = ''.join(x.get('text', '') for x in t if isinstance(x, dict)) if isinstance(t, list) else (t or '')
    for r in rows:
        r['out'] = res.get(r['tid'])
    return rows


def methods_rows(mt):
    """a methods bank's rows, by its "=== <method> -- <word>" blocks at the line's start (b690's defect (g): a bank banked indented reads
    no row here, and G-RULE-METHOD-READINESS fails on it -- the positive control in CONTROLS)."""
    rows = []
    for blk in re.split(r'(?m)^(?==== )', mt)[1:]:
        h = re.match(r'^=== (.*?) -- (READY|NOT READY|NOT YET USED TWICE)\s*$', blk.split(NL)[0])
        if h:
            num = lambda k: int((re.search(r'^\s+%s (\d+):' % k, blk, re.M) or [None, -1])[1])   # noqa: E731
            rows.append(dict(method=h.group(1), word=h.group(2), acts=num('acts'), banks=num('banks'), defects=num('defects')))
    return rows


BINARY_FLOOR = 680          # ### b680 row 1 binds from b680 (its first application data/b680_fig_hashes.txt)
CORRIGENDA = 'b675_corrigenda.txt'   # ### b696, (R306)(2): the corrigenda bank a frozen hashes row is corrected by


def corrigenda_rows(t):
    """the corrigenda bank's rows that correct a binary's path: each row `  (N) relay data/<bank> :<line>, ...` read whole across its wrapped
    lines, carrying `THE CORRECTION: the file stands as data/<path>, sha256 <64 hex>`; returns [dict(row, bank, line, path, sha, at)]."""
    out, L = [], t.split(NL)
    for i, l in enumerate(L):
        m = re.match(r'^  \((\d+)\) relay (data/\S+?) :(\d+)\b', l)
        if not m:
            continue
        j = i + 1
        while j < len(L) and L[j].startswith('      ') and not re.match(r'^  \(\d+\) ', L[j]):
            j += 1
        whole = ' '.join(x.strip() for x in L[i:j])
        c = re.search(r'THE CORRECTION: the file stands as (data/[^\s,;]+),? sha256 ([0-9a-f]{64})\b', whole)
        if c:
            out.append(dict(row=int(m.group(1)), bank=m.group(2), line=int(m.group(3)), path=c.group(1), sha=c.group(2), at=i + 1))
    return out


def corrected(b, corr):
    """the corrigendum rows that correct binary `b`: citing a root-named text bank of its act and the line carrying its sha256 (a frozen row),
    naming its path as it stands and its equal sha256."""
    return [c for c in corr if c['path'] == b['path'] and c['sha'] == b['sha'] and any((fb, fi) == (c['bank'], c['line']) for fb, fi, _l in b.get('frozen') or [])]
RECUT_FLOOR = 691           # ### b690 rows (1) and (2) bind from b691
LEDGER_READ = ('FINDINGS.md', 'OPEN_TRAILS.md', '_scanfile_entry', '_scanfile_trail', 'scanfile_entry', 'scanfile_trail')
SHELL_FILTER = re.compile(r'(?<![\w.-])(?:sed|awk|grep|head|tail|cat|less|more|cut|tr|sort|uniq|wc)(?![\w.-])')
REDIRECT = re.compile(r'(?<![<>=\-])(?:\d?>>?|&>)(?!&)')
SUITE_PART = re.compile(r'_checks\.py\b[^|;&]*?--part\s+(\S+)')


# ================================================================================ THE SOURCES
def sources(act, jsonl, anchor, parts, lock_epoch=None, pre_relay=None, pre_pp=None):
    """the trace every rule arm reads, read once. `act` 'bNNN'; `parts` the suite's declared parts; `lock_epoch` the face's lock."""
    n = int(act[1:])
    R = dict(act=act, n=n, parts=list(parts), lock=lock_epoch)
    # ### the declarations (rows (1), (5), (6), (7), (9))
    decl = []
    for p in _banks('b*.txt', 670) + [os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')]:
        for m in DECL.finditer(_rd(p)):
            decl.append((os.path.basename(p), m.group(1)))
    R['decl'] = decl
    # ### the reading acts' distances: b670's state bank (its four rows (i)-(iv), the first figure of each) and every later closing that prints
    # ### "THE DISTANCE FROM THE PAIR`S BAR <n>"; the last two read
    st = _rd(os.path.join(D, 'b670_state.txt'))
    first = {}
    for m in re.finditer(r'(?m)^  \((i|ii|iii|iv)\)\s+(\d+)', st):
        first.setdefault(m.group(1), int(m.group(2)))
    rd_ = [('b670_state.txt', [first[k] for k in ('i', 'ii', 'iii', 'iv') if k in first])] if st else []
    for p in _banks('b*_closing.txt', 671):
        f = [int(x) for x in re.findall(r'DISTANCE FROM THE PAIR[`\']S BAR (\d+)', _rd(p))]
        if f:
            rd_.append((os.path.basename(p), f))
    R['reading_dists'] = rd_[-2:]
    outs = _banks('b*_outside.txt')
    ot = _rd(outs[-1]) if outs else ''
    mo = re.search(r'ENTRIES (\d+) ;.*?ALL THREE (\d+)', ot)
    R['outside'] = (os.path.basename(outs[-1]) if outs else None, int(mo.group(1)) if mo else None, int(mo.group(2)) if mo else None)
    meths = _banks('b*_methods.txt')
    mt = _rd(meths[-1]) if meths else ''
    R['methods'] = (os.path.basename(meths[-1]) if meths else None, methods_rows(mt))
    R['methods_text'] = mt
    R['ferries_retire'] = [os.path.basename(p) for p in _banks('b*_ferry.txt') if re.search(r'WITHHOLDING RULES? (?:ARE )?RETIRED', _rd(p))]
    # ### row (3): the rowgen banks
    rg = {}
    for a in range(674, n + 1):
        p = os.path.join(D, 'b%d_rowgen_stepzero.txt' % a)
        t = _rd(p)
        rg[a] = dict(present=os.path.exists(p), clean='CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0' in t, at=_iso((TS.search(t) or [''])[0]) if t else None)
    R['rowgen'] = rg
    pc = [int(x) for x in _g(PP, 'log', '--reverse', '--format=%ct', '%s..HEAD' % pre_pp).split() if x.isdigit()] if pre_pp else []
    R['pp_first_ct'] = pc[0] if pc else None
    # ### row (10): the progress banks
    pr = []
    for p in _banks('b*progress*.txt', PROGRESS_FLOOR):
        for l in _rd(p).split(NL):
            m = re.match(r'^([A-Z]+) (\{.*\})\s*$', l)
            if m:
                try:
                    o = json.loads(m.group(2))
                except ValueError:
                    o = {}
                pr.append((os.path.basename(p), m.group(1), bool(o.get('at'))))
    R['progress'] = pr
    # ### row (11): mid-act checks against each root
    late = []
    nroot = 0
    for a in range(672, n + 1):
        j = {}
        try:
            j = json.load(io.open(os.path.join(D, 'b%d_act_root.json' % a), encoding='utf-8'))
        except Exception:
            continue
        at = j.get('at_epoch') or _iso(j.get('at') or '')
        if not at:
            continue
        nroot += 1
        for it in j.get('items') or []:
            b = it.split()[0]
            if b.startswith('data/') and b.endswith(('.txt', '.json', '.md')):
                for m in re.finditer(r'THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', _rd(os.path.join(ROOT, *b.split('/')))):
                    if _iso(m.group(1)) and _iso(m.group(1)) > at:
                        late.append(('b%d' % a, b, m.group(1)))
    R['midact'] = (nroot, late)
    # ### row (12): the consumers sections
    cs = []
    for p in _banks('b*plan*.txt', 672):
        t = _rd(p)
        h = re.search(r'(?m)^== \d+\. THE CONSUMERS SECTION', t)          # ### the section's own header, not a title naming it
        if not h:
            continue
        sec = t[h.start():]
        k = re.search(r'(?m)^== ', sec[1:])
        sec = sec[:k.start() + 1] if k else sec
        cs.append((os.path.basename(p), bool(re.search(r'data/b\d{3}_[\w.-]+\.(?:txt|json)', sec))))
    R['consumers'] = cs
    # ### row (14): the runner banks
    rn = []
    for p in _banks('b*_runner_*.txt', 673):
        t = _rd(p)
        rid = re.search(r'the run: id (\d+)', t)
        ref = re.search(r'the ref built \(out/ref\.txt\): ([0-9a-f]{40})', t) or re.search(r'the ref input ([0-9a-f]{40})', t)
        if rid:
            rn.append((_act_of(p), os.path.basename(p), rid.group(1), ref.group(1) if ref else None))
    R['runner'] = rn
    # ### row (15): the walk banks
    wk = []
    for p in _banks('b*_zeta_walk*.txt', WALK_FLOOR):
        t = _rd(p)
        m = re.search(r' at ([0-9a-f]{7,40}) \(', t)
        nm = re.search(r'_zeta_walk_([0-9a-f]{7})\.txt$', p)
        wk.append((os.path.basename(p), nm.group(1) if nm else None, m.group(1)[:7] if m else None))
    R['walks'] = wk
    R['walk_before_floor'] = [os.path.basename(p) for p in _banks('b*_zeta_walk*.txt', 674, WALK_FLOOR - 1)
                              if not re.search(r'_zeta_walk_[0-9a-f]{7}\.txt$', p)]
    # ### row (19): the naming banks
    nb = []
    for p in _banks('b*_naming.txt', 674):                                  # ### the rule's act on (b200's sector naming bank is another kind)
        t = _rd(p)
        v = re.search(r'NAMED (SIDE-[\w-]+) ; TIED (\d+)', t)
        ent, ls = [], t.split(NL)
        for i, l in enumerate(ls):
            m = re.match(r'^\s+(\d+)\s+(SIDE-[\w-]+)\s+licensed table :\d+', l)
            if m:
                o = re.search(r'\(outside of any kind (\d+) ; rows (\d+)\)', ls[i + 1] if i + 1 < len(ls) else '')
                ent.append((int(m.group(1)), m.group(2), (int(o.group(1)), int(o.group(2))) if o else None))
        nb.append(dict(bank=os.path.basename(p), named=v.group(1) if v else None, tied=int(v.group(2)) if v else None, rows=ent))
    R['naming'] = nb
    # ### rows (13), (16), (18): the act's own tool calls
    R['calls'] = transcript(jsonl, anchor) if jsonl and os.path.exists(jsonl) else []
    rl = [l.split(' ', 2) for l in _g(ROOT, 'log', '--reverse', '--format=%h %ct %s', '%s..HEAD' % pre_relay).split(NL) if l.strip()] if pre_relay else []
    sc = [int(x[1]) for x in rl if len(x) == 3 and x[2].startswith('%s seal' % act)]
    R['seal_ct'] = sc[0] if sc else None
    # ### row (20): the ruling's weight clause and the previous closing's head line
    R['ferry'] = _rd(os.path.join(D, '%s_ferry.txt' % act))
    R['prev_head'] = (_rd(os.path.join(D, 'b%d_closing.txt' % (n - 1))).split(NL) or [''])[0]
    # ### row (21): the gate banks
    gb = {}
    for a in range(675, n + 1):
        t = _rd(os.path.join(D, 'b%d_reg_gate.txt' % a))
        gb[a] = dict(present=bool(t), clean='THE CLOSING DRY-RUN STEP : CLEAN' in t, at=_iso((TS.search(t) or [''])[0]) if t else None)
    R['gates'] = gb
    # ### rows (22), (24): the suite's run banks
    runs = {}
    for a in range(678, n + 1):
        for kind in ('arms_prerun', 'checks', 'checks_postpush'):
            t = _rd(os.path.join(D, 'b%d_%s.txt' % (a, kind)))
            if t:
                runs[(a, kind)] = [(p, int(s)) for p, _n, s in re.findall(r'(?m)^  ### PART ([\w-]+) : ARMS (\d+) ; (\d+) s$', t)]
    R['runs'] = runs
    # ### b684's carry-time repair (the navigator's answer on the split rule): each act's governing parts read from the rules banks -- the
    # ### latest rules bank at or before the act whose rows name the suite's standing parts (`standing-<x>`), those parts and the act's
    # ### part; b678 row 1 (three parts) governs b678-b683, b684 row (1) (four) from b684.
    gov = []
    for p in _banks('b*_rules.txt', 678):
        rows = [r for r in re.split(r'(?m)^  \((?=\d+\) )', _rd(p)) if re.search(r'\bstanding-[a-z][0-9]?\b', r)]
        if rows:
            gov.append((_act_of(p), os.path.basename(p), sorted(set(re.findall(r'\bstanding-[a-z][0-9]?\b', ' '.join(rows)))) + ['act']))
    R['governing'] = gov
    pv = _rd(os.path.join(D, 'b%d_arms_prerun.txt' % (n - 1)))
    R['prev_longest'] = max([int(x) for x in re.findall(r'THE LONGEST PHASE (\d+) s', pv)] or [0])
    R['prev_parts'] = len(set(p for p, _s in runs.get((n - 1, 'arms_prerun'), [])))
    # ### b680 row 1 (added b691): every tracked binary bank of relay data from b680 -- gz, png, zip -- with its sha256 (of its bytes) and the
    # ### text banks of its act that its act's root names, each text bank's text
    import hashlib
    bins = []
    for p in sorted(set(_g(ROOT, 'ls-files', '--', 'data/*.gz', 'data/*.png', 'data/*.zip').split(NL)) - {''}):
        a = _act_of(p)
        if a is None or a < BINARY_FLOOR:
            continue
        try:
            sha = hashlib.sha256(open(os.path.join(ROOT, *p.split('/')), 'rb').read()).hexdigest()
        except OSError:
            sha = None
        try:
            items = json.load(io.open(os.path.join(D, 'b%d_act_root.json' % a), encoding='utf-8')).get('items') or []
        except Exception:
            items = None
        named = [it.split()[0] for it in (items or [])]
        texts = [(b, _rd(os.path.join(ROOT, *b.split('/')))) for b in named if b.endswith('.txt') and os.path.basename(b).startswith('b%d_' % a)]
        bins.append(dict(path=p, act=a, sha=sha, root=items is not None, in_root=p in named,
                         carried_by=[b for b, t in texts if p in t and sha and sha in t],
                         frozen=[(b, i, l.strip()) for b, t in texts for i, l in enumerate(t.split(NL), 1) if sha and sha in l]))
    R['binaries'] = bins
    R['corrigenda'] = corrigenda_rows(_rd(os.path.join(D, CORRIGENDA)))
    # ### b690 row (2) (added b691): every quotation-search bank from b691 (data/b<act>_quote_*.json) and the merge of its tip, with the
    # ### act's cut banks and the residues they enter
    qs = []
    for p in _banks('b*_quote_*.json', RECUT_FLOOR):
        try:
            q = json.load(io.open(p, encoding='utf-8'))
        except Exception:
            q = {}
        kd, tip, at = q.get('kernel'), q.get('tip') or '', _iso(q.get('at') or '')
        mg = None
        if kd and tip:
            for l in _g(kd, 'log', '--merges', '--format=%H %P %ct', 'main').split(NL):
                f = l.split()
                if len(f) >= 4 and f[2].startswith(tip[:7]):
                    mg = (f[0], int(f[3]))
        rows = q.get('rows') or []
        lines = sorted(set('%s :%s' % (h.split(':', 3)[1], h.split(':', 3)[2]) for r in rows for h in (r.get('hits_wide') or [])))
        a = _act_of(p)
        cuts = ''.join(_rd(x) for x in _banks('b%d_*cut*.txt' % a, a, a)) + ''.join(_rd(x) for x in _banks('b%d_*cut*.json' % a, a, a))
        qs.append(dict(bank=os.path.basename(p), act=a, at=at, merge=mg, rows=len(rows),
                       needled=all(r.get('needle') and r['needle'] in (r.get('line') or '') for r in rows) and bool(rows),
                       quoting=lines, unentered=[x for x in lines if not re.search(re.escape(x.split(' :')[0]) + r'[^\n]{0,40}?' +
                                                                                    r'(?:", |\s:?)' + x.split(' :')[1] + r'\b', cuts)]))
    # ### b703, (R313)(2): the arm branched on the kind of cut -- a paper cut's search (data/b<act>_quote.json, the b670 form: a `document`, no
    # ### kernel and no merge) read beside the kernel cuts' (b676's form above): its "merge" the cut's own PLACE-papers commit (the act's cut
    # ### bank's `base` less its `^`), its time that commit's; its quoting lines (file, line) entered where the cut bank's residues carry them
    for p in _banks('b*_quote.json', RECUT_FLOOR):
        try:
            q = json.load(io.open(p, encoding='utf-8'))
        except Exception:
            q = {}
        if not q.get('document') or q.get('kernel'):
            continue
        a = _act_of(p)
        try:
            cj = json.load(io.open(os.path.join(D, 'b%d_cut.json' % a), encoding='utf-8'))
        except Exception:
            cj = {}
        cc = (cj.get('base') or '').rstrip('^') if (cj.get('base') or '').endswith('^') else ''
        if not cc:   # ### a cut bank written before its commit names HEAD: the first commit of the act touching the document after the search
            qa = _iso(q.get('at') or '') or 0
            for l in _g(PP, 'log', '--reverse', '--format=%H %ct %s', '--', q['document']).split(NL):
                f = l.split(' ', 2)
                if len(f) == 3 and f[1].isdigit() and int(f[1]) > qa and f[2].startswith('b%d ' % a):
                    cc = f[0]
                    break
        ct = _g(PP, 'log', '-1', '--format=%H %ct', cc).split() if cc else []
        mg = (ct[0], int(ct[1])) if len(ct) == 2 and ct[1].isdigit() else None
        rows = q.get('rows') or []
        lines = sorted(set('%s :%s' % (f, n_) for f, n_ in (q.get('quoting') or [])))
        res = set('%s :%s' % (f, n_) for f, n_ in (cj.get('residues') or []))
        qs.append(dict(bank=os.path.basename(p), act=a, at=_iso(q.get('at') or ''), merge=mg, rows=len(rows), kind='paper',
                       needled=all(r.get('needle') and r['needle'] in (r.get('line') or '') for r in rows) and bool(rows),
                       quoting=lines, unentered=[x for x in lines if x not in res]))
    R['quotes'] = qs
    R['cut_banks'] = dict((a, len([x for x in _banks('b%d_*cut.txt' % a, a, a)])) for a in range(RECUT_FLOOR, n + 1))
    return R


# ================================================================================ THE READINGS: (ok, rows read, rows failing, note)
def _decl_reading(R, states, cond, what):
    ds = [d for d in R['decl'] if d[1] in states]
    if not ds:
        return True, 0, 0, 'VACUOUS: no declaration of %s in any bank or ledger (the condition now %s)' % ('/'.join(states), cond(R)[1])
    ok, why = cond(R)
    return ok, len(ds), 0 if ok else len(ds), '%d declaration(s) %s; the condition %s' % (len(ds), ds[:3], why)


def _dists_zero(R, both=True):
    rd_ = R['reading_dists']
    need = rd_[-2:] if both else rd_[-1:]
    ok = bool(need) and len(need) == (2 if both else 1) and all(d and all(x == 0 for x in d) for _b, d in need)
    return ok, 'distances %s' % [(b, d) for b, d in need]


def _t2(R):
    b, e, a = R['outside']
    return (e is not None and a is not None and e == a and e > 0), 'the outside-reader bank %s: ALL THREE %s of ENTRIES %s' % (b, a, e)


def _t3(R):
    b, rows = R['methods']
    return (bool(rows) and all(r['word'] == 'READY' for r in rows)), 'the methods bank %s: READY %d of %d' % (
        b, sum(r['word'] == 'READY' for r in rows), len(rows))


def _t5(R):
    return bool(R['ferries_retire']), 'ferry banks carrying a ruling that retires the withholding: %s' % (R['ferries_retire'] or 'NONE')


def reading(name, R):
    n = R['n']
    if name == 'G-RULE-PAIR-OF-READINGS':
        return _decl_reading(R, ('PAIR OF READINGS',), lambda R: _dists_zero(R, True), 'the pair')
    if name == 'G-RULE-TRIGGER-T1':
        return _decl_reading(R, ('T1',), lambda R: _dists_zero(R, True), 'T1')
    if name == 'G-RULE-TRIGGER-T2':
        return _decl_reading(R, ('T2',), _t2, 'T2')
    if name == 'G-RULE-TRIGGER-T3':
        return _decl_reading(R, ('T3',), _t3, 'T3')
    if name == 'G-RULE-TRIGGER-T5':
        return _decl_reading(R, ('T5',), _t5, 'T5')
    if name == 'G-RULE-METHOD-READINESS':
        b, rows = R['methods']
        bad = [r['method'] for r in rows if r['word'] == 'READY' and (r['acts'] < 2 or r['banks'] < 1 or r['defects'] < 1)]
        return bool(rows) and not bad, len(rows), len(bad), 'the methods bank %s: rows %d, READY %d, READY against the criteria %s' % (
            b, len(rows), sum(r['word'] == 'READY' for r in rows), bad or 'NONE')
    if name == 'G-RULE-ROWGEN-REVIEW':
        rg = R['rowgen']
        bad = [a for a, v in rg.items() if not (v['present'] and v['clean'])]
        cur = rg.get(n) or {}
        late = bool(cur.get('at') and R['pp_first_ct'] and cur['at'] > R['pp_first_ct'])
        return bool(rg) and not bad and not late, len(rg), len(bad) + late, 'acts b674-b%d: banks %d, missing or not exit 0 %s ; this act`s before its first ledger write %s' % (
            n, sum(v['present'] for v in rg.values()), ['b%d' % a for a in bad] or 'NONE', not late)
    if name == 'G-RULE-DETACHED-PRINT':
        pr = R['progress']
        bad = [x for x in pr if not x[2]]
        return True if not pr else not bad, len(pr), len(bad), ('VACUOUS: no progress bank from b%d' % PROGRESS_FLOOR) if not pr else (
            'unit rows %d in %s ; without a time %d' % (len(pr), sorted(set(x[0] for x in pr)), len(bad)))
    if name == 'G-RULE-MIDACT-AFTER-ROOT':
        nr, late = R['midact']
        return nr > 0 and not late, nr, len(late), 'roots read %d (b672 on) ; mid-act headers after the root in a root-named bank %s' % (nr, late[:3] or 'NONE')
    if name == 'G-RULE-CONSUMER-TOLERANCE':
        cs = R['consumers']
        bad = [b for b, ok in cs if not ok]
        return bool(cs) and not bad, len(cs), len(bad), 'consumers sections %d (plan banks b672 on) ; citing no bank %s' % (len(cs), bad or 'NONE')
    if name == 'G-RULE-SCORES-BEFORE-SEAL':
        sc = [c for c in R['calls'] if re.search(r'\b%s_record\.py\s+scores\b' % R['act'], c['cmd'])]
        first = min((_iso(c['ts']) for c in sc if _iso(c['ts'])), default=None)
        ok = bool(sc) and (R['seal_ct'] is None or (first is not None and first < R['seal_ct']))
        return ok, len(sc), 0 if ok else 1, 'score-route calls %d, the first %s ; the seal commit %s' % (
            len(sc), time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(first)) if first else 'NONE',
            time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(R['seal_ct'])) if R['seal_ct'] else 'not yet')
    if name == 'G-RULE-DISPATCH-PER-TREE':
        rn = R['runner']
        seen, bad = {}, []
        for a, b, rid, ref in rn:
            if ref is None:
                bad.append(b)
                continue
            k = (a, ref)
            if k in seen and seen[k] != rid:
                bad.append(b)
            seen.setdefault(k, rid)
        return bool(rn) and not bad, len(rn), len(bad), 'runner banks %d (b673 on), every run`s built tree read ; two runs of one tree in an act %s' % (len(rn), bad or 'NONE')
    if name == 'G-RULE-WALK-TIP':
        wk = R['walks']
        bad = [b for b, nm, tip in wk if not nm or not tip or nm != tip]
        return not bad, len(wk), len(bad), ('VACUOUS: no walk bank from b%d (the floor); before it, without its tip: %s (b680`s defect (c))' % (
            WALK_FLOOR, R['walk_before_floor'] or 'NONE')) if not wk else 'walk banks %d from b%d ; without their tip %s' % (len(wk), WALK_FLOOR, bad or 'NONE')
    if name == 'G-RULE-ONE-GIT-WRITE':
        per = {}
        for c in R['calls']:
            if GIT_WRITE.search(QUOTED.sub('""', c['cmd'])):
                per.setdefault(c['mid'], []).append(c['ts'])
        bad = [(m, ts) for m, ts in per.items() if len(ts) > 1]
        return bool(R['calls']) and not bad, len(per), len(bad), 'messages carrying a git write %d ; with more than one %s' % (
            len(per), [ts[0] for _m, ts in bad][:3] or 'NONE')
    if name == 'G-RULE-REMOTE-REREAD':
        ls = [c for c in R['calls'] if 'ls-remote' in c['cmd']]
        multi = [c['ts'] for c in ls if c['cmd'].count('ls-remote') > 1]
        empty_unread = []
        for i, c in enumerate(ls):
            if c['out'] is not None and not (c['out'] or '').strip():
                nxt = ls[i + 1] if i + 1 < len(ls) else None
                if nxt is None or nxt['cmd'].count('ls-remote') != 1:
                    empty_unread.append(c['ts'])
        return not multi and not empty_unread, len(ls), len(multi) + len(empty_unread), (
            'VACUOUS: no ls-remote call in this act`s shell commands' if not ls else
            'ls-remote calls %d ; naming more than one %s ; an empty read not re-read alone %s' % (len(ls), multi or 'NONE', empty_unread or 'NONE'))
    if name == 'G-RULE-TIE-BREAK':
        nb, bad, ties = R['naming'], [], 0
        for x in nb:
            if not x['rows'] or x['named'] is None:
                bad.append(x['bank'])
                continue
            top = max(c for c, _k, _o in x['rows'])
            tied = [(k, o) for c, k, o in x['rows'] if c == top]
            if len(tied) != x['tied']:
                bad.append(x['bank'])
            elif len(tied) > 1:
                ties += 1
                if any(o is None for _k, o in tied) or max(tied, key=lambda t: t[1])[0] != x['named']:
                    bad.append(x['bank'])
            elif tied[0][0] != x['named']:
                bad.append(x['bank'])
        return bool(nb) and not bad, len(nb), len(bad), 'naming banks %d, ties %d ; named against the rule %s' % (len(nb), ties, bad or 'NONE')
    if name == 'G-RULE-HEAD-LINE-QUOTED':
        h = R['prev_head'].strip()
        m = re.search(r'^\(1\)(.*?)(?=^\(2\))', R['ferry'], re.M | re.S)
        # ### b689, (R299)(2) as the author's word amends it: every whitespace character and line break removed from both strings, no space
        # ### retained, so a quote pasted over lines -- broken after a hyphen or not -- reads (data/b689_tool_repairs.txt)
        ok = bool(h) and bool(m) and ''.join(h.split()) in ''.join(m.group(1).split())
        return ok, 1, 0 if ok else 1, 'the previous closing`s :1 %r in this ruling`s (1): %s' % (h[:60], ok)
    if name == 'G-RULE-CLOSING-DRY':
        gb = R['gates']
        cur_req = R['lock'] is not None
        bad = [a for a, v in gb.items() if (a < n or cur_req) and not (v['present'] and v['clean'])]
        late = bool(cur_req and gb.get(n, {}).get('at') and R['seal_ct'] and gb[n]['at'] > R['seal_ct'])
        return not bad and not late, len([a for a in gb if a < n or cur_req]), len(bad) + late, (
            'gate banks b675-b%d read %d ; without the closing dry-run step CLEAN %s ; this act`s %s' % (
                n, len([a for a in gb if a < n or cur_req]), ['b%d' % a for a in bad] or 'NONE',
                ('before the seal %s' % (not late)) if cur_req else 'not yet required (the face unlocked)'))
    if name == 'G-RULE-LONG-PHASE-SPLIT':
        trig = R['prev_longest'] > 450
        ok = (not trig) or len(set(R['parts'])) > R['prev_parts']
        return ok, 1, 0 if ok else 1, 'the previous act`s pre-run`s longest phase %d s (above 450 s: %s) ; its parts %d, this act`s %d%s' % (
            R['prev_longest'], trig, R['prev_parts'], len(set(R['parts'])), '' if trig else ' -- NOT REACHED')
    if name == 'G-RULE-SUITE-PARTS':
        runs, gov = R['runs'], R.get('governing') or []

        def parts_of(a):
            g_ = [x for x in gov if x[0] <= a]
            return (g_[-1][2], g_[-1][1]) if g_ else (None, None)

        def met(run, gp):
            # ### b692, (R302)(2) on the author's word: a governing part is met by itself or by its numbered halves (standing-b by
            # ### standing-b1 and standing-b2, the split data/b684_rules.txt row (1) orders) and by no other numbering; never both.
            fam = {}
            for p in run:
                fam.setdefault(re.sub(r'(?<=^standing-[a-z])[0-9]$', '', p), []).append(p)
            return sorted(fam) == sorted(gp) and all(v == [k] or (len(v) >= 2 and len(set(v)) == len(v) and k not in v) for k, v in fam.items())
        bad = [('b%d' % a, k) for (a, k), ps in runs.items() if parts_of(a)[0] is None or not met([p for p, _s in ps], parts_of(a)[0])
               or any(s >= 600 for _p, s in ps)]
        return bool(runs) and bool(gov) and not bad, len(runs), len(bad), (
            'run banks b678-b%d %d, each against its act`s governing parts (%s) ; without them or with a part at or above 600 s %s' % (
                n, len(runs), '; '.join('%s from b%d: %s' % (b, a, ps) for a, b, ps in gov), bad or 'NONE'))
    if name == 'G-RULE-BINARY-HASHES':
        bs = R['binaries']
        corr = R.get('corrigenda') or []
        byc = [(b, corrected(b, corr)) for b in bs if b['root'] and not b['in_root'] and not b['carried_by']]
        byc = [(b, cs) for b, cs in byc if cs]
        okc = set(b['path'] for b, _cs in byc)
        bad = [b['path'] for b in bs if not b['root'] or b['in_root'] or not (b['carried_by'] or b['path'] in okc)]
        beside = ['%s OK BY CORRIGENDUM -- the frozen row %s :%d as written %r ; the correction data/%s row (%d) :%d, the file standing as %s, '
                  'sha256 %s equal' % (b['path'], c['bank'], c['line'], next(l for fb, fi, l in b['frozen'] if (fb, fi) == (c['bank'], c['line']))[:90],
                                       CORRIGENDA, c['row'], c['at'], c['path'], c['sha'][:16]) for b, cs in byc for c in cs[:1]]
        return bool(bs) and not bad, len(bs), len(bad), 'binary banks from b%d %d, each carried by sha256 in a root-named text bank of its act, '\
            'the root not naming the binary itself, or its frozen row corrected by a corrigendum (%d: %s) ; failing %s' % (
                BINARY_FLOOR, len(bs), len(beside), ' ; '.join(beside) or 'NONE', bad or 'NONE')
    if name == 'G-RULE-SUITE-PART-CALLS':
        pc = [c for c in R['calls'] if SUITE_PART.search(c['cmd']) or re.search(r'_checks\.py\b[^|;&]*--combine', c['cmd'])]
        two = [c['ts'] for c in pc if len(SUITE_PART.findall(c['cmd'])) + len(re.findall(r'--combine', c['cmd'])) > 1]
        per = {}
        for c in pc:
            per.setdefault(c['mid'], []).append(c['ts'])
        shared = [ts[0] for _m, ts in per.items() if len(ts) > 1]
        return not two and not shared, len(pc), len(two) + len(shared), (
            'VACUOUS: no suite part or combine call in this act`s shell commands yet' if not pc else
            'suite part and combine calls %d ; carrying more than one %s ; sharing a message %s' % (len(pc), two or 'NONE', shared or 'NONE'))
    if name == 'G-RULE-POSTSEAL-READ':
        sc = R['seal_ct']
        if R['n'] < RECUT_FLOOR:
            return True, 0, 0, 'VACUOUS: the rule binds from b%d' % RECUT_FLOOR
        after = [c for c in R['calls'] if sc and _iso(c['ts']) and _iso(c['ts']) > sc]
        reads = [c for c in after if any(x in c['cmd'] for x in LEDGER_READ) and '_record.py' not in c['cmd'] and '_checks.py' not in c['cmd']]
        bad = [c['ts'] for c in reads if SHELL_FILTER.search(QUOTED.sub('""', c['cmd'])) or REDIRECT.search(QUOTED.sub('""', c['cmd']))]
        return not bad, len(reads), len(bad), ('VACUOUS: the seal not yet made (no `%s seal` commit); the calls read after it 0' % R['act']) if not sc else (
            'shell calls after the seal %d ; naming the entry, the dry entry or the trail %d ; by a shell filter or a redirect %s' % (
                len(after), len(reads), bad or 'NONE'))
    if name == 'G-RULE-RECUT-QUOTE':
        qs = R['quotes']
        bad = [q['bank'] for q in qs if not q['needled'] or not q['merge'] or q['at'] is None or q['at'] >= q['merge'][1] or q['unentered']]
        short = [a for a, c in R['cut_banks'].items() if c > len([q for q in qs if q['act'] == a])]
        return bool(qs) and not bad and not short, len(qs), len(bad) + len(short), (
            'quotation-search banks from b%d %d, each removed line needled, the search before its merge, every quoting line entered in a cut bank '
            'of the act ; failing %s ; acts with more cut banks than searches %s' % (RECUT_FLOOR, len(qs), bad or 'NONE', short or 'NONE'))
    raise KeyError(name)


def _p(R, k, v):
    R = dict(R)
    R[k] = v
    return R


def _with(d, k, v):
    out = dict(d)
    out[k] = v
    return out


def _decl_plant(state):
    return lambda R: _p(R, 'decl', R['decl'] + [('planted', state)])


ARMS = [
    ('G-RULE-PAIR-OF-READINGS', 'b670 row 1: every declaration of the pair in the banks and ledgers, against the two latest reading acts` distances',
     _decl_plant('PAIR OF READINGS')),
    ('G-RULE-METHOD-READINESS', 'b670 row 2: the latest methods bank`s rows, each READY against its acts, banks and lettered defects',
     lambda R: _p(R, 'methods', (R['methods'][0], R['methods'][1] + [dict(method='planted', word='READY', acts=1, banks=1, defects=0)]))),
    ('G-RULE-ROWGEN-REVIEW', 'b670 row 3: every act`s rowgen step-zero bank from b674, both exits 0; this act`s before its first ledger write',
     lambda R: _p(R, 'rowgen', _with(R['rowgen'], 674, dict(present=False, clean=False, at=None)))),
    ('G-RULE-TRIGGER-T1', 'b671 row 2: every declaration of T1 against data/b670_state.txt`s distances and the reading acts`', _decl_plant('T1')),
    ('G-RULE-TRIGGER-T2', 'b671 row 3: every declaration of T2 against the latest outside-reader bank', _decl_plant('T2')),
    ('G-RULE-TRIGGER-T3', 'b671 row 4: every declaration of T3 against the latest methods bank (its methods half)', _decl_plant('T3')),
    ('G-RULE-TRIGGER-T5', 'b671 row 6: every declaration of T5 against the ferry banks` rulings', _decl_plant('T5')),
    ('G-RULE-DETACHED-PRINT', 'b671 row 7: every unit row of every progress bank from b672, its time',
     lambda R: _p(R, 'progress', R['progress'] + [('planted', 'POINT', False)])),
    ('G-RULE-MIDACT-AFTER-ROOT', 'b672 row 1: every root from b672 and the banks it names, no mid-act check header timed after it',
     lambda R: _p(R, 'midact', (R['midact'][0], R['midact'][1] + [('planted', 'data/x', 'x')]))),
    ('G-RULE-CONSUMER-TOLERANCE', 'b672 row 2: every plan bank`s consumers section from b672, a bank cited',
     lambda R: _p(R, 'consumers', R['consumers'] + [('planted', False)])),
    ('G-RULE-SCORES-BEFORE-SEAL', 'b672 row 3: this act`s calls of its score route against its seal commit',
     lambda R: _p(R, 'calls', [c for c in R['calls'] if 'scores' not in c['cmd']])),
    ('G-RULE-DISPATCH-PER-TREE', 'b673 row 1: every runner bank from b673, its run id and the tree it built, one run per tree in an act',
     lambda R: _p(R, 'runner', R['runner'] + ([(R['runner'][0][0], 'planted', '1', R['runner'][0][3])] if R['runner'] else [(1, 'planted', '1', None)]))),
    ('G-RULE-WALK-TIP', 'b673 row 2: every walk bank from b684 (the author`s floor), its name`s tip against the tip it read; data/b679_zeta_walk.txt the breach before the floor',
     lambda R: _p(R, 'walks', R['walks'] + [('b684_zeta_walk.txt', None, 'abcdef0')])),
    ('G-RULE-ONE-GIT-WRITE', 'b673 row 3: this act`s shell calls by assistant message, git writes per message',
     lambda R: _p(R, 'calls', R['calls'] + [dict(mid='planted', tid='p1', ts='x', cmd='git commit -m x', out=''),
                                            dict(mid='planted', tid='p2', ts='x', cmd='git push origin x', out='')])),
    ('G-RULE-REMOTE-REREAD', 'b674 row 1: this act`s ls-remote calls with their outputs, one repository per call, an empty read re-read alone',
     lambda R: _p(R, 'calls', R['calls'] + [dict(mid='p', tid='p1', ts='x', cmd='git ls-remote a && git ls-remote b', out='')])),
    ('G-RULE-TIE-BREAK', 'b674 row 2: every naming bank`s rows and its named document, ties broken by the rule',
     lambda R: _p(R, 'naming', R['naming'] + [dict(bank='planted', named='SIDE-b', tied=2, rows=[(4, 'SIDE-a', (4, 48)), (4, 'SIDE-b', (4, 30))])])),
    ('G-RULE-HEAD-LINE-QUOTED', 'b674 row 3: this act`s ferry bank`s (1) against the previous closing`s :1',
     lambda R: _p(R, 'prev_head', R['prev_head'] + ' planted')),
    ('G-RULE-CLOSING-DRY', 'b675 row 1: every gate bank from b675, the closing dry-run step CLEAN; this act`s before its seal once locked',
     lambda R: _p(R, 'gates', _with(R['gates'], 675, dict(present=True, clean=False, at=None)))),
    ('G-RULE-LONG-PHASE-SPLIT', 'b675 row 2: the previous act`s pre-run`s longest phase against this act`s parts',
     lambda R: _p(_p(R, 'prev_longest', 500), 'parts', ['x'])),
    ('G-RULE-SUITE-PARTS', 'b678 row 1 (and b677 row 1 through it) and b684 row (1): every run bank from b678, against its act`s governing parts from the rules banks, each under 600 s',
     lambda R: _p(R, 'runs', _with(R['runs'], (678, 'planted'), [('standing', 1)]))),
    # ### b691, (R301)(6): the four rules data/b691_arms_sort.txt sorts TRACEABLE, each arm run at HEAD and counted before it is declared
    ('G-RULE-BINARY-HASHES', 'b680 row 1: every tracked binary bank of relay data from b680 (gz, png, zip), its sha256 in a text bank of its act that its act`s root names, the root not naming the binary',
     lambda R: _p(R, 'binaries', R['binaries'] + [dict(path='data/b999_planted.gz', act=999, sha='0' * 64, root=True, in_root=True, carried_by=[])])),
    ('G-RULE-SUITE-PART-CALLS', 'b685 row 1: this act`s suite part and combine calls, one part per call and each call its own message',
     lambda R: _p(R, 'calls', R['calls'] + [dict(mid='planted', tid='p1', ts='x', cmd='python tools/b999_checks.py --prerun --part standing-a && '
                                                                                    'python tools/b999_checks.py --prerun --part act', out='')])),
    ('G-RULE-POSTSEAL-READ', 'b690 row (1): this act`s shell calls after its seal commit naming the entry, the dry entry or the trail, none by a shell filter or a redirect',
     lambda R: _p(_p(R, 'seal_ct', R['seal_ct'] or 1), 'calls', R['calls'] + [dict(mid='planted', tid='p1', ts='2099-01-01T00:00:00Z',
                                                                                    cmd='sed -n 1p FINDINGS.md > /dev/null', out='')])),
    ('G-RULE-RECUT-QUOTE', 'b690 row (2): every quotation-search bank from b691, each removed line needled, the search timed before the merge of its tip, every quoting line entered in a cut bank of its act',
     lambda R: _p(R, 'quotes', R['quotes'] + [dict(bank='planted', act=R['n'], at=10, merge=('x', 5), rows=1, needled=True, quoting=[], unentered=[])])),
]
ARMS = [(nm, reads, (lambda k: lambda R: reading(k, R)[0])(nm), plant) for nm, reads, plant in ARMS]
NAMES = [a[0] for a in ARMS]
RULE_OF = dict(zip(NAMES, ('b670 row 1', 'b670 row 2', 'b670 row 3', 'b671 row 2', 'b671 row 3', 'b671 row 4', 'b671 row 6', 'b671 row 7',
                           'b672 row 1', 'b672 row 2', 'b672 row 3', 'b673 row 1', 'b673 row 2', 'b673 row 3', 'b674 row 1', 'b674 row 2',
                           'b674 row 3', 'b675 row 1', 'b675 row 2', 'b678 row 1', 'b680 row 1', 'b685 row 1', 'b690 row (1)', 'b690 row (2)')))
# ### b691, (R301)(6): a positive control for an arm by a defect that arm caught -- (arm, the defect, the plant). b690's defect (g): the latest
# ### methods bank banked four spaces in reads no row, and G-RULE-METHOD-READINESS fails on it (the pre-run found it so).
CONTROLS = [
    ('G-RULE-METHOD-READINESS', 'b690 (g): the latest methods bank re-read with every line four spaces in (relay data/b690_defects.txt :40-:45)',
     lambda R: _p(R, 'methods', (R['methods'][0], methods_rows(NL.join('    ' + l for l in R.get('methods_text', '').split(NL)))))),
    # ### b696, (R306)(2): b694's (k) -- its circuit figure's hashes bank naming the PNG under b692's path -- read with the corrigendum withheld
    ('G-RULE-BINARY-HASHES', 'b694 (k): the frozen row with no corrigendum -- the corrigenda bank`s rows withheld (relay data/b694_defects.txt :43-:51)',
     lambda R: _p(R, 'corrigenda', [])),
]
